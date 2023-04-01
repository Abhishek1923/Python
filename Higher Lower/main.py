import random
from art import logo,vs
from game_data import data


def ranDetails(account):
  ranName = account['name']
  ranDesc = account["description"]
  ranCountry = account['country']

  return (f"{ranName}, a {ranDesc}, from {ranCountry}.")

def check_guess(guess,aCount,bCount):
        if(aCount>bCount):
                return guess=='A'
        else:
                return guess=='B'

print(logo)
score=0
gameEnds=True
ranVal_b = random.choice(data)

while gameEnds:
	ranVal_a = ranVal_b
	ranVal_b = random.choice(list(data))

	print("Compare A: "+ranDetails(ranVal_a))
	aCount = int(ranVal_a['follower_count'])
	print(vs)
	print("Against B: "+ranDetails(ranVal_b))
	bCount = int(ranVal_b['follower_count'])
	
	guess = input("Who has more followers? Type 'A' or 'B':").upper()

	isCorrect = check_guess(guess, aCount, bCount)

	if isCorrect:
		score+=1
		print(f"You're right! Current Score is: {score}")
	else:
		gameEnds=False
		print(f"Sorry, you're wrong. Final Score is: {score}")

