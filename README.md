# 🎓 University Admission Management System (UAMS)

A complete **Django-based University Admission Management System** designed to streamline the entire academic workflow — from student registration and course applications to faculty management, course enrollment, and results tracking.

---

## 🚀 Features

### 👤 Authentication & Accounts
- User registration and login (students, staff, and admin)
- Role-based dashboard views
- Secure session handling with Django Auth

### 🏫 Admissions Module
- Departments and Programs management
- Students can view available programs
- Apply online with document uploads (transcripts, certificates)
- Admins can approve, reject, or comment on applications

### 🧾 Enrollment & Results
- Students can register for approved courses
- Admins manage enrolled students
- Automatic GPA and grade calculation
- Students can view results and course history

### 👨‍🏫 Faculty & Courses Management
- Faculty profile creation and assignment to courses
- Faculty can manage teaching schedules
- Faculty can submit grades for enrolled students
- Admin can manage all courses and faculty data

---

## 🏗️ Project Structure

```
university_admission/
│
├── accounts/                # User registration, login, dashboard
├── admissions/              # Departments, programs, and student applications
├── results_and_enrollment/  # Enrollments, results, course registration
├── faculty_management/      # Faculty profiles and course schedules
├── templates/               # Global templates (base, dashboard, etc.)
├── static/                  # Static assets (CSS, JS, images)
├── media/                   # Uploaded files (certificates, transcripts)
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/university_admission_portal_django.git
cd university_admission_portal_django
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```

Now open your browser and go to **http://127.0.0.1:8000/** 🎉

---

## 🧩 Default Apps Included

| App Name | Description |
|-----------|-------------|
| **accounts** | Handles login, registration, and dashboard. |
| **admissions** | Students can apply for programs; admin can approve/reject. |
| **results_and_enrollment** | Students register courses, view results. |
| **faculty_management** | Faculty manage courses, upload grades. |

---

## 💾 Tech Stack

- **Backend:** Django 5+, Python 3.8+  
- **Frontend:** HTML5, Bootstrap 5, JavaScript  
- **Database:** SQLite (default), supports PostgreSQL/MySQL  
- **Authentication:** Django’s built-in user model  
- **File Storage:** Django Media (FileField/ImageField)

---

## 🔐 User Roles

| Role | Permissions |
|------|--------------|
| **Student** | Apply for programs, register courses, view results |
| **Faculty** | Manage assigned courses, upload grades |
| **Admin** | Full access to all modules, approvals, and reports |

---

## 🌍 URLs Overview

| URL | Description |
|------|-------------|
| `/register` | Register new user |
| `/login` | Login for existing user |
| `/dashboard` | Main dashboard |
| `/programs` | View available programs |
| `/apply/<id>` | Apply for a program |
| `/my-applications` | View submitted applications |
| `/enrollment_dashboard` | Manage course registrations |
| `/view_results` | View grades and GPA |
| `/faculty_dashboard` | Faculty’s course management panel |

---

## 🧠 Future Enhancements

- Notifications for admission status changes  
- Payment integration for admission fee  
- PDF export for transcripts and results  
- Email verification and OTP login

---

## 👨‍💻 Author
**Developed by:** Enigmatix  
**Role:** Backend Developer  
**Language:** Python (Django Framework)

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.