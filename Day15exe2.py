import time

# Get the current hour in 24-hour format
current_hour = int(time.strftime("%H"))

# Greet based on the hour
if current_hour < 12:
    print("Good Morning")
elif 12 <= current_hour < 18:
    print("Good Afternoon")
elif 18 <= current_hour < 22:
    print("Good Evening")
else:
    print("Good Night")