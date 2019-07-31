from ..common import *
from .base import *
from bs4 import BeautifulSoup
import requests
import time
import datetime



class USDJPYCrawler(InvestingCrawler):
    
    def __init__(self):
        super().__init__()
        self.formData = {"curr_id": 3,
            "smlID": 106684,
            "header": "USD/JPY Historical Data",
            "st_date": "",
            "end_date": "",
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }
        self.itemName="USD/JPY"
        self.collection = "dailyIndex"
        self.isAmountExist = False