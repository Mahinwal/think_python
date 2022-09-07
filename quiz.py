def quiz():
    score = 0
    collection = {
        'question1': {
            'question':'Who is hosting the Asia cup 2022?',
            'answer': 'Sri Lanka'
        },
        'question2':
        {
            'question':'Which team scored the lowest score for the Asia cup 2022?',
            'answer' : 'Hongkong'
        },
        'question3':
        {
            'question':'Which country is going to host the ICC T20 World Cup?',
            'answer' : 'Australia'
        },
    }

    for key, value in collection.items():
        print(value['question'])
        answer = input("Answer? ")
        print("")
        if value['answer'].lower() == answer.lower():
            score +=1
    
    print("Your score is", score, " out of 3")

if __name__ == '__main__':
    choice = input("Welcome to the Quiz of this week. Do you want to check your knowledge about recent cricket matches Y/N? ")
    if choice == 'Y' or choice == 'y':
        print("quiz is started..")
        quiz()
    else:
        print("Thanks for coming...")
        quit()