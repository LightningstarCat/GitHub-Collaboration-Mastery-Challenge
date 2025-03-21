# GitHub Collaboration Mastery Challenge

## Overview
Welcome to the **GitHub Collaboration Mastery Challenge**! Your mission is to make a meaningful contribution by submitting a **pull request (PR)** following proper GitHub collaboration practices. 

## Challenge Steps

### **1️ Fork & Clone the Repo**
1. Fork this repository to your GitHub account.
2. Clone your fork to your local machine.
   ```bash
   git clone https://github.com/TheEmeraldHack/GitHub-Collaboration-Mastery-Challenge.git
   cd github-collab-challenge
   ```
3. Add the original repository as an upstream remote.
   ```bash
   git remote add upstream https://github.com/TheEmeraldHack/GitHub-Collaboration-Mastery-Challenge.git
   ```

### **2️ Explore & Plan**
- Read the **README.md** and understand the structure.
- Browse the **Issues tab** and pick one labeled **"Collab Challenge"**.
- Create a feature branch for your work.
   ```bash
   git checkout -b feature-yourname
   ```

### **3️ Make a Meaningful Contribution**
Choose **one or more** tasks from below:
- **Add yourself** to `contributors.json`
- **Write about something you learned** learnings.md in `docs/`
- **Solve a bug** in `bugs.txt` or `scripts/`
- **Enhance a feature** in `features.md`
- **Refactor** or optimize a small section of code

### **4️ Commit & Push **
1. Stage and commit your changes with a meaningful message.
   ```bash
   git add .
   git commit -m "feat: Improved error handling in script.py"
   ```
2. Push your branch.
   ```bash
   git push origin feature-yourname
   ```

### **5️ Submit a Pull Request**
1. Open a pull request from your fork’s **feature branch** to the **main** branch of this repo.
2. Write a clear title and description explaining your changes.
3. Engage by reviewing at least **one other PR** and leaving constructive feedback.

## Repository Structure
```
📦 github-collab-challenge
 ┣ 📂 scripts
 ┃ ┣ 📜 script.py      # Simple Python script for improvements
 ┣ 📂 docs
 ┃ ┣ 📜 learnings.md       # Documentation for improvements
 ┣ 📜 contributors.json # Participants add their names here
 ┣ 📜 bugs.txt         # List of minor bugs to fix
 ┣ 📜 features.md      # Suggest and implement new features
 ┣ 📜 README.md        # This file (Instructions)
```

## Completion Criteria
✅ Your PR follows contribution guidelines.
✅ It includes a meaningful change.
✅ You followed proper GitHub collaboration practices.


Happy coding!
