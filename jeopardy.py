import requests
from flask import Markup

class Jeopardy:
    API_endpoint = "https://jservice.io/api/clues"
    API_query = "value=1000"
    API_url = API_endpoint + "?" + API_query
    r = requests.get(API_url)
    clues = r.json()

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.number = 0
        self.answer = ""
        self.correct = None
    
    def display_clue(self, clue):
        clue_html = ""
        question = clue["question"]
        value = clue['value']
        category = clue['category']['title']
        clue_html += '<h2>Category: ' + category.title() + "</h2>"
        clue_html += '<h3>Question: ' + question + "</h3>"
        clue_html += '<h2>Value: ' + str(value) + "</h2>"
        # print('answer: ' + clue['answer'] )
        return clue_html

    def jeopardy(self):
            page = ""
            number = self.number
            clue = self.clues[number]
            
            if(number > 0):
                if(self.correct):
                    page += f"<p>CORRECT! The answer was {self.answer.title()}</p> <hr/>"
                else:
                    page += f"<p>Sorry, but the correct answer was {self.answer.title()}.</p> <hr/>"
            
            page += f'<h1>Question #{number + 1}:</h1>'
            page += self.display_clue(clue)
            answer = self.answer
            if clue["answer"].lower() == answer:
                self.score +=  clue['value']
                self.correct = True
            else:
                # print("Incorrect")
                self.correct = False
            
            self.number += 1
            return Markup(page)

            # ask_quit()

    # def ask_quit(self):
    #     print('\n------------------\n')
    #     choice = input("Do you want to keep on going Y/N ").lower()
    #     if choice == 'n':
    #         exit()
    #     else:
    #         print('Ok keep on playing!')

    # def generate_categories(self):
    #     categories = []
    #     rand = requests.get('https://jservice.io/api/random').json()
    #     for i in range(5):
    #         categories.append(rand[i]['category']['title'])
    #     print(categories)

    # def misspell(answer):
    #     for char1 in answer: