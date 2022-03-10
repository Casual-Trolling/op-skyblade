
import requests as rq
from src.lib.logger import logger as log
import asyncio

class GetReq():
    def __init__(self, url):
        self.url = url 
        self.__data = rq.get(url)
        self._body = self.__data.text
        self.code = self.__data.status_code
        self.isok = self.__data.ok
        self.gone = self.__isNotFound()
        self.hasgit = self.__hasGit()
        self.usrname = self.getGitUSR()
        self.url = f"https://github.com/{self.usrname}/"
        
        
        log(f"request initialised: {url}")
        log(f"request returned status: {self.code}")

    
    def __isNotFound(self):
        if self.code == 404:
            self.__data.close()
            return True
    
    def __hasGit(self):
        if "https://github.com/" in self._body:
            return True
        else:
            return False
            
    def getGitUSR(self):
        if self.hasgit:
            url = self._body.split("https://github.com/")[-1].split("\"")[0].split("/")[0]
            #log(f"located git download: {url}")
            return url
            
        else:
            return None
    

    def cloesCon(self):
        self.__data.close()
    

    
