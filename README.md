# Experimental Statistical Analysis Toolkit

A Python-based toolkit designed to perform statistical analysis on experimental results. This project provides utilities for data preprocessing, statistical testing, visualization, and reproducible analysis workflows.

---

## Overview

This repository contains scripts and modules created to support experimental research through structured statistical analysis. The goal is to simplify the process of loading datasets, running statistical tests, and generating clear analytical outputs.

The project is suitable for:

* Scientific experiments
* Academic research
* Data analysis workflows
* Engineering and laboratory testing

---

## Technologies Used

* Python 3.x
* NumPy
* Pandas
* SciPy
* Matplotlib / Seaborn (optional for visualization)
* itertools
* Object-Oriented Programming (OOP)-based architecture for scalability and maintainability

---

## ▶️ Usage

Example of running an analysis script:

```bash
python main.py
```

Or import the modules in your own project:

```python
from analysis import run_statistical_analysis

results = run_statistical_analysis("data/experiment.csv")
print(results)
```

---

## Project Structure

```
└── 📁Analytix
    └── 📁filtros
        ├── __init__.py
        ├── loc_produto.py
        ├── loc.py
        ├── produto.py
    └── 📁metodos
        ├── __init__.py
        ├── carta_amplitude.py
        ├── distribuicao.py
        ├── information.py
    ├── .gitignore
    ├── data.py
    ├── ifiltro.py
    ├── igraph.py
    └── main.py
```
