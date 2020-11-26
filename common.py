import logging
import datetime
import pymongo
from selenium import webdriver
import time
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import json

load_dotenv(verbose=True)

def getMinDate(datetimeObjList):
    curMinDatetimeObj = datetime.datetime.now()
    for datetimeObj in datetimeObjList:
        if curMinDatetimeObj > datetimeObj:
            curMinDatetimeObj = datetimeObj
        
    return curMinDatetimeObj

def setupLogging(fileName):
    # setup log file and log depth 

    fileHandler = logging.FileHandler(fileName)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter( logging.Formatter('%(asctime)s:%(levelname)s:[%(filename)s.%(funcName)s]%(message)s', '%m-%d %H:%M:%S'))

    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter( logging.Formatter('%(asctime)s:%(levelname)s:[%(filename)s.%(funcName)s]%(message)s', '%m-%d %H:%M:%S'))

    logger = logging.getLogger('')

    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


def tryCatchWrapped(func):
    # this is for decorator

    def wrapperFunc(*args, **kwargs):
        try:
            result =  func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(str(e), exc_info=True)
            return None

    return wrapperFunc

@tryCatchWrapped
def getDBConnection(databaseName="whalebroker", ip="127.0.0.1", port=27017):
    conn = pymongo.MongoClient(str(ip), int(port))
    db = conn.get_database(databaseName)
    return db

@tryCatchWrapped
def sortJsonList(jsonList,keyName="time", reverse=False):
    sortedJsonList = sorted(jsonList, key=lambda k: k.get(keyName, 0), reverse=reverse)
    return sortedJsonList


@tryCatchWrapped
def crawlProxyServerList():
    CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.implicitly_wait(3)

    #generalPagesFormat = 'http://free-proxy.cz/en/proxylist/main/{}';
    httpsPagesFormat = 'http://free-proxy.cz/en/proxylist/country/all/https/speed/all/{}'


    proxyList = []
    for i in [4,1,3,2]:
        driver.get(httpsPagesFormat.format(i))
        driver.find_element_by_id('clickexport').click()
        driver.implicitly_wait(1)
        element = driver.find_element_by_id('zkzk')
        proxyList += (element.text).split("\n")
        time.sleep(10)
    driver.quit()

    return proxyList

@tryCatchWrapped
def getRecentProxyListFromMongo(dbConn):
    col = dbConn.get_collection(PROXY_COLLECTION_NAME)
    recentActiveDictList = col.find({
        'recentActiveDate': {'$gte': datetime.datetime.now() - datetime.timedelta(days=14)}
    })

    recentActiveList = [recentActiveDict["_id"] for recentActiveDict in recentActiveDictList]
    return recentActiveList

@tryCatchWrapped
def updateProxyList(dbConn, proxyList):
    # consider resultData format and db collection
    # consider the case utilizing multiple collection    
    
    col = dbConn.get_collection(PROXY_COLLECTION_NAME)
    for proxyIpPort in proxyList:
        col.update_one(
        {"_id":proxyIpPort},
        {"$set":{"_id":proxyIpPort,"recentActiveDate":datetime.datetime.now()}},
        upsert=True
        )

@tryCatchWrapped
def getStockDictList():
    targetUrl = "https://kind.krx.co.kr/corpgeneral/corpList.do"
    headers={
        "Host":"kind.krx.co.kr",
        "Connection":"keep-alive",
        "Content-Length":"211",
        "Cache-Control":"max-age=0",
        "Upgrade-Insecure-Requests":"1",
        "Origin":"https://kind.krx.co.kr",
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-User":"?1",
        "Sec-Fetch-Dest":"document",
        "Referer":"https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-US,en;q=0.9,ko;q=0.8",
        "Cookie":"__smVisitorID=NB_GGZU_TNA; JSESSIONID=OGbNigpXNqPA5izT1PcrH1GMhhP7dacwFM8GwmC9QcA5jnH6V6q8aZCiDDQ6z3SB.amV1c19kb21haW4vMTBfRFNUMg==",
    }

    data={
        "method":"download",
        "pageIndex":"1",
        "currentPageSize":"5000",
        "orderMode":"3",
        "orderStat":"D",
        "searchType":"13",
        "fiscalYearEnd":"all",
        "location":"all",
    }
    res = requests.post(targetUrl, data=data, headers=headers)
    df = pd.read_html(res.text, header=0)[0]
    stockDictList = []
    for row in df.iloc:
        stockDict = {}
        rawCode = row['종목코드']
        shortCode = "A"+"0"*(6-(len(str(rawCode))))+ str(rawCode) # 종목코드의 길이가 6자리 미만인경우, 앞을 0으로 채워넣어야한다.
        stockDict["shortCode"] = shortCode
        stockDict["codeName"] = row["회사명"]
        stockDict["businessType"] = row["업종"]
        stockDict["product"] = row["주요제품"]
        stockDict["settlementMonth"] = int(row["결산월"].replace("월",""))
        rawFloatTime = row["상장일"]
        year, month, day = rawFloatTime.split("-")
        stockDict["floatTime"] = datetime.datetime(int(year), int(month), int(day))
        stockDict["location"] = row["지역"]
        stockDict["category"] = "stock"
        stockDictList.append(stockDict)

    return stockDictList

@tryCatchWrapped
def getEtfDictList():

    url = 'https://finance.naver.com/api/sise/etfItemList.nhn'
    rawInfoDict = json.loads(requests.get(url).text)
    preDictList = rawInfoDict['result']['etfItemList']
    etfDictList = [{"shortCode": "A"+preDict["itemcode"], "codeName":preDict["itemname"], "marketSum":preDict["marketSum"], "updateTime":datetime.datetime.now(), "category":"etf"} for preDict in preDictList]
    
    return etfDictList

@tryCatchWrapped
def updateCodesInfo(dbConn, codeDictList):

    col = dbConn.get_collection(KR_MARKET_CODE_COLLECTION_NAME)
    for codeDict in codeDictList:
        col.update_one(
        {"_id":codeDict["shortCode"][-6:]},
        {"$set":codeDict},
        upsert=True
        )

    return True

@tryCatchWrapped
def getStockCodeListFromMongo(dbConn, minDayNew=7):
    col = dbConn.get_collection(KR_MARKET_CODE_COLLECTION_NAME)
    recentActiveDictList = col.find({
        'updateTime': {'$gte': datetime.datetime.now() - datetime.timedelta(days=minDayNew)}
    })
    
    return list(recentActiveDictList)


KR_MARKET_CODE_COLLECTION_NAME = "KoreaMarketCode"
PROXY_COLLECTION_NAME = "ProxyConnInfo"
