a = "a"
while True:
    a = input("Enter something: ")
    typ = (eval(a)).__class__
    print(a)
    print(type(a))
    print(typ(a))
    print(type(typ(a)))d831873a-3bf7-4128-ab0a-1e1a7ce568f8
