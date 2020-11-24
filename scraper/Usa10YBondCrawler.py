from .base import *

class Usa10YBondCrawler(InvestingCrawler):
    
    def __init__(self, dbConn=getDBConnection(), bypassProxy=False, mixNoneProxy=False):
        super().__init__(dbConn, bypassProxy, mixNoneProxy)
        self.formData = {
            "curr_id": 23705,
            "smlID": 200646,
            "header": "United States 10-Year Bond Yield Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="usa10YBond"
        self.collection = "DailyIndex"
        self.isAmountExist = False