# CECS 456 Machine Learning Project: AI-Generated Image Detection (CIFAKE)

Classifier distinguishing real photographs from AI-generated images on the CIFAKE dataset, including evaluation under image perturbations (such as JPEG compression, blur, or noise) and generalization limits across image sources.

## Team & Responsibilities
- **Member 1:** Kent Do
- **Member 2:** Son Nguyen

## Dataset
- **Source:** *CIFAK: Real and AI-Generated Synthetic Images* (Kaggle)
- **Note:** Keep the dataset folder outside the Git repository (or ignored in `.gitignore`) so large image folders are not committed to GitHub.

## Environment Setup
```bash
python -m venv .venv
# Windows (Powershell):
.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Project
Verify your environment, random seed, and device setup (`cpu`/`cuda`):
```bash
python main.py
```
