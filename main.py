def prompt_choice():
	return

def prompt_ai():
	return

def check_result(human_choice, ai_choice):
	return
	
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