[app]

title = Aviator Predictor
package.name = aviatorpredictor
package.domain = org.aviator

source.dir = .
source.include_exts = py,png,jpg,kv,json,txt

version = 2.5.7

requirements = python3,kivy==2.2.1,numpy,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

p4a.bootstrap = sdl2

android.accept_sdk_license = True

log_level = 2
