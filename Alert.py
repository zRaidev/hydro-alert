from plyer import notification

def notification_alert():
  notification.notify(
    title='Drink Wather',
    message="It's time to drink some water.",
    app_name='HydroAlert',
    app_icon='HA-icon.ico',
    timeout=10,
    ticker='Drink Water'
  )
