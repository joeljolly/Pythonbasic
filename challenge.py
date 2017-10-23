
num =0
lis = []
print("Enter the number limit of list")
count=int(input())
print ("Enter the list :")
for i in range(0,count):
	temp = int(input())
	lis.append(temp)

print("Enter the number of commands")
n= int(input())
for j in range(0,n):
	print("Enter command : ")
	comm = input()
	comm2= comm.split(" ")
	if(comm2[0]=="append"):
		tm=int(comm2[1])
		lis.append(tm)
	elif(comm2[0]=="reverse"):
		lis.reverse()
	elif(comm2[0]=="sort"):
		lis.sort()
	elif(comm2[0]=="pop"):
		lis.pop()
	elif(comm2[0]=="print"):
		print(lis)
	elif(comm2[0]=="count"):
		tm=int(comm2[1])
		print(lis.count(tm))

