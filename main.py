import random  # Importing random module to allow the computer to make random choices

# 🎮 Game Introduction
print("Welcome to Snake-Water-Gun Game!")
print("Instructions: Type 's' for Snake, 'w' for Water, 'g' for Gun")

# 🧮 Initialize scores
count_computer = 0
count_you = 0

# 🔁 Ask user how many rounds they want to play
limit = int(input("Enter how many times you want to play with the computer: "))
no_of_round = 0

# 🗺️ Create dictionaries to map user input and choices
youdict = {'s': 1, 'w': -1, 'g': 0}
reversedict = {1: 'Snake', -1: 'Water', 0: 'Gun'}

# 🎯 Main game loop
while no_of_round < limit:
    computer = random.choice([1, -1, 0])  # Computer randomly selects a choice
    youstr = input("\nEnter Your Choice (s/w/g): ").lower()  # User input

    # ❌ Input validation
    if youstr not in youdict:
        print("❌ Invalid input! Please enter 's', 'w', or 'g'.")
        continue  # Skip invalid input without increasing the round count

    you = youdict[youstr]  # Convert user input to numerical form for comparison

    # 🧾 Display choices
    print(f"Computer chose {reversedict[computer]}, You chose {reversedict[you]}.")

    # 🥊 Game logic to determine the winner
    if computer == you:
        print("🤝 It's a Draw!")  # Both chose same
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        print("💻 Computer Wins this round!")  # Conditions where computer wins
        count_computer += 1
    else:
        print("🎉 You Win this round!")  # All other valid cases where user wins
        count_you += 1

    # 📊 Show current scores
    print(f"🏆 Scores => You: {count_you} | Computer: {count_computer}")
    no_of_round += 1  # Move to next round

# 🏁 Game Over and Final Results
print("\n🔚 Game Over!")
print("🎯 Final Scores:")
print(f"🧑 You: {count_you} | 💻 Computer: {count_computer}")

# 🏆 Declare the overall winner
if count_computer > count_you:
    print("💻 Computer is the Overall Winner!")
elif count_you > count_computer:
    print("🎉 Congratulations! You are the Overall Winner!")
else:
    print("🤝 It's a Tie Overall!")  # Both have equal scores
