print("Welcome to the Geography Quiz!")

playing = input("Would you like to play my geography game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
user_score = 0 



answer = input("What is the capital of Lebanon? ")
if answer.lower() == "beirut":
        print("Amazing! Correct")
        user_score +=  1 
else:
     print("incorrect")

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
        print("Amazing! Correct")
        user_score +=  1 

else:
     print("incorrect")

answer = input("What is largest country in the world? ")
if answer.lower() == "russia":
        print("Amazing! Correct")
        user_score +=  1 

else:
     print("incorrect")


answer = input("What is most populous country in the world? ")
if answer.lower() == "china":
        print("Amazing! Correct")
        user_score +=  1 

else:
     print("incorrect")



print("You got " + str(user_score) + " questions correct!")
print("You got " + str(user_score*25) + "%" + " of the quiz correct!")







