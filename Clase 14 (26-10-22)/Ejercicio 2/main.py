from Writter import Writter, HeadOfWritters
from Section import Section

def get_writters_entertainment():
    return [
        Writter('Pedro', 1234),
        Writter('Juan', 1234),
        Writter('Maria', 1234),
        Writter('Jose', 1234),
        Writter('Alan', 1234),
        Writter('Paula', 1234)
    ]

def get_writters_sports():
    return [
        Writter('Rodrigo', 1234),
        Writter('Jesus', 1234),
        Writter('Samantha', 1234),
        Writter('Manuela', 1234),
        Writter('Carol', 1234),
        Writter('Angel', 1234)
    ]

def get_writters_politics():
    return [
        Writter('Leonardo', 1234),
        Writter('Lorena', 1234),
        Writter('Samuel', 1234),
        Writter('Andres', 1234),
        Writter('Kevin', 1234),
        Writter('Isabella', 1234)
    ]


def process_articles(section):
    for escritor in section.head_writters.writters_group:
        None

def main():

    head_writters_entertainment = HeadOfWritters('Jose Quevedo',1234,get_writters_entertainment)
    head_writters_sports = HeadOfWritters('Luis Bello',1234,get_writters_sports)
    head_writters_politics = HeadOfWritters('Antonio Guerra',1234,get_writters_politics)

    section_entertainment = Section(head_writters_entertainment, 'Entertainment')
    section_sports= Section(head_writters_sports, 'Sports')
    section_politics = Section(head_writters_politics, 'Politics')

    process_articles(section_entertainment)
    process_articles(section_sports)
    process_articles(section_politics)
main()