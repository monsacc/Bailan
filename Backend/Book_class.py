from Account_class import Writer

class Book:
    def __init__(self, name, id, writer, book_type, price_coin, intro, content):
        self.__name = name
        self.__id = id
        self.__writer = writer
        self.__book_type = book_type
        self.__price_coin = price_coin
        self.__intro = intro
        self.__content = content
        self.__review = None
        self.__promotion = None
        self.__num_of_reader = 0

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id

    @property
    def writer(self):
        return self.__writer

    @property
    def book_type(self):
        return self.__book_type

    @property
    def price_coin(self):
        return self.__price_coin

    @property
    def intro(self):
        return self.__intro

    @property
    def content(self):
        return self.__content

    @property
    def review(self):
        return self.__review
    
    @review.setter
    def review(self, new_review):
        self.__review = new_review

    @property
    def promotion(self):
        return self.__promotion

    @promotion.setter
    def promotion(self, new_promotion):
        self.__promotion = new_promotion
        
        if self.__promotion.discount > 0 and self.__promotion.discount <= 100:
            self.__price_coin *= 1-(self.__promotion.discount*0.01)

    @property
    def num_of_reader(self):
        return self.__num_of_reader

    @num_of_reader.setter
    def num_of_reader(self, new_num_of_reader):
        self.__num_of_reader += new_num_of_reader