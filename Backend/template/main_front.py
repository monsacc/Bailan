import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import *

import webbrowser
import os
import requests
import asyncio
import aiohttp
from typing import List

# API_ENDPOINT1 = "http://127.0.0.1:8000/docs#/Cart/add_book_to_card_addcart_get"
# API_ENDPOINT2 = "http://127.0.0.1:8000/docs#/Cart/remove_book_from_cart_removebook_delete"
# API_ENDPOINT3 = "http://127.0.0.1:8000/Cart/showcart"
# API_ENDPOINT4 = "http://127.0.0.1:8000/docs#/Cart/select_book_checkout_select_book_checkout_post"

root = ttk.Window()
root.title("Bailan")

style = Style('vapor')

root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.resizable(False, False)

#header
style.configure('Header.TFrame', background='#4CAF50')
header = ttk.Frame(root, style='Header.TFrame')
header.pack(fill=X, ipady=0)

# Add Bailan label
lable_bailan = ttk.Label(header, text="Bailan", font=("Helvetica", 20, "bold"), background='#4CAF50', foreground='white')
lable_bailan.pack(pady=5, padx=10)

menu_frame = ttk.Frame(root)
menu_frame.pack(pady=20)

def clicker_menu():
    if my_menu.get() == "หน้าแรก":
        root.deiconify()
    else:
        my_lable.config(text=my_menu.get())

menu_list = ["หน้าแรก", "โปรโมชัน"]
my_menu = StringVar()

for menu in menu_list:
    ttk.Radiobutton(menu_frame, bootstyle="success toolbutton", variable = my_menu, text=menu, 
                    value = menu).pack(side=LEFT, padx=5, pady=5)

# Label to display selected menu
my_label = ttk.Label(root, text="", font=("Helvetica", 12))
my_label.pack(pady=10)

# Add shopping cart button
button_cart = ttk.Button(header, text="ตะกร้า", width=5, command=lambda: asyncio.run(show_cart_ui()))
button_cart.place(x=1500, y=10)

# async def click_show_cart():
#     async with aiohttp.ClientSession() as session:
#         async with session.get("http://127.0.0.1:8000/Cart/showcart") as response:
#             data = await response.json()
#             show_cart_ui(data)

def show_cart_ui():
    cart_window = ttk.Toplevel(root)
    cart_window.title("Shopping Cart")
    cart_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    label_title = ttk.Label(cart_window, text="ตะกร้า", font=("Helvetica", 30, "bold"))
    label_title.pack(pady=20, padx=20)
    label_title2 = ttk.Label(cart_window, text="เลือกหนังสือที่ต้องการชำระเงิน", font=("Helvetica", 15, "bold"))
    label_title2.pack(pady=5, padx=20)

    # Add a back button
    back_button = ttk.Button(cart_window, text="Back", command=cart_window.destroy)
    back_button.pack()

    # Wait for 100 milliseconds before showing the window
    cart_window.after(100, cart_window.deiconify)

# Search bar
search_frame = ttk.Frame(root, style='Header.TFrame')
search_frame.place(x=1580, y=10)

entry_search = ttk.Entry(search_frame, width=30)
entry_search.pack(side=LEFT, padx=(0, 5))

# Search button
def search_function():
    search_query = entry_search.get()
    # Do something with the search query, for example, print it
    print("Search Query:", search_query)

    search_window = ttk.Toplevel(root)
    search_window.title("Search Book")
    search_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    label_title1 = ttk.Label(search_window,text="ค้นหาด้วยชื่อหนังสือ",font=("Helvetica", 20, "bold"))
    label_title1.pack(pady=30,padx=30)
    
    label_title2 = ttk.Label(search_window,text = "ค้นหาด้วยชื่อผู้แต่ง",font=("Helvetica", 20, "bold"))
    label_title2.pack(pady=30,padx=30)

    label_title3 = ttk.Label(search_window,text = "ประเภทหนังสือ",font=("Helvetica", 20, "bold"))
    label_title3.pack(pady=30,padx=30)


button_search = ttk.Button(search_frame, text="ค้นหา", width=5, command=search_function)
button_search.pack(side=LEFT)


def view_profile():
    # สร้างเมนูบัตรเลือก
    profile_menu = ttk.Menubutton(header, text="สวัสดี User", width=10)
    profile_menu.place(x=20, y=10) 

    # สร้างเมนู
    options_menu = ttk.Menu(profile_menu, tearoff=False)
    profile_menu["menu"] = options_menu

    # เพิ่มตัวเลือกในเมนู
    options_menu.add_command(label="ข้อมูล", command=lambda: print("ข้อมูล clicked"))
    options_menu.add_command(label="coin", command=lambda: print("coin clicked"))
    options_menu.add_command(label="เติม coin", command=lambda: print("เติม coin clicked"))
    options_menu.add_command(label="ชั้นหนังสือของฉัน", command=lambda: print("ชั้นหนังสือของฉัน clicked"))
    options_menu.add_command(label="ประวัติการเติมเงิน", command=lambda: print("ประวัติการเติมเงิน clicked"))
    options_menu.add_command(label="ประวัติการใช้จ่ายเหรียญ", command=lambda: print("ประวัติการใช้จ่ายเหรียญ clicked"))
    options_menu.add_command(label="Logout", command=lambda: print("Logout clicked"))


view_profile()

root.mainloop()