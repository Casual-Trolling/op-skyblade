from src.main import main


def getinput(txt : str):
    return input(f"[--:--:--]: {txt} >> ")

def ynToTF(inp : str):
    if inp.upper() == "Y":
        return True
    else:
        return False

with open("src/data/usrs/users.log", "a") as log:
    pass

link = getinput("Enter URL")
loop  = getinput("Loop y/N?")
if ynToTF(loop):
    clock = int(getinput("Enter TPM"))
else:
    clock = 1
willlog = getinput("Log  y/N?")

main(url=link, clock=clock, loop=ynToTF(loop), logusrnm=ynToTF(willlog))