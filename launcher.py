from src.main import main


def getinput(txt : str):
    return input(f"[--:--:--]: {txt} >> ")

def ynToTF(inp : str):
    if inp.upper() == "Y":
        return True
    else:
        return False

link = getinput("Enter URL")
loop  = getinput("Loop y/N?")
if ynToTF(loop):
    clock = int(getinput("Enter TPM"))
else:
    clock = 1
link = "https://gitxhub.com/ee/game/raw/main/SkyBlade/"
main(url=link, clock=clock, loop=ynToTF(loop))