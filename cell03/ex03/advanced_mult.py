import sys
if len(sys.argv) > 1 :
    print("none") 
else: 
    for i in range(11):
        print(f"Table de {i}:", end=" ")
        for j in range(11):
            print(i * j, end=" ")
        print()
#C:/Users/pob_r/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pob_r/OneDrive/Desktop/discovery_piscine/cell03/ex03/advanced_mult.py "yolo"