from abc import *
import random
from ..common import *
import time
import datetime
import requests
from bs4 import BeautifulSoup
import math
import pymongo

from lxml.html import fromstring

class InfoCrawler(object):
    __metaclass__ = ABCMeta
     
    def __init__(self):
        self.baseUrl = ""
        self.breakTime = 1 # do crawling with break time
        self.headers = {}
        self.itemName = None
        self.collection = None
        self.proxyList = self.getProxyList()
        

    def setRandomUserAgent(self):
        userAgentList = [
            #Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            #Firefox
            'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
        ]
        userAgent = random.choice(userAgentList)
        self.headers['User-Agent'] = userAgent
        return userAgent

    @tryCatchWrapped
    def getProxyList(self, minPerformanceTime=10):
        targetUrlList = ['https://short.krx.co.kr/main/main.jsp', 'https://www.investing.com/', 'https://finance.naver.com/']
        
        # deprecated
        '''
        listUrl = 'https://free-proxy-list.net/'

        response = requests.get(listUrl)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        '''
        proxyResults = []
        for proxyUrl in PROXY_LIST:
            checkUrlCount = 0
            for targetUrl in targetUrlList:
                tempProxies = {"http" : proxyUrl, "https" : proxyUrl}
                try:
                    response = requests.get(targetUrl, proxies=tempProxies, timeout=minPerformanceTime)
                    if response is None:
                        break

                    checkUrlCount +=1
                except:
                    logging.info("Slow or Error : {0}".format(proxyUrl))
                    break

            if(checkUrlCount == 3):
                proxyResults.append(tempProxies)
                logging.info("Success Proxy  : {0}".format(proxyUrl))
        
        logging.info("Number of Success Proxy : {0}".format(len(proxyResults)))
        self.proxyList = proxyResults
        return proxyResults

    @abstractmethod
    def getResultData(self, inputN, rangeN):
        # this method is the goal of class
        # argument should be considered with efficiency
        # if range input is date, date format is 'YYYY/MM/DD'
        pass

        
    @tryCatchWrapped
    def putDataToMongo(self, dbConn, resultData):
        # consider resultData format and db collection
        # consider the case utilizing multiple collection    

        if self.collection is None:
            return None
        
        col = dbConn.get_collection(self.collection)
        for code, infoDictList in resultData.items():
            for infoDict in infoDictList:
                res = col.find_one({"_id":code,"data.time":infoDict["time"]})
                if res is None: # if data if this date is new 
                    res = col.update({"_id":code},{"$push":{"data":infoDict}},upsert=True)

                else: # if already exist
                    for k, v in infoDict.items():
                        res = col.update({"_id":code,"data.time":infoDict["time"]},{"$set":{
                                "data.$.{0}".format(k):v
                            }
                        })
                        
        return True

    @tryCatchWrapped
    def requestGetWithProxy(self, *args,**kwargs):
        retryCount = 7
        for idx in range(0,retryCount):
            try:
                proxies = random.choice(self.proxyList)
                res = requests.get(*args, **kwargs, proxies=proxies)
                if res is not None:
                    return res
            except Exception as e:
                logging.error("Request Error in trial #{0}".format(idx))
                logging.error(str(e), exc_info=True)

        return None


    @tryCatchWrapped
    def requestPostWithProxy(self, *args,**kwargs):
        retryCount = 7
        for idx in range(0,retryCount):
            try:
                proxies = random.choice(self.proxyList)
                res = requests.post(*args, **kwargs, proxies=proxies)
                if res is not None:
                    return res
            except Exception as e:
                logging.error("Request Error in trial #{0}".format(idx))
                logging.error(str(e), exc_info=True)

        return None


class InvestingCrawler(InfoCrawler):
    # input is items of form data (ex : curr_id: 8830, smlID: 300004, header: Gold Futures Historical Data)
    # range is date to date, and no limit

    def __init__(self):
        super().__init__()
        self.baseUrl = "https://www.investing.com/instruments/HistoricalDataAjax"
        self.headers = {
            'User-Agent' : '',
	        'referer': "https://www.investing.com",
	        'host' : 'www.investing.com',
	        'X-Requested-With' : 'XMLHttpRequest',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',

        }
        self.isAmountExist = False
        self.setRandomUserAgent()

    @tryCatchWrapped
    def convertDateStrToDate(self, dateStr):
        month, day, year = dateStr.split(" ")
        monDic = {
            "Dec": 12,
            "Nov": 11,
            "Oct": 10,
            "Sep": 9,
            "Aug": 8,
            "Jul": 7,
            "Jun": 6,
            "May": 5,
            "Apr": 4,
            "Mar": 3,
            "Feb": 2,
            "Jan": 1,
        }
        month = int(monDic[month])
        day = int(day.replace(",",""))
        year = int(year)
        dateObj = datetime.datetime(year, month, day)
        return dateObj

    @tryCatchWrapped
    def parseAmount(self, amountStr):
        if amountStr == '-':
            amount = 0
        elif amountStr[-1] == "K":
            amount = float(amountStr[:-1])*1000
        elif amountStr[-1] == "M":
            amount = float(amountStr[:-1])*1000000
        elif amountStr[-1] == "B":
            amount = float(amountStr[:-1])*1000000000
        else:
            amount = float(amountStr)
        
        return math.floor(amount)

    def setCustomDateFormat(self, dateStr):
        # our input format is YYYY/MM/DD, so convert it proper considering format of investing.com
        year, month, day = dateStr.split("/")
        investingDateStr = "{0}/{1}/{2}".format(month, day, year)
        return investingDateStr

    @tryCatchWrapped
    def getResultData(self, fromDate, toDate):
        
        resultDict = {}
        infoDictList = []
        # investing.com input date format : dd/mm/yyyy
        self.formData["st_date"] = self.setCustomDateFormat(fromDate)
        self.formData["end_date"] = self.setCustomDateFormat(toDate)
        res = requests.post(self.baseUrl, headers=self.headers, data=self.formData)
        if res is None or res.ok is False:
            logging.error("Some problem in request")
            return None
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.select(
            'tbody > tr'
        )
        for row in rows[:-1]:
            infoList = row.select(
                'td'
            )

            infoDict = {}
            dateObj = self.convertDateStrToDate(infoList[0].text)
            endPrice = float(infoList[1].text.replace(",",""))
            startPrice = float(infoList[2].text.replace(",",""))
            highPrice = float(infoList[3].text.replace(",",""))
            lowPrice = float(infoList[4].text.replace(",",""))
            infoDict = {"time":dateObj, "startPrice":startPrice, "endPrice":endPrice, 
            "highPrice":highPrice, "lowPrice":lowPrice}
            
            if self.isAmountExist is True:
                amountStr = (infoList[5].text.replace(",",""))
                amount = self.parseAmount(amountStr)
                infoDict["amount"] = amount
            
            infoDictList.append(infoDict)


        resultDict[self.itemName] = infoDictList
        return resultDict





class NaverFinanceCrawler(InfoCrawler):
    # input is code (ex : SK is 034730)
    # loop by page

    def __init__(self):
        super().__init__()
        self.baseUrl = "https://finance.naver.com"
        self.headers = {
            'User-Agent' : '',
            'referer': "https://finance.naver.com",
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.setRandomUserAgent()

