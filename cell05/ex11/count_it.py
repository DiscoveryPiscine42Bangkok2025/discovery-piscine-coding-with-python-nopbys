import sys
if len(sys.argv) < 2 :
    print("none")
else:
    num_params = len(sys.argv) - 1
    for i in range(len(sys.argv)):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell05/ex11/count_it.py "BOMOMO" "luffy" "mario"