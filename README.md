# ⚙️ PyCompileX — A Mini Compiler Engine in Python

### 👤 Author

**Name:** *Shreyansh Singh*
**Reg No:** *RA2311003050275*

---

## 🚀 Overview

**PyCompileX** is a Python-based mini compiler engine that simulates how real-world compilers transform source code into machine-level instructions.

This project walks through every critical stage of compilation — from breaking code into tokens to generating optimized low-level instructions — offering a hands-on understanding of compiler design.

---

## 🧩 Features

* 🔍 Tokenization of source code
* 🧠 Grammar validation (Syntax checking)
* ⚡ Semantic error detection
* 🔁 Three Address Code generation
* 🚀 Code optimization techniques
* 🖥️ Simple machine code generation

---

## 🏗️ Architecture

The compiler is divided into 6 independent modules:

```bash
Compiler-Design/
│
├── Phase1_Lexical/
├── Phase2_Syntax/
├── Phase3_Semantic/
├── Phase4_ICG/
├── Phase5_Optimizer/
├── Phase6_CodeGen/
│
└── README.md
```

Each module handles a specific stage of compilation.

---

## 🔄 Compilation Pipeline

### 1️⃣ Lexical Analysis

Breaks input code into tokens.

```c
int a = 5;
```

```
KEYWORD     : int
IDENTIFIER  : a
OPERATOR    : =
NUMBER      : 5
SEPARATOR   : ;
```

---

### 2️⃣ Syntax Analysis

Checks if the input follows valid grammar rules.

```
a = b + c
```

```
✔ Syntax is VALID
```

---

### 3️⃣ Semantic Analysis

Ensures logical correctness.

* Variable declaration check
* Redeclaration detection
* Usage before declaration

```
✔ Semantic Analysis Successful
```

---

### 4️⃣ Intermediate Code Generation

Generates Three Address Code (TAC).

```
a = b + c * d
```

```
t1 = c * d
t2 = b + t1
a = t2
```

---

### 5️⃣ Code Optimization

Removes redundancy and improves efficiency.

```
Before:
t1 = c * d
t2 = b + t1
a = t2

After:
a = t2
```

---

### 6️⃣ Code Generation

Produces simplified machine-level instructions.

```
MOV R1, c
MUL R1, d
MOV t1, R1
MOV R2, b
ADD R2, t1
MOV t2, R2
```

---

## ⚙️ Tech Stack

* Python 3
* Regular Expressions
* File Handling
* Core Compiler Design Concepts

---

## ▶️ How to Run

```bash
cd Phase1_Lexical
python lexer.py
```

Run each phase independently using its respective Python file.

---

## 🎯 What You’ll Learn

* How compilers process code internally
* Differences between syntax & semantic errors
* Intermediate representations like TAC
* Basic optimization strategies
* Low-level instruction generation


---

## ⭐ Highlights

* Clean modular design
* Easy to understand
* End-to-end compiler simulation
* Strong foundation for advanced compiler projects

---

## 📌 Future Improvements

* GUI-based compiler visualization
* Support for complex grammar
* Integration with real parsers (like ANTLR)
* Assembly-level code generation

