# Personal Budget Tracker API

## Introduction

The Personal Budget Tracker API is a Django REST Framework backend designed to help users manage their finances effectively. It provides endpoints for user authentication, wallet management, transaction tracking, and category management. This API is built to support a web-based application that allows users to monitor their income and expenses, and achieve better financial planning. [cite: 3, 4]

## Features

The API currently supports the following core features:

* **User Authentication:**
    * Secure user registration and login[cite: 5].
    * Personalized data storage for each user[cite: 5].
* **Wallet Management:**
    * Creation and management of multiple wallets per user (e.g., Checking, Savings)[cite: 6].
    * Wallet attributes:
        * Name [cite: 7]
        * Type [cite: 7]
        * Current balance [cite: 7]
* **Transaction Tracking:**
    * Recording of income and expense transactions[cite: 7].
    * Transaction details:
        * Date [cite: 8]
        * Amount [cite: 8]
        * Description [cite: 8]
        * Category (e.g., Groceries, Rent) [cite: 8]
        * Associated Wallet [cite: 8]
        * Transaction Type (Income or Expense) [cite: 8]
* **Expense Categories:**
    * Management of transaction categories[cite: 8, 9].
    * Customizable categories per user[cite: 9].

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
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
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

* `POST /api/users/register/` - Register a new user[cite: 27].
* `POST /api/users/login/` - Log in an existing user[cite: 27].

### Wallets API

* `GET /api/wallets/` - List all wallets for the user[cite: 28].
* `POST /api/wallets/` - Create a new wallet[cite: 29].
* `GET /api/wallets/{id}/` - Fetch wallet details[cite: 29].
* `PUT /api/wallets/{id}/` - Update wallet details[cite: 30].
* `DELETE /api/wallets/{id}/` - Delete a wallet (if no transactions exist)[cite: 30].
* `PUT /api/wallets/{id}/update_balance/` - Update the balance of a specific wallet.

### Transactions API

* `GET /api/transactions/` - List all transactions[cite: 31].
* `POST /api/transactions/` - Add a transaction[cite: 31].
* `PUT /api/transactions/{id}/` - Update a transaction[cite: 32].
* `DELETE /api/transactions/{id}/` - Delete a transaction[cite: 32].
* `GET /api/transactions/?wallet_id={id}` - Filter transactions by wallet[cite: 33].

### Categories API

* `GET /api/categories/` - List all categories.
* `POST /api/categories/` - Create a new category.
* `PUT /api/categories/{id}/` - Update a category.
* `DELETE /api/categories/{id}/` - Delete a category.

## Models

### Users App

* **Custom User Model:**
    * Extends Django's `AbstractUser`[cite: 13].
    * Fields: `username`, `email`, `password`[cite: 13].
    * Relationships: One-to-Many with Transactions and Wallets[cite: 14].
    * Constraints: `email` must be unique[cite: 14].

### Wallets App

* **Wallet Model:**
    * Fields:
        * `name` (CharField) [cite: 14]
        * `balance` (DecimalField) [cite: 15]
        * `type` (CharField) [cite: 15]
        * `created_at` (Timestamp) [cite: 15]
        * `user` (ForeignKey to User) [cite: 16]
    * Relationships: One-to-Many with Transactions[cite: 16].
    * Constraints:
        * Each wallet belongs to a single user[cite: 16].
        * `balance` >= 0[cite: 17].

### Transactions App

* **Transaction Model:**
    * Fields:
        * `amount` (DecimalField) [cite: 17]
        * `type` (CharField - Income/Expense) [cite: 18]
        * `category` (ForeignKey to Category) [cite: 18]
        * `wallet` (ForeignKey to Wallet) [cite: 18]
        * `date` (DateField) [cite: 19]
        * `description` (TextField) [cite: 19]
        * `user` (ForeignKey to User) [cite: 19]
    * Relationships: Many-to-One with Category, Wallet, and User[cite: 20].
    * Constraints:
        * `amount` > 0[cite: 20].
        * Transaction linked to a valid wallet and category[cite: 21].

* **Category Model:**
    * Fields:
        * `name` (CharField) [cite: 21]
        * `user` (ForeignKey to User) [cite: 22]
    * Relationships: Many-to-One with Transactions[cite: 22].
    * Constraints: Category name unique per user[cite: 22].

## Current Status

The API currently supports user authentication, wallet management, transaction tracking, and category management.

* User registration and login are implemented.
* Users can create, retrieve, update, and delete wallets.
* Users can record income and expense transactions, categorized by user-defined categories.
* Wallet balances are automatically updated upon transaction creation and deletion.

## Future Enhancements

* Budget Goals: Implement functionality for users to set budget limits. [cite: 10]
* Date Filtering: Add endpoints to filter transactions by date ranges. [cite: 9]
* Dashboard: Develop endpoints for financial summaries and visualizations. [cite: 10, 12]
* Testing: Implement comprehensive test suites.
* Documentation: Expand API documentation with detailed request/response examples.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

[License information]