# QUIZ APPLICATION
import random


def quiz_app():
    # Group questions by difficulty
    quiz_pool = {
        "easy": [
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What color is the sky?", "answer": "blue"},
            {"question": "How many days are in a regular year?", "answer": "365"}
        ],
        "medium": [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "How many continents are there?", "answer": "7"},
            {"question": "Which planet is closest to the sun?", "answer": "Mercury"}
        ],
        "hard": [
            {"question": "What is the chemical symbol for Gold?", "answer": "Au"},
            {"question": "Who developed the theory of relativity?", "answer": "Einstein"},
            {"question": "Find the larger real value of x for x^4 - 4x^3 + 5x^2 - 4x + 1 = 0.\nHint: (3 + sqrt(5)) / 2",
             "answer": "(3 + sqrt(5)) / 2"}
        ]
    }

    print("=== Welcome to the Ultimate Quiz App! ===")

    while True:
        # Step 1: Select difficulty
        difficulty = input("\nChoose difficulty (easy, medium, hard): ").strip().lower()
        if difficulty not in quiz_pool:
            print("Invalid choice. Please type easy, medium, or hard.")
            continue

        # Get and shuffle questions for variety
        questions = quiz_pool[difficulty]
        random.shuffle(questions)

        # Step 2: Run the quiz game
        score = 0
        print(f"\n--- Starting {difficulty.upper()} Mode ---")

        for index, q in enumerate(questions, 1):
            print(f"\nQuestion {index}: {q['question']}")
            user_answer = input("Your Answer: ").strip()

            # Case-insensitive answer checking
            if user_answer.lower() == q["answer"].lower():
                print("Correct! 🎉")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['answer']}")

        # Show final score
        print(f"\nQuiz Finished! Your total score: {score}/{len(questions)}")

        # Step 3: Play again option
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye.")
            break


# This line runs the app when you execute the script
if __name__ == "__main__":
    quiz_app()



