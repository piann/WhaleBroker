from .base import *

class Korea1YBondCrawler(InvestingCrawler):
    
    def __init__(self):
        super().__init__()
        self.formData = {
            "curr_id": 29294,
            "smlID": 205695,
            "header": "South Korea 1-Year Bond Yield Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="korea1YBond"
        self.collection = "DailyIndex"
        self.isAmountExist = False