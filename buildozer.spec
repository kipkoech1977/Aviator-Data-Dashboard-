[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 2.5.7

# Added hostpython3, openssl, sqlite3, and vital python network packages
requirements = python3, hostpython3, kivy, numpy, requests, openssl, sqlite3, chardet, idna, urllib3, certifi

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.accept_sdk_license = True

# Target modern API 34 with an optimized, verified NDK version
android.api = 34
android.minapi = 24
android.ndk = 26b

# Modern Android devices require arm64-v8a
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
