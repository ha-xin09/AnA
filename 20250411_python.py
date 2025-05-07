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
    tmp = 0
    
    for i in range(3):
      
        if a > b:
            tmp = a
            a = b
            b = tmp

        if b > c:
            tmp = b
            b = c
            c = tmp

        if a > b:
            tmp = a
            a = b
            b = tmp
    return a,b,c

print(sort(3, 1, 2))