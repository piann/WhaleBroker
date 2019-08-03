from .base import *

class Korea10YBondCrawler(InvestingCrawler):
    
    def __init__(self):
        super().__init__()
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
        self.itemName="Korea10YBond"
        self.collection = "DailyIndex"
        self.isAmountExist = False