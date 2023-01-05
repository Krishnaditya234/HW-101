'''
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
'''
import random
response = "Y"
def a():
    while response == "Y":
        no = random.randint(1,6)
        if no == 1:
            print("[-----]") 
            print("[     ]") 
            print("[  0  ]") 
            print("[     ]") 
            print("[-----]")
        if no == 2: 
            print("[-----]") 
            print("[ 0   ]") 
            print("[     ]") 
            print("[   0 ]") 
            print("[-----]") 
        if no == 3: 
            print("[-----]") 
            print("[     ]") 
            print("[0 0 0]") 
            print("[     ]") 
            print("[-----]") 
        if no == 4: 
            print("[-----]") 
            print("[0   0]") 
            print("[     ]") 
            print("[0   0]") 
            print("[-----]") 
        if no == 5: 
            print("[-----]") 
            print("[0   0]") 
            print("[  0  ]") 
            print("[0   0]") 
            print("[-----]") 
        if no == 6: 
            print("[-----]") 
            print("[0 0 0]") 
            print("[     ]") 
            print("[0 0 0]") 
            print("[-----]")
        break
a()
while True:
    response = input("Press Y is roll again N to exit : ")
    if response == "Y":
        a()
    else:
        print("Exiting......")
        raise SystemExit

