from datetime import datetime


def logger(info):
    timenow = datetime.now().strftime("%H:%M:%S")
    datenow = datetime.now().strftime("%Y-%m-%d")
    with open(f"./src/data/log/{datenow}.log", "a") as log:
        data = f"[{timenow}]: {info}"
        log.write(f"\n {data}")
        print(data)

def logusr(url):
    with open(f"./src/data/usrs/users.log", "a") as usrs:
        logger(f"logging {url}")
        usrs.write(f"\n{url}")
