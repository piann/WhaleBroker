from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests
import time
import datetime
import random

class KOSPISingle2Crawler(NaverFinanceCrawler):
# foreigner, institute

    def __init__(self):
        super().__init__()
        self.basePriceUrl = self.baseUrl + "/item/frgn.nhn"

    @tryCatchWrapped
    def getResultData(self, code, fromPage, toPage):
        totalInfoDict = {}
        if fromPage > toPage:
            logging.error("fromPage value cannot be bigger than toPage value")
            return None
        
        prevInfoDictInPage = None

        for pageIdx in range(fromPage, toPage+1):
            infoDictInPage = self.parsePage(code,pageIdx)
            if pageIdx is not None:
                totalInfoDict.update(infoDictInPage)
            
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
        res = requests.get(self.basePriceUrl, headers=self.headers, params=params)
        if res is None or res.ok is False:
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
        infoDict = {}

        # must consider when endPrice is blank b4 market is closed
        for infoSoup in infoSoupList:
            dateInfoList = infoSoup.select(dateSelector)
            amountInfoList = infoSoup.select(amountInfoSelector)

            if len(dateInfoList) > 0:
                dateStr = dateInfoList[0].text
                year, month, day = dateStr.split(".")
                dateObj = datetime.date(int(year), int(month), int(day))
            if len(amountInfoList) > 0:
                instituteAmount = int(amountInfoList[4].text.replace(",",""))
                foreignerAmount = int(amountInfoList[5].text.replace(",",""))
                infoDict[dateObj] = {
                "instituteAmount":instituteAmount, 
                "foreignerAmount":foreignerAmount
                }
        
        return infoDict
        