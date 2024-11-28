#!/bin/bash

# Update and install required packages
apt-get update && apt-get install -y ssh

# Run the bot
python3 bot.py