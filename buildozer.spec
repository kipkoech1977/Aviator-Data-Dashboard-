[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.5.7

# FIXED: Explicitly added kivy so the app engine boots up smoothly on Android
requirements = python3, hostpython3, kivy==2.3.0, sqlite3, openssl

orientation = portrait
fullscreen = 0

# FIXED: Completed 'ACCES' into 'ACCESS_NETWORK_STATE' to avoid system parsing crashes
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.accept_sdk_license = True

# Target modern API 34 with an optimized toolchain
android.api = 34
android.minapi = 24
android.ndk = 26b

# FIXED: Completed 'armeabi-v7' into 'armeabi-v7a' for proper mobile compiler mapping
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
