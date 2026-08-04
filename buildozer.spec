[app]

# (string) Title of your application
title = Aviator Predictor

# (string) Package name
package.name = aviatorpredictor

# (string) Package domain (needed for android packaging)
package.domain = org.aviator

# (string) Source code directory
source.dir = .

# (list) Source files to include (comma separated)
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# (string) Application version
version = 2.5.7

# (list) Application requirements
# Added pyjnius so your Python code can bridge over to Android's native system features
requirements = python3, kivy, hostpython3, openssl, sqlite3, pyjnius

# (string) Supported orientations (valid options are: landscape, portrait, portrait-reverse, landscape-reverse)
orientation = portrait

# (int) Fullscreen mode, 0 or 1
fullscreen = 0

# (list) Android permissions 
android.permissions = INTERNET

# (bool) Accept SDK license without operator input
android.accept_sdk_license = True

# Target modern API 34 with an optimized NDK match
android.api = 34
android.minapi = 24
android.ndk = 26b

# Modern Android devices require arm64-v8a architectures to install
android.archs = arm64-v8a, armeabi-v7a

# (list) List of services to declare
# This entry tells Buildozer to pack 'service.py' as a persistent background engine
services = MyWidgetService:service.py

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
