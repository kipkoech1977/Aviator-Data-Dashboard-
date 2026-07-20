[app]

# (string) Title of your application
title = Aviator Predictor

# (string) Package name
package.name = aviatorpredictor

# (string) Package domain (needed for android packaging)
package.domain = org.aviator

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let extensions cover standard files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application versioning
version = 2.5.7

# (list) Application requirements
# Added hostpython3 and verified recipes
requirements = python3, kivy, numpy, hostpython3

# (string) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (string) Android NDK version to use
android.ndk = 25b

# CRITICAL: This allows GitHub Actions workflow to auto-accept the SDK licenses
android.accept_sdk_license = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug and error)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
