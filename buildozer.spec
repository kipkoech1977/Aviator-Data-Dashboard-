[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.5.7
requirements = python3, kivy, numpy, requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
