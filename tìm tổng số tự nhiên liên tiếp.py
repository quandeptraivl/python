def timso(N):
    ketqua=[]
    for i in range(1,N//2+1):
        j=i
        tong=i
        while tong<N:
            j+=1
            tong+=j
            if tong==N:
                ketqua.append(list(range(i,j+1)))
    return ketqua
print(timso(9))