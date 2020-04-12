k=int(input())
for i in range(k):
	l=int(input())
	arr=list(map(int,input().split(" ")))
	a=0
	b=0
	am=min(arr)
	bm=min(arr)
	if(arr[0]==am):
		a=a+1
	for j in arr:
		if(j>am):
			a=a+1
			am=j
		if(j>=bm):
			b=b+1
			bm=j
	print(b-a)		
				
