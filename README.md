# coffee-shop


## Overview

This project models a coffee shop using object-oriented programming in Python. It consists of three main entities:

- `Customer`
- `Coffee`
- `Order`

These classes are designed to simulate real-world relationships and business logic within a coffee shop system.

##  Folder Structure

coffee-shop/
|__lib/
    ├── customer.py
    ├── coffee.py
    ├── order.py
    ├── debug.py
|__ tests/
 ├── test_customer.py
 ├── test_coffee.py
 └── test_order.py
├── Pipfile
├── Pipfile.lock
└── README.md



##  Domain Model

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

> This forms a many-to-many relationship between `Customer` and `Coffee` through `Order`.

---

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Michael-juma/coffee-shop.git
   cd coffee-shop

