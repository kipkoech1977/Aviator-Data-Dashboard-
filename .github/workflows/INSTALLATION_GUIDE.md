# Aviator Predictor v2.5.7 - Complete Installation Guide

## 📋 Prerequisites

Before you start, make sure you have:

1. **Git** installed → https://git-scm.com/download
2. **Python 3.8+** installed → https://www.python.org/downloads
3. **Java Development Kit (JDK 11+)** → https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
4. **A Windows/Mac/Linux computer** with 10GB free space
5. **An Android phone** (Android 5.0+) with USB cable

---

## STEP #1: Clone the Repository

### What This Does:
Downloads all the Aviator Predictor code to your computer.

### Instructions:

#### **Option A: Using Command Line (Recommended)**

**Windows:**
```bash
# Open Command Prompt (cmd.exe) or PowerShell
# Navigate to where you want to save the project
cd Desktop

# Clone the repository
git clone https://github.com/kipkoech1977/Aviator-Data-Dashboard-.git

# Enter the directory
cd Aviator-Data-Dashboard-
```

**macOS/Linux:**
```bash
# Open Terminal
# Navigate to where you want to save the project
cd ~/Desktop

# Clone the repository
git clone https://github.com/kipkoech1977/Aviator-Data-Dashboard-.git

# Enter the directory
cd Aviator-Data-Dashboard-
```

#### **Option B: Using GitHub Desktop (Easier for Beginners)**

1. Download GitHub Desktop → https://desktop.github.com
2. Click **File** → **Clone Repository**
3. Paste: `https://github.com/kipkoech1977/Aviator-Data-Dashboard-.git`
4. Choose where to save
5. Click **Clone**

### ✅ Verify Success:
You should see files like:
- `main.py`
- `predictor.py`
- `betika_scraper.py`
- `requirements.txt`
- etc.

---

## STEP #2: Set Up Python Environment

### What This Does:
Creates an isolated Python workspace so dependencies don't conflict with other projects.

### Instructions:

**Windows (Command Prompt or PowerShell):**

```bash
# Make sure you're in the project directory
cd Aviator-Data-Dashboard-

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) at the start of your command line
```

**macOS/Linux (Terminal):**

```bash
# Make sure you're in the project directory
cd Aviator-Data-Dashboard-

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) at the start of your command line
```

### ✅ Verify Success:
Your command line should show:
```
(venv) C:\Users\YourName\Aviator-Data-Dashboard->
```
or on Mac/Linux:
```
(venv) username@computer:~/Aviator-Data-Dashboard-$
```

---

## STEP #3: Install Dependencies

### What This Does:
Downloads and installs all required Python packages.

### Instructions:

**Windows:**

```bash
# Make sure (venv) is shown in your command line
# Install all requirements
pip install -r requirements.txt

# Install additional build tools
pip install buildozer cython
```

**macOS/Linux:**

```bash
# Make sure (venv) is shown in your command line
# Install all requirements
pip install -r requirements.txt

# Install additional build tools
pip install buildozer cython

# Install Java (macOS only)
brew install openjdk@11
```

### 📦 Packages Being Installed:

- **kivy** - Mobile UI framework
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **requests** - HTTP library
- **beautifulsoup4** - Web scraping
- **selenium** - Browser automation
- **buildozer** - Android packaging tool
- And more...

### ⏱️ This may take 5-15 minutes depending on your internet speed.

### ✅ Verify Success:
After installation completes without errors, you should see:
```
Successfully installed [package names]...
```

---

## STEP #4: Build Android APK

### What This Does:
Converts your Python app into an Android package (.apk file) that can be installed on phones.

### ⚠️ Important Notes:
- **First time build takes 30-60 minutes** - It downloads Android SDK and NDK
- **Needs 5-10GB free space**
- **Keep your computer powered on** during build
- **Don't close the terminal**

### Instructions:

**Windows:**

```bash
# Make sure (venv) is active
# Navigate to project directory
cd Aviator-Data-Dashboard-

# Initialize buildozer (first time only)
# This downloads Android SDK - takes time!
buildozer android debug

# Wait for completion... you'll see "BUILD SUCCESSFUL"
```

**macOS/Linux:**

```bash
# Make sure (venv) is active
# Navigate to project directory
cd Aviator-Data-Dashboard-

# Initialize buildozer (first time only)
# This downloads Android SDK - takes time!
buildozer android debug

# Wait for completion... you'll see "BUILD SUCCESSFUL"
```

### 📊 Build Progress:

You'll see messages like:
```
[INFO]    - Downloading Android SDK tools...
[INFO]    - Downloading Android NDK...
[INFO]    - Configuring buildozer...
[INFO]    - Building APK...
[INFO]    - Package ready at: bin/aviatorpredictor-2.5.7-debug.apk
```

### ✅ Verify Success:

After build completes, check:
```
bin/aviatorpredictor-2.5.7-debug.apk
```

This file should exist and be 50-100MB in size.

### 🐛 If Build Fails:

```bash
# Clean previous build
buildozer android clean

# Try building again
buildozer android debug

# Or see detailed errors
buildozer android debug -- --verbose
```

---

## STEP #5: Install on Phone

### ⚠️ Prerequisites:

1. **Enable USB Debugging on Android:**
   - Go to **Settings** → **About Phone**
   - Tap **Build Number** 7 times (until it says "Developer mode enabled")
   - Go back to **Settings** → **Developer Options**
   - Enable **USB Debugging**

2. **Connect Android Phone to Computer via USB cable**

### Option A: Automatic Installation (Recommended)

**Windows:**

```bash
# In your project directory with (venv) active
buildozer android debug deploy run

# This will:
# 1. Build the APK
# 2. Install it on your phone
# 3. Launch the app automatically
```

**macOS/Linux:**

```bash
# In your project directory with (venv) active
buildozer android debug deploy run

# This will:
# 1. Build the APK
# 2. Install it on your phone
# 3. Launch the app automatically
```

### Option B: Manual Installation

**Step 1: Find the APK file**
```
Aviator-Data-Dashboard-/bin/aviatorpredictor-2.5.7-debug.apk
```

**Step 2: Transfer to Phone**
- Connect phone via USB
- Find the APK file in file explorer
- Copy and paste to phone's Downloads folder

**Step 3: Install on Phone**
- On your phone, open **File Manager**
- Navigate to **Downloads**
- Tap the **aviatorpredictor-2.5.7-debug.apk** file
- Tap **Install**
- Grant permissions when prompted

**Step 4: Launch App**
- Installation complete!
- Open app drawer
- Tap **"Aviator Predictor"**

### ✅ Verify Success:

- App appears in your app drawer
- App opens without errors
- You see the dashboard with buttons

---

## STEP #6: Add to Home Screen (On Phone)

### Instructions:

### **For Android 10 and Above:**

1. **Open your app drawer** (swipe up or tap apps icon)

2. **Find "Aviator Predictor"** app

3. **Long-press (hold for 2 seconds)** on the app icon

4. **Select "Add to Home Screen"** from menu

5. **Choose position** on home screen

6. **Tap "Add"** to confirm

7. ✅ **Done!** The app now appears on your home screen

### **For Android 9 and Below:**

1. **Open app drawer**

2. **Find "Aviator Predictor"**

3. **Long-press the icon**

4. **Drag it up to home screen**

5. **Release your finger**

6. ✅ **App added to home screen!**

### **Create a Shortcut (Alternative):**

1. **Long-press on empty home screen space**

2. Select **"Widgets"** or **"Shortcuts"**

3. **Find "Aviator Predictor"**

4. **Tap and drag to home screen**

5. ✅ **Shortcut created!**

### **To Launch:**

- Simply **tap the icon on your home screen**
- App opens immediately
- Dashboard displays with all features ready

---

## 🚀 First Run - Using the App

### When You Open the App:

1. **Status Label** shows "Status: Ready" in green

2. **Current Prediction** section displays latest predictions

3. **Current Odds** shows HIGH and LOW multipliers

4. **Statistics** shows your performance metrics

### **Main Buttons:**

- **🟢 Start Prediction** - Begins live Aviator predictions
- **🔴 Stop** - Stops prediction process
- **🔵 Analytics** - View charts and statistics
- **🟡 Refresh** - Update data from Betika

### **First Time Setup:**

1. Tap **"Refresh"** to load initial data from Betika.com
2. Wait 2-3 seconds for data to load
3. Tap **"Start Prediction"** to begin predictions
4. Watch predictions update every 2 seconds

---

## ⚠️ Troubleshooting

### Problem: "Python not found"

**Windows:**
```bash
# Reinstall Python from https://www.python.org
# Make sure to check "Add Python to PATH" during installation
```

**macOS/Linux:**
```bash
# Install Python3
brew install python3
```

### Problem: "Git not found"

Download and install Git:
https://git-scm.com/download

### Problem: Virtual environment not activating

**Windows:**
```bash
# Try this instead:
python -m venv venv
python venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
# Try this instead:
python3 -m venv venv
. venv/bin/activate
```

### Problem: Build fails with "No Java found"

**Windows:**
- Download JDK 11: https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
- Set JAVA_HOME environment variable

**macOS:**
```bash
brew install openjdk@11
```

**Linux:**
```bash
sudo apt-get install openjdk-11-jdk
```

### Problem: "Module not found" errors

```bash
# Make sure virtual environment is activated (venv)
# Then reinstall requirements
pip install -r requirements.txt --upgrade
```

### Problem: App won't install on phone

```bash
# Make sure USB Debugging is enabled
# Settings → Developer Options → USB Debugging ✓

# Try uninstalling old version first
adb uninstall org.aviator.aviatorpredictor

# Then reinstall
buildozer android debug deploy run
```

### Problem: App crashes on startup

```bash
# Check logs
adb logcat -s "Aviator"

# Or rebuild from scratch
buildozer android clean
buildozer android debug
```

---

## 📞 Quick Reference Commands

```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build APK
buildozer android debug

# Install on phone
buildozer android debug deploy run

# Clean previous build
buildozer android clean

# Test locally (on Windows/Mac/Linux)
python main.py
```

---

## 🎉 Congratulations!

You've successfully:
- ✅ Cloned the repository
- ✅ Set up Python environment
- ✅ Installed all dependencies
- ✅ Built an Android APK
- ✅ Installed on your phone
- ✅ Added to home screen

**Your Aviator Predictor is now live on your Android device!** 🚀

---

## 📱 Next Steps

1. **Configure Betika API** (if needed)
   - Edit `config.py`
   - Update API endpoints

2. **Test the App**
   - Tap app on home screen
   - Click "Start Prediction"
   - Monitor live predictions

3. **Monitor Performance**
   - Check statistics in Analytics
   - Track accuracy over time

4. **Share with Friends**
   - Transfer APK to others
   - They can install the same way

---

## ❓ Need Help?

- Check the main **README.md** for more features
- Review **config.py** for settings
- Check **betika_scraper.py** for scraping details
- Report issues on GitHub

**Happy predicting!** 🎯

---

**Version:** 2.5.7  
**Last Updated:** June 2026  
**Repository:** https://github.com/kipkoech1977/Aviator-Data-Dashboard-
