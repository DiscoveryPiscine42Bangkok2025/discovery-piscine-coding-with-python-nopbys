def greetings(a="noble stranger"):
    if type(a) != str:
        print("Error! It was not a name.")
    else:
        print(f"Hello , {a}.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
