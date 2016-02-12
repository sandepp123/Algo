def MerseSort(alist):
	#print ("Spliting Data array",alist)
	
	if len(alist)>1 :
		mid = len(alist)//2
		left = alist[:mid]
		right= alist[mid:]
		MerseSort(left)
		MerseSort(right)
		Merge(left,right,alist)
		return alist
	else:
		return alist;	
def Merge(list1,list2,alist):
	i=0
	j=0
	k=0
	m=[]
	while i<len(list1) and j<len(list2):
		if list1[i]<list2[j]:
			alist[k]=list1[i]
			i=i+1
		else:
			alist[k]=list2[j]
			j=j+1
		k=k+1
	while i<len(list1):
		alist[k]=list1[i]
		i=i+1
	while j<len(list2):
		alist[k]=list2[j]
		j=j+1
	#print ("merging ",alist)

#alist =[54,26,93,17,17,31,44,55,20]
#MerseSort(alist)
#print alist

