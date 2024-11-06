import requests
import tautulli_config  # Import the configuration file

def get_activity():
    # Define the parameters for the API request
    params = {
        'apikey': tautulli_config.TAUTULLI_API_KEY,  # Use API key from config
        'cmd': 'get_activity'
    }

    try:
        # Send the GET request to the Tautulli API
        response = requests.get(tautulli_config.TAUTULLI_URL, params=params)  # Use URL from config
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Check if the response was successful
        if data['response']['result'] == 'success':
            return data['response']['data']['sessions']
        else:
            print("Error: Tautulli API responded with an error.")
            print(data['response']['message'])
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def print_activity(sessions):
    if not sessions:
        print("No active sessions.")
    else:
        for session in sessions:
            user = session['username']
            title = session['full_title']
            platform = session['platform']
            quality = session['quality_profile']
            print(f"User: {user} is watching {title} on {platform} in {quality} quality.")

def main():
    print("Polling Tautulli API...")
    sessions = get_activity()
    print_activity(sessions)

if __name__ == '__main__':
    main()