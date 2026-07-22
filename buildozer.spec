[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 2.5.7

# Added hostpython3 and verified recipes
requirements = python3, kivy, numpy

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

android.api = 33
android.minapi = 24
android.ndk = 25b

# CRITICAL: This allows GitHub Actions to accept SDK license
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
