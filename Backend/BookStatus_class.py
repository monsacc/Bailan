class BookStatus:
    def __init__(self, start_date, end_date, status, book):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__status = status
        self.__book = book

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, new_start_date):
        self.__start_date = new_start_date

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, new_end_date):
        self.__end_date = new_end_date

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    @property
    def book(self):
        return self.__book