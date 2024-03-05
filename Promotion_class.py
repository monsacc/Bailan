class Promotion:
    def __init__(self, name_fastival, discount, start_date_time = None, end_date_time = None):
        self.__name_fastival = name_fastival
        self.__discount = discount
        self.__book_list = []
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__promotion_dict = {} # ใช้จัดรูปแบบข้อมูลก่อนแสดงผลเท่านั้น

    @property
    def name_fastival(self):
        return self.__name_fastival

    @property
    def discount(self):
        return self.__discount

    @property
    def book_list(self):
        return self.__book_list

    @property
    def start_date_time(self):
        return self.__start_date_time

    @property
    def end_date_time(self):
        return self.__end_date_time
    
    def add_book_in_book_list(self, book):
        self.__book_list.append(book)
    
    def show_info(self):
        return f"For {self.__name_fastival} fastival we give you {self.__discount} discount!"