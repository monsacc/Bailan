class Coin_transaction:
    def __init__(self, coin, date_time, type):
        self.__coin = coin
        self.__date_time = date_time.strftime("%c")
        self.__type = type
        
    @property
    def coin(self):
        return self.__coin

    @property
    def  date_time(self):
        return self.__date_time

    @property
    def  type(self):
        return self.__type