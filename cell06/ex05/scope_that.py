def add_one(num):
    num += 1
    print(f"Inside function: {num}")
x = 5
print(f"Before function: {x}")
add_one(x)
print(f"After function: {x}")
#ทำในฟังชั้นไม่มีผลต่อตัวแปรglobal ถ้าอยากให้มีผลต้อง x= add_one(x) มันจะทับค่าตัวแปรglobalทำให้มันมีผล
