[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,ttf
version = 0.1
requirements = 
    kivy,
    pyjnius,
    android  # Thêm Android dependency
android.permissions = 
    BLUETOOTH,
    BLUETOOTH_ADMIN,
    INTERNET  # Cần cho kết nối Bluetooth
android.api = 31
android.minapi = 21
android.ndk = 25b  # Sử dụng NDK phiên bản 25b
android.sdk = 34  # SDK phiên bản 34
p4a.branch = develop  # Sử dụng nhánh develop của Python-for-Android
