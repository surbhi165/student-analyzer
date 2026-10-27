# Student Performance Analysis System

A Flask-based web application for student performance tracking, analysis, and prediction with machine learning capabilities.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Default Credentials](#default-credentials)

---

## Project Overview

This application provides a comprehensive student performance management system with:
- User authentication (login/register)
- Dashboard with performance visualization
- Student profile management
- Subject analysis and comparison tools
- ML-powered score prediction
- Fraud detection for assessment integrity

## Features

1. **Authentication System**: Secure login/registration with password hashing
2. **Dashboard**: Visual overview of student performance with charts
3. **Student Profile**: Detailed student information display
4. **Subject Analysis**: Analyze performance by subject
5. **Comparison Tools**: Compare student performances
6. **Score Prediction**: ML-based prediction using Linear Regression
7. **Fraud Detection**: CNN-GRU-Attention model for detecting suspicious activity
8. **Reports & Trends**: Generate reports and view performance trends
9. **Teacher Insights**: Analytics for educators

## Technology Stack

### Backend
- **Python 3.x**
- **Flask** - Web framework
- **MySQL** - Database
- **scikit-learn** - Machine learning
- **pandas/numpy** - Data processing
- **joblib** - Model persistence

### Frontend
- **HTML/CSS/JavaScript**
- **Chart.js** (for visualizations)

### Optional (package.json)
- Next.js/React dependencies are present but not actively used in the Flask application

---

## Prerequisites

Before running this application, ensure you have the following installed:

1. **Python 3.8+**
   ```bash
   python --version
   ```

2. **MySQL Server**
   ```bash
   mysql --version
   ```

3. **pip** (Python package manager)

---

## Installation

### Step 1: Clone/Navigate to Project Directory

```bash
cd "c:/Users/vikas/Documents/New folder"
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (Command Prompt):
venv\Scripts\activate.bat

# On Windows (PowerShell):
venv\Scripts\Activate.ps1

# On Linux/Mac:
source venv/bin/activate
```

### Step 3: Install Python Dependencies

Create a `requirements.txt` file with the following content:

```txt
flask
python-dotenv
mysql-connector-python
pymysql
werkzeug
pandas
numpy
scikit-learn
joblib
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install flask python-dotenv mysql-connector-python pymysql werkzeug pandas numpy scikit-learn joblib
```

---

## Database Setup

### Step 1: Start MySQL Server

Ensure your MySQL server is running on `localhost` (default port 3306).

### Step 2: Create Database

Open MySQL command line or use a tool like MySQL Workbench/phpMyAdmin:

```sql
CREATE DATABASE student_managerment_db;
```

### Step 3: Configure Database Connection

The application uses these default database settings (from [`config.py`](config.py:1)):

| Setting    | Default Value            |
|------------|--------------------------|
| Host       | localhost / 127.0.0.1    |
| User       | root                     |
| Password   | 072005 (config.py) / root (app.py) |
| Database   | student_managerment_db   |

**Note:** The application will automatically create the required `users` and `prediction_logs` tables on first run.

### Step 4: (Optional) Create .env File

Create a `.env` file in the project root to override default settings:

```env
FLASK_SECRET=your_secret_key_here
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=student_managerment_db
```

---

## Running the Application

### Option 1: Run the Basic Application (app.py)

```bash
python app.py
```

- **URL**: http://127.0.0.1:5000
- **Features**: Basic authentication, dashboard, profile, reports

### Option 2: Run the Enhanced Application (uapp.py) - Recommended

```bash
python uapp.py
```

- **URL**: http://127.0.0.1:5000
- **Features**: All features including ML prediction and fraud detection

### Option 3: Run with Flask CLI

```bash
# Set FLASK_APP environment variable
# Windows (Command Prompt):
set FLASK_APP=uapp.py

# Windows (PowerShell):
$env:FLASK_APP="uapp.py"

# Linux/Mac:
export FLASK_APP=uapp.py

# Run the application
flask run
```

### Option 4: Run in Debug Mode

```bash
flask run --debug
```

---

## API Endpoints

### Authentication Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Redirect to login or dashboard |
| `/login` | GET, POST | User login |
| `/register` | GET, POST | User registration |
| `/logout` | GET | User logout |

### Page Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/dashboard` | GET | Main dashboard |
| `/student-profile` | GET | Student profile page |
| `/subject-analysis` | GET | Subject analysis page |
| `/comparison` | GET | Student comparison page |
| `/prediction` | GET, POST | Score prediction page |
| `/reports` | GET | Reports page |
| `/teacher-insights` | GET | Teacher insights page |
| `/trends` | GET | Trends page |

### ML Prediction API

| Route | Method | Description |
|-------|--------|-------------|
| `/predict_api` | POST | Score prediction API |
| `/predict_fraud_api` | POST | Fraud detection API |

#### Score Prediction API Example

**Request to `/predict_api`:**
```json
{
    "Age": 20,
    "Attendance": 85,
    "Assignment_Submission": 90,
    "Assessment_Report": 78,
    "Activity_Logs": 15,
    "Gender_Male": 1
}
```

**Response:**
```json
{
    "predicted_score": 82.45
}
```

#### Fraud Detection API Example

**Request to `/predict_fraud_api`:**
```json
{
    "Age": 20,
    "Attendance": 85,
    "Assignment_Submission": 90,
    "Assessment_Report": 78,
    "Activity_Logs": 15,
    "Gender_Male": 1,
    "Device_Changes": 2,
    "Tab_Switches": 5,
    "Submission_Delay_Minutes": 30,
    "IP_Changes": 1
}
```

**Response:**
```json
{
    "predicted_score": 82.45,
    "fraud_probability": 0.23,
    "risk_level": "Low",
    "attention_peak_step": 3,
    "top_risk_factors": ["Tab switching during assessment", "Late submission behavior"]
}
```

---

## Project Structure

```
New folder/
├── app.py                      # Basic Flask application
├── uapp.py                     # Enhanced Flask app with ML features
├── list.py                     # Student list API (alternative)
├── config.py                   # Database configuration
├── score_predictor.joblib      # Trained ML model (auto-generated)
├── student_performance_analysis_100.csv  # Dataset (auto-generated)
├── package.json                # Node.js dependencies (optional)
├── .gitignore                  # Git ignore file
├── README.md                   # This documentation
├── static/
│   ├── css/
│   │   ├── app.css
│   │   ├── comparison.css
│   │   ├── dashboard-1.css
│   │   ├── ex.css
│   │   ├── footer.css
│   │   ├── index-1.css
│   │   ├── login.css
│   │   ├── navbar.css
│   │   ├── Prediction.css
│   │   ├── register.css
│   │   ├── Report.css
│   │   ├── student-profile.css
│   │   ├── style.css
│   │   ├── subject-analysis.css
│   │   ├── Teacher Insights.css
│   │   └── Trends.css
│   └── js/
│       ├── app.js
│       ├── comparison.js
│       ├── dashboard-1.js
│       ├── dashboard.js
│       ├── e.js
│       ├── ex.js
│       ├── footer.js
│       ├── login.js
│       ├── navbar.js
│       ├── Prediction.js
│       ├── Reports.js
│       ├── student-profile.js
│       ├── subject-analysis.js
│       ├── Teacher Insights.js
│       └── Trends.js
└── templates/
    ├── comparison.html
    ├── dashboard.html
    ├── login.html
    ├── prediction.html
    ├── prediction - Copy.html
    ├── predictionapi.py
    ├── Register.html
    ├── reports.html
    ├── student-profile.html
    ├── subject-analysis.html
    ├── teacher-insights.html
    └── trends.html
```

---

## Environment Variables

The application supports the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_SECRET` | Secret key for session management | `safer_key_for_no_keyerror` |
| `MYSQL_HOST` | MySQL server host | `127.0.0.1` |
| `MYSQL_USER` | MySQL username | `root` |
| `MYSQL_PASSWORD` | MySQL password | `root` |
| `MYSQL_DB` | MySQL database name | `student_managerment_db` |

---

## Default Credentials

### Demo Login (Fallback)
- **Email**: `student@school.edu`
- **Password**: `password123`

### MySQL (from config.py)
- **User**: `root`
- **Password**: `072005`

**Note:** These credentials work when the database is unavailable (fallback mode) or if configured accordingly.

---

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure MySQL server is running
   - Verify database credentials in `config.py` or `.env`
   - Check if the database `student_managerment_db` exists

2. **Module Not Found Error**
   - Install missing dependencies: `pip install <module_name>`
   - Ensure virtual environment is activated

3. **Port Already in Use**
   - Change the port: `app.run(debug=True, port=5001)`
   - Or kill the process using port 5000

4. **Template Not Found**
   - Ensure `templates/` folder exists with HTML files
   - Check file names match the route handlers

5. **ML Model Issues**
   - The model files are auto-generated on first run
   - If corrupted, delete `.joblib` files and restart the application

---

## Development

### Running in Development Mode

The application runs in debug mode by default (`debug=True`), which provides:
- Auto-reload on code changes
- Detailed error messages
- Debug console

### Adding New Routes

Add new routes in `app.py` or `uapp.py`:

```python
@app.route('/new-page')
def new_page():
    return render_template('new-page.html')
```

---

## License

This project is for educational purposes.

---

## Support

For issues or questions, please check the troubleshooting section or review the code comments.
