import requests
API_endpoint = "https://jservice.io/api/clues"
API_query = "value=1000"
API_url = API_endpoint + "?" + API_query
r = requests.get(API_url)
data = r.json()
page = ""

def display_clue(clue):
    question = clue["question"]
    value = clue['value']
    category = clue['category']['title']
    page += 'Question: ' + question
    page += 'Value: ' + str(value)
    page += 'Category: ' + category.title()
    # print('answer: ' + clue['answer'] )
    return page

def jeopardy():
        name = input('What is your name? ')
        score = 0
        print(f'Welcome to jeopardy {name}')
        for number in range(len(data)):
            clue = data[number]
            print('\n------------------\n')
            print(f'Question #{number + 1}:\n')
            display_clue(clue)
            answer = input("What is ").lower()
            if clue["answer"].lower() == answer:
                score +=  clue['value']
                print(f"Your current score is {score}.")
            else:
                print("Incorrect")
            ask_quit()


def ask_quit():
    print('\n------------------\n')
    choice = input("Do you want to keep on going Y/N ").lower()
    if choice == 'n':
        exit()
    else:
        print('Ok keep on playing!')


def generate_categories():
    categories = []
    rand = requests.get('https://jservice.io/api/random').json()
    for i in range(5):
        categories.append(rand[i]['category']['title'])
    print(categories)


# def misspell(answer):
#     for char1 in answer:


# generate_categories()
jeopardy()