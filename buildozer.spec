name: Buildozer Python APK

on:
  push:
    branches: [ "main" ]
  workflow_dispatch: # This allows you to manually trigger the build anytime

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    # Sets up a clean Python environment required by Buildozer
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    # Installs the precise development tools Buildozer needs to compile successfully
    - name: Install System Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y libunwind-dev
        sudo apt-get install -y build-essential git python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
        sudo apt-get install -y libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav libgstreamer-plugins-base1.0-dev
        sudo apt-get install -y p7zip-full ccache libffi-dev libssl-dev autoconf automake libtool pkg-config
        pip3 install --upgrade pip
        pip3 install buildozer cython virtualenv

    # Instructs Buildozer to build the APK
    - name: Build APK with Buildozer
      run: |
        buildozer android debug

    # Automatically saves the .apk file into your GitHub account so you can download it
    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: python-built-apk
        path: bin/*.apk
