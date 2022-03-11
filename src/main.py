from src.lib.logger import logger as log
from src.lib.logger import logusr 
from src.lib.requester import GetReq as Scrape
import time




def gitx(url, logusrnm):
        with open("./src/data/usrs/users.log", "r") as usrs:
            users = usrs.read().split("\n")                                     # makes list of all users in users.log
        try:
            data = Scrape(url)                                                  # scrapes html
            if data.isok:                                                       # only execute on 200
                giturl = data.url                                               # giturl == url found in html
                if data.usrname != None:                                        # if username exists
                    gitdata = Scrape(giturl)                                    # scrapes the profile link to see if it exists
                    if not gitdata.gone and logusrnm and giturl not in users:
                        logusr(giturl)                                          # logs git profile
                    elif not gitdata.gone:
                        log(f"passing {giturl}")                                # if profile exists, dont log it again
                    gitdata.cloesCon()                                          # close connections
                    data.cloesCon()
                    return giturl                                               # return the giturl to main()
                log("request returned no links")
            else:
                log("Connection Refused")                                       # log this whenever data is not ok
                data.cloesCon()
        except:
            log(f"request erroneus url {url}")                                   # error is most likely URL, will notify user

# turns TPM -> array to make timechecking easier
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
    if loop:                                                                    # if user asks to loop, loop
        while True:
            timenow = time.localtime().tm_min                                   # gets current min
            if timenow in arr:
                gitx(url=url, logusrnm=logusrnm)                                # if its time to tick, run gitx
                while timenow in arr:
                    time.sleep(1)                                               # if its run gitx, wait til next tick
            else:
                time.sleep(1)
    else:
        gitx(url=url, logusrnm=logusrnm)                                        # run gitx as normal if user doesnt want a loop
        
