[app]

#        *** Naming ***
title = tukang
source.dir = .



#source.include_patterns = image/tukang.jpg
#source.exclude_patterns = image/tukang.jpg
#icon.filename = image/tukang.jpg

package.name = tukang
package.domain = msp.web.id

#        *** Important ***
version = 0.01
requirements = kivy,hostpython3,python3,requests
#android.permissions = INTERNET
android.permissions = INTERNET, ACCESS_NETWORK_STATE
p4a.source_dir = 
p4a.bootstrap = sdl2

p4a.branch = master


# (int) Android API to use
android.api = 27
# (int) Minimum API required
android.minapi = 21
# (int) Android SDK version to use
android.sdk = 23
# (str) Android NDK version to use
android.ndk = 19c
# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
#android.gradle_dependencies = 'com.google.firebase:firebase-ads:10.2.0'

#android.meta_data = com.google.android.gms.ads.APPLICATION_ID={ca-app-pub-6594734967578033~3189059211}
android.arch = armeabi-v7a

#        *** Constant App Settingsa ***
orientation = portrait

fullscreen = 1

android.ndk_path = ~/Desktop/python3/android-ndk-r19c-linux-x86_64/android-ndk-r19c (arahkan ke folder yang di extrak)

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = ~/.buildozer/android/platform/android-sdk  (arahkan ke folder yang di extrak)

# (str) ANT directory (if empty, it will be automatically downloaded.)
android.ant_path = ~/.buildozer/android/platform/apache-ant-1.9.4 (arahkan ke folder yang di extrak)
[buildozer]

log_level = 2
warn_on_root = 1
