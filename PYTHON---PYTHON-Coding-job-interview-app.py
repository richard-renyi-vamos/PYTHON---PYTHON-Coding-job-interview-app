import random
import time

def coding_challenges():
    challenges = {
        "Easy": [
            ("Reverse a string", "def reverse_string(s): return s[::-1]"),
            ("Find the max number in a list", "def max_number(lst): return max(lst)")
        ],
        "Medium": [
            ("Check if a number is prime", "def is_prime(n): return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))"),
            ("Find the factorial of a number", "def factorial(n): return 1 if n == 0 else n * factorial(n-1)")
        ],
        "Hard": [
            ("Implement a basic LRU Cache", "Use collections.OrderedDict"),
            ("Solve the Two Sum problem", "Use a dictionary to track indices")
        ]
    }
    difficulty = input("Choose difficulty (Easy/Medium/Hard): ").capitalize()
    if difficulty in challenges:
        challenge, solution = random.choice(challenges[difficulty])
        print(f"Your challenge: {challenge}\nTry to code it yourself!")
        input("Press Enter to see the solution...")
        print(f"Suggested Solution:\n{solution}")
    else:
        print("Invalid choice!")

def mcq_questions():
    questions = [
        ("What is the output of 'print(2 ** 3)'?", "A) 5  B) 8  C) 6", "B"),
        ("Which keyword is used to define a function in Python?", "A) func  B) def  C) lambda", "B")
    ]
    question, options, answer = random.choice(questions)
    print(question)
    print(options)
    user_answer = input("Your answer: ").strip().upper()
    if user_answer == answer:
        print("Correct! 🎉")
    else:
        print(f"Wrong! The correct answer is {answer}")

def practice_timer():
    duration = int(input("Set a timer for how many minutes? "))
    print(f"Starting timer for {duration} minutes...")
    time.sleep(duration * 60)
    print("Time's up! ⏳")

def main():
    while True:
        print("\nPython Interview Prep")
        print("1. Coding Challenges")
        print("2. Multiple Choice Questions")
        print("3. Practice Timer")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            coding_challenges()
        elif choice == "2":
            mcq_questions()
        elif choice == "3":
            practice_timer()
        elif choice == "4":
            print("Good luck with your interview! 🚀")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
