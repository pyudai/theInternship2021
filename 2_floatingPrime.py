def isprime(num):
	i=2
	while i<num:
		if not num%i:
			return False
		i+=1
	return True

while True :
	num=""
	while True :
		check=True 
		num=input("num : ").strip()
		try:
			floating=float(num)
		except ValueError:
			check=False
			print("Could not convert data to a float.")
			continue

		if len(num) >= 12+1+1:
			check=False
			print("Length not less than or equal 12.")
		elif (floating<=1.0 or floating >=10.0) and num!="0.0" : 
			check=False
			# if num=="0.0":
			# 	check=True
			# else :
			print("There isn't between 1.0 to 10.0 .")
		if check==True :
			break 

	if num=="0.0":
		break
	test=num.split(".")
	while len(test[1])< 3:
		test[1]+="0"
	for i in range(3):
		test[0]+=test[1][i]
		if isprime(int(test[0])):
			print("TRUE")
			break
		if i==2 and not isprime(int(test[0])):
			print("FALSE")
		i+=1 