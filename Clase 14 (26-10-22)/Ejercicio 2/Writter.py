from Article import Article
import random

class Writter:
    def __init__(self, name, id, section):
        self.name = name
        self.id = id
        self.section = section

def write_article(self):
    print('You\'re writting an article')
    article = Article(
        input('Title: '),
        input('Abstract: '),
        input('Body: '),
        input('Picture: '),
        input('Creation date: '),
        self.name
    )
    print('You finished writting the article ', article.title)
    return article

class HeadOfWritters(Writter):
    def __init__(self, name, id, section, writters_list):
        super().__init__(name, id, section)
        self.writters = writters_list

def supervise(self):
    print('Everything\'s okay')

def decide(self, article):
    if random.random() > 0.5:
        print(f'The article {article.title} was approved')
    else:
        print(f'The article {article.title} was not approved')
        