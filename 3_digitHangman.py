while True :
	checkProb=True
	prob=input("Problem : ").strip().split(" ")
	if len(prob)!=12:
		checkProb=False
		print("The size of the problem is not equal to 12. Please enter problem again.")
	else :
		for x in prob:
			if not x.isdigit():
				checkProb=False
				print("Something in the Problem isn't a number. Please enter problem again.")
				break
	if checkProb==True:
		break

score=0
ans=["_"]*12
for n in range(5) :
	checkAns=False
	while True:
		guess=input("Guess "+str(n+1)+" : ").strip()
		if guess.isdigit():
			break
		print("There isn't a number. Please guess again.")

	for i in range(len(prob)) :
		if prob[i]==guess :
			if ans[i]=="_":
				score+=1
			ans[i]=guess
			checkAns=True
			
	if checkAns==False : 
		ans.append(guess)

	print(" ".join(ans))
print("score : "+str(score))