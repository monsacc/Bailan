from typing import Union
import uvicorn
from fastapi import FastAPI

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = FastAPI()

from PaymentMethod_class import PaymentMethod
from Controller_class import Controller
from Account_class import Account , Reader
from PaymentHistory import PaymentHistory
from Coin_transection_class import Coin_transection
from Book_class import Book
from BaseModel import BaseModel

root = ttk.Window()
b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()


#if __name__ == "__main__":
  #  uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")


chanels = [
    PaymentMethod("bank",1),
    PaymentMethod("credit card",2)
    ]
controller = Controller()
T = Reader('get','1234','1')
#T.update_payment_history_list(PaymentHistory("500","Jan","add"))
for c in chanels:
    controller.add_payment_method(c)
controller.add_reader(T)

book1 = Book("Great Book", 1, "writer1", "Fiction", 100, "intro", "Content")
book2 = Book("Thai Book", 2, "writer1", "Non-fiction", 200, "intro", "Content")
book3 = Book("Japan Book", 3, "writer1", "Non-fiction", 300, "intro", "Content")
book4 = Book("Code Book", 4, "writer1", "Non-fiction", 400, "intro", "Content")
book5 = Book("Food Book", 5, "writer1", "Non-fiction", 500, "intro", "Content")

controller.add_book(book1)
controller.add_book(book2)
controller.add_book(book3)
controller.add_book(book4)
controller.add_book(book5)

controller.top_up("1",500,"bank")
controller.buy_book([1],'1')

print(T.book_collection_list)
print(T.coin_transaction_history_list)
print(T.coin)
for info in T.coin_transaction_history_list:
    print(info)




""""
@app.post("/buy_book", tags =["buy"])
async def buy_book(list_book :  , account_id : dict , date_time : dict)->dict:
    return {
        "status" : controller.buy_book(list_book,account_id,date_time)
    }

@app.get("/listbook", tags=["listbook"])
async def get_collection()->dict:
    return {'book':T.book_collection_list}

@app.post("/top_up", tags=['top up'])
async def top_up(account : str, money : int , chanel : str ,date : str)->dict:
    return {
        "status" : controller.top_up(account,money,chanel,date)
        }

print(controller.top_up("1",500,"bank","Jan"))
print(T.payment_history_list)
print(T.coin_transaction_history_list)
print('----------------------------------------')

"""





"""

chanels = [
    PaymentMethod("SCB"),
    PaymentMethod("credit_card"),
    PaymentMethod("K_plus")
]

controller = Controller()

for c in chanels:
    controller.add_payment_method(c)

print(controller.payment_method_list.chanel_name)"""








