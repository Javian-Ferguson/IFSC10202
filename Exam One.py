import random

print("=== Welcome to Winners and Losers Game ===")  # Title of the game

# Initialize scores
human_score = 0
computer_score = 0

# Play 5 rounds
for round_num in range(1, 6):
    print("\n--- Round {} ---".format(round_num))  # Display round number

    # Human input
    human_choice = int(input("Enter a number between 1 and 5: "))

    # Computer random choice
    computer_choice = random.randint(1, 5)

    # Display guesses
    print("Human chose: {}".format(human_choice))
    print("Computer chose: {}".format(computer_choice))

    # Calculate sum
    total = human_choice + computer_choice
    print("Sum = {}".format(total))

    # Determine even/odd and award points
    if total % 2 == 0:
        print("Sum is Even → Human scores a point!")
        human_score += 1
    else:
        print("Sum is Odd → Computer scores a point!")
        computer_score += 1

    # Display current scores
    print("Current Scores → Human: {} | Computer: {}".format(human_score, computer_score))

# Final Result
print("\n=== Final Result ===")
if human_score > computer_score:
    print("Human Wins 🎉")
elif computer_score > human_score:
    print("Computer Wins 🤖")
else:
    print("It's a Tie!")
