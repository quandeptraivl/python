def fibonacy(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacy(n-1) + fibonacy(n-2)
print(fibonacy(int(input('Nhập số n: '))))