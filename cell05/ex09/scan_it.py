import sys
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    count = text.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell05/ex09/scan_it.py "the" "the the the"
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell05/ex09/scan_it.py "the"