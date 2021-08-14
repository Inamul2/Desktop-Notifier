# pip install plyer
from plyer import notification

notification.notify(
title = "Hello Python",
message = "Thank you for subscribing us",
app_name = "Programming Forever",
app_icon = "wallpaper.ico",
timeout = 30,
ticker = "New Notification",
toast = False
)
