def choose_category():
    print("\nCHOOSE QUIZ CATEGORY")
    print("1. General Knowledge")
    print("2. Python Basics")

    choice = input("Enter your choice (1 or 2): ")

    while choice != "1" and choice != "2":
        print("Invalid choice. Please choose 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")

    match choice:
        case "1":
            return "1"
        case "2":
            return "2"


def run_quiz(player_name, category):
    score = 0

    print("\nWelcome,", player_name)

    if category == "1":
        print("QUIZ: General Knowledge")
    else:
        print("QUIZ: Python Basics")

    print("Choose A, B, C, or D.")
    print("--------------------------")

    for number in range(1, 6):

        if category == "1":
            match number:
                case 1:
                    question = "What is the capital of Rwanda?"
                    options = "A. Kigali  B. Nairobi  C. Kampala  D. Accra"
                    correct_answer = "A"

                case 2:
                    question = "How many days are in a week?"
                    options = "A. 5  B. 6  C. 7  D. 8"
                    correct_answer = "C"

                case 3:
                    question = "Which planet do we live on?"
                    options = "A. Mars  B. Earth  C. Venus  D. Jupiter"
                    correct_answer = "B"

                case 4:
                    question = "What is 5 + 3?"
                    options = "A. 6  B. 7  C. 9  D. 8"
                    correct_answer = "D"

                case 5:
                    question = "Which animal is known as man's best friend?"
                    options = "A. Cat  B. Dog  C. Cow  D. Goat"
                    correct_answer = "B"

        else:
            match number:
                case 1:
                    question = "Which function gets user input?"
                    options = "A. print()  B. input()  C. int()  D. type()"
                    correct_answer = "B"

                case 2:
                    question = "Which symbol means multiplication?"
                    options = "A. +  B. -  C. *  D. /"
                    correct_answer = "C"

                case 3:
                    question = "Which keyword checks a condition?"
                    options = "A. if  B. print  C. input  D. for"
                    correct_answer = "A"

                case 4:
                    question = "Which loop can repeat while a condition is true?"
                    options = "A. if  B. match  C. else  D. while"
                    correct_answer = "D"

                case 5:
                    question = "Which keyword defines a function?"
                    options = "A. return  B. def  C. input  D. match"
                    correct_answer = "B"

        print("\nQuestion", number, ":", question)
        print(options)

        answer = input("Your answer: ")

        while (answer != "A" and answer != "B"
               and answer != "C" and answer != "D"):
            print("Invalid answer. Enter A, B, C, or D.")
            answer = input("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect. The correct answer is", correct_answer)

    percentage = score / 5 * 100

    print("\n========== QUIZ RESULT ==========")
    print("Player:", player_name)
    print("Score:", score, "out of 5")
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent work!")
    elif percentage >= 60:
        print("Good job!")
    elif percentage >= 40:
        print("Keep practising!")
    else:
        print("Study more and try again!")

    return score


def main():
    print("================================")
    print("       PYTHON QUIZ SYSTEM")
    print("================================")

    player_name = input("Enter your name: ")

    play_again = "yes"

    while play_again == "yes":
        category = choose_category()
        run_quiz(player_name, category)

        play_again = input("\nDo you want to play again? (yes/no): ")

        while play_again != "yes" and play_again != "no":
            print("Please enter yes or no.")
            play_again = input(
                "Do you want to play again? (yes/no): "
            )

    print("\nThank you for using the Python Quiz System!")


main()
