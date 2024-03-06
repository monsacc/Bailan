class Complain:
    def __init__(self, user, date_time, info, complain_list):
        self.__user = user
        self.__date_time = date_time
        self.__info = info
        self.__complain_list = complain_list

    def user(self):
        return self.__user

    def date_time(self):
        return self.__date_time

    def info(self):
        return self.__info

    def complain_list(self):
        return self.__complain_list

    def display_complaint(self):
        print(f"User: {self.user()}")
        print(f"Date and Time: {self.date_time()}")
        print(f"Info: {self.info()}")
        print("Complaint List:")
        for complaint in self.complain_list():
            print(f"  - {complaint}")