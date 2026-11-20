[app]
title = kkk
package.name = kkk
package.domain = org.abomzlom
version = 1.0.0
source.dir = .
source.include_exts = py,html,css,js,json,txt,png,jpg,jpeg,kv,atlas,ttf,otf,whl
icon.filename = icon/icon.png
requirements = python3,kivy,requests==2.33.1
orientation = portrait
fullscreen = 0
p4a.branch = develop
android.api = 33
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET,ACCESS_NETWORK_STATE,POST_NOTIFICATIONS,VIBRATE,WAKE_LOCK,FOREGROUND_SERVICE,FOREGROUND_SERVICE_DATA_SYNC
services = background:services/background_service.py:foreground:sticky:foregroundServiceType=dataSync

[buildozer]

