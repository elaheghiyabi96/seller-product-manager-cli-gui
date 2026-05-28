# seller-product-manager-cli-gui
Product management system for sellers with CLI and GUI versions. Features: add/edit/delete products, profit calculation, filter, sorting. JSON storage. Create JSON file first.
# 📦 Seller's Product Management System

## 📌 Introduction

This repository contains **two Python codes** with the **same concept** – a digital notebook for sellers to store and manage their products, calculate profits, filter, and sort inventory.

- **Version 1:** Command Line Interface (CLI)
- **Version 2:** Graphical User Interface (GUI) with Tkinter

Both codes work with the same JSON file structure and provide identical functionality.

---

## 🎯 What is this for?

Sellers can:

- ✅ Add, edit, search, and delete products
- ✅ Store for each product: **name, quantity, buying price, selling price, date**
- ✅ Calculate **profit per product** and **total profit**
- ✅ **Filter products** by minimum profit threshold
- ✅ **Sort products** by profit (highest first)
- ✅ Data persists in a JSON file

---

## ⚠️ Important Note

> The JSON file for storing data **must be created in advance** at the desired location before running the codes.

---

## 🚀 How to Run

### Step 1: Create the JSON file

Run this code **once** to create an empty JSON file at your desired path:

```python
import json

file_path = r"YOUR_DESIRED_PATH\products.json"

with open(file_path, "w") as f:
    json.dump({}, f)

print(f"File created at: {file_path}")
Replace YOUR_DESIRED_PATH with the actual folder path on your system.

Step 2: Update the file path in both codes
In both Python files, find this line:

python
file_path = r"D:\python_train\train\products.json"
Change it to the path you used in Step 1.

Step 3: Run the files
Run both Python files in the repository.

Version	How to Run
CLI	Run in terminal
GUI	A window will open
🔐 CLI Version Password
The CLI version includes a simple password:

Password: elahe_ghiyabi

🛠 Features (Both Versions)
Feature	Description
➕ Add product	Add new product with all details
❌ Delete product	Remove product by name
🔍 Search product	View product details
✏️ Edit product	Modify name and details
💰 Product profit	Show profit for a single product
📊 Total profit	Calculate total inventory profit
📋 Show all	List all products
🔎 Filter by profit	Show products with profit ≥ threshold
📈 Sort by profit	Sort products descending by profit
📁 Repository Structure
text
├── 📄 Python file 1 (CLI version)
├── 📄 Python file 2 (GUI version)
└── 📖 README.md
Note: products.json is not included in the repository. You must create it yourself using Step 1 above.

📜 License
Educational purposes. Free to use with credit.

⭐ Star this repo if you find it useful!
