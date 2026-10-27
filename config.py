# config.py
import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'student_app',
    'password': 'StudentApp@2026',
    'database': 'student_managerment_db'
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)