[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.5.7

# CRITICAL FIX: Explicitly list kivy and the required data tools on one solid line
requirements = python3, kivy==2.3.0, matplotlib, numpy, sqlite3, openssl, hostpython3, python3-setuptools, kivy_garden.matplotlib

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.accept_sdk_license = True

# Target modern API 34 with optimized NDK architectures 
android.api = 34
android.minapi = 24
android.ndk = 26b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
