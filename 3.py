n = int(input())
flag=True
i,c=1,0
while flag:
    y=False
    for x in str(i):
        if x=='0' or x=='1' or x=='2' or x=='5' or x=='6' or x=='8' or x=='9':
            y=True
        else:
            y=False
    if y==True:
        c=c+1
    if c==n:
        print(i)
    i=i+1