<div align="center">
  <img src="static/images/logo.png" alt="Logo" width="380"/>
  <p><em>A Comprehensive Platform for Students & Professionals</em></p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
    <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
    <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status" />
  </p>
</div>

<hr/>

## 📖 About LinkedHub

**LinkedHub** is a dynamic platform designed to connect people through tasks and shared knowledge. Whether you're a student looking for study materials, or a professional aiming to build your profile, showcase your portfolio, and find gig opportunities, LinkedHub brings it all together!

---

## ✨ Amazing Features

### 🧑‍💼 Professional Profiles
Build a strong personal brand with customizable profiles:
- **Profile & Banner Images**
- **Education History & Degrees**
- **Portfolio & Document Uploads** (Resumes, Certificates)
- **Social Links** integration (GitHub, LinkedIn, Twitter, etc.)

### 📝 Task Management & Gigs
Post and apply for tasks seamlessly:
- **Task Categories:** General, Urgent, Delivery, Cleaning.
- **Budgeting & Deadlines**
- **Application System:** Users can apply, and creators can accept/reject.

### 📚 Study Materials Hub
Share and access valuable academic resources:
- **Uploads:** PDFs, Images, Notes, and Books.
- **Categories:** School/College Question Papers, Competitive Exams, Sample Papers.
- **View Tracking:** See how many times your materials are accessed!

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default) / PostgreSQL (configurable)
- **Storage:** Amazon S3 (for media, profile pics, and documents)
- **Frontend:** HTML5, CSS3, JavaScript (with responsive UI components)

---

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SOMU3103/LinkedHub.git
cd LinkedHub
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your configuration (e.g., PSQL,MYSQL, FOR PRODUCTION USE AWS EC2-S3)

### 5️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to see the magic happen! 🎉

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/SOMU3103">SOMU3103</a> & Contributors</p>
</div>
