n=0
while True:
	n=input("Amount of words : ")
	if n.isdigit() :
		break
	print("Input isn't number. Please enter input again.")

i=0
ans=[]
while i < int(n) :

	while True :
		words = input("Words "+str(i+1)+" : ").strip().split(" ")
		check=True
		for j in range(len(words)):
			for k in range(len(words[j])):
				if words[j][k].isdigit():
					check=False
					break
			if check==False:
				break
		if check==True:
			break
		print("Words can't contain number. Please enter agian.")

	j=0
	Acronym=""
	while j < len(words):
		if words[j][0].isupper() :
			Acronym+=words[j][0]
		j+=1
	ans.append(Acronym)
	i+=1
ans.sort(key=lambda x: (len(x), x))
i=0
while i < len(ans):
	print(ans[i])
	i+=1 