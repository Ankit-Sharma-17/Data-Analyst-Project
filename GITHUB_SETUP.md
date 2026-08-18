# GitHub Setup & Deployment Guide

## Quick Start: Push to GitHub

### Prerequisites
- GitHub account ([create here](https://github.com/signup))
- Git installed on your machine
- SSH key configured (recommended) or GitHub Personal Access Token

---

## Option 1: Using SSH (Recommended)

### Step 1: Generate SSH Key (if you don't have one)
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
# Press Enter for all prompts to accept defaults
# This creates ~/.ssh/id_ed25519 and ~/.ssh/id_ed25519.pub
```

### Step 2: Add SSH Key to GitHub
1. Copy your public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. Go to GitHub → Settings → SSH and GPG keys
3. Click "New SSH key"
4. Paste the key and save

### Step 3: Test SSH Connection
```bash
ssh -T git@github.com
# Should print: Hi {username}! You've successfully authenticated...
```

### Step 4: Create Repository on GitHub
1. Go to [github.com/new](https://github.com/new)
2. Fill in:
   - **Repository name:** `Telecom-Customer-Value-Analytics`
   - **Description:** `End-to-end analytics pipeline for telecom churn prediction and customer value segmentation`
   - **Public** (so employers can see it)
   - Check "Add a README file" ❌ (we already have one)
   - Check "Add .gitignore" ❌ (we already have one)
   - **License:** MIT License ✅
3. Click "Create repository"

### Step 5: Connect Local Repository to GitHub
```bash
cd "C:\Users\ankit\Desktop\Data Analyst Project\Telecom-Customer-Value-Analytics"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin git@github.com:YOUR_USERNAME/Telecom-Customer-Value-Analytics.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 6: Verify on GitHub
Visit `https://github.com/YOUR_USERNAME/Telecom-Customer-Value-Analytics` and confirm all files are there.

---

## Option 2: Using HTTPS (Personal Access Token)

### Step 1: Create Personal Access Token
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token"
3. Give it a name like "Telecom Analytics Push"
4. Select scopes: `repo` (full control of private repositories)
5. Click "Generate token" and **copy it immediately** (you won't see it again)

### Step 2: Create Repository on GitHub
(Same as Option 1, Step 4)

### Step 3: Connect & Push
```bash
cd "C:\Users\ankit\Desktop\Data Analyst Project\Telecom-Customer-Value-Analytics"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/Telecom-Customer-Value-Analytics.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main

# When prompted for password, use your Personal Access Token
```

---

## Verify Remote Configuration

```bash
# Check remote is configured correctly
git remote -v

# Should show:
# origin  git@github.com:YOUR_USERNAME/Telecom-Customer-Value-Analytics.git (fetch)
# origin  git@github.com:YOUR_USERNAME/Telecom-Customer-Value-Analytics.git (push)
```

---

## After Initial Push: Workflow

### Making Updates to Your Project
```bash
# Make changes to files
# ... edit code ...

# Stage changes
git add src/new_feature.py

# Commit with descriptive message
git commit -m "Add real dataset integration from Kaggle API

- Support for IBM Telecom Customer Churn dataset
- Auto-standardization of column names
- Cleaning and outlier handling
- Fallback to UCI GitHub mirror if Kaggle unavailable"

# Push to GitHub
git push origin main
```

### Common Commands
```bash
# See commit history
git log --oneline

# See what changed in last commit
git show HEAD

# See status of working directory
git status

# See differences since last commit
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Create a new branch for a feature
git checkout -b feature/powerbi-dashboard

# Push a new branch
git push -u origin feature/powerbi-dashboard
```

---

## Repository Settings (Optional but Recommended)

### Enable GitHub Pages (for portfolio/docs)
1. Go to your repository → Settings → Pages
2. Select "main branch" as source
3. GitHub will host your README at `https://YOUR_USERNAME.github.io/Telecom-Customer-Value-Analytics`

### Add Repository Topics
1. Go to repository → About (top right)
2. Add topics: `data-analytics`, `python`, `sql`, `power-bi`, `portfolio`, `churn-prediction`, `customer-analytics`

### Add Branch Protection (Optional)
1. Settings → Branches → Add rule
2. Protect `main` branch to prevent accidental deletions
3. Require pull requests for changes (good practice if collaborating)

---

## Troubleshooting

### "fatal: remote origin already exists"
```bash
# Remove old remote
git remote remove origin

# Add correct remote
git remote add origin git@github.com:YOUR_USERNAME/Telecom-Customer-Value-Analytics.git
```

### "Permission denied (publickey)"
- SSH key not set up properly
- Try HTTPS method (Option 2) instead
- Or regenerate SSH key and add to GitHub

### "Everything up-to-date" but files aren't showing on GitHub
```bash
# Force push (only do this if you're sure)
git push -u origin main --force
```

---

## Sharing Your Project

Once pushed to GitHub, share your project link with:

### Recruiters & Employers
- Email: "I built an end-to-end analytics project: https://github.com/YOUR_USERNAME/Telecom-Customer-Value-Analytics"
- LinkedIn: Add link to project in Experience section
- Portfolio website: Embed project summary and link

### In Job Applications
- Cover letter: "My recent portfolio project (see GitHub link) demonstrates full-stack analytics capability"
- Resume: Add as "Projects" section with GitHub link

### Social Media
- Twitter/X: "Shipped my latest analytics project. End-to-end pipeline for telecom churn prediction. [Link] #DataAnalytics #Python #SQL"
- LinkedIn post: Share project summary with key learnings

---

## Next Steps After Initial Push

### Week 1: Polish & Share
- ✅ Push to GitHub
- ✅ Add topics & description
- ✅ Add LinkedIn project link
- ✅ Share with network

### Week 2-4: Enhance
- [ ] Add real Kaggle dataset implementation
- [ ] Implement Power BI .pbix dashboard
- [ ] Add blog post link in README
- [ ] Create GitHub Releases for version milestones

### Month 2+: Maintenance
- [ ] Monitor GitHub for issues/questions from visitors
- [ ] Add trending topics (e.g., "Add LLM-powered insights")
- [ ] Update with new datasets or features
- [ ] Respond to any GitHub stars or forks

---

## Pro Tips

### Make Your Commits Tell a Story
```bash
# Bad
git commit -m "updates"

# Good
git commit -m "Add Kaggle dataset loader with auto-standardization

Implements load_kaggle_churn_dataset() and load_uci_telecom_dataset()
with automatic column name standardization and data quality checks.
Supports fallback to GitHub mirror if Kaggle API unavailable."
```

### Use .gitignore Effectively
- Never commit: `.env`, `api_keys.json`, `kaggle.json`, `*.pem`
- Our `.gitignore` already handles most cases
- Check with `git status` before committing

### Keep Repository Clean
```bash
# Remove accidental commits before pushing
git reset --soft HEAD~1
git reset HEAD file_to_unstage.py
git checkout file_to_discard.py
```

---

## GitHub URLs You'll Use

| Purpose | URL |
|---------|-----|
| Your repository | https://github.com/YOUR_USERNAME/Telecom-Customer-Value-Analytics |
| Issues tracker | https://github.com/YOUR_USERNAME/Telecom-Customer-Value-Analytics/issues |
| Commit history | https://github.com/YOUR_USERNAME/Telecom-Customer-Value-Analytics/commits/main |
| Releases | https://github.com/YOUR_USERNAME/Telecom-Customer-Value-Analytics/releases |
| Fork this repo | https://github.com/YOUR_USERNAME/Telecom-Customer-Value-Analytics/fork |

---

## Questions?

Refer to:
- GitHub Docs: https://docs.github.com/en/github
- Git Cheat Sheet: https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf
- This repository's README.md for usage instructions

**Good luck with your analytics portfolio! 🚀**
