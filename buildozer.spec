[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 2.5.7

# Added hostpython3 and verified recipes
requirements = python3, kivy, numpy, hostpython3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21
android.ndk = 25b

# CRITICAL: This allows GitHub Actions to accept licenses
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
