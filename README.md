# UI_Project_Playwright
This project automates UI tests using Playwright.

Playwright docs - https://playwright.dev/python/docs/intro

## Setup

1. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   ```
   a. Activate the virtual environment:
      - For Linux/macOS:
         ```bash
         source venv/bin/activate
      - For Windows:
         ```bash
         venv\Scripts\activate
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
3. Install browsers (Chromium, Firefox, Webkit):
   ```bash
   playwright install --with-deps
4. Run tests:
    ```bash
    pytest