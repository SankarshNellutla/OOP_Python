# OOP_Python

## About

`OOP_Python` was created by Sankarsh Nellutla as a personal learning tool to reinforce core OOP principles in Python through practical, hands-on Jupyter notebooks. This repo serves both as a study aid and as a reference for anyone looking to solidify their understanding of classes, inheritance, encapsulation, and polymorphism.

## Overview

`OOP_Python` is a household repo of Jupyter notebooks exploring fundamental object-oriented programming (OOP) concepts in Python.

Currently includes:

- **main.ipynb**: Consolidated examples and exercises for classes, inheritance, encapsulation.
- **Oop_practice.ipynb**: Interactive walkthrough of basic OOP principles.

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

- Python (version 3.x) — on some systems invoke via `python`, on others via `python3`. Use whichever points to Python 3.
- Jupyter Notebook or JupyterLab
- (Optional) [Virtual environment](https://docs.python.org/3/tutorial/venv.html)

## Installation & Usage

1. **Clone repository**:
   ```bash
   git clone https://github.com/SankarshNellutla/OOP_Python.git
   cd OOP_Python
   ```

2. **(Optional) Create a virtual environment**:
   - If your system’s Python 3 is invoked with `python3`:
     ```bash
     python3 -m venv venv
     source venv/bin/activate      # macOS/Linux
     venv\Scripts\activate.bat   # Windows
     ```
   - If `python` points to Python 3:
     ```bash
     python -m venv venv
     source venv/bin/activate
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

## Acknowledgments

I learned many of the core concepts in this repository from the following resource:

- **YouTube Video:** [Learn OOP in Python](https://www.youtube.com/watch?v=IbMDCwVm63M)
  - Code samples have been completely rewritten and adapted from the author’s demonstrations to reinforce understanding.

Feel free to check out the original creator’s channel for more in-depth tutorials!

## Contributing

Feel free to fork, file issues, or submit pull requests with improvements or additional examples.

## License

This project is licensed under MIT. See [LICENSE](LICENSE) for details.
