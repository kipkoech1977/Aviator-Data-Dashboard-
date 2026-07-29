[app]

# (string) Title of your application
title = Aviator Predictor

# (string) Package name
package.name = aviatorpredictor

# (string) Package domain (needed for android packaging)
package.domain = org.aviator

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version
version = 2.5.7

# (list) Application requirements
# CRITICAL: Added requests, urllib3, and openssl so Python can process HTTPS mobile/WiFi data
requirements = python3, kivy, numpy, requests, urllib3, openssl

# (string) Supported orientations
orientation = portrait

# (int) Fullscreen mode, 0 = False, 1 = True
fullscreen = 0

# (list) Permissions
# CRITICAL: Grants full access to internet data pipelines via cellular data bundles or WiFi
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (string) Android NDK version to use
android.ndk = 25b

# (bool) CRITICAL: Allows non-HTTPS traffic if your server or API uses unencrypted HTTP endpoints
android.manifest.application_uses_cleartext_traffic = true

# CRITICAL: This allows GitHub Actions to accept SDK licenses automatically during runner build
android.accept_sdk_license = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug and outputs everything)
log_level = 2

# (int) Display warning if buildozer is run as root (1 = True, 0 = False)
warn_on_root = 1
