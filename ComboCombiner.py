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

def doComboCombiner():
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
    time.sleep(1)
    print("---------------------------------------------------------------")
    print("loaded accounts.")
    time.sleep(1)
    print("---------------------------------------------------------------")
    merge = input(str("With which file do you want to merge? "))
    try:
        verify = open(merge, "r")
    except:
        time.sleep(1)
        print("---------------------------------------------------------------")
        print("Something went wrong while trying to load your file.")
        doWTD()
    time.sleep(1)
    print("---------------------------------------------------------------")
    print("loaded accounts.")
    time.sleep(1)
    print("---------------------------------------------------------------")
    createOut = open("LiquidComboCombiner-" + combo,"w+")
    with open("LiquidComboCombiner-" + combo, "a") as infile:
        comboFile = open(combo, "r")
        contentsCombo = comboFile.read()
        mergeFile = open(merge, "r")
        contentsMerge = mergeFile.read()
        infile.write(contentsCombo + "\n" + contentsMerge)
    print("Done!")
    doWTD()