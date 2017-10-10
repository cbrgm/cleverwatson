# /bin/bash/python
# coding=utf-8

from cleverwatson import TextToSpeech, CleverBotConnector
import os
import json


def main():

    active = True
    credentials = load_credentials()
    tts = TextToSpeech(
        username=credentials["username"], password=credentials["password"])
    clw = CleverBotConnector(remote_url=credentials["selenium_url"])

    while active:
        message = raw_input("<Enter Message> :  ")

        if message == "Bye":
            tts.say("Bye Bye! Nice to talk with you!")
            clw.shutdown()
            quit()
        elif message == "Reset":
            tts.say(
                "Im restarting my system! Hang on a second! Maybe you can count sheeps in the meantime or so...")
            clw.reset()
        else:
            tts.say(message, voice="en-US_AllisonVoice")
            reply = clw.talk(message)

            print("Watson says: " + reply)
            tts.say(reply)


def load_credentials():
    """loads the credentials for ibm speech to text api stored in /resources/credentials.json"""
    print("Loading credentials from ./resources/credentials.json ...")
    base_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(base_dir, "./resources/credentials.json")
    with open(filepath) as credentials_file:
        data = json.load(credentials_file)
    return data


if __name__ == '__main__':
    main()
