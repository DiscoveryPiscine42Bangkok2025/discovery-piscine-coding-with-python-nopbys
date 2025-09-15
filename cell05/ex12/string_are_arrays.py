import sys
count = 0
if len(sys.argv) > 2 or len(sys.argv)==1:
    print("none")
else:
    word = sys.argv[1]
    count = word.count('z')
    print(f"z"*count)
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell05/ex12/string_are_arrays.py "BOMOMOzzzZz"