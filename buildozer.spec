[app]

title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt,xml

version = 2.5.7

requirements = python3,kivy==2.2.1,requests,python-dateutil,beautifulsoup4

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21

android.archs = arm64-v8a

p4a.bootstrap = sdl2

android.accept_sdk_license = True

android.gradle_options = -Xmx2048M

log_level = 2

warn_on_root = 1

# Keep build size small
presplash.color = #000000
