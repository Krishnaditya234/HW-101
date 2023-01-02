import random
def a():
    if resp == "y" or resp == "Y":
        print("[       ]")
        print("|",random.randint(1,6),random.randint(1,6),random.randint(1,6),"|")
        print("[       ]")
    elif resp == "N" or resp == "n":
        print("Thanks for the response. Exiting")
	    
resp = input("Enter Y(want to roll)| N(Exit) : ")
if resp == "y" or resp == "Y":
    while resp == "y" or resp == "Y":
	    a()
	    break
    resp = input("Enter Y(want to roll)| N(Exit) : ")
else:
    while resp == "n" or resp == "N":
	    a()
	    break
    raise SystemExit
