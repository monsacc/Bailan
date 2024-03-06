class Coin_transection:
    def __init__(self, coin, date_time, type):
        self.__coin = coin
        self.__date_time = date_time
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
    
    def __str__(self):
        return f"You {self.type} {self.coin} coin on {self.date_time}"
    


