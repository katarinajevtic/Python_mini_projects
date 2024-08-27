class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


flashcards = [Flashcard("What is the capital city of France?", "Paris"),
              Flashcard("Which planet is known as the 'Red Planet'?", "Mars"),
              Flashcard("Who wrote the play 'Hamlet'?", "William Shakespeare"),
              Flashcard("What is the largest planet in our solar system?", "Jupiter"),
              Flashcard("Who painted the Mona Lisa?", "Leonardo da Vinci"),
              Flashcard("What is the smallest prime number?", "2"),
              Flashcard("What is the capital city of Japan?", "Tokyo")]


def main():
    score = 0

    print("Welcome to Flashcard Quiz")
    print("Type 'exit' any time you want to exit quiz\n")

    for flashcard in flashcards:
        user_input = input(f"Question: {flashcard.question}\nYour answer: ")

        if user_input.lower() == "exit":
            print("Thank you for playing!")
            break
        if user_input.lower() == flashcard.answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! Correct answer is {flashcard.answer}\n")

    print(f"Your total score is {score}")


if __name__ == '__main__':
    main()
