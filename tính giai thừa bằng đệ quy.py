# Dùng đệ quy để tính giai thừa
def giaithua(x):
    if x==0:
        return 1
    return x*giaithua(x-1)
x=int(input('Bạn cần tính giai thừa của '))
result=giaithua(x)
print(f'Giai thừa của {x} là {result}')