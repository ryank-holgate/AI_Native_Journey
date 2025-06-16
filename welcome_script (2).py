#!/usr/bin/env python3
import random
import time

def get_time_greeting():
    """Return appropriate greeting based on time of day"""
    from datetime import datetime
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good evening"

def print_with_border(message, char="="):
    """Print message with decorative border"""
    print(char * len(message))
    print(message)
    print(char * len(message))

def typing_effect(text, delay=0.03):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    # Welcome animation
    print("\n🎉 Welcome to Ryan's Interactive Greeting System! 🎉")
    time.sleep(1)
    
    # Get user information
    print("\nLet me get to know you better...")
    user_name = input("What's your name? ").strip()
    
    # Validate name input
    while not user_name:
        user_name = input("Please enter your name: ").strip()
    
    # Get more details
    print(f"\nNice to meet you, {user_name}!")
    
    # Ask for mood
    print("\nHow are you feeling today?")
    print("1. Great!")
    print("2. Okay")
    print("3. Not so good")
    print("4. Excited!")
    
    mood_choice = input("Choose 1-4: ").strip()
    
    mood_responses = {
        "1": "That's awesome! Your positive energy is contagious! 🌟",
        "2": "That's perfectly fine! Every day is a new opportunity! 😊",
        "3": "I hope things get better for you! You've got this! 💪",
        "4": "Your excitement is amazing! Let's keep that energy going! 🚀"
    }
    
    # Get user's interest
    print(f"\nWhat brings you here today, {user_name}?")
    print("1. Learning to code")
    print("2. Just exploring")
    print("3. Working on a project")
    print("4. Having fun")
    
    interest_choice = input("Choose 1-4: ").strip()
    
    interest_responses = {
        "1": "Coding is such an exciting journey! Every line of code is a step forward! 👨‍💻",
        "2": "Exploration is the best way to learn! Keep that curiosity alive! 🔍",
        "3": "Projects are where the magic happens! Hope it goes amazingly! 🛠️",
        "4": "Fun is the best motivation! Enjoy every moment! 🎈"
    }
    
    # Time-based greeting
    time_greeting = get_time_greeting()
    
    # Create Ryan's personalized introduction
    print("\n" + "="*60)
    typing_effect(f"{time_greeting}, {user_name}!")
    typing_effect("My name is Ryan and I am absolutely delighted to have you here!")
    
    # Respond to mood
    mood_response = mood_responses.get(mood_choice, "Thanks for sharing! 😊")
    typing_effect(mood_response)
    
    # Respond to interest
    interest_response = interest_responses.get(interest_choice, "Whatever you're up to, I'm here to help! 🤝")
    typing_effect(interest_response)
    
    print("="*60)
    
    # Fun interactive features
    print(f"\n{user_name}, would you like to:")
    print("1. Get a random motivational quote")
    print("2. Play a quick guessing game")
    print("3. Get a fun fact")
    print("4. Just chat")
    
    activity_choice = input("Choose 1-4 (or press Enter to skip): ").strip()
    
    if activity_choice == "1":
        quotes = [
            "The best time to plant a tree was 20 years ago. The second best time is now!",
            "You are capable of amazing things!",
            "Every expert was once a beginner!",
            "Progress, not perfection!",
            "Your potential is endless!"
        ]
        print(f"\n💫 Here's your quote: {random.choice(quotes)}")
        
    elif activity_choice == "2":
        print(f"\n🎮 Quick game, {user_name}!")
        secret_number = random.randint(1, 10)
        guess = input("I'm thinking of a number between 1-10. What's your guess? ")
        try:
            if int(guess) == secret_number:
                print(f"🎉 Amazing! You got it! The number was {secret_number}!")
            else:
                print(f"Good try! The number was {secret_number}. You're awesome anyway! 🌟")
        except ValueError:
            print(f"That's okay! The number was {secret_number}. Thanks for playing! 😊")
            
    elif activity_choice == "3":
        facts = [
            "Honey never spoils! Archaeologists have found edible honey in Egyptian tombs!",
            "A group of flamingos is called a 'flamboyance'!",
            "Bananas are berries, but strawberries aren't!",
            "The shortest war in history lasted only 38-45 minutes!",
            "Octopuses have three hearts and blue blood!"
        ]
        print(f"\n🤓 Fun fact: {random.choice(facts)}")
        
    elif activity_choice == "4":
        print(f"\n💬 {user_name}, it's been wonderful chatting with you!")
        print("Feel free to run this script again anytime you want to chat!")
    
    # Farewell message
    print(f"\n🌈 Thanks for spending time with me today, {user_name}!")
    print("Remember: You're doing great, and I believe in you!")
    
    # Ask if they want to save their session
    save_choice = input(f"\nWould you like me to remember your name for next time? (y/n): ").lower().strip()
    if save_choice == 'y':
        try:
            with open('user_greeting.txt', 'w') as f:
                f.write(f"Last user: {user_name}\nMood: {mood_choice}\nInterest: {interest_choice}")
            print("Great! I'll remember you next time! 📝")
        except:
            print("Couldn't save the info, but that's okay! 😊")
    
    print("\nHave an amazing day! 🎊")

if __name__ == "__main__":
    main()