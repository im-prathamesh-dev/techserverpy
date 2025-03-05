import requests
import time

# Backend URL from your React code (POST request)
URL = "https://techmantraregi.onrender.com/api/v1/status"

def keep_backend_awake():
    while True:
        try:
            # Sending a dummy POST request to keep the backend active
            response = requests.post(URL, json={"amount": 100})  # 100 is just a test value
            if response.status_code == 200:
                print(f"[✅] Successfully pinged {URL} - Status: {response.status_code}")
            else:
                print(f"[⚠️] Server responded with status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[❌] Error pinging {URL}: {e}")

        # Wait 9 minutes (540 seconds) before sending another request
        time.sleep(540)

# Run the script
if __name__ == "__main__":
    keep_backend_awake()
