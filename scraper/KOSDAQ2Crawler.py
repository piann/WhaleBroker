from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests
import time
import datetime
import math
import random

class KOSDAQ2Crawler(NaverFinanceCrawler):
# date, endPrice, startPrice, highPrice, lowPrice, amount

    def __init__(self, dbConn=getDBConnection(), bypassProxy=False, mixNoneProxy=False):
        super().__init__(dbConn, bypassProxy, mixNoneProxy)
        self.baseAmountUrl = self.baseUrl + "/sise/investorDealTrendDay.nhn"
        self.collection = "DailyIndex"
        self.itemName="KOSDAQ"

    @tryCatchWrapped
    def getResultData(self, fromPage, toPage):
        totalInfoDict = {self.itemName:[]}
        if fromPage > toPage:
            logging.error("fromPage value cannot be bigger than toPage value")
            return None
        
        prevInfoDictInPage = {}

        for pageIdx in range(fromPage, toPage+1):
            logging.info("process : {0} / {1} ".format(pageIdx, toPage))
            infoDictInPage = self.parsePage(pageIdx)

            # check if this page is last page
            if infoDictInPage == prevInfoDictInPage:
                logging.info("large page index : {0}".format(pageIdx))
                break

            self.breakTime = random.randint(1,6)
            self.setRandomUserAgent()
            time.sleep(self.breakTime)
            if infoDictInPage is not None:
                totalInfoDict[self.itemName] += infoDictInPage[self.itemName]
                prevInfoDictInPage = infoDictInPage

        logging.info(totalInfoDict)
        return totalInfoDict


    @tryCatchWrapped
    def parsePage(self, pageIdx):
        now = datetime.datetime.now()
        y = str(now.year)
        m = str(now.month).rjust(2,"0")
        d = str(now.day).rjust(2,"0")
        params = {"bizdate":"{0}{1}{2}".format(y,m,d), "page":str(pageIdx), "sosok":"02"}
        res = self.requestGetWithProxy(self.baseAmountUrl, headers=self.headers, params=params, timeout=15)
        if res is None or res.ok is False:
            logging.error("kosdaq{{'code':{0},'pageIdx':{1}}}".format(code,pageIdx))
            logging.error("Some problem in request")
            return None
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.select(
            'table.type_1 > tr'
        )
        

        rows = rows[3:]
        infoSoupList = [row for row in rows if str(row).find("date") >= 0]
        infoSelector = 'td'

        resultDict = {}
        infoDictList = []
        
        for infoSoup in infoSoupList:
            infoArray = infoSoup.select(infoSelector)
            dateStr = infoArray[0].text
            year, month, day = dateStr.split(".")
            year = "20"+year
            dateObj = datetime.datetime(int(year), int(month), int(day))
            # handle date info
            antNetAmount = int(infoArray[1].text.replace(",",""))
            foreignerNetAmount = int(infoArray[2].text.replace(",",""))
            instituteNetAmount = int(infoArray[3].text.replace(",",""))
            investNetAmount = int(infoArray[4].text.replace(",",""))
            insuranceNetAmount = int(infoArray[5].text.replace(",",""))
            privateNetAmount = int(infoArray[6].text.replace(",",""))
            bankNetAmount = int(infoArray[7].text.replace(",",""))
            etcNetAmount = int(infoArray[8].text.replace(",",""))
            npsNetAmount = int(infoArray[9].text.replace(",",""))
            
            infoDictList.append({
            "time":dateObj,
            "antNetAmount": antNetAmount,
            "foreignerNetAmount": foreignerNetAmount,
            "instituteNetAmount": instituteNetAmount,
            "investNetAmount": investNetAmount,
            "insuranceNetAmount": insuranceNetAmount,
            "privateNetAmount": privateNetAmount,
            "bankNetAmount": bankNetAmount,
            "etcNetAmount": etcNetAmount,
            "npsNetAmount": npsNetAmount
            })
        
        resultDict[self.itemName] = infoDictList
        return resultDict


