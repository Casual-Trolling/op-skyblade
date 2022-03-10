# curl https://api.github.com/repos/voenv/game
from src.lib.requester import GetReq
import requests as rq
from src.lib.logger import logger as log

class GetGit(GetReq):
    def __init__(self, url):
        super().__init__(url)
    


    def getGitREP(self):
        rep = self.url.split("raw")[0]
        log(f"located git repository: {rep}")
        return rep

    def getGitUSR(self):
        usr = self.getGitREP().split("github.com/")[-1].split("/")[0]
        log(f"located git user {usr}")
        return usr
