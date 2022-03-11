from datetime import datetime


def logger(info):
    timenow = datetime.now().strftime("%H:%M:%S")                       # gets current date and time
    datenow = datetime.now().strftime("%Y-%m-%d")
    with open(f"./src/data/log/{datenow}.log", "a") as log:             # opens log file for the day
        data = f"[{timenow}]: {info}"                                   # formats the input data
        log.write(f"\n {data}")                                         # writes data to file
        print(data)                                                     # outputs data to screen

def logusr(url):
    with open(f"./src/data/usrs/users.log", "a") as usrs:               # appends user data to users list
        logger(f"logging {url}")
        usrs.write(f"\n{url}")
