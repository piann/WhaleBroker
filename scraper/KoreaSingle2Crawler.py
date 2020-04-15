from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests
import time
import datetime
import random

class KoreaSingle2Crawler(NaverFinanceCrawler):
# foreigner, institute

    def __init__(self):
        super().__init__()
        self.basePriceUrl = self.baseUrl + "/item/frgn.nhn"
        self.collection = "DailyKoreaStock"


    @tryCatchWrapped
    def getResultData(self, code, fromPage, toPage):
        totalInfoDict = {code:[]}
        if fromPage > toPage:
            logging.error("fromPage value cannot be bigger than toPage value")
            return None
        
        prevInfoDictInPage = None

        for pageIdx in range(fromPage, toPage+1):
            logging.info("process : {0} / {1} ".format(pageIdx, toPage))
            infoDictInPage = self.parsePage(code,pageIdx)
            if infoDictInPage is not None:
                totalInfoDict[code] += infoDictInPage[code]
            
            # check if this page is last page
            if infoDictInPage == prevInfoDictInPage:
                break
            
            self.breakTime = random.randint(1,4)
            self.setRandomUserAgent()
            time.sleep(self.breakTime)
            prevInfoDictInPage = infoDictInPage

        return totalInfoDict


    @tryCatchWrapped
    def parsePage(self, code, pageIdx):
        params = {"code":str(code), "page":str(pageIdx)}
        res = self.requestGetWithProxy(self.basePriceUrl, headers=self.headers, params=params,  timeout=15)
        if res is None or res.ok is False:
            logging.error("2{{'code':{0},'pageIdx':{1}}}".format(code,pageIdx))
            logging.error("Some problem in request")
            return None
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.select(
            'table.type2 > tr'
        )
        infoSoupList = [row for row in rows if str(row).find("mouseOut") >= 0]
        
        
        dateSelector = 'span.tah'
        amountInfoSelector = 'td.num > span.tah'
        infoDictList = []
        resultDict = {}

        # must consider when endPrice is blank b4 market is closed
        for infoSoup in infoSoupList:
            dateInfoList = infoSoup.select(dateSelector)
            amountInfoList = infoSoup.select(amountInfoSelector)

            if len(dateInfoList) > 0:
                dateStr = dateInfoList[0].text
                year, month, day = dateStr.split(".")
                dateObj = datetime.datetime(int(year), int(month), int(day))
            if len(amountInfoList) > 0:
                instituteAmount = int(amountInfoList[4].text.replace(",",""))
                foreignerAmount = int(amountInfoList[5].text.replace(",",""))
                infoDictList.append({
                "time":dateObj,
                "instituteNetAmount":instituteAmount, 
                "foreignerNetAmount":foreignerAmount
                })

        resultDict[code] = infoDictList
        return resultDict
