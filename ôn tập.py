#1  ****Đảo ngược chuỗi trong Python
print('Bài 1')
A='abcdef'
B=A[::-1]
print(B)
#2 ****Viết hoa ký tự đầu của mỗi từ 
print('Bài 2')
A='abcdef'
A=A.title()
print(A)
#3 ****Loại bỏ các ký tự trùng lặp trong 1 chuỗi
print('Bài 3')
my_string = "aavvccccddddeee"

# Chuyển chu>ỗi thành một set
temp_set = set(my_string)

# Chuyển set thành một chuỗi sử dụng join
new_string = ''.join(temp_set)

print(new_string)
# Vì set không có thứ tự
# nên thứ tự chuỗi mới nhận được là ngẫu nhiên


#4 ****Tạo 1 list mới dựa vào list cũ
print('Bài 4')

original_list = [1,2,3,4]

new_list = [3*x for x in original_list]

print(new_list)

#5 ***hoán đổi giá trị của 2 biến
print('Bài 5')
a=1
b=2
a,b=b,a

#6 ***tách chuỗi thành 1 list
print('Bài 6')
string_1 = "tôi tên là Đỗ Minh Quân "
string_2 =  "học/sinh/lớp/11B4"

# Tách chuỗi mặc định sẽ tách từ khoảng trắng ' '
print(string_1.split())

# Tách chuỗi từ ký tự '/'
print(string_2.split('/'))

#7 Nối danh sách thành chuỗi
print('Bài 7')
list=['tôi', 'tên', 'là', 'Đỗ', 'Minh', 'Quân']
print(' '.join(list))

#8 Kiểm tra chuỗi đối xứng
print('Bài 8')
A='abcdcba'
if A==A[::-1]:
    print('Chuỗi đối xứng')
else:
    print('Chuỗi không đối xứng')


#9 Tính số lần xuất hiện của các phần tử trong một List
print('Bài 9')
A=['a','a','b','b','b','c','b','c','b','a','a']
from collections import Counter
count=Counter(A)
print(count)
print(count['b'])
print(count.most_common(1))

#10 Kiểm tra đảo chữ
print('Bài 10')
str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, cnt_3  = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print('1 và 2 Đảo chữ')
if cnt_1 == cnt_3:
    print('1 và 3 Đảo chữ')

#11 chạy mà khồng tính đến lỗi
print('Bài 11')
a, b = 1,0

try:
    print(a/b)
    # Ngoại lệ xảy ra khi b == 0
except ZeroDivisionError:
    print("Chia cho số 0")
else:
    print("Không có ngoại lệ xảy ra")
finally:
    print("Luôn luôn chạy lệnh này!")

#12 hợp nhất hai dic
print('Bài 12')

dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
#13 Tính tời gian thực thi 1 đoạn code
print('Bài 13')
import time 

start = time.time()

for i in range(5):
    print(5-i)
end=time.time()

time_use= (end-start)
print(time_use,'giây')

#14 chọn phần tử ngẫu nhiên từ danh sách
print('Bài 14')
my_list=[1,2,4,5,76,8,0,42,1,4,6,7]
import random 
number=2
samples = random.sample(my_list, number)
print(samples)

#15 Chuyển 1 số thành danh sách các số
print('Bài 15')
num = 123456789
list_num= [int(x) for x in (str(num))]
print(list_num)

#16 Kiểm tra tính duy nhát của phần tử
print('Bài 16')
def unique(l):
    if len(l)==len(set(l)):
        print('Không phần tử nào trùng nhau')
    else:
        print('có phần tử trùng nhau')
unique([1,2,3,4])  
unique([1,2,3,4,1])      
