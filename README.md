# VSC Typing Animation

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)


VSC Typing Animation is a **Python GUI tool** that records your code as a typing animation in a VS Code-like interface.  
It supports multiple programming languages with **syntax highlighting**.

⚠ **Important Warning:**  
The program **does not filter file types**. It will try to open **any file you add**, including large files like videos or binaries.  
Adding huge files may **freeze or crash the program**, so only drag files you actually want to animate.

---

## Features

- VS Code-like interface with tabs, sidebar
- Syntax highlighting for some keyword in languages
- Live typing animation of your code
- Automatic start and stop of recording for each file(save to Videos)
- Lightweight and easy to use

---

## Installation

Clone the repository and install the dependencies:

```bash
git clone "https://github.com/HirunDinukshana/Vsc-Typing-Animation"
cd VSC-Typing-Animation
pip install -r requirements.txt
python main.py
