import sys
if len(sys.argv) != 2:
    print("none")
else:
    x = input("What was the parameter? ")
    if x ==sys.argv[1]:
        print("Good Job!")
    else:
        print("Nope, sorry...")
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell05/ex10/parameter_matching.py "BOMOMO"