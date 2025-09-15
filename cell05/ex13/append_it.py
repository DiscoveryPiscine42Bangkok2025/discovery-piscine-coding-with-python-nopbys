import sys
if len(sys.argv) < 2 :
    print("none")  
else:
    for i in range(1,len(sys.argv)):
        if sys.argv[i].endswith("ism"):
            continue
        else:
            sys.argv[i] += "ism"
            print(sys.argv[i])
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell05/ex13/append_it.py "BOMOMOzzzZz" "egoism" "pepo" "human"