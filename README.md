# Farm Management System

A Django-based Farm Management System to streamline farm operations and data management keeping track of farm operations.
Agriculture is the backbone of every growing economy.
Not just the economy, but  i can just name it as a breath!!
Yeah!! you cant live without breathing!!

sure you cant live without agriculture!! 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

# Introduction

Welcome to the Farm Management System.This farm management system aims to keep truck of the most operations in a farm. Keeping records of your daily operations is an important factor for a successfull and profitable farming. I aim to make your work easier by providing this platform where you can keep your farm records.

# Features

## Crop Management 🌾
The heart of the Farm Management System lies in its robust Crop Management section. Seamlessly monitor all operations related to your crops with a user-friendly interface. This includes tracking the planting day, the associated field, and adding essential details such as crop operations, variety, crop name, sales, and expenses, each meticulously timestamped for a comprehensive overview.

#### Crop Operations
Record every facet of your crop operations, including:

- **Operation Date:** Capture the date of each operation.
- **Operation Name:** Specify the type of operation, such as planting, harvesting, or irrigation.
- **Additional Notes:** Add any relevant notes or details for future reference.

#### Expenses Details
Efficiently manage your crop-related expenses with detailed records:

- **Expense Date:** Document the date of each expense.
- **Expense Type:** Categorize expenses based on their types.
- **Expense Description:** Provide a brief description of the expense.
- **Budget Amount:** Set a budget amount for better financial planning.
- **Expense Amount:** Record the actual expense amount.
- **Supplier Name:** Identify the supplier associated with the expense.
- **Payment Method:** Specify the payment method used.
- **Receipt Number:** Log the receipt number for easy reference.

#### Sales Details
Keep track of your crop sales with precision:

- **Sales Date:** Record the date of each sale.
- **Quantity Sold:** Specify the quantity of crops sold.
- **Unit Price:** Set the unit price for accurate pricing.
- **Total Price:** Automatically calculated based on quantity and unit price.
- **Buyers Information:** Document details about the buyers.
- **Payment Method:** Specify the payment method used by the buyer.
- **Payment Status:** Track the payment status (paid, pending, etc.).
- **Invoice Number:** Assign a unique invoice number to each sale.
- **Additional Information:** Include any supplementary information related to the sale.

Effortlessly manage and organize your farming activities, ensuring you have a detailed record of every step in your crop cultivation journey. Stay on top of your agricultural operations with the Crop Management feature, designed to enhance your farming experience.



## Employees 🌾👩‍🌾👨‍🌾
The Employees section acts as your farm's personnel hub, maintaining comprehensive records of the hardworking individuals contributing to your agricultural success. Keep track of essential employee details, including:

- **Names:** Easily identify and manage your team members.
- **Phone Numbers:** Maintain direct communication channels with each employee.
- **Position:** Clearly define the roles and responsibilities of each team member.
- **Salary:** Track financial aspects with a record of salaries for transparent payroll management.
- **Performance:** Assess and document employee performance to recognize and encourage growth.

With the Employees feature, empower your farm's workforce management, ensuring a harmonious and efficient collaboration between your team members.


## Livestock 🐄🐖🐑
Manage your livestock efficiently with the Livestock section, equipped with features tailored to meet the diverse needs of your farm's animals. Track crucial information about each animal, including:

- **Age:** Keep tabs on the age of your livestock for strategic planning.
- **Breed:** Document the specific breeds, aiding in targeted breeding programs.
- **Production Details:** Monitor the overall production-related metrics for each animal.
- **Animal Type:** Categorize animals based on their types for easy identification.

The Production Features allow you to record key data points aligned with production activities:

- **Production Date:** Capture the date of each production cycle.
- **Feed Consumed:** Track the feed consumption patterns, ensuring a well-balanced diet.
- **Production Amount:** Document the quantity or output of each production cycle.
- **Comments:** Add additional insights or observations related to the production.

Designed with an intuitive interface, the Livestock feature provides a seamless way to manage and optimize your livestock, fostering a healthy and productive environment on your farm.


## Machinery 🚜🛠️
Efficiently manage your farm's machinery with the Machinery section, designed to keep detailed records of essential equipment. Each piece of machinery is meticulously documented with the following information:

- **Equipment Name:** Easily identify and categorize your farm machinery.
- **Purchase Price:** Record the cost associated with acquiring each piece of equipment.
- **Purchase Date:** Capture the date when the machinery was purchased.
- **Operations:** Track the usage and operational history of each piece, ensuring optimal efficiency.
- **Maintenance Activities:** Document essential maintenance activities, safeguarding the longevity and performance of your machinery.

With the Machinery feature, stay in control of your farming infrastructure, optimize equipment utilization, and ensure that your machinery operates at peak efficiency throughout its lifecycle.




## Egg production and Milk production 🐔🐓🐄
Your production!!

The main aim of rearing animals is the production.

Using this system you as a farmer things have been simplified for you.
You can keep track of your milk and egg production records. Some of the fields that are contained in the records are:

- **Production Year, month and Day:**   You need to keep the record of the production aligning with the respective dates for easier analysing. This section also contains a graphical interface for visualisation, You can seethe comparison between feeds consumed and the day, production vs day in the milk production section.

- **Number of livestock involved:** You will record the number of animals involved in the production for a better analysingtallation


# Installation

Follow these steps to set up the Farm Management System on your local machine:

## 1) Clone the Repository:

```bash

git clone https://github.com/denisganga/Farm_Management_System.git
```

## 2) Navigate to the Project Directory:

```bash

cd farm-management-system
```

## 3) Create Virtual Environment:

```bash

python -m venv venv
```

## 4) Activate Virtual Environment:

   For Windows:

```bash

venv\Scripts\activate
```

For MacOS/Linux:

```bash

    source venv/bin/activate
```

## 5) Install Dependencies:

```bash

pip install -r requirements.txt
```

## 6) Run Migrations:

```bash

python manage.py migrate
```

## 7) Create Superuser:

```bash

python manage.py createsuperuser
```

## 8) Run the Development Server:

```bash

    python manage.py runserver
```

  ## 9) Access the Application:
   Open your web browser and go to `http://localhost:8000/` 
  to access the Farm Management System.

# Usage

  Login:
        Access the admin dashboard by going to `http://localhost:8000/admin/`.
        Log in using the superuser credentials created during the installation.

  Explore Features:
        Navigate through the Crop Management, Employees, Livestock, Machinery, Egg Production, and Milk Production sections to manage your farm operations.

  Record Data:
        Add crop operations, expenses, sales, employee details, livestock information, machinery records, egg production, and milk production data using the user-friendly forms provided.

  Visualize Data:
        Utilize the graphical interfaces in the  Milk Production sections to analyze and visualize production trends.

# Configuration

The Farm Management System can be configured based on specific farm requirements. Adjust settings, customize forms, and modify templates to tailor the system to your farm's unique needs.

# Contributing

We welcome contributions to enhance and improve the Farm Management System. To contribute, follow these steps:

  1) Fork the repository.
  2) Create a new branch for your feature or bug fix.
  3) Make your changes and commit them with descriptive commit messages.
  4) Push your changes to your fork.
  5) Submit a pull request, detailing the changes you made.

For more details, check the Contribution Guidelines.
# License

This project is licensed under the [MIT_license](MIT_license).
# Contact

For any inquiries or assistance, feel free to contact me at denisnganga16@gmail.com. I appreciate your feedback and suggestions!

Thank you for choosing the Farm Management System. Happy farming!






