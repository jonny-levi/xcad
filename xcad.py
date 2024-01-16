import subprocess


def run_chrome():
    try:
        command  = "google-chrome --kiosk https://www.google.com"
    except Exception as e:
        print(f"Error: ={e}")
