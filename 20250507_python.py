# class Hello:
#     def hello_world(self):
#         print("Hello World!")

# a = Hello()
# a.hello_world()


# class Hfgn:
#     def ghfnvn(self):
#         for i in range(10):
#             for j in range(i+1):
#                 print("*",end="")
#             print()
# a = Hfgn()
# a.ghfnvn()


# class Member:
#     def __init__(self, name):
#         self.name = name

#     def member_me(self):
#         print("제 이름은 {} 입니다.".format(self.name))

# a = Member("나하진")
# a.member_me()


# class MyInfo:
#     def __init__(self, name, age, home):
#         self.name = name
#         self.age = age
#         self.home = home
#     def member_me(self):
#         print("제 이름은 {0}이고, 나이는 {1}살, 사는곳은 {2}입니다.".format(self.name, self.age, self.home))

# a = MyInfo("나하진", "17", "서울")
# a.member_me()


class Bread:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def buy(self):
        if self.stock <= 0:
            print("재고가 없습니다.")
        else:
            print("구매해주셔서 감사합니다.")
            self.stock -= 1

    def bake(self, stock):
        self.stock += stock
        print(f"{self.name}을/를 {stock}개 만들었습니다.")



class Bun(Bread):
    def __init__(self, name, price, stock, inside):
        super().__init__(name, price, stock)
        self.inside = inside

    def buy(self):
        super().buy()

    def bake(self, stock):
        print("만들기 실패!")

a = Bread("붕어빵", 1000000, 1000000)
a.bake(4)
for i in range(15):
    a.buy()

b = Bun("슈붕", 1500000, 5000, "슈크림")
b.bake(3)
for i in range(10):
    b.buy()
