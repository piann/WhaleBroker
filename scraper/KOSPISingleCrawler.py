from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests
import time
import datetime


class KOSPISingleCrawler(NaverFinanceCrawler):

    def __init__(self):
        super().__init__()
        self.basePriceUrl = self.baseUrl + "/item/sise_day.nhn"

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
            
            time.sleep(self.breakTime)
            prevInfoDictInPage = infoDictInPage
        
        return totalInfoDict


    @tryCatchWrapped
    def parsePage(self, code, pageIdx):
        params = {"code":str(code), "page":str(pageIdx)}
        res = requests.get(self.basePriceUrl, headers=self.headers, params=params)
        if res is None:
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
        InfoDict = {}

        # must consider when endPrice is blank b4 market is closed
        for infoSoup in infoSoupList:
            dateInfoList = infoSoup.select(dateSelector)
            priceInfoList = infoSoup.select(priceInfoSelector)

            if len(dateInfoList) > 0:
                dateStr = dateInfoList[0].text
                year, month, day = dateStr.split(".")
                dateObj = datetime.date(int(year), int(month), int(day))
            if len(priceInfoList) > 0:
                endPrice = int(priceInfoList[0].text.replace(",",""))
                startPrice = int(priceInfoList[2].text.replace(",",""))
                highPrice = int(priceInfoList[3].text.replace(",",""))
                lowPrice = int(priceInfoList[4].text.replace(",",""))
                amount = int(priceInfoList[5].text.replace(",",""))
                InfoDict[dateObj] = {"startPrice":startPrice, "endPrice":endPrice, 
                "highPrice":highPrice, "lowPrice":lowPrice, "amount":amount}
        
        return InfoDict