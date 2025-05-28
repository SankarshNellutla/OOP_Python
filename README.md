# Python

## About

`Python` is a personal learning repository created by Sankarsh Nellutla to consolidate foundational Python programming concepts along with object-oriented programming (OOP) principles. This collection of Jupyter notebooks is aimed at both reinforcing theory and providing hands-on coding practice.

## Overview

This repository serves as a structured resource for:

* Understanding Python syntax and structure
* Practicing object-oriented principles
* Reinforcing programming logic through examples and exercises

It includes foundational and intermediate-level Python material designed for both quick reference and deeper exploration.

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation & Usage](#installation--usage)
* [Repository Structure](#repository-structure)
* [Hiding Personal Notes](#hiding-personal-notes)
* [Making the Repo Private](#making-the-repo-private)
* [Acknowledgments](#acknowledgments)
* [Contributing](#contributing)
* [License](#license)

## Features

* Well-organized Jupyter notebooks for:

  * Python basics: syntax, data types, control flow
  * Object-oriented programming: classes, inheritance, polymorphism, encapsulation
  * Real-world inspired exercises and demos

## Requirements

* Python 3.x
* Jupyter Notebook or JupyterLab
* (Optional) [Virtual environment](https://docs.python.org/3/tutorial/venv.html)

## Installation & Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SankarshNellutla/Python.git
   cd Python
   ```

2. **(Optional) Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate.bat
   ```

3. **Install any dependencies** (if applicable):

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**:

   ```bash
   jupyter notebook
   ```

5. Open any of the notebooks in your browser to begin learning.

## Repository Structure

```text
Python/
├── BasicPython_main.ipynb   # Python fundamentals: syntax, data types, control flow
├── OopPython_main.ipynb     # Object-oriented programming examples
├── Oop_practice.ipynb       # Hands-on OOP exercises
├── .gitignore               # Ignore patterns (e.g., .DS_Store)
└── README.md                # This file
```

## Hiding Personal Notes

To keep notebooks private or exclude personal study notes from public view:

1. Remove them from version control:

   ```bash
   git rm --cached *.ipynb
   ```

2. Add to `.gitignore`:

   ```text
   *.ipynb
   ```

3. Commit and push:

   ```bash
   git add .gitignore
   git commit -m "Exclude notebooks from version control"
   git push origin main
   ```

Alternatively, maintain a separate private repository.

## Making the Repo Private

* **Via GitHub UI**:

  1. Go to **Settings** > **General**
  2. Scroll to **Danger Zone** > **Change repository visibility**
  3. Choose **Make private** and confirm

* **Via GitHub CLI**:

  ```bash
  gh repo edit SankarshNellutla/Python --visibility private
  ```

## Acknowledgments

The content is largely inspired by personal exploration and supplemented by tutorials such as:

* [Learn OOP in Python](https://www.youtube.com/watch?v=IbMDCwVm63M)
* [Python Programming - Programming with Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc)

Code samples have been adapted and rewritten to enhance clarity and retention.

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature-topic`
3. Add or modify content
4. Ensure notebooks run error-free
5. Submit a Pull Request

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

© 2025 Sankarsh Nellutla
