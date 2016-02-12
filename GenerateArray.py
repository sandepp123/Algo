#Generates arrays of random numbers and calculates Sorting time
import random
import timeit
from MergeSort import MerseSort
i=2
target=open("Sortingtime.txt",'w')

while i<=100000:
	k=[random.randint(0,100000) for j in xrange(i)]
	start=timeit.default_timer()
	#print "unsorted", k
	k=MerseSort(k)
	stop=timeit.default_timer()
	print i,stop-start

	#print "sorted", k
	target.write(str(i)+"\t"+str(stop-start)+"\n")
	i=i+10

target.close()