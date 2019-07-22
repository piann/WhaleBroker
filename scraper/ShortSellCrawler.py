from .base import *

class ShortSellCrawler(InfoCrawler):

    def __init__(self):
        super().__init__()
        self.baseUrl = "https://short.krx.co.kr/contents/SRT/99/SRT99000001.jspx"
