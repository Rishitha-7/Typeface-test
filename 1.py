n=int(input())
q=1
s=""
while q!=0:
	r=n%3
	q=n//3
	n=q
	s=s+str(r)
print(s)