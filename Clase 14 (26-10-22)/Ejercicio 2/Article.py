class Article:
    def __init__(self, title, abstract, body, pictures, creation_date, writter):
        self.title = title
        self.abstract = abstract
        self.body = body
        self.pictures = pictures
        self.creation_date = creation_date
        self.approval_date = None #debe ser aprobado por el Jefe
        self.writter = writter