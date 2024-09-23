danhba={}
def themdanhba():
    ten=input('Nhập tên người liên hệ: ')
    sdt=input("Nhập số điện thoại người liên hệ: ")
    danhba[ten]=sdt
def xemdanhba():
    for x,y in danhba.items():
        print(f"Tên người dùng: {x}  \nSố điện thoại :{str(y)}\n" )
while True:
    print("1.Thêm liên hệ ")
    print("2.xem danh bạ ")
    print("3.Thoát ")
    chose=input('\nNhập lựa chọn của bạn: ')
    if chose== "1":
        themdanhba()
    elif chose== "2":
        xemdanhba()
    elif chose== "3":
        break