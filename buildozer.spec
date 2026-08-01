[app]

title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,kv,json,txt,xml

version = 2.5.7

# Use only Android-compatible packages
requirements = python3,kivy==2.2.1,numpy,requests,python-dateutil,beautifulsoup4

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21

android.archs = arm64-v8a

p4a.bootstrap = sdl2

log_level = 2

android.ndk = 25b
android.ndk_api = 21

# Gradle settings
android.gradle_options = org.gradle.jvmargs=-Xmx1024m

# Buildozer timeout
android.accept_sdk_license = True
