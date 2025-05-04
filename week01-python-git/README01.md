# Week 1 – Python Foundations & Git Basics

## 📌 Overview

This week focuses on setting up a proper Python environment, getting comfortable with Git basics, and building a simple CSV analysis script that reads a dataset and outputs summary statistics.

## 🎯 Milestone Project

**CSV Analyzer** – A Python CLI script that:

* Loads a CSV file using `pandas`
* Displays the first 5 rows
* Prints summary statistics
* Handles missing file errors

## 🧠 Key Skills Practiced

* Creating and activating a Python virtual environment
* Using Git commands: `init`, `add`, `commit`, `branch`, `merge`, `push`
* Writing modular Python with `argparse`
* Handling exceptions gracefully

## 📁 Project Structure

```
week01-python-git/
├── analyze_data.py       # Main script
├── iris.csv              # Sample dataset
└── README.md             # This file
```

## 🚀 How to Run

```bash
# From the project folder
python analyze_data.py --file iris.csv
```

## 🧾 Dependencies

* Python 3.10+
* pandas

Install via:

```bash
pip install -r requirements.txt
```

## 💡 Example Output

```
First 5 rows:
   sepal_length  sepal_width  petal_length  petal_width    species
0           5.1          3.5           1.4          0.2     setosa
1           4.9          3.0           1.4          0.2     setosa
...

Summary statistics:
       sepal_length  sepal_width  petal_length  petal_width
count     150.000000   150.000000    150.000000   150.000000
mean        5.843333     3.057333      3.758000     1.199333
...
```

## 🌱 What I Learned

* Creating Python virtual environments
* Using Git to track changes and collaborate
* Structuring Python scripts with CLI and functions
* Interacting with real-world datasets using pandas

## 🛰️ Version Control Summary

* Branch: `week01-python-git`
* Feature branch: `add-stats-functions`
* All commits pushed to remote GitHub repo

---

✅ End of Week 1
