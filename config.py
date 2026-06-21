"""
Configuration Module
Stores settings and constants
"""

import os
from datetime import datetime

# API Configuration
API_BASE_URL = "https://api.example.com"  # Replace with real API
API_TIMEOUT = 10
REFRESH_INTERVAL = 2  # seconds

# Prediction Settings
MIN_CONFIDENCE = 0.5
MAX_CONFIDENCE = 1.0
PREDICTION_BATCH_SIZE = 10

# Database Settings
DB_PATH = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(DB_PATH):
    os.makedirs(DB_PATH)

DB_FILE = os.path.join(DB_PATH, 'predictions.db')

# UI Settings
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 960
THEME_COLOR = (0.2, 0.6, 1.0, 1.0)  # Blue

# Logging
LOG_DIR = os.path.join(DB_PATH, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, f'predictor_{datetime.now().strftime("%Y%m%d")}.log')

# Model Settings
MODEL_PATH = os.path.join(DB_PATH, 'model.pkl')
TRAINING_DATA_SIZE = 1000
VALIDATION_SPLIT = 0.2

# Notification Settings
ENABLE_NOTIFICATIONS = True
NOTIFY_ON_HIGH_CONFIDENCE = True
CONFIDENCE_THRESHOLD = 0.80
