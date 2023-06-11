# 개발자
# 프로그래머

# 프로그램?
# 입력 > 계산 > 출력

# 좋은 프로그램을 만들 수 있을까??

# 함수
# y = ax + b :
# y = 3x + 10 : (1, 13), (2, 16)

# def add(a, b): 
#     c = a + b
#     return c

# def sub(a, b):
#     c = a - b
#     return c

# ******중복성의 제거
# 이쁘게 하기 위해서

def hello(name):
    print("----")
    print("안녕하세요")
    print(name)
    print("님!!")
    print("----")

def bye(name):
    print("잘가세요")
    print(name)
    print("님!!")
    print("----")

for i in range(5):
    n = input()
    hello(n)
    bye(n)
    