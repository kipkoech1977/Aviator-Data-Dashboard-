[app]

# (string) Title of your application
title = Aviator Predictor

# (string) Package name
package.name = aviatorpredictor

# (string) Package domain (needed for android packaging)
package.domain = org.aviator

# (string) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version
version = 2.5.7

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# Added hostpython3 and verified recipes
requirements = python3, kivy, numpy, requests

# (string) Supported orientation (one of landscape, sensorLandscape, portrait or sensorPortrait)
orientation = portrait

# (int) Fullscreen mode, 0 or 1
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (string) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip the license question and accept the successfully downloaded SDK/NDK licenses
# CRITICAL: This allows GitHub Actions
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
