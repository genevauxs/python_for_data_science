point = (0,0)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On the X-Axis at X = {x}")
    case (0, y):
        print(f"On the Y-Axis at Y = {y}")
    case _:
        print("Somewhere on plane")

a = list(range(10))
print(a[-9::])
print(a[-9::-1])
