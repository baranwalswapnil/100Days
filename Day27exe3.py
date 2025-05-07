questions = [
    ("What is the capital of Australia?", "a) Sydney", "b) Melbourne", "c) Canberra", "d) Brisbane", "c", 5000),
    ("Who wrote Romeo and Juliet?", "a) William Wordsworth", "b) William Shakespeare", "c) Charles Dickens", "d) Jane Austen", "b", 10000)
]

total_winnings = 0

for question in questions:
    print(question[0])
    for option in question[1:5]:
        print(option)
    
    answer = input("Your answer: ").strip().lower()
    
    if answer == question[5]:
        total_winnings += question[6]
        print(f"Correct! You won {question[6]} Rs. Total: {total_winnings} Rs\n")
    else:
        print("Wrong answer! Game Over.")
        break