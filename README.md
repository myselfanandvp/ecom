# 🛒 Django E-Commerce Product Manager

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-success.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> A minimal Django-based product management system for small-scale e-commerce applications. Easily create, update, delete, and list products with image upload support and a session-based "Recently Edited" product tracker.

---

## ✨ Features

- 🔒 User authentication (login required for all actions)
- 🖼️ Upload product images
- ✍️ Create, edit, and delete products
- 🧾 View all products in a styled list
- 🧠 Tracks 3 recently edited products using session
- 💬 Form validation with error messages
- 💅 Responsive UI using Bootstrap + MDB
- ♻️ Image deletion on product removal
- 🧼 Clean UX with CSRF protection and `never_cache`

---

## 🖼️ Demo Preview

| Product List | Edit Product | Create Product |
|--------------|--------------|----------------|
| ![List](static/screenshots/product_list.png) | ![Edit](static/screenshots/edit_product.png) | ![Create](static/screenshots/create_product.png) |

---

## 🛠 Tech Stack

| Layer     | Tech                                    |
|-----------|-----------------------------------------|
| Backend   | Django (Python)                         |
| Frontend  | Bootstrap 5 + MDB (Material Design)     |
| Database  | SQLite (Django default)                 |
| Forms     | Django ModelForm                        |
| Media     | Django `ImageField` & `MEDIA_ROOT`      |

---

## 📁 Project Structure

```bash
ecommerce_project/
├── products/
│   ├── templates/
│   │   ├── product_create.html
│   │   ├── product_edit.html
│   │   └── productlist.html
│   ├── models.py        # Products model
│   ├── forms.py         # ProductForm (with field hiding if needed)
│   ├── views.py         # All CRUD views + recent edit logic
│   └── urls.py
├── media/               # Uploaded product images
├── static/              # Static files (MDB, Bootstrap)
├── templates/
│   └── index.html       # Base template
├── manage.py
└── db.sqlite3
