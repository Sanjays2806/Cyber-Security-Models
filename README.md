# Password Strength Analyzer

## Overview
Password Strength Analyzer is a Python-based security tool that evaluates the strength of user-entered passwords. The application analyzes password length, complexity, entropy, and uniqueness while providing suggestions for creating stronger passwords.

## Features
- Password length validation
- Complexity analysis (uppercase, lowercase, digits, special characters)
- Password entropy calculation
- Detection of common passwords
- Prevention of password reuse
- Secure password suggestions
- Detailed security feedback

## Technologies Used
- Python 3
- Regular Expressions (re)
- Math Module
- Secrets Module

## How It Works
1. User enters a password.
2. System checks:
   - Length requirements
   - Character variety
   - Entropy score
   - Common password usage
   - Password reuse
3. Security feedback is generated.

# Vulnerability Scanner

## Overview
This project is a mini vulnerability assessment tool developed in Python. It scans common ports, identifies running services, checks for outdated software versions, and generates a vulnerability report.

## Features
- Open port scanning
- Service identification
- Detection of insecure configurations
- Outdated software version detection
- Vulnerability reporting
- Risk assessment summary

## Technologies Used
- Python 3
- Socket Programming

## Scan Capabilities
- FTP (21)
- SSH (22)
- Telnet (23)
- HTTP (80)
- HTTPS (443)
- HTTP Alternate (8080)

## How It Works
1. User enters target host or IP.
2. Scanner checks common ports.
3. Service banners are analyzed.
4. Known vulnerable versions are identified.
5. A vulnerability report is generated.

# Phishing Email Detection Model

## Overview
This project uses Machine Learning to classify emails as either Phishing or Safe. The model analyzes email content and identifies suspicious patterns commonly found in phishing attacks.

## Features
- Email classification
- TF-IDF feature extraction
- Machine learning based prediction
- Accuracy evaluation
- Confusion matrix generation
- Confidence score calculation

## Technologies Used
- Python 3
- Scikit-Learn
- NumPy

## Machine Learning Workflow
1. Data preprocessing
2. TF-IDF vectorization
3. Model training
4. Prediction
5. Performance evaluation

## Algorithms Used
- Multinomial Naive Bayes
- TF-IDF Vectorizer

## Sample Output
5. Stronger alternatives are suggested if required.

# Secure Login System

## Overview
Secure Login System is a Flask-based web application that provides secure user authentication using password hashing, session management, and database-backed user storage.

## Features
- User Registration
- Secure Login
- Password Hashing using Bcrypt
- SQLite Database Integration
- Session Management
- Input Validation
- Protection against SQL Injection
- Secure Logout

## Technologies Used
- Python 3
- Flask
- Flask-Bcrypt
- SQLite

## Security Features
### Password Security
- Bcrypt password hashing
- Password policy enforcement
- Secure credential storage

### Database Security
- Parameterized SQL queries
- SQL Injection prevention

### Session Security
- Authenticated user sessions
- Secure logout functionality

## How It Works
1. User registers an account.
2. Password is hashed before storage.
3. User logs in using credentials.
4. Session is created after authentication.
5. User can securely logout.

## Installation
```bash
pip install flask flask-bcrypt
python app.py
