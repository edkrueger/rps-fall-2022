from random import randint

def is_valid(choice):
	if choice == None:
		return False

	if choice.lower() in {"r", "p", "s"}:
		return True

	return False

def prompt_choice():

	choice = None

	while not is_valid(choice):
		choice = input("Choose R/P/S!") 

	return choice

def prompt_ai():
	return ["r", "p", "s"][(randint(0, 2))]

def check_result(human_choice, ai_choice):
	
	human_choice = human_choice.lower()

	if human_choice == ai_choice:
		return "tie"

	elif (ai_choice == "r" and human_choice == "s") or \
		(ai_choice == "s" and human_choice == "p") or \
		(ai_choice == "p" and human_choice == "r"):
		return "human"
	else:
		return "ai"

def play():

	human_choice = prompt_choice()
	ai_choice = prompt_ai()

	# return 'tie', 'human', 'ai'
	result = check_result(human_choice, ai_choice)

	if result == "human":
		print("You win!")
	elif result == "ai":
		print("You lose!")
	elif result == "tie":
		print("Its a tie")
	else:
		print("Something went wrong!")


if __name__ == "__main__":
	play()