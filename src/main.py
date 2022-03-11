from src.lib.logger import logger as log
from src.lib.logger import logusr 
from src.lib.requester import GetReq as Scrape
import asyncio
import time




def gitx(url, logusrnm):
        with open("./src/data/usrs/users.log", "r") as usrs:
            users = usrs.read().split("\n")
            #print(users)
        try:
            data = Scrape(url)
        
    
            if data.isok:
                giturl = data.url
                if data.usrname != None:
                    gitdata = Scrape(giturl)
        
                    if not gitdata.gone and logusrnm and giturl not in users:
                        logusr(giturl)

                    elif not gitdata.gone:
                        log(f"passing {giturl}")

                    gitdata.cloesCon()
                    data.cloesCon()
                    return giturl
                log("request returned no links")
            else:
                log("Connection Refused")
                data.cloesCon()
        except:
            log(f"request erroneus url ({url})")

def clockToArr(clock : int):
    if clock == 0:
        clock = 1
    elif clock > 60:
        clock = 60
    rate = 60//clock
    current = 0
    ls = []
    ls.append(current)
    while current < 60:
        current += rate
        ls.append(current)
    return ls


def main(url : str, clock : int, loop : bool, logusrnm : bool):
    arr = clockToArr(clock)
    log(f"loading {url}")
    if loop:
        while True:
            timenow = time.localtime().tm_min
            if time.localtime().tm_min in arr:
                gitx(url=url, logusrnm=logusrnm)
                while time.localtime().tm_min in arr:
                    time.sleep(1)
            else:
                
                time.sleep(1)
    else:
        gitx(url=url, logusrnm=logusrnm)
        
