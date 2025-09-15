import sys
def shrink(s):
    print(s[:8])
def enlarge(s):
    s = s + 'Z' * (8 - len(s))
    print(s)
if len(sys.argv) < 2:
    print("none")
else:
    for i in sys.argv[1:]:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(i)
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell06/ex04/methods_everywhere.py 'lol' 'physically' 'backpack' 