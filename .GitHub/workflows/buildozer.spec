[app]
title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 2.5.7

requirements = python3,kivy,numpy,matplotlib,requests,pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 31
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
