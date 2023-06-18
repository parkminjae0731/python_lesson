## 함수

#### 27866번
>단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.

```python
def solve(s, i):
    ans = s[i-1]

    return ans

s = input()
i = int(input())

print(solve(s, i))
```

---


#### 2743번
>알파벳으로만 이루어진 단어를 입력받아, 그 길이를 출력하는 프로그램을 작성하시오.

```python
def s(b):
    aa=len(b)
    return aa
b=input()
print(s(b))
```

---


#### 9086번
>문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

```python
def s(a,b):
    ad=b[0]+b[len(b)-1]
    return ad
a=int(input())

for i in range(a):
    b=input()
    print(s(a,b))
```

---


#### 11654번
>알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

```python
def s(a):
    ad=ord(a)
    return ad
a=input()
print(s(a))
```

---


#### 11720번
>N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

```python
def solve(a):
    s = 0
    for c in a:
        s += int(c)
    return s

input()
a = input()

print(solve(a))
```

---


#### 10809번
>알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

```python
def q(s):
    alp = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alp)):
        if alp[i] in s:
            print(s.index(alp[i]),end=' ')
        else :
            print(-1,end=' ')
s = input()
q(s)
```

---


#### 2675번
>문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

```python
def s(n):
    a, b = map(str, input().split())   
    for i in range(len(b)):
        print(b[i] * int(a), end='')
    print()
n=int(input())
for i in range(n):
    s(n)
```

---


#### 5622번
>상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.



전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

```python
def p(s):
    base=["ABC", "DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ" ]
    c=0
    a=[0]*len(base)
    for i in range(len(base)):
        for u in s:
            if u in base[i]:
                c+=i+3
    print(c)
s=str(input())
p(s)
```
