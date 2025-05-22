# 🏗️ Construction Materials Management System

A simple, efficient, and terminal-based system built using **Python** and **MySQL** for managing construction materials across different sites or projects. The system helps track materials, suppliers, orders, and inventory levels for smooth construction operations.

## 🚀 Features

- 🧱 Add, update, delete, and view:
  - Construction materials
  - Suppliers
  - Inventory records
  - Purchase orders
- 📦 Track available stock of each material
- 📝 Record material purchases and supplier details
- 📊 Generate inventory reports

## 🛠️ Technologies Used

- **Python** – Core application logic and CLI interface
- **MySQL** – Backend database
- **MySQL Connector for Python** – Used for database operations

## 📂 Project Structure

construction_materials/
│
├── main.py # Main program flow and user interface
├── report.py # Database connection settings and reporting feature
├── materials.py # Material management (CRUD)
└── person.py # Supplier, Client and Builder management (CRUD)


## 🧑‍💻 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/sadain-ahmad/construction-materials-management.git
cd construction-materials-management
```

2. Set up the MySQL database

- Open MySQL or your preferred GUI (like phpMyAdmin)

3. Configure the database

- Edit `main.py` with your `MySQL host`, `user`, `password`, and `database details`

4. Install required libraries

```bash
pip install mysql-connector-python
```

5. Run the application

```bash
python main.py
```

## 🧾 Example Use Cases

- View all available materials and their quantities

- Add new suppliers and assign them to purchase orders

- Track which materials are used on specific sites

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to add.