# Tìm kiếm nhị phân
def binarysearch(A,k):
    low=0
    high=len(A)
    mid=0
    while low <high:
        mid=(low+high)//2
        if A[mid]==k:
            return mid
        if A[mid]>k:
            high=mid-1
        if A[mid]<k:
            low=mid+1
    return -1
n= int(input('Nhập vào sô phần tử của danh sách '))
A=[]
for i in range(n):
    A.append(int(input('Nhập vào phần tử thứ '+ str(i+1) +': ')))
A.sort()
k=int(input('Hãy nhập vào k '))
result = binarysearch(A,k)
if result == -1:
    print(f' Không có giá trị {k} trong danh sách')
else:
    print(f" Giá trị của {k} trong danh sách là {result}")