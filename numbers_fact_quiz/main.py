import requests


def get_facts(number):
    url = f"http://numbersapi.com/{number}/trivia"
    response = requests.get(url)
    return response.text


def main():
    print("--Welcome to number trivia facts--\n")
    while True:
        facts_input = input("Enter a number that you want to know an interesting fact ( q to quit): ")
        if facts_input.lower() == "q":
            break
        try:
            number = int(facts_input)
            fact = get_facts(number)
            print(fact)
        except ValueError:
            print(purple("That is not a number, please try again!"))


def purple(text):
    return f"\033[95m{text}\033[0m"


if __name__ == "__main__":
    main()
