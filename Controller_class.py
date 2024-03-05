import datetime
class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__complain_list = []
        self.__book_list = []
        self.__payment_method_list = []

    @property
    def reader_list(self):
        return self.__reader_list
    
    @property
    def writer_list(self):
        return self.__writer_list

    @property
    def complain_list(self):
        return self.__complain_list

    @complain_list.setter
    def complain_list(self, new_complain_list):
        self.__complain_list = new_complain_list

    @property
    def book_list(self):
        return self.__book_list

    @book_list.setter
    def book_list(self, new_book_list):
        self.__book_list = new_book_list

    @property
    def payment_method_list(self):
        return self.__payment_method_list

    @payment_method_list.setter
    def payment_method_list(self, new_payment_method_list):
        self.__payment_method_list = new_payment_method_list

    def add_reader(self, reader):
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__writer_list.append(writer)

    def add_complain(self, complain):
        self.__complain_list.append(complain)

    def add_book(self, book):
        self.__book_list.append(book)

    def add_payment_method(self, payment_method):
        self.__payment_method_list.append(payment_method)

    def search_book(self, book_id):
        for book in self.__book_list:
            if book.id == book_id:
                return book
        return None
    
    def search_reader(self, reader_id):
        for reader in self.__reader_list:
            if reader.id_account == reader_id:
                return reader
        return None
    
    def show_payment_method(self):
        for chanels in self.__payment_method_list:
            return chanels 
    
    def top_up(self, id_account, money, chanel):
        if self.search_reader(id_account) is not None:
            account = self.search_reader(id_account)
            for c in self.__payment_method_list:
                if c.chanel_id == chanel:
                    if money % 2 == 0:
                        coin = money/2
                        date_time = datetime.datetime.now()
                        account.adding_coin = coin
                        account.update_payment_history_list(money,date_time)
                        account.update_coin_transaction_history_list(coin,date_time,"top up")
                        return "Success"
                    else : return "Please increse/decrese money 1 Baht"
                return "Not Found Chanel"
        return "Don't Have any Account"
        
    def buy_book(self, list_book_id, id_account): 
        if self.search_reader(id_account) is not None:
            account = self.search_reader(id_account)
            price = 0
            for id in list_book_id:
                if self.search_book(id) is not None:
                    book = self.search_book(id)
                    price += book.price_coin
                    account.update_book_collection_list(book)
                else : return "No Book"
            if account.coin >= price:
                date_time = datetime.datetime.now()
                account.update_coin_transaction_history_list(price,date_time,"paid")
                account.losing_coin = price 
                book.num_of_reader = 1
                return "success" 
            else : return "Don't have coin enough"
        else : return "Not Found Account"
            

    def show_book_info(self, book_id):
        book = self.search_book(book_id)
        if book:
            print(f"Book ID: {book.id}")
            print(f"Book Title: {book.title}")
            print(f"Book Author: {book.author}")
            print(f"Book Price: {book.price}")
            print(f"Book Description: {book.description}")
            return True
        return False

    def login(self, username, password):
        for account in self.__account_list:
            if account.username == username and account.password == password:
                return account
        return None

    def transfer(self, sender_account_id, receiver_account_id, amount):
        sender_account = self.login(sender_account_id, None)
        receiver_account = self.login(receiver_account_id, None)
        if sender_account and receiver_account:
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                receiver_account.balance += amount
                return True
        return False
    
