from .base import *

class Korea10YBondCrawler(InvestingCrawler):
    
    def __init__(self, dbConn=getDBConnection(), bypassProxy=False, mixNoneProxy=False):
        super().__init__(dbConn, bypassProxy, mixNoneProxy)
        self.formData = {
            "curr_id": 29292,
            "smlID": 205673,
            "header": "South Korea 10-Year Bond Yield Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="korea10YBond"
        self.collection = "DailyIndex"
        self.isAmountExist = False