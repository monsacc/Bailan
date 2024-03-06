class Review:
    def __init__(self, reader, book, date_time):
        self.__reader = reader
        self.__book = book
        self.__date_time = date_time
        self.__rating = None
        self.__rating_list = []
        self.__comment_list = []
        self.__comment_dict = {}  # ใช้จัดรูปแบบข้อมูลก่อนแสดงผลเท่านั้น

    @property
    def reader(self):
        return self.__reader

    @property
    def book(self):
        return self.__book

    @property
    def date_time(self):
        return self.__date_time
    
    @property
    def rating(self):
        return self.__rating

    @property
    def rating_list(self):
        return self.__rating_list

    @property
    def comment_list(self):
        return self.__comment_list
    
    @property
    def comment_dict(self):
        return self.__comment_dict
    
    def add_rating(self, rating):
        self.__rating_list.append(rating)
        self.__rating = sum(self.__rating_list) / len(self.__rating_list)
    
    def add_comment(self, reader, comment):
        self.__comment_list.append((reader, comment))
        
    def show_comment(self):
        for account, comment in self.__comment_list:
            if account.account_name in self.__comment_dict:
                self.__comment_dict[account.account_name].append(comment)
            else:
                self.__comment_dict[account.account_name] = [comment]

        format = []
        for account, comments in self.__comment_dict.items():
            format.append(f"{account} account : {', '.join(comments)}")

        return format