#tp = ("사과", "바나나", "딸기")

#print(tp[0])
#print(tp[1])
#print(tp[2])


# tp = ("사과", "바나나", "딸기")
# yeayea = ("사과","포도","망고")
# new = tp + yeayea

# print(new)

# tp = ("사과", "바나나", "딸기")

# apple, banana, strawberry = tp
# print(apple)
# print(banana)
# print(strawberry)

# def two(a,b,c):
#     return (a+b, b*c)

# ab, bc = two(2, 4, 5)
# print(ab)
# print(bc)

# try:
#     #실행할 코드
#     pass
# except:
#     pass

# tp = ("사과", "바나나", "딸기")

# try:
#     tp[0] = "포도"
     
# except:
#      print("오류가 발생하였습니다")

tp = ("a", "b", "c")

# try:
#     a = 2 / 0
#     tuple[0] = "g"
     
# except TypeError as e:
#      print(f"오류 내용: {e}")
#except ZeroDivisionError:
#     print("오류2")

try:
    tuple[0] = "g"
     
except TypeError as e:
     print(f"오류 내용: {e}")
finally:
     print("예외 처리 완료")