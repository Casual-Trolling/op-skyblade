
import requests as rq
from src.lib.logger import logger as log

class GetReq():
    def __init__(self, url):
        self.url = url                                                  # gets url to be used later
        self.__data = rq.get(url)                                       # makes HTTP request to url
        self._body = self.__data.text                                   # extracts html data from http req
        self.code = self.__data.status_code                             # extracts status code from http req
        self.isok = self.__data.ok                                      # checks if data is ok
        self.gone = self.__isNotFound()                                 # checks if code == 404
        self.hasgit = self.__hasGit()                                   # checks if html has a github link
        self.usrname = self.__getGitUSR()                               # gets git usrname from html data
        self.url = f"https://github.com/{self.usrname}/"                # formats the profile url
        
        # general housekeeping with logging script
        log(f"request initialised: {url}")
        log(f"request returned status: {self.code}")

    # checks if status code is 404
    def __isNotFound(self):
        if self.code == 404:
            self.__data.close()
            return True
    
    # looks for git link in html
    def __hasGit(self):
        if "https://github.com/" in self._body:
            return True
        else:
            return False
    
    # gets git usrname if there is a git link in the html data 
    def __getGitUSR(self):
        if self.hasgit:
            url = self._body.split("https://github.com/")[-1].split("\"")[0].split("/")[0]
            return url   
        else:
            return None
    
    # closes http connection
    def cloesCon(self):
        self.__data.close()
    

    
