[app]

# (string) Title of your application
title = Aviator Predictor

# (string) Package name
package.name = aviatorpredictor

# (string) Package domain (needed for android packaging)
package.domain = org.aviator

# (string) Source code directory where main.py resides
source.dir = .

# (list) Source files to include (extensions separated by commas)
source.include_exts = py,png,jpg,kv,atlas,json

# (string) Application version
version = 2.5.7

# ==========================================
# FIXED REQUIREMENTS BLOCK
# ==========================================
# Cleaned out hostpython3 toolchain duplicates to ensure 
# your Kivy elements compile natively for Android.
requirements = python3,kivy

# (str) Supported orientations (one of landscape, portrait or all)
orientation = portrait

# (int) Fullscreen mode (0 for false, 1 for true)
fullscreen = 0

# (list) Permissions required by the application
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# ==========================================
# ANDROID SDK & BUILD ARCHITECTURES
# ==========================================
# Optimized targets to comply with modern app configurations
android.api = 34
android.minapi = 24
android.ndk = 26b

# Builds specifically optimized packages for modern smartphones
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
