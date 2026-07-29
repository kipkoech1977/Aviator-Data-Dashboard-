import os
import time
from time import sleep

# Import your network packages here (e.g., requests)
# import requests 

def send_data_to_kwgt(variable_name, text_value):
    from jnius import autoclass
    Intent = autoclass('android.content.Intent')
    # Use PythonService context instead of PythonActivity when running inside a service
    PythonService = autoclass('org.kivy.android.PythonService')
    current_service = PythonService.mService
    
    intent = Intent("org.kustom.widget.ACTION_SEND")
    intent.putExtra("org.kustom.widget.extra.NAME", variable_name)
    intent.putExtra("org.kustom.widget.extra.TEXT", str(text_value))
    current_service.sendBroadcast(intent)

if __name__ == '__main__':
    # This loop runs continuously in the background using your data bundles
    while True:
        try:
            # 1. PLACE YOUR REPOSITORY FETCHING LOGIC HERE
            # example_data = requests.get("https://yourwebsite.com").json()
            live_metric = "Active: 4.12x" 
            
            # 2. Push the network metric straight to the home screen widget
            send_data_to_kwgt("aviator_prediction", live_metric)
            
        except Exception as e:
            print(f"Background network fetch failed: {e}")
            
        # Sleep for 15 seconds before using data bundles to fetch again
        sleep(15)
