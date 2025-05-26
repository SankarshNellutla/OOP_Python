# OOP_Python

## Overview

`OOP_Python` is a household repo of Jupyter notebooks exploring fundamental object-oriented programming (OOP) concepts in Python.

Currently includes:

- **Oop_practice.ipynb**: Interactive walkthrough of basic OOP principles.
- **main.ipynb**: Consolidated examples and exercises for classes, inheritance, encapsulation.

> **Note**: These notebooks contain personal study notes. Consider moving them to a private repository or local directory if you wish to keep them confidential.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation & Usage](#installation--usage)
- [Repository Structure](#repository-structure)
- [Hiding Personal Notes](#hiding-personal-notes)
- [Making the Repo Private](#making-the-repo-private)
- [Contributing](#contributing)
- [License](#license)

## Features

- Hands-on Jupyter notebooks covering:
  - Class and object definitions
  - Inheritance and polymorphism
  - Encapsulation with private/protected members
  - Real-world Python examples and exercises

## Requirements

- Python 3.8+
- Jupyter Notebook or JupyterLab
- (Optional) [Virtual environment](https://docs.python.org/3/tutorial/venv.html)

## Installation & Usage

1. **Clone repository**:
   ```bash
   git clone https://github.com/SankarshNellutla/OOP_Python.git
   cd OOP_Python
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\\Scripts\\activate.bat # Windows
   ```

3. **Install dependencies** (if you add any in `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

5. **Open** `Oop_practice.ipynb` or `main.ipynb` in your browser.

## Repository Structure

```
OOP_Python/
├── .gitignore
├── Oop_practice.ipynb  # Notebook: practicing classes, inheritance, encapsulation
├── main.ipynb          # Notebook: consolidated examples and exercises
└── README.md           # Project overview and instructions
```

## Hiding Personal Notes

If you want to exclude these notebooks (which contain your study notes) from a public repo:

1. **Remove** them from version control:
   ```bash
   git rm --cached *.ipynb
   ```
2. **Ignore** them in future commits by adding:
   ```text
   # .gitignore
   *.ipynb
   ```
3. **Commit** and **push** changes:
   ```bash
   git add .gitignore
   git commit -m "Exclude notebooks from public repo"
   git push origin main
   ```

Alternatively, maintain a separate **private** repo for your personal notebooks.

## Making the Repo Private

- **Via GitHub UI**:
  1. Go to **Settings** > **General**.
  2. Scroll to **Danger Zone** > **Change repository visibility**.
  3. Choose **Make private** and confirm.

- **Via GitHub CLI**:
  ```bash
  gh repo edit SankarshNellutla/OOP_Python --visibility private
  ```

## Contributing

Feel free to fork, file issues, or submit pull requests with improvements or additional examples.

## License

This project is licensed under MIT. See [LICENSE](LICENSE) for details.
