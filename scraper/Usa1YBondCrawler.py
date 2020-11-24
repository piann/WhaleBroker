from .base import *
from ..common import *

class Usa1YBondCrawler(InvestingCrawler):
    
    def __init__(self, dbConn=getDBConnection(), bypassProxy=False, mixNoneProxy=False):
        super().__init__(dbConn, bypassProxy, mixNoneProxy)
        self.formData = {
            "curr_id": 23700,
            "smlID": 200591,
            "header": "United States 1-Year Bond Yield Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="usa1YBond"
        self.collection = "DailyIndex"
        self.isAmountExist = False