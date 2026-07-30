[app]

# (string) Title of your application
title = Aviator Predictor

# (string) Package name
package.name = aviatorpredictor

# (string) Package domain (needed for android package name)
package.domain = org.aviator

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (comma separated)
source.include_exts = py,png,jpg,kv,atlas,json

# (string) Application versioning
version = 2.5.7

# (list) Application requirements
# WARNING: Removed 'hostpython3' to prevent modern toolchain crashes.
# Add your custom data science/network dependencies here (e.g., requests, certifi)
requirements = python3, kivy, requests, certifi

# (str) Supported orientations
orientation = portrait

# (bool) Use fullscreen mode
fullscreen = 0

# (list) Permissions needed for live network data streaming over cellular/Wi-Fi
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (int) Target Android API (Android 14)
android.api = 34

# (int) Minimum API supported (Android 7.0)
android.minapi = 24

# (str) Android NDK version compatible with Target API 34 compilation
android.ndk = 25b

# (list) The architectures to build for. Modern devices strictly use arm64-v8a.
android.archs = arm64-v8a

[buildozer]

# (int) Log level (2 = standard details, 1 = error only)
log_level = 2

# (int) Warning when running buildozer as root user
warn_on_root = 1
