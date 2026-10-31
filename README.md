<div align="center">

# 🧮 Python Tkinter Calculator

**A modern, lightweight, and responsive desktop calculator built with Python & Tkinter.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey?style=for-the-badge)](#platform-support)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

<br/>

```text
 ┌──────────────────────────────────┐
 │        Modern Calculator         │
 ├──────────────────────────────────┤
 │                     25 × 4 + 10  │  ◄── Live Expression History
 │                              110 │  ◄── Clean Active Display
 ├──────────────────────────────────┤
 │ [ C ]    [ ⌫ ]    [ % ]    [ ÷ ] │
 │ [ 7 ]    [ 8 ]    [ 9 ]    [ × ] │
 │ [ 4 ]    [ 5 ]    [ 6 ]    [ - ] │
 │ [ 1 ]    [ 2 ]    [ 3 ]    [ + ] │
 │ [ ± ]    [ 0 ]    [ . ]    [ = ] │
 └──────────────────────────────────┘
```

</div>

---

## 🌟 Overview

The **Python Tkinter Calculator** is an elegant desktop utility designed for everyday arithmetic and calculations. It combines clean modern ergonomics with rock-solid Python execution, zero external dependencies, and seamless physical keyboard controls.

Whether you're looking for a daily desktop tool or an open-source reference for building clean desktop GUIs with Python's standard `tkinter` library, this project provides both a full-featured modern calculator and an accessible classic implementation.

---

## ✨ Features

- 🎨 **Modern Dark Aesthetics**: Curated Obsidian / Zinc dark theme with contrasting warm-orange operators and emerald action buttons.
- ⌨️ **Full Physical Keyboard Support**: Complete keyboard bindings for digits, operators, backspace, clear, and enter.
- 🧠 **Dual-Line Display**: Shows the previous formula and operator sequence above your active answer, exactly like modern operating system calculators.
- 🛡️ **Guarded Evaluation Engine**: Built with a sandboxed mathematical evaluator that prevents arbitrary code execution and handles `ZeroDivisionError` gracefully.
- 🎯 **Smart Number Formatting**:
  - Automatically suppresses floating-point artifacts (e.g., `0.1 + 0.2` neatly resolves to `0.3`).
  - Converts whole floating results into clean integers (e.g., `8.0` displays as `8`).
  - Adds comma separators for large integer numbers (`1,000,000`).
- ⌫ **Backspace & Decimal Guards**: Prevent duplicate decimal points (`..`) and seamlessly correct typos on the fly.
- ⚡ **Zero Third-Party Dependencies**: Runs directly out-of-the-box using the built-in Python standard library.

---

## 📁 Repository Editions

This repository includes two versions to explore:

| File | Edition | Description |
| :--- | :--- | :--- |
| **[`main.py`](main.py)** | **Enhanced Modern Edition** | Modular OOP architecture, dark theme, dual-line display, keyboard navigation, hover animations, backspace & decimals. |
| **[`Tkinter calculator.py`](Tkinter%20calculator.py)** | **Original Classic Edition** | The lightweight procedural grid calculator originally coded by Neev Panchal. |

---

## 🚀 Getting Started

### Prerequisites

All you need is **Python 3.8 or higher**. Tkinter is bundled by default with standard Python installers on Windows and macOS.

> On Linux (Debian/Ubuntu), if Tkinter is not installed by default:
> ```bash
> sudo apt-get install python3-tk
> ```

### Installation & Launch

1. **Clone the repository**:
   ```bash
   git clone https://github.com/neevpanchal/Python-Tkinter-Calculator.git
   cd Python-Tkinter-Calculator
   ```

2. **Run the Modern Calculator**:
   ```bash
   python main.py
   ```

3. **Or run the Original Classic Calculator**:
   ```bash
   python "Tkinter calculator.py"
   ```

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
| :--- | :--- |
| `0` - `9` (and Numpad) | Type numbers |
| `+`, `-`, `*`, `/` | Arithmetic operations (`+`, `-`, `×`, `÷`) |
| `%` | Modulo / Percentage operation |
| `.` | Add decimal point (smart guard prevents duplicates) |
| `Enter` / `Return` / `=` | Calculate answer |
| `Backspace` | Delete previous character |
| `Escape` / `C` / `c` | Clear calculator |

---

## 📦 Packaging as Standalone Desktop App (.exe)

Want to run this without needing Python or the command line? You can compile it into a standalone executable using `pyinstaller`:

```bash
# 1. Install PyInstaller
pip install pyinstaller

# 2. Build single-file executable
pyinstaller --noconsole --onefile main.py
```

The compiled executable will be located in the newly created `dist/` folder:
- **Windows**: `dist/main.exe`
- **macOS/Linux**: `dist/main`

---

## 📂 Project Structure

```text
Python-Tkinter-Calculator/
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md          # Standard bug report template
│       └── feature_request.md     # Feature suggestion template
├── .gitignore                     # Git ignore rules for Python
├── CONTRIBUTING.md                # Community contribution guidelines
├── LICENSE                        # MIT Open Source License
├── README.md                      # Project documentation & visual guide
├── requirements.txt               # Dependencies and packaging references
├── Tkinter calculator.py          # Original classic edition by Neev Panchal
└── main.py                        # Enhanced modern edition
```

---

## 🤝 Contributing

Contributions are warmly welcome! Whether it is adding scientific functions, sound effects, or new color schemes:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Check out [`CONTRIBUTING.md`](CONTRIBUTING.md) for full guidelines.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">

Crafted with ❤️ by **[Neev Panchal](https://github.com/neevpanchal)**

⭐ If you found this project helpful or inspiring, please consider giving it a star on GitHub!

</div>
