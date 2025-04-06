# Personal Budget Tracker API

## Introduction

The Personal Budget Tracker API is a Django REST Framework backend designed to help users manage their finances effectively. It provides endpoints for user authentication, wallet management, transaction tracking, category management, and budget tracking. This API is built to support a web-based application that allows users to monitor their income and expenses, and achieve better financial planning.

## Features

The API currently supports the following core features:

* **User Authentication:**
    * Secure user registration and login.
    * Personalized data storage for each user.
* **Wallet Management:**
    * Creation and management of multiple wallets per user (e.g., Checking, Savings).
    * Wallet attributes:
        * Name
        * Type
        * Current balance
* **Transaction Tracking:**
    * Recording of income and expense transactions.
    * Transaction details:
        * Date
        * Amount
        * Description
        * Category (e.g., Groceries, Rent)
        * Associated Wallet
        * Transaction Type (Income or Expense)
* **Expense Categories:**
    * Management of transaction categories.
    * Customizable categories per user.
* **Budget Tracking:**
    * Creation and management of budgets per category and month.
    * Budget details:
        * Amount
        * Category
        * Month
        * Optional associated wallet

## Technology Stack

* Python
* Django
* Django REST Framework

## Setup

1.  **Prerequisites:**
    * Python 3.x
    * pip

2.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

3.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    venv\Scripts\activate # On Windows
    source venv/bin/activate # On macOS/Linux
    ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Users API

* `POST /api/users/register/` - Register a new user.
* `POST /api/users/login/` - Log in an existing user.

        JSON: (Example login)
            {
            "username": "testuser_check",
            "password": "SecurePass123!"
            }

### Wallets API

* `GET /api/wallets/` - List all wallets for the user.
* `POST /api/wallets/` - Create a new wallet.
* `GET /api/wallets/{id}/` - Fetch wallet details.
* `PUT /api/wallets/{id}/` - Update wallet details.
* `DELETE /api/wallets/{id}/` - Delete a wallet (if no transactions exist).
* `PUT /api/wallets/{id}/update_balance/` - Update the balance of a specific wallet.

    JSON: (Example - Create new wallet)

{
    "name": "New Wallet",
    "balance": 250.50,
    "type": "Cash"
}

JSON (Example - Update wallet detail)

{
    "name": "Updated Wallet Name",
    "balance": 300.00
}

### Transactions API

* `GET /api/transactions/` - List all transactions.
* `POST /api/transactions/` - Add a transaction.
* `PUT /api/transactions/{id}/` - Update a transaction.
* `DELETE /api/transactions/{id}/` - Delete a transaction.
* `GET /api/transactions/?wallet_id={id}` - Filter transactions by wallet.

JSON (Example)

{
    "amount": 25.75,
    "type": "Expense",
    "category": 1,  // Replace with an existing category ID
    "wallet": 1,    // Replace with an existing wallet ID
    "date": "2025-04-06",
    "description": "Coffee"
}


### Categories API

* `GET /api/categories/` - List all categories.
* `POST /api/categories/` - Create a new category.
* `PUT /api/categories/{id}/` - Update a category.
* `DELETE /api/categories/{id}/` - Delete a category.

JSON (Example - create category)

{
    "name": "Utilities"
}

### Budgets API

* `GET /api/budgets/` - List all budgets for the user.
* `POST /api/budgets/` - Create a new budget.
* `GET /api/budgets/{id}/` - Fetch budget details.
* `PUT /api/budgets/{id}/` - Update budget details.
* `DELETE /api/budgets/{id}/` - Delete a budget.
* `GET /api/budgets/?category_id={id}` - Filter budgets by category.
* `GET /api/budgets/?wallet_id={id}` - Filter budgets by wallet.
* `GET /api/budgets/?month=YYYY-MM-DD` - Filter budgets by month.

JSON(Example - create new Budget)

{
    "amount": 150.00,
    "category": 2,  // Replace with an existing category ID
    "month": "2025-05-01"
}

## Models

### Users App

* **Custom User Model:**
    * Extends Django's `AbstractUser`.
    * Fields: `username`, `email`, `password`.
    * Relationships: One-to-Many with Transactions, Wallets, and Budgets.
    * Constraints: `email` must be unique.

### Wallets App

* **Wallet Model:**
    * Fields:
        * `name` (CharField)
        * `balance` (DecimalField)
        * `type` (CharField)
        * `created_at` (Timestamp)
        * `user` (ForeignKey to User)
    * Relationships: One-to-Many with Transactions and Budgets.
    * Constraints:
        * Each wallet belongs to a single user.
        * `balance` >= 0.

### Transactions App

* **Transaction Model:**
    * Fields:
        * `amount` (DecimalField)
        * `type` (CharField - Income/Expense)
        * `category` (ForeignKey to Category)
        * `wallet` (ForeignKey to Wallet)
        * `date` (DateField)
        * `description` (TextField)
        * `user` (ForeignKey to User)
    * Relationships: Many-to-One with Category, Wallet, and User.
    * Constraints:
        * `amount` > 0.
        * Transaction linked to a valid wallet and category.

* **Category Model:**
    * Fields:
        * `name` (CharField)
        * `user` (ForeignKey to User)
    * Relationships: Many-to-One with Transactions and Budgets.
    * Constraints: Category name unique per user.

### Budgets App

* **Budget Model:**
    * Fields:
        * `amount` (DecimalField)
        * `category` (ForeignKey to Category)
        * `wallet` (ForeignKey to Wallet, optional)
        * `month` (DateField)
        * `user` (ForeignKey to User)
    * Relationships: Many-to-One with Category, Wallet, and User.
    * Constraints:
        * `amount` > 0.
        * Unique budget per category per month per user.

## Current Status

The API currently supports user authentication, wallet management, transaction tracking, category management, and budget tracking.

* User registration and login are implemented.
* Users can create, retrieve, update, and delete wallets.
* Users can record income and expense transactions, categorized by user-defined categories.
* Wallet balances are automatically updated upon transaction creation and deletion.
* Users can create, retrieve, update, and delete budgets.
* Users can filter budgets by category, wallet, and month.

## Future Enhancements

* Build Dashboards and Visualizations for User Insights

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.