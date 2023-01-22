#Ask if user wants to play
#condition to continue to quiz or end
#create a container to store user score
#Ask questions and store correct or incorrect scores
#show users score with percentage

states_and_capitals = [
    {"state": "Abia", "capital": "Umauhia"},
    {"state": "Adamawa", "capital": "Yola"},
    {"state": "Akwa Ibom", "capital": "Uyo"},
    {"state": "Anambra", "capital": "Awka"},
    {"state": "Bauchi", "capital": "Bauchi"},
    {"state": "Bayelsa", "capital": "Yenagoa"},
    {"state": "Benue", "capital": "Markurdi"},
    {"state": "Borno", "capital": "Maiduguri"},
    {"state": "Cross River", "capital": "Calabar"},
    {"state": "Delta", "capital": "Asaba"},
    {"state": "Ebonyi", "capital": "Abakaliki"},
    {"state": "Edo", "capital": "Benin"},
    {"state": "Ekiti", "capital": "Ado-Ekiti"},
    {"state": "Enugu", "capital": "Enugu"},
    {"state": "Gombe", "capital": "Gombe"},
    {"state": "Imo", "capital": "Owerri"},
    {"state": "Jigawa", "capital": "Dutse"},
    {"state": "Kaduna", "capital": "Kaduna"},
    {"state": "Kano", "capital": "Kano"},
    {"state": "Kastina", "capital": "Kastina"}
]

print("Welcome to Inem's State and Capital game? ")
playing = input("Do you want to play. Type 'yes'? ")
if playing == "yes":
    print("Nice!!! Let's play")
else: 
    quit()

score = 0
counter = 0

for state_and_capital in states_and_capitals:
    answer = input(f"What's the capital of {state_and_capital['state']} state? ")
    if answer.capitalize() == state_and_capital['capital']:
        print("correct")
        score += 1
    else:
        print("incorrect")
    counter+=1

percent = (score/counter)*100
        
print ("You got " + str(score) + " answers correct")
print ("Your have " + str(percent) + " %")

if percent >= 80: 
	print("Excellent job")
elif percent >=50:
	print ("Good job")
else: print ("You can do better. Try again!") 
