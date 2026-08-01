[app]

# Application metadata
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

# Source directory
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt,xml

# Versioning
version = 2.5.7

# Python requirements - ONLY Android-compatible packages
requirements = python3,kivy==2.2.1,numpy,requests,python-dateutil,beautifulsoup4

# Kivy specific
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Android build target
android.api = 33
android.minapi = 21

# Use archs instead of arch
android.archs = armeabi-v7a,arm64-v8a

# Bootstrap
p4a.bootstrap = sdl2

# Logging
log_level = 2

# NDK
android.ndk = 25b
android.ndk_api = 21
