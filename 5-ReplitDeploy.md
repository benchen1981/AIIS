# Replit Deployment Guide

## Step 1: Create Replit Project
- Go to [Replit](https://replit.com)
- Click **Create Repl**
- Choose **Python** as language
- Name your project `linear_regression_app`

## Step 2: Upload Project Files
- Upload `app.py`, `requirements.txt`, `.replit`, `replit.nix` and other docs

## Step 3: Configure Replit
- `Replit.replit` file:

- `replit.nix` file:
```nix
{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.python310Packages.pip
  ];
}