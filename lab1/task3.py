n = int(input())

lst = []
i = n
while i > 0:
    lst.append(i)
    i -= 1
print("Numbers from 1 to n in reversed order:", *lst)

ans = 1
i = 2
while i <= n:
    ans *= i
    i += 1
print("Factorial of number n:", ans)