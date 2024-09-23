# ucln dạng cộng trừ
def ucln1(a,b):
    while a!=b:
        if a >b:
            a -= b
        else:
            b -= a
    return a
#ucln dạng chia
def ucln2(a,b):
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b
a,b=map(int,input('Nhập 2 số a ,b: ').split())
print("Kết quả",ucln1(a,b))
print("Kết quả",ucln2(a,b))
print(f'Ươc chung lớn nhất của {a} và {b} là ',ucln1(a,b))