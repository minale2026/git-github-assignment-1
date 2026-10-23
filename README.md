# Git and GitHub Assignment 1

## Project Overview
This project demonstrates a basic Git and GitHub workflow by creating a small sample dataset with Python, tracking project files with Git, and publishing the repository on GitHub.

## Objectives
- Create and manage a local Git repository.
- Track files and record changes with Git commits.
- Create a public GitHub repository and connect it to the local repository.
- Synchronize local and remote work using `git push` and `git pull`.
- Document the project using Markdown.

## Project Files
- `sample_data.py` — creates a small example public-health dataset and saves it as `sample_data.csv`.
- `README.md` — describes the project and explains how to run it.

## Requirements
- Python 3 installed (only needed to run the script).
- Git installed.
- A GitHub account and internet connection (needed to publish the repository).

## How to Run
Open a terminal in this folder and run:

```bash
python sample_data.py
```

If your system uses the Python launcher, use:

```bash
py sample_data.py
```

The script creates `sample_data.csv` in the same folder. The values are fictional examples for learning only and are not real patient data.

## Example Dataset
The script includes fictional records with an ID, age in months, sex, and weight in kilograms. Do not use this demonstration data for clinical or research decisions.

## Basic Git Workflow
```bash
git status
git add README.md sample_data.py
git commit -m "Add project README and sample data script"
git log --oneline
git push
```

## Learning Outcome
This project demonstrates how to initialize a repository, track files, create commits, connect to GitHub, and publish a project with clear documentation.
