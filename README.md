# 📔 Digital Diary / Notes Manager

A simple and user-friendly **Digital Diary / Notes Manager** built using Python 3. This project allows users to create, view, search, and delete personal notes through a menu-driven interface.

The project uses Python's built-in modules and file handling to store notes permanently without requiring external libraries.

## 🚀 Features

- **Add Notes:** Create new notes with a specific date.
- **View All Notes:** Display all saved diary entries.
- **Search Notes:** Find notes using keywords.
- **Delete Notes:** Delete notes using their note numbers.
- **Date Validation:** Ensures dates follow the `YYYY-MM-DD` format.
- **Input Validation:** Handles empty notes and invalid menu choices.
- **File Storage:** Saves notes in `diary.txt` so they remain available after closing the program.

## 🛠️ Technologies Used

- Python 3
- File Handling
- Functions
- Lists and Dictionaries
- String Methods
- Exception Handling
- JSON (built-in Python module)

**No external libraries required!**

## 📂 Project Structure

```text
Digital-Diary-Project/
│
├── digital_diary.py
├── diary.txt
└── README.md
```

Note: `diary.txt` is automatically created when the first note is saved.

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Digital-Diary-Project
```

### 3. Run the Python Program

```bash
python digital_diary.py
```

## 💻 Menu Options

```text
========== DIGITAL DIARY / NOTES MANAGER ==========

1. Add Note
2. View All Notes
3. Search Notes
4. Delete Note
5. Exit

===================================================
```

## 📌 Example

```text
Enter your choice (1-5): 1

--- ADD NOTE ---

Enter date (YYYY-MM-DD): 2026-10-10
Enter note text: Started my Python project

Note saved.
1 | 2026-10-10 | Started my Python project
```

## 🎯 Project Objective

The main objective of this project is to understand and implement basic Python programming concepts through a practical application.

It demonstrates file handling, functions, conditional statements, loops, lists, dictionaries, input validation, and exception handling.

## 👨‍💻 Author

**Ayush Puri**

B.Tech – Computer Science Engineering (Artificial Intelligence & Machine Learning)

## 📜 License

This project is open-source and available for educational and learning purposes under the MIT License.
