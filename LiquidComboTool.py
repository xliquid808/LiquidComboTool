import time
import os
from MailToUser import doMailToUser
from CaptureRemoverV2 import doCRV2
from ComboCombiner import doComboCombiner





def doMain():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" █   █ ▄▀▄ █ █ █ █▀▄   ▄▀▀ ▄▀▄ █▄ ▄█ ██▄ ▄▀▄   ▀█▀ ▄▀▄ ▄▀▄ █   ")
    print(" █▄▄ █ ▀▄█ ▀▄█ █ █▄▀   ▀▄▄ ▀▄▀ █ ▀ █ █▄█ ▀▄▀    █  ▀▄▀ ▀▄▀ █▄▄ ")
    time.sleep(1)
    print("-------------------------Choose action-------------------------")
    time.sleep(1)
    menu = input("[0] Mail to User\n[1] Capture Remover\n[2] Combo Combiner\n[3] Exit\n---------------------------------------------------------------\n")

    if menu == "0":
        doMailToUser()
    elif menu == "1":
        doCRV2()
    elif menu == "2":
        doComboCombiner()
    elif menu == "3":
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
        doMain()


doMain()
