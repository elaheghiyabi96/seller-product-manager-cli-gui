# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:21:57 2026
add products for shopper
@author: Shayan System
"""

import json
import os
#with open(r"D:\python_train\train\products.json", "w") as f:
    #f.write("{}")
file_path = r"D:\python_train\train\products.json"
with open(file_path, "r") as f:
    products = json.load(f)
con=1
  
def add_():
    a = input('Enter name of product: ')
    a = a.lower()
    a = a.strip()
    b = input(f'Enter number of {a}: ')
    b = b.lower()
    b = b.strip()
    c = input('Enter buying_price : ')
    c = c.lower()
    c = c.strip()
    d = input('Enter sale_price : ')
    d = d.lower()
    d = d.strip()
    e = input('Enter date of enterance: ').strip().lower()
    products[a] = {"number": b, "buying_price": c, "sale_price": d, "date" : e}
    print(products)
def remove_():
    a = input('Enter name of product: ')
    a = a.lower()
    a = a.strip()
    if a in products:
        del products[a]
    else:
        print(f'there is not {a}')
def search_():
    a = input('Enter name of product: ')
    a = a.lower()
    a = a.strip()
    if a in products:
        print(f'{a} = {products[a]}')
    else:
        print(f'there is not {a}')
def edite_():
    a = input('Enter name of product: ')
    a = a.lower()
    a = a.strip()
    if a in products:
        A = input('Enter name of new product that you want to replace: ').strip().lower()
        B = input(f'Enter number of {A}: ').strip().lower()
        C = input('Enter buying_price : ').strip().lower()
        D = input('Enter sale_price : ').strip().lower()
        E = input('Enter date of enterance: ').strip().lower()
        products[A] = products.pop(a)
        products[A]["number"]=B
        products[A]["buying_price"]=C
        products[A]["sale_price"]=D
        products[A]["date"]=E
    else:
        print(f'there is not {a}')
def profit_():
    a = input('enter name of product: ').strip().lower()
    if a in products:
        v = int(products[a]["sale_price"]) - int(products[a]["buying_price"])
        print(f'profit of {a} is {v}')
    else:
        print(f'there is not {a}')
def total_profit():
    kol=0
    for i in products:
        ko = (int(products[i]["sale_price"]) - int(products[i]["buying_price"]))*int(products[i]["number"])
        kol = kol+ko
    print(f'total profit is {kol}')
def total_show():
    if not products:
        print('no products')
    else:
        for i,j in products.items():
            print(f'{i}:{j}')
def filter_by_profit():
    a = int(input('Enter threshold: '))
    dd =[]
    for i in products:
        if (int(products[i]["sale_price"]) - int(products[i]["buying_price"])) >= a:
         dd.append(i)
    print(dd)
def sort_by_profit():
    product_profit = []
    for i in products:
        profit = (int(products[i]["sale_price"]) - int(products[i]["buying_price"]))
        product_profit.append((i, profit))
    for j1 in range(len(product_profit)):
        for j2 in range(j1+1, len(product_profit)):
            if product_profit[j1][1]<product_profit[j2][1]:
                product_profit[j1], product_profit[j2] = product_profit[j2], product_profit[j1]
    print("\n--- Products sorted by profit (highest first) ---")
    for name, profit in product_profit:
        print(f"{name}: {profit} Tomans")
    with open(r"D:\python_train\train\profit_sorted.json", "w") as f:
        json.dump(product_profit, f, indent=4)
pass1 = 'elahe_ghiyabi'
pass2 = input('Enter password for entrance: ').strip().lower()
if pass1 == pass2: 
    while con==1:
        con = int(input('Enter 1 for continue and 0 for end: '))
        if con == 1:
            choice = int(input('Enter (add = 1, delete = 2, search = 3, edite = 4,'
                               'profit of product = 5, total_profit = 6, total_show=7, filter by profit = 8, ' 
                               'sort by profit = 9): '))
            if choice ==1:
                add_()
            elif choice ==2:
                remove_()
            elif choice ==3:
                search_()
            elif choice ==4:
                edite_()
            elif choice ==5:
                profit_()
            elif choice ==6:
                total_profit()
            elif choice ==7:
                total_show()
            elif choice ==8:
                filter_by_profit()
            elif choice ==9:
                sort_by_profit()
        else:
            break
    with open(file_path, "w") as f:
        json.dump(products, f, indent=4)
else:
    print('password is wrong')
     
