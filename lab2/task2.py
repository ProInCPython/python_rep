try:
    a, b = list(map(int, input().split()))
    y = a/b
except ZeroDivisionError:
    print("Zero division error!")
except TypeError:
    print("Wrong input data format!")
except:
    print("Other error(s)")
else:
    print(y)
