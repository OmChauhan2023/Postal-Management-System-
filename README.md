<!-- 
README.md 
Postal Management System - CBSE Computer Science 12th Grade Project (2022-23)
Developed with Python, MySQL, and supporting libraries
-->

<h1 align="center">📮 Postal Management System</h1>
<p align="center">
CBSE Computer Science 12th Grade Project (Academic Year 2022-23) &nbsp;|&nbsp; Developed with 🐍 Python & 🐬 MySQL
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python"/>
<img src="https://img.shields.io/badge/MySQL-8+-orange?logo=mysql" alt="MySQL"/>
<img src="https://img.shields.io/badge/CBSE-Computer%20Science-teal?logo=google-classroom" alt="CBSE CS"/>
</p>

---

## ✨ Project Overview

Welcome to the **Postal Management System**, a project I built in Grade 12 (2022-23) as part of my CBSE Computer Science course.  
This console-based system helps manage postal sender and receiver data with secure login functionality, tracking, and database integration.

---

## 🌟 Features

### 🔐 User Authentication  
- User registration and login with password reset using Python's `pickle` to store credentials in `admin.dat`.

### 📨 Manage Postal Records  
- Add, edit, delete sender and receiver details stored securely in MySQL tables.  
- Automatically generate unique tracking IDs for each post.

### 📋 Data Display & Export  
- Beautiful, formatted terminal tables using `tabulate`.  
- CSV logs for each tracked post, recording transaction history.

### 📂 File & Database Integration  
- Python MySQL Connector (`mysql-connector-python`) for seamless DB access.  
- Local file handling for authentication and CSV export.

### 💻 Command Line Interface  
- User-friendly, menu-driven CLI for easy navigation.


## 🛠️ Tech Stack & Features

- **Python** for back-end & interface
- **MySQL** for persistent data storage (`mysql-connector-python` for integration)
- **tabulate** for beautiful terminal tables
- **pickle** for lightweight file-based authentication (`admin.dat`)
- **csv** for exports/record-keeping


## ⚡ Main Functionalities

  - 🔑 User login, registration, and password reset
  - 📝 Add, edit, delete sender & receiver records, all managed in MySQL
  - 🔎 Automatic and unique Tracking ID generation
  - 📊 Tabular data views using <code>tabulate</code>
  - 📦 CSV log for every transaction (per post)
  - 📃 "About Us" and custom exit messaging

## 🎯 How It Works

- Users can **register**, **login**, or **reset passwords**.  
- Once logged in, users can **add new postal entries** with sender and receiver information.  
- Posts are assigned a **unique tracking ID**.  
- Data can be **viewed, updated, or deleted** via intuitive menus.  
- Each addition creates a **CSV log file** recording the post event.  
- The **About Us** section displays project info from `aboutus.txt`.  
- Clean exit with a thank-you screen.

---

## 🏗️ Project Structure

Postal-Management-System/<br>
├── postal_management_system.py # Main source code<br>
├── aboutus.txt # Project info displayed in-app<br>
├── admin.dat # User credentials file <br>
├── exit.txt # Exit Note Displayed <br>
└── README.md # This documentation file<br>

---

## 📸 Screenshots

### MySQL Tables
<img width="1401" height="883" alt="sql" src="https://github.com/user-attachments/assets/75bfb03c-8a6c-4b6f-b73c-83fc5f5610f9" />
<br>

#### Sender Table
<img width="1243" height="486" alt="sender" src="https://github.com/user-attachments/assets/8e438b86-c324-4d10-b430-ed3f2dbb3971" />


#### Receiver Table
<img width="1237" height="490" alt="receiver" src="https://github.com/user-attachments/assets/20ac79c2-8791-46c8-b9f9-4b9d5efae528" />

### Application UI

#### Main Menu
<img width="597" height="337" alt="mainmenu" src="https://github.com/user-attachments/assets/0c98a2e9-ab81-4026-a257-bcfbb937c631" />


#### About Us
<img width="1561" height="397" alt="aboutus" src="https://github.com/user-attachments/assets/4d2af655-f548-445c-a907-d8395ce385bd" />


#### Exit Screen
<img width="917" height="272" alt="exit" src="https://github.com/user-attachments/assets/8d42e7cd-136b-4cab-8daa-a9a8396ed05d" />


---

## 📁 CSV Files

- Each post generates a CSV log with `Tracking_ID`, Date, and Description.
<img width="443" height="173" alt="csv" src="https://github.com/user-attachments/assets/1aa33a10-2cbf-4c1d-ab15-39d77ca2a547" />

---

## 🤝 Contributing
- Contributions, suggestions, and pull requests are welcome! <br>
- Please open an issue for major changes first.
---

## 📝 Academic Credits

- *This project was developed as part of the CBSE Computer Science syllabus during academic year 2022-23.*  
- It demonstrates file handling, CLI design, and integration with MySQL databases via Python.





