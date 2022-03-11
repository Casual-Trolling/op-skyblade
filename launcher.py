from src.main import main

# input formatting
def getinput(txt : str):
    return input(f"[--:--:--]: {txt} >> ")

# turns y/n into bool
def ynToTF(inp : str):
    if inp.upper() == "Y":
        return True
    else:
        return False

# makes user file if one does not exist
with open("src/data/usrs/users.log", "a") as log:
    pass

# user config input with default values
link = getinput("Enter URL")
loop  = getinput("Loop y/N?")
if ynToTF(loop):
    clock = int(getinput("Enter TPM"))
else:
    clock = 1
willlog = getinput("Log  y/N?")

# run main loop
main(url=link, clock=clock, loop=ynToTF(loop), logusrnm=ynToTF(willlog))