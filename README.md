📌 Playwright Python E-Commerce Automation Framework
📖 Overview

This project is a UI test automation framework built using Playwright (Python) and Pytest, applying the Page Object Model (POM) design pattern.
It automates end-to-end scenarios for an e-commerce web application.

🧰 Tech Stack
Python
Playwright
Pytest
Page Object Model (POM)
GitHub Actions (CI)

🏗️ Framework Architecture
pages/        → Page Object Models (UI interactions)
tests/        → Test cases (business scenarios)
fixtures/     → Test data (JSON-based)
constants/    → Locators and URLs

🚀 Features
Page Object Model (POM) design
Data-driven testing using JSON fixtures
Reusable base page utilities
End-to-end test coverage (Login → Product → Cart → Checkout)
CI-ready (GitHub Actions support)
Cross-page reusable components
▶️ How to Run Tests
pip install -r requirements.txt
pytest

Run with UI:

pytest --headed

Run with tracing:

pytest --tracing=on
📊 Test Flow Example
Login to application
Validate product listing
Add product to cart
Validate cart details
Proceed to checkout
⚙️ CI (GitHub Actions)

Tests run automatically on:

push to main
pull requests

👤 Author

Cesar Lecona Castillo
SDET (Python | Playwright)