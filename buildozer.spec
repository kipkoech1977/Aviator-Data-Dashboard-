[app]

# Application metadata
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

# Source directory and includes
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt,xml

# Versioning
version = 2.5.7

# Python requirements - MUST match your requirements.txt
requirements = python3,kivy==2.2.1,numpy,matplotlib,requests,pandas,scipy,scikit-learn,python-dateutil,beautifulsoup4,lxml

# Kivy specific
orientation = portrait
fullscreen = 0

# Permissions needed for network access
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Android build target settings
android.api = 33
android.minapi = 21

# Architecture - support both 32-bit and 64-bit
android.arch = armeabi-v7a, arm64-v8a

# Bootstrap
p4a.bootstrap = sdl2

# Buildozer-specific settings
log_level = 2

# Increase timeout for CI environments
android.gradle_dependencies = 

# Keep SSL verification working
android.accept_sdk_license = True

# Exclude unnecessary files
exclude_patterns = .github,.git,bin,build,.buildozer

# JNI if needed for native code
android.ndk = 25b
android.ndk_api = 21
