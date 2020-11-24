from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests
import time
import datetime
import math
import random

class KoreaSingleCrawler(NaverFinanceCrawler):
# date, endPrice, startPrice, highPrice, lowPrice, amount

    def __init__(self, dbConn=getDBConnection(), bypassProxy=False, mixNoneProxy=False):
        super().__init__(dbConn, bypassProxy, mixNoneProxy)
        self.basePriceUrl = self.baseUrl + "/item/sise_day.nhn"
        self.collection = "DailyKoreaStock"

    @tryCatchWrapped
    def getResultData(self, code, fromPage, toPage):
        totalInfoDict = {code:[]}
        if fromPage > toPage:
            logging.error("fromPage value cannot be bigger than toPage value")
            return None
        
        prevInfoDictInPage = {}

        for pageIdx in range(fromPage, toPage+1):
            logging.info("process : {0} / {1} ".format(pageIdx, toPage))
            infoDictInPage = self.parsePage(code,pageIdx)

            # check if this page is last page
            if infoDictInPage == prevInfoDictInPage:
                logging.info("large page index : {0}".format(pageIdx))
                break

            self.setRandomUserAgent()
            # self.breakTime = random.randint(6,12)
            # time.sleep(self.breakTime) no need with proxy
            if infoDictInPage is not None:
                totalInfoDict[code] += infoDictInPage[code]
                prevInfoDictInPage = infoDictInPage

        logging.info(totalInfoDict)
        return totalInfoDict


    @tryCatchWrapped
    def parsePage(self, code, pageIdx):
        params = {"code":str(code), "page":str(pageIdx)}
        res = self.requestGetWithProxy(self.basePriceUrl, headers=self.headers, params=params, timeout=20)
        if res is None or res.ok is False:
            logging.error("1{{'code':{0},'pageIdx':{1}}}".format(code,pageIdx))
            logging.error("Some problem in request")
            return None
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.select(
            'table.type2 > tr'
        )
        infoSoupList = [row for row in rows if str(row).find("mouseOut") >= 0]
        
        dateSelector = 'span.tah'
        priceInfoSelector = 'td.num > span.tah'
        resultDict = {}
        infoDictList = []

        # must consider when endPrice is blank b4 market is closed
        for infoSoup in infoSoupList:
            dateInfoList = infoSoup.select(dateSelector)
            priceInfoList = infoSoup.select(priceInfoSelector)

            if len(dateInfoList) > 0:
                dateStr = dateInfoList[0].text
                year, month, day = dateStr.split(".")
                dateObj = datetime.datetime(int(year), int(month), int(day))
            if len(priceInfoList) > 0:
                endPrice = int(priceInfoList[0].text.replace(",",""))
                startPrice = int(priceInfoList[2].text.replace(",",""))
                highPrice = int(priceInfoList[3].text.replace(",",""))
                lowPrice = int(priceInfoList[4].text.replace(",",""))
                amount = int(priceInfoList[5].text.replace(",",""))
                tValue = int(math.floor((lowPrice + highPrice)/2)) * amount
                infoDictList.append({"time":dateObj, "startPrice":startPrice, "endPrice":endPrice, 
                "highPrice":highPrice, "lowPrice":lowPrice, "tValue":tValue})
        
        resultDict[code] = infoDictList
        return resultDict


