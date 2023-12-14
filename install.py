import os
import shutil

# Ask the user for their API key
api_key = input("Please enter your Openai API key: ")

# Define the paths
service_file = '/etc/systemd/system/deck-dictation.service'
script_file = '/path/to/deck-dictation.py'

# Create the service file
service_content = f'''
[Unit]
Description=Deck Dictation Service
After=network.target

[Service]
Environment="DECK_DICTATION_OPENAI_API_KEY={api_key}"
ExecStart=/usr/bin/python3 {script_file}
WorkingDirectory={os.path.dirname(script_file)}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
'''
with open(service_file, 'w') as f:
    f.write(service_content)

# Enable and start the service
os.system('systemctl enable deck-dictation.service')
os.system('systemctl start deck-dictation.service')