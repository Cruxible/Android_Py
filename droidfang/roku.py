import time

def rokuon():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="PowerOn"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/PowerOn', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV turned on successfully')
        time.sleep(2)
    else:
        print(f'Failed to turn on Roku TV with error code: {response.status_code}')

def youtuberoku():
    import requests
    # Set the IP address of your Roku device
    ROKU_IP = 'your ip'

    # Launch the YouTube app
    try:
        app_url = f'http://{ROKU_IP}:8060/launch/837'
        response = requests.post(app_url)
        time.sleep(2)
    except requests.exceptions.HTTPError as e:
        print(f"Error launching app: {e}")
        print(f'Failed to send {command} command with error code: {response.status_code}')

def rokuhome():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="Home"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/Home', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV turned on successfully')
        time.sleep(2)
    else:
        print(f'Failed to return home Roku TV with error code: {response.status_code}')

def rokuoff():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="PowerOff"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/PowerOff', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV turned off successfully')
        time.sleep(2)
    else:
        print(f'Failed to turn off Roku TV with error code: {response.status_code}')

def volumeup():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    for i in range(5):
        # Construct the POST request payload to turn on the TV
        payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="VolumeUp"></Power></root>'

        # Send the POST request to the Roku TV
        response = requests.post(f'http://{roku_ip}:8060/keypress/VolumeUp', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print('Roku TV turned up successfully')
            time.sleep(.25)
        else:
            print(f'Failed to turn up Roku TV with error code: {response.status_code}')

def rokumute():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="VolumeMute"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/VolumeMute', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV volume increased successfully')
        time.sleep(2)
    else:
        print(f'Failed to increase volume on Roku TV with error code: {response.status_code}')

def volumedown():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    for i in range(5):
        # Construct the POST request payload to turn on the TV
        payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="VolumeDown"></Power></root>'

        # Send the POST request to the Roku TV
        response = requests.post(f'http://{roku_ip}:8060/keypress/VolumeDown', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print('Roku TV volume decreased successfully')
            time.sleep(.25)
        else:
            print(f'Volume failed to decrease with error code: {response.status_code}')

def rokuselect():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="Select"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/Select', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV pressed select button successfully')
        time.sleep(2)
    else:
        print(f'Failed to press select button on Roku TV with error code: {response.status_code}')

def rokuplay():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="Play"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/Play', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV press play button successfully')
        time.sleep(2)
    else:
        print(f'Failed to press play button on Roku TV with error code: {response.status_code}')

def rokuback():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="Back"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/Back', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV pressed back button successfully')
        time.sleep(2)
    else:
        print(f'Failed to press back button seccessfully on Roku TV with error code: {response.status_code}')

def rokuup():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="Up"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/Up', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV pressed up button successfully')
        time.sleep(2)
    else:
        print(f'Failed to press up button on Roku TV with error code: {response.status_code}')

def rokudown():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="Down"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/Down', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV pressed down button successfully')
        time.sleep(2)
    else:
        print(f'Failed to press down button on Roku TV with error code: {response.status_code}')

def rokuleft():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="Left"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/Left', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV pressed left button successfully')
        time.sleep(2)
    else:
        print(f'Failed to press left button on Roku TV with error code: {response.status_code}')

def rokuright():
    import requests

    roku_ip = 'your ip'  # Replace with your Roku TV's IP address

    # Construct the POST request payload to turn on the TV
    payload = '<?xml version="1.0" encoding="UTF-8"?><root><Power mode="Right"></Power></root>'

    # Send the POST request to the Roku TV
    response = requests.post(f'http://{roku_ip}:8060/keypress/Right', data=payload)

    # Check if the request was successful
    if response.status_code == requests.codes.ok:
        print('Roku TV pressed right button successfully')
        time.sleep(2)
    else:
        print(f'Failed to press right button on Roku TV')
