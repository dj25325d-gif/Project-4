# 🐍 Python Data Processing CLI System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Type](https://img.shields.io/badge/Project-Portfolio-important)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Project Overview

This project is a **menu-driven Python command-line application** designed to demonstrate strong foundational programming skills in data handling and algorithmic thinking.

It allows users to input datasets (1D or 2D) and perform multiple analytical operations including statistical summaries, recursive factorial computation, filtering using lambda expressions, and sorting.

The project emphasizes **clean function design, modular structure, and real-world problem solving**, making it suitable for showcasing core Python competencies in a professional portfolio.

```
project4.py
```

---

## 🎯 Key Skills Demonstrated

* Python fundamentals & clean coding practices
* Functional decomposition and modular design
* Recursion implementation
* Lambda expressions and higher-order functions
* Data transformation and statistical analysis
* Interactive CLI application development
* Error handling and user-driven workflows

---

## 🧭 System Architecture

The application follows a structured flow:

```mermaid
flowchart TD
    A[Start Program] --> B[Display Main Menu]
    B --> C{User Choice}
    C -->|1| D[Input Dataset]
    C -->|2| E[Display Summary]
    C -->|3| F[Factorial Calculation]
    C -->|4| G[Filter Data]
    C -->|5| H[Sort Data]
    C -->|6| I[Dataset Statistics]
    C -->|7| J[Exit Program]
    D --> B
    E --> B
    F --> B
    G --> B
    H --> B
    I --> B
```

---

## 🖥️ Application Walkthrough

### Main Menu Interface

The program runs in a continuous loop, allowing users to perform multiple operations without restarting the application. Each menu option maps to a specific Python concept.

📸 **Screenshot — Main Menu**
---

![](menu.png)

---

### Option 1 — Input Dataset

Users can input either:

* A 1D numeric list
* A 2D numeric matrix

The dataset is normalized internally for efficient processing.

📸 **Screenshot — Input Dataset**
---

![](input_data.png)


---

### Option 2 — Display Data Summary

Generates a quick statistical overview using Python built-in functions:

* Count
* Minimum
* Maximum
* Sum
* Average

📸 **Screenshot — Data Summary**
---

![](data_summary.png)


---

### Option 3 — Recursive Factorial Calculator

Demonstrates recursion by computing factorial values through self-calling functions.

📸 **Screenshot — Factorial Calculation**
---

![](factorial.png)


---

### Option 4 — Lambda-Based Filtering

Applies functional programming techniques using lambda expressions to filter dataset values based on user-defined thresholds.

📸 **Screenshot — Filtered Output**
---

![](lambda_function.png)


---

### Option 5 — Sorting Engine

Implements ascending and descending sorting using Python’s built-in sorting mechanisms.

📸 **Screenshot — Sorted Data**

---

![](sort.png)


---

### Option 6 — Dataset Statistics

Performs structured statistical analysis using reusable helper functions.

📸 **Screenshot — Dataset Statistics**
---

![](dataset.png)


---

### Option 7 — Program Exit

Gracefully terminates the application.

📸 **Screenshot — Exit Message**
---

![](goodbye.png)


---

## 🧠 Core Functional Design

### Data Processing Pipeline

```mermaid
flowchart LR
    A[Raw Input] --> B[Dataset Storage]
    B --> C[Flatten Function]
    C --> D[Statistical Functions]
    D --> E[User Output]
```

---

## ▶️ How to Run

```bash
git clone <repository-url>
cd <project-folder>
python project4.py
```

---

## 📁 Project Structure

```
├── project4.py
├── README.md
└── screenshots/
 	-menu.png
	-data_summary.png
	-dataset.png
	-factorial.png
	-goodbye.png
	-input_data.png
	-lambda_function
	-sort.png
```

---

## 🚀 Portfolio Value

This project highlights:

* Practical application of Python fundamentals
* Structured problem-solving ability
* Clean CLI design
* Readable and maintainable code
* Real-world data processing logic

It serves as a strong example of early-stage software engineering capability and programming discipline.

---

## 🔮 Possible Enhancements

* GUI interface using Tkinter or PyQt
* Data visualization with Matplotlib
* File import/export (CSV/JSON)
* Unit testing framework
* Performance optimizations

---

## 📜 License

This project is released under the MIT License.

---

## 👤 Author

Developed as part of a Python learning portfolio project focused on building strong programming foundations.

---

⭐ If you found this project useful, consider starring the repository!
"# Project-4" 
