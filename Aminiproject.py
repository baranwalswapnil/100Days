import time
import random

questions = [
    "Would you like to go on a little adventure with me? 🌟",
    "Or maybe, a simple date to spend some time together? 🥰",
    "Imagine us having a cozy night, just you and me... ❤️",
    "So, what do you say? Will you go on a date with me? 💐"
]

# starting ka yes/no
first_answer = input("Hi lady! 😊 Can I ask you a quick question? (yes/no): ").strip().lower()

# Agar haa hai to
if first_answer == "yes":
    # delay wala
    for question in questions:
        print(question)
        time.sleep(2)  # 2-second break

    print("\nI'm waiting for your answer, lady! 💌")
    print()

    # response
    answer = input("Are you coming, miss? 😶😶 (yes/no): ").strip().lower()

    # answer and respond
    if answer == "yes":
        print("Text me then, baby, on WhatsApp 8887175307, and we'll decide the time in privacy 🎉")
    elif answer == "no":
        print("Ok hmmm Koi nhi. Maybe next time! 😔")
    else:
        print("Please answer with 'yes' or 'no'.")
elif first_answer == "no":
    print("Me guchha Bye! 👋")
else:
    print("Please answer with 'yes' or 'no'.")

# Mood check
mood = input("How are you feeling today? (happy/sad/angry/confused): ")

if mood == "happy":
    print("Yay! Spread the happiness like confetti! 🎉")
elif mood == "sad":
    print("Aww, it's okay. Sending you virtual chocolate! 🍫")
elif mood == "angry":
    print("Take a deep breath... and imagine a cute puppy! 🐶")
elif mood == "confused":
    print("It's okay to be confused! That's how I feel about life too... 🤔")
else:
    print("Hmm, that's a new one! Let me grab my emotion dictionary. 📚")

# Jokes section
joke = input("Do you want to hear a joke? (yes/no): ")

while joke.lower() == "yes":
    print("Why don’t scientists trust atoms? Because they make up everything! 😂")
    joke = input("Do you want to hear another one? (yes/no): ")

print("Alright, no more jokes! Have a good day! 😄")

# Sheep counting
sleep_count = int(input("How many sheep do you want to count to sleep? "))

for i in range(1, sleep_count + 1):
    print(f"{i} sheep... 🐑")
    if i == sleep_count:
        print("ZZZ... Goodnight! 😴")

# Compliment section
compliments = ["You have a great sense of humor!", "You are amazing!", 
               "You're as sharp as a tack!", "You have a kind heart!", 
               "You're cooler than a polar bear's toenails!"]

for i in range(len(compliments)):
    user_input = input("Do you want a compliment? (yes/no): ")
    if user_input.lower() == "yes":
        print(compliments[i])
    else:
        print("Okay, no more compliments for now!")
        break

# Magic 8-ball style Q&A
answers = ["Yes!", "Nope.", "Maybe...", "Ask again later.", 
           "Absolutely!", "Not a chance.", "Definitely not.", "Go for it!"]

question = input("Ask me a yes/no question: ")

while question.lower() != "stop":
    print(random.choice(answers))
    question = input("Ask another question or type 'stop' to quit: ")

print("Goodbye, hope you got your answers! 🎱")
