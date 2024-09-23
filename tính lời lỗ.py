total_profit=0
with open ('test1.txt','r') as in_p, open ('test2.txt','w') as out_p:
    N=int(in_p.readline())
    for i in range(N):
        M,B=map(int,in_p.readline().split())
        profit=B-M
        total_profit+=profit
    out_p.write(str(total_profit))

