from src.lib.logger import logger as log
from src.lib.logger import logusr 
from src.lib.requester import GetReq as Scrape
from src.lib.gitter import GetGit as Git
import asyncio
import time




def gitx(url):
        with open("./src/data/usrs/users.log", "r") as usrs:
            users = usrs.read().split("\n")
            #print(users)
    
        data = Scrape(url)
    
        if data.isok:
            try:
                giturl = data.url
                gitdata = Scrape(giturl)
            
                if gitdata.isok and giturl not in users:
                    log(f"active: {giturl}")
                    logusr(giturl)

                elif gitdata.isok:
                    log(f"passing {giturl}")

                gitdata.cloesCon()
                data.cloesCon()
                return giturl
            except:
                log("no links on site")
        else:
            log("Connection Refused")
            data.cloesCon()


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


def main(url : str, clock : int, loop : bool):
    arr = clockToArr(clock)
    log(f"loading {url}")
    if loop:
        while True:
            timenow = time.localtime().tm_min
            if time.localtime().tm_min in arr:
                gitx(url=url)
                while time.localtime().tm_min in arr:
                    time.sleep(1)
            else:
                
                time.sleep(1)
    else:
        gitx(url=url)
        
