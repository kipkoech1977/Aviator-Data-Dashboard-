[app]

# (change these)
title = AviatorData
package.name = aviator_data
package.domain = org.yourname
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt,xml

# Versioning
version = 0.1
# python-for-android supports certain Python versions — test with python3.8/3.9/3.10 as needed
# Buildozer uses the system python to package; don't require an unsupported interpreter.
requirements = python3,kivy==2.2.0,requests,beautifulsoup4,websocket-client,plyer

# Kivy specific
orientation = portrait
fullscreen = 0

# Permissions needed for network access and monitoring
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Android build target settings
# android.api is the Android SDK API level to compile against
android.api = 33
# android.minapi is the minimum Android API supported on devices
android.minapi = 21

# Leave ndk/ndk-api blank to use sensible defaults unless you need a specific NDK
# android.ndk = 25b
# android.ndk_api = 21

# Architecture: include both 32-bit and 64-bit unless you want to restrict
android.arch = armeabi-v7a, arm64-v8a

# Use the SDL2 bootstrap for typical Kivy apps
p4a.bootstrap = sdl2

# Optionally pin p4a branch to a stable release if you get build failures
# p4a.branch = master

# Private or third-party Android Java packages (none by default)
# android.add_jars =

# If you need to include custom Java/Kotlin code, point to the .java/.kt files or AARs
# android.add_aars =

# Keystore (fill for signing release). For debug builds Buildozer produces a debug keystore automatically.
# android.release_keyalias = mykey
# android.release_keystore = /path/to/keystore.jks
# android.release_storepass = YOUR_STOREPASS
# android.release_keypass = YOUR_KEYPASS

# Logging / verbosity
log_level = 2

# Buildozer-specific
# Uncomment to force a specific p4a version or use recipe versions if needed:
# p4a.source_dir =
# android.requirements =
# (If you add recipes that are not present in upstream p4a, include them here.)

# If your app requires background service or auto-start, you may need additional perms:
# android.permissions += RECEIVE_BOOT_COMPLETED, WAKE_LOCK

# Exclude large files you don't want packaged:
# exclude_patterns = tests, docs

# Increase the timeout (for CI environments that are slow)
# android.recent_setup_time = 1200

# If using pure-Python websocket client (websocket-client) prefer it over async websockets that may need extra recipes.
