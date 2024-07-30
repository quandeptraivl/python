# hàm tìm số nguyên tố
def isprime(n):
    if n <=1:
        return False
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return False
    return True
# hàm tím số nguyên tố trong khoảng star end
def prime(start,end):
    A=[]
    if start>end:
        return -1
    for i in range(start,end+1):
        if isprime(i):
            A.append(i)
    return A
    
start = int(input('Nhập vào điểm bắt đầu: '))  
end = int(input('Nhập vào điểm kết thúc: '))
result = prime(start,end)
if result ==-1:
    print(" Dữ liệu nhập vào không hợp lệ ")
else:
    print(f" Dãy số nguyên tố từ {start} đến {end} là {result} ")