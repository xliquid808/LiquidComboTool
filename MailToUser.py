import time
import os

def doWTD():
    time.sleep(1)
    print("---------------------------------------------------------------")
    wtd = input("What do you want to do now? | [0] Return to main menu | [1] Exit ")
    if wtd == "0":
        from LiquidComboTool import doMain
        doMain()
    elif wtd == "1":
        time.sleep(1)
        print("---------------------------------------------------------------")
        time.sleep(1)
        print("Thanks for editing with liquid combo tool ~ xliquid")
        exit(0)
    else:
        time.sleep(1)
        print("---------------------------------------------------------------")
        time.sleep(1)
        print("Bozo, bitch, are you dumb-d-dumb-dumb-dumb-d-dumb-dumb-dumb? (Stupid)")
        time.sleep(1)
        doWTD()

def doMailToUser():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" █   █ ▄▀▄ █ █ █ █▀▄   ▄▀▀ ▄▀▄ █▄ ▄█ ██▄ ▄▀▄   ▀█▀ ▄▀▄ ▄▀▄ █   ")
    print(" █▄▄ █ ▀▄█ ▀▄█ █ █▄▀   ▀▄▄ ▀▄▀ █ ▀ █ █▄█ ▀▄▀    █  ▀▄▀ ▀▄▀ █▄▄ ")
    time.sleep(1)
    print("---------------------------------------------------------------")
    time.sleep(1)
    combo = input(str("Whats the name of your account file? "))
    try:
        verify = open(combo, "r")
    except:
        time.sleep(1)
        print("---------------------------------------------------------------")
        print("Something went wrong while trying to load your file.")
        doWTD()
    print("loaded accounts.")
    time.sleep(1)
    print("---------------------------------------------------------------")
    createOut = open("Mail To User-" + combo,"w+")
    with open(combo) as infile:
        for line in infile:
            with open("Mail To User-" + combo, "a") as out:
                accountSplitted = line.split(":")
                mail_to_user = accountSplitted[0].split("@")
                account = mail_to_user[0] + ":" + accountSplitted[1]
                out.write(account)
    print("Done!")
    doWTD()
