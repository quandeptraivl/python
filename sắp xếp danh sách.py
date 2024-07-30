# Sắp xếp 
def sapxep(A):  
    n = len(A)  
    for i in range(n):  
        min_index = i  # Đổi tên biến để rõ nghĩa hơn  
        for j in range(i + 1, n):  
            if A[j] < A[min_index]:  # So sánh với A[min_index] thay vì A[i]  
                min_index = j  
        # Hoán đổi chỉ khi min_index khác i  
        if min_index != i:  
            A[i], A[min_index] = A[min_index], A[i]  
    return A  

n = int(input('Nhập vào số phần tử của danh sách: '))  
A = []  
for i in range(n):  
    A.append(int(input('Nhập vào phần tử thứ ' + str(i + 1) + ': ')))  
print('Danh sách sau khi được sắp xếp là:', sapxep(A))