[app]

title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,kv,json,txt,xml

version = 2.5.7

# Minimal requirements - no numpy, scipy, sklearn
requirements = python3,kivy==2.2.1,requests,python-dateutil,beautifulsoup4

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

android.gradle_options = org.gradle.jvmargs=-Xmx1024m

android.accept_sdk_license = True
