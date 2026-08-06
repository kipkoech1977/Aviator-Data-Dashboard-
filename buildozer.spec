[app]

# Application
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

# Source
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt,xml
source.exclude_dirs = .git,.github,bin,venv,__pycache__

# Version
version = 2.5.7

# Main requirements
requirements = python3,kivy==2.2.1,requests,beautifulsoup4,python-dateutil

# Orientation
orientation = portrait

fullscreen = 0

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Android versions
android.api = 33
android.minapi = 21

# Architecture
android.archs = arm64-v8a

# Bootstrap
p4a.bootstrap = sdl2

# SDK / NDK
android.ndk = 25b
android.ndk_api = 21

# AndroidX
android.enable_androidx = True

# Gradle
android.gradle_options = -Xmx4096m

# Accept licenses
android.accept_sdk_license = True

# Icon (optional)
#icon.filename = icon.png

# Presplash (optional)
#presplash.filename = presplash.png

# Logging
log_level = 2

# Copy every project file
source.include_patterns = **/*.py,**/*.kv,**/*.json,**/*.txt,**/*.xml

# Ignore unnecessary files
source.exclude_patterns = **/__pycache__/*,**/*.pyc,**/*.pyo

##################################################

[buildozer]

warn_on_root = 1

# Faster incremental builds
build_dir = .buildozer

# Enable Android logcat
android.logcat_filters = *:S python:D

# Use modern python-for-android
p4a.branch = develop
