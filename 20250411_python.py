# def makefishShapeBun(taste):
#     print(f"{taste}맛 붕어빵 완성!")
#     print("맛있게 드세요")

# makefishShapeBun("팥")
# makefishShapeBun("슈크림")



# x = 10

# def example():
#     x=20
#     print(x)

# example()
# print(x)



# def for10(a):
#     for i in range(10):
#         print(f"{a}")

# for10("HelloWorld")




def sort(a, b, c):
    if (a>=b and b>=c):
        print(sort(c, b, a))
    elif (b>=a and a>=c):
        print(sort(c, a, b))
    elif (c>=a and a>=b):
        print(sort(b, a, c))
    elif (a>=c and c>=b):
        print(sort(b, c, a))
    elif (c>=b and b>=a):
        print(sort(a, b, c))
    elif (b>=c and c>=a):
        print(sort(a, c, b))


#print(sort(3, 1, 2))