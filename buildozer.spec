[app]

# (str) Title of your application
title = Avi App

# (str) Package name (should be all lowercase, letters/numbers only, no spaces)
package.name = aviapp

# (str) Package domain (needed for android packaging)
package.domain = com.kipkoech1977

# (str) Source code directory where your main.py is located
source.dir = .

# (list) Source files to include (comma separated)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy,kivymd
requirements = python3,kivy

# (str) Supported orientations (valid options: landscape, portrait, all)
orientation = portrait

# ----------------------------------------------------
# Android specific configuration
# ----------------------------------------------------

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use private storage for data (True or False)
android.private_storage = True

# (str) Format used to package the app for release (apk or aab)
android.archs = armeabi-v7a, arm64-v8a

# (bool) Allow backup
android.allow_backup = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
