[app]

title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt,xml
source.exclude_dirs = .git,.github,.buildozer,bin,__pycache__

version = 2.5.7

# Python requirements
requirements = python3,kivy==2.2.1,requests,beautifulsoup4,python-dateutil

orientation = portrait
fullscreen = 0

# Android permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Android SDK
android.api = 33
android.minapi = 21

# Architecture
android.archs = arm64-v8a

# Bootstrap
p4a.bootstrap = sdl2

# Android NDK
android.ndk = 25b
android.ndk_api = 21

# Automatically accept SDK licenses
android.accept_sdk_license = True

# AndroidX support
android.enable_androidx = True

# Gradle memory
android.gradle_options = org.gradle.jvmargs=-Xmx4096m

# Build logging
log_level = 2

warn_on_root = 1
