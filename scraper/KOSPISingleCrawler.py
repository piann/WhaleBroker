from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests

class KOSPISingleCrawler(NaverFinanceCrawler):

    def __init__(self):
        super().__init__()
        self.basePriceUrl = self.baseUrl + "/item/sise_day.nhn"

    @tryCatchWrapped
    def getResultData(self, code, fromPage, toPage):
        pass



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
        for infoSoup in infoSoupList:
            dateInfoList = infoSoup.select(dateSelector)
            priceInfoList = infoSoup.select(priceInfoSelector)

            if len(dateInfoList) > 0:
                date = dateInfoList[0].text
            if len(priceInfoList) > 0:
                endPrice = priceInfoList[0].text
                startPrice = priceInfoList[2].text
                highPrice = priceInfoList[3].text
                lowPrice = priceInfoList[4].text
                amount = priceInfoList[5].text
                InfoDict[date] = {"startPrice":startPrice, "endPrice":endPrice, "highPrice":highPrice, "lowPrice":lowPrice}
        
        return InfoDict