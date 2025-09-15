import sys
def downcase_all(a):
    return a.lower()
if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1,len(sys.argv)):
        print(downcase_all(sys.argv[i]))
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell06/ex02/downcase_all.py "BOMOMOzzzZz" "POPOPO" "LOLOLO" "TOTO"