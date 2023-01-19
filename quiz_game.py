#Ask if user wants to play
#condition to continue to quiz or end
#create a container to store user score
#Ask questions and store correct or incorrect scores
#show users score with percentage


print("Welcome to Inem's State and Capital game? ")

playing = input("Do you want to play. Type 'yes'? ")

if (playing == "yes"):
	print("Nice!!! Let's play")
else: quit()

score = 0

answer = input("Whats the capital of Abia state? ")
if (answer.capitalize() == "Umauhia"):
	print("correct")
	score+=1
else: print("incorrect")


answer = input("Whats the capital of Adamawa state? ")
if (answer.capitalize() == "Yola"):
	print("correct")
	score+=1
else: print("incorrect")	

answer = input("Whats the capital of Akwa Ibom state? ")
if (answer.capitalize() == "Uyo"):
	print("correct")
	score+=1
else: print("incorrect")

answer = input("Whats the capital of Anambra? ")
if (answer.capitalize() == "Awka"):
	print("correct")
	score+=1
else: print("incorrect")

print ("You got " + str(score) + " answers correct")
print ("Your have " + str((score/4)*100) + " %")
percent = (score/4)*100

if percent >= 80: 
	print("Excellent job")
elif percent >=50:
	print ("Good job")
else: print ("You can do better. Try again!") 

