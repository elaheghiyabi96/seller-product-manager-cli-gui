# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:32:58 2026
book_shop_tkinter
@author: Shayan System
"""
import json
import os
from tkinter import*
file_path = r"D:\python_train\train\products.json"
with open(file_path, "r") as f:
    products = json.load(f)

def add_product():
    add_win = Toplevel(root)
    add_win.title("Add Product")
    add_win.geometry("300x400")
    
    Label(add_win, text="Name:").pack(pady=5)
    name_entry = Entry(add_win)
    name_entry.pack(pady=5)
    
    Label(add_win, text="Number:").pack(pady=5)
    num_entry = Entry(add_win)
    num_entry.pack(pady=5)
    
    Label(add_win, text="Buying Price:").pack(pady=5)
    buy_entry = Entry(add_win)
    buy_entry.pack(pady=5)
    
    Label(add_win, text="Sale Price:").pack(pady=5)
    sale_entry = Entry(add_win)
    sale_entry.pack(pady=5)
    
    Label(add_win, text="Date:").pack(pady=5)
    date_entry = Entry(add_win)
    date_entry.pack(pady=5)
    
    def save():
        a = name_entry.get().strip().lower()
        b = num_entry.get().strip()
        c = buy_entry.get().strip()
        d = sale_entry.get().strip()
        e = date_entry.get().strip()
        
        if a and b and c and d and e:
            products[a] = {"number": b, "buying_price": c, "sale_price": d, "date": e}
            messagebox.showinfo("Success", f"{a} added!")
            with open(file_path, "w") as f:
                json.dump(products, f, indent=4)
            add_win.destroy()
        else:
            messagebox.showerror("Error", "All fields required!")
    
    Button(add_win, text="Save", command=save).pack(pady=20)

def search_product():
    search_win = Toplevel(root)
    search_win.title("Search Product")
    search_win.geometry("300x200")
    
    Label(search_win, text="Enter product name:").pack(pady=10)
    name_entry = Entry(search_win)
    name_entry.pack(pady=5)
    
    def do_search():
        a = name_entry.get().strip().lower()
        if a in products:
            info = products[a]
            messagebox.showinfo("Found", 
                f"Name: {a}\n"
                f"Number: {info['number']}\n"
                f"Buying Price: {info['buying_price']}\n"
                f"Sale Price: {info['sale_price']}\n"
                f"Date: {info['date']}")
            search_win.destroy()
        else:
            messagebox.showerror("Error", f"{a} not found!")
            search_win.destroy()
    
    Button(search_win, text="Search", command=do_search).pack(pady=10)
def total_show():
    show_win = Toplevel(root)
    show_win.title("All Products")
    show_win.geometry("550x400")
    
    if not products:
        Label(show_win, text="No products found!").pack(pady=20)
    else:
        frame = Frame(show_win)
        frame.pack(fill=BOTH, expand=True)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=70, height=15)
        listbox.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        
        for name, info in products.items():
            profit = int(info["sale_price"]) - int(info["buying_price"])
            listbox.insert(END, f"{name} | count: {info['number']} | buy: {info['buying_price']} | sell: {info['sale_price']} | profit/unit: {profit} | date: {info['date']}")
    
    Button(show_win, text="Close", command=show_win.destroy).pack(pady=10)
def profit_product():
    profit_win = Toplevel(root)
    profit_win.title("Product Profit")
    profit_win.geometry("300x200")
    
    Label(profit_win, text="Enter product name:").pack(pady=10)
    name_entry = Entry(profit_win)
    name_entry.pack(pady=5)
    
    def show_profit():
        a = name_entry.get().strip().lower()
        if a in products:
            v = int(products[a]["sale_price"]) - int(products[a]["buying_price"])
            messagebox.showinfo("Profit", f"Profit of {a} is {v} Tomans")
            profit_win.destroy()
        else:
            messagebox.showerror("Error", f"{a} not found!")
            profit_win.destroy()
    
    Button(profit_win, text="Calculate", command=show_profit).pack(pady=10)
def total_profit():
    kol = 0
    for i in products:
        ko = (int(products[i]["sale_price"]) - int(products[i]["buying_price"])) * int(products[i]["number"])
        kol = kol + ko
    
    profit_win = Toplevel(root)
    profit_win.title("Total Profit")
    profit_win.geometry("300x150")
    
    Label(profit_win, text=f"Total profit: {kol} Tomans", font=("Arial", 14)).pack(pady=30)
    Button(profit_win, text="Close", command=profit_win.destroy).pack(pady=10)
def sort_by_profit():
    if not products:
        messagebox.showerror("Error", "No products to sort!")
        return
    
    product_profit = []
    for i in products:
        profit = (int(products[i]["sale_price"]) - int(products[i]["buying_price"]))
        product_profit.append((i, profit))
    
    # Bubble sort
    for j1 in range(len(product_profit)):
        for j2 in range(j1+1, len(product_profit)):
            if product_profit[j1][1] < product_profit[j2][1]:
                product_profit[j1], product_profit[j2] = product_profit[j2], product_profit[j1]
    
   
    sort_win = Toplevel(root)
    sort_win.title("Products Sorted by Profit")
    sort_win.geometry("400x400")
    
   
    frame = Frame(sort_win)
    frame.pack(fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=50, height=15)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
   
    for name, profit in product_profit:
        listbox.insert(END, f"{name}: {profit} Tomans")
    
    Button(sort_win, text="Close", command=sort_win.destroy).pack(pady=10)
def filter_by_profit():
    if not products:
        messagebox.showerror("Error", "No products to filter!")
        return
    
  
    filter_win = Toplevel(root)
    filter_win.title("Filter Products")
    filter_win.geometry("300x200")
    
    Label(filter_win, text="Enter minimum profit:").pack(pady=10)
    threshold_entry = Entry(filter_win)
    threshold_entry.pack(pady=5)
    
    def do_filter():
        try:
            a = int(threshold_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return
        
        dd = []
        for i in products:
            profit = int(products[i]["sale_price"]) - int(products[i]["buying_price"])
            if profit >= a:
                dd.append(i)
        
      
        result_win = Toplevel(root)
        result_win.title("Filter Results")
        result_win.geometry("300x300")
        
        if not dd:
            Label(result_win, text=f"No products with profit >= {a}").pack(pady=20)
        else:
            Label(result_win, text=f"Products with profit >= {a}:", font=("Arial", 10, "bold")).pack(pady=5)
            
            frame = Frame(result_win)
            frame.pack(fill=BOTH, expand=True)
            
            scrollbar = Scrollbar(frame)
            scrollbar.pack(side=RIGHT, fill=Y)
            
            listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=40, height=10)
            listbox.pack(side=LEFT, fill=BOTH, expand=True)
            scrollbar.config(command=listbox.yview)
            
            for name in dd:
                profit = int(products[name]["sale_price"]) - int(products[name]["buying_price"])
                listbox.insert(END, f"{name}: {profit} Tomans")
        
        Button(result_win, text="Close", command=result_win.destroy).pack(pady=10)
        filter_win.destroy()
    
    Button(filter_win, text="Filter", command=do_filter).pack(pady=10)
def edit_product():
    if not products:
        messagebox.showerror("Error", "No products to edit!")
        return
    
    edit_win = Toplevel(root)
    edit_win.title("Edit Product")
    edit_win.geometry("300x500")
    
    Label(edit_win, text="Enter product name to edit:").pack(pady=10)
    name_entry = Entry(edit_win)
    name_entry.pack(pady=5)
    
    def load_product():
        a = name_entry.get().strip().lower()
        if a not in products:
            messagebox.showerror("Error", f"{a} not found!")
            return
        
        for widget in edit_win.winfo_children():
            widget.destroy()
        
        Label(edit_win, text=f"Editing: {a}", font=("Arial", 12, "bold")).pack(pady=10)
        
        Label(edit_win, text="New name (Enter to keep old):").pack(pady=5)
        new_name_entry = Entry(edit_win)
        new_name_entry.pack(pady=5)
        new_name_entry.insert(0, a)
        
        Label(edit_win, text="Number:").pack(pady=5)
        num_entry = Entry(edit_win)
        num_entry.pack(pady=5)
        num_entry.insert(0, products[a]["number"])
        
        Label(edit_win, text="Buying Price:").pack(pady=5)
        buy_entry = Entry(edit_win)
        buy_entry.pack(pady=5)
        buy_entry.insert(0, products[a]["buying_price"])
        
        Label(edit_win, text="Sale Price:").pack(pady=5)
        sale_entry = Entry(edit_win)
        sale_entry.pack(pady=5)
        sale_entry.insert(0, products[a]["sale_price"])
        
        Label(edit_win, text="Date:").pack(pady=5)
        date_entry = Entry(edit_win)
        date_entry.pack(pady=5)
        date_entry.insert(0, products[a]["date"])
        
        def save_edit():
            new_name = new_name_entry.get().strip().lower()
            if not new_name:
                new_name = a
            
           
            if new_name != a and new_name in products:
                messagebox.showerror("Error", f"{new_name} already exists!")
                return
            
            B = num_entry.get().strip()
            C = buy_entry.get().strip()
            D = sale_entry.get().strip()
            E = date_entry.get().strip()
            
            if B and C and D and E:
                products[new_name] = products.pop(a)
                products[new_name]["number"] = B
                products[new_name]["buying_price"] = C
                products[new_name]["sale_price"] = D
                products[new_name]["date"] = E
                
                with open(file_path, "w") as f:
                    json.dump(products, f, indent=4)
                
                messagebox.showinfo("Success", f"Product edited successfully!")
                edit_win.destroy()
            else:
                messagebox.showerror("Error", "All fields required!")
        
        Button(edit_win, text="Save Changes", command=save_edit).pack(pady=20)
    
    Button(edit_win, text="Load Product", command=load_product).pack(pady=10)
def delete_product():
    if not products:
        messagebox.showerror("Error", "No products to delete!")
        return
    
    delete_win = Toplevel(root)
    delete_win.title("Delete Product")
    delete_win.geometry("300x200")
    
    Label(delete_win, text="Enter product name to delete:").pack(pady=10)
    name_entry = Entry(delete_win)
    name_entry.pack(pady=5)
    
    def do_delete():
        a = name_entry.get().strip().lower()
        if a in products:
         
            confirm = messagebox.askyesno("Confirm", f"Are you sure to delete {a}?")
            if confirm:
                del products[a]
                with open(file_path, "w") as f:
                    json.dump(products, f, indent=4)
                messagebox.showinfo("Success", f"{a} deleted!")
                delete_win.destroy()
        else:
            messagebox.showerror("Error", f"{a} not found!")
            delete_win.destroy()
    
    Button(delete_win, text="Delete", command=do_delete).pack(pady=10)
root = Tk()
# جایگزین pack با grid
buttons_frame = Frame(root)
buttons_frame.pack(pady=20)

Button(buttons_frame, text='add', width=12, command=add_product).grid(row=0, column=0, padx=5, pady=5)
Button(buttons_frame, text='search', width=12, command=search_product).grid(row=0, column=1, padx=5, pady=5)
Button(buttons_frame, text='show all', width=12, command=total_show).grid(row=0, column=2, padx=5, pady=5)

Button(buttons_frame, text='profit', width=12, command=profit_product).grid(row=1, column=0, padx=5, pady=5)
Button(buttons_frame, text='total profit', width=12, command=total_profit).grid(row=1, column=1, padx=5, pady=5)
Button(buttons_frame, text='sort by profit', width=12, command=sort_by_profit).grid(row=1, column=2, padx=5, pady=5)

Button(buttons_frame, text='filter', width=12, command=filter_by_profit).grid(row=2, column=0, padx=5, pady=5)
Button(buttons_frame, text='edit', width=12, command=edit_product).grid(row=2, column=1, padx=5, pady=5)
Button(buttons_frame, text='delete', width=12, command=delete_product).grid(row=2, column=2, padx=5, pady=5)
root.title('Book_Products')
root.geometry('400x200')
root.mainloop()