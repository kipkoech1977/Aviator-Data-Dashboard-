[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 2.5.7

# Added hostpython3 and verified recipes for numpy/matplotlib on Android
requirements = python3,requests,urllib3,certifi,idna

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21
android.ndk = 25b

# CRITICAL: This allows GitHub Actions to bypass the license prompt
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
