[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 2.5.7

# Added hostpython3, openssl, sqlite3
requirements = python3, hostpython3, 

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCES
android.accept_sdk_license = True

# Target modern API 34 with an optimi
android.api = 34
android.minapi = 24
android.ndk = 26b

# Modern Android devices require arm6
android.archs = arm64-v8a, armeabi-v7

[buildozer]
log_level = 2
warn_on_root = 1
