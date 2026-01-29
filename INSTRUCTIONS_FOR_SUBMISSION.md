# Submission Instructions

Since Git is not installed or available in the system PATH, you will need to perform the version control steps manually.

## 1. Install Git
If you haven't already, download and install Git from [git-scm.com](https://git-scm.com/downloads).

## 2. Initialize and Commit (Local)
Open your terminal (PowerShell, Command Prompt, or Git Bash) in the project folder:
c:\Users\Anirudha TH\.gemini\antigravity\brain\c3d0419c-043e-4bd1-94cb-65ceba066dd8\Project chatbot

Run these commands:
\\\ash
git init
git add .
git commit -m "Initial commit of AI Chatbot"
\\\

## 3. Push to GitHub
1.  Go to [GitHub.com](https://github.com) and create a **New Repository**.
    *   Name it Project-chatbot (or similar).
    *   Do **not** check "Initialize with README" (since we have one).
2.  Copy the URL of the new repository (e.g., https://github.com/YOUR_USERNAME/Project-chatbot.git).
3.  Run these commands in your terminal:
\\\ash
git branch -M main
git remote add origin <PASTE_YOUR_REPO_URL_HERE>
git push -u origin main
\\\

## 4. PDF Report Generation
1.  Open the file Project Report.md in a Markdown viewer or VS Code.
2.  **Screenshots:** Paste your screenshots into the "Screenshots" section.
3.  **Export:** Use a "Markdown to PDF" extension or "Print to PDF" to save it as a PDF file.
