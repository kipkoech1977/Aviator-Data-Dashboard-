"""
Configuration Module
Stores settings and constants
"""

import os
from datetime import datetime


# API Configuration
API_BASE_URL = "https://yourdatasource.com"
API_TIMEOUT = 10
REFRESH_INTERVAL = 2  # seconds


# Prediction Settings
MIN_CONFIDENCE = 0.5
MAX_CONFIDENCE = 1.0
PREDICTION_BATCH_SIZE = 10


# Android Writable Path Fix
# Checks if running inside an Android package environment
if "ANDROID_ARGUMENT" in os.environ:
    from android.storage import app_context

    # Safely targets the private app storage directory assigned by the OS
    BASE_STORAGE_DIR = app_context.getFilesDir().getAbsolutePath()
else:
    # Uses standard computer local storage for desktop testing/coding
    BASE_STORAGE_DIR = os.path.dirname(os.path.abspath(__file__))


# Database Settings
DB_PATH = os.path.join(BASE_STORAGE_DIR, "data")
os.makedirs(DB_PATH, exist_ok=True)

DB_FILE = os.path.join(DB_PATH, "predictions.db")


# UI Settings
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 960
THEME_COLOR = (0.2, 0.6, 1.0, 1.0)


# Logging
LOG_DIR = os.path.join(DB_PATH, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Safe filename layout using hyphens instead of system-breaking characters
LOG_FILE = os.path.join(
    LOG_DIR,
    f"predict_{datetime.now().strftime('%Y%m%d')}.log"
)


# Model Settings
MODEL_PATH = os.path.join(DB_PATH, "model.pkl")
TRAINING_DATA_SIZE = 1000
VALIDATION_SPLIT = 0.2


# Notification Settings
ENABLE_NOTIFICATIONS = True
NOTIFY_ON_HIGH_CONFIDENCE = True
CONFIDENCE_THRESHOLD = 0.80
