# !/usr/bin/python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json


class CleverBotConnector(object):
    """Connecting IBM Watson API with Chatbot. Do conversations with Watson and let him talk with you"""

    def __init__(self):
        """Startup for watsontalker"""
        self.driver = None
        self.startup()

    def startup(self):
        """Check if Watsontalker in interactive or not"""
        if self.driver is None:
            self.driver = webdriver.Firefox()
            self.driver.get("http://cleverbot.com")
            return True
        else:
            return False

    def shutdown(self):
        """Stops connection to cleverbot"""
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
            return True
        else:
            return False

    def reset(self):
        """Reset the conversation, close connection and initialize connection again"""
        if self.driver is not None:
            self.shutdown()
            self.startup()

    def talk(self, message):
        """Sends a message to watsontalker and he will reply to you"""
        if self.driver is not None:
            webelement = self.driver.find_element_by_css_selector(
                "input.stimulus")
            webelement.send_keys(message)
            webelement.send_keys(Keys.RETURN)
            time.sleep(3)  # wait for 3 seconds, then return response
            webelement = self.driver.find_elements_by_xpath(
                "//span[contains(@class,'bot')]")
            return webelement[-1].text


from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import os


class TextToSpeech(object):
    """Encapsulates IBMs text to speech service"""

    def __init__(self):

        print("Initializing TextToSpeech ...")
        credentials = self.load_credentials()
        self.user = credentials["username"]
        self.passwd = credentials["password"]
        self.tts = TextToSpeechV1(
            username=self.user, password=self.passwd,  x_watson_learning_opt_out=True)

        print("Done!")

    def load_credentials(self):
        """loads the credentials for ibm speech to text api stored in /resources/credentials.json"""
        print("Loading credentials from ./resources/credentials.json ...")
        base_dir = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(base_dir, "./resources/credentials.json")
        with open(filepath) as credentials_file:
            data = json.load(credentials_file)
        return data

    def say(self, message):
        """Converts a given message into audio file using watson text to speech"""
        base_dir = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(base_dir, "resources/output.wav")
        with open(filepath, "w+") as audio_file:
            audio_file.write(self.tts.synthesize(message, accept='audio/wav',
                                                 voice="en-US_AllisonVoice"))
        print("Watson says: " + message)
        self.play_audio()

    def play_audio(self):
        """Plays the last received audio file"""
        cmd = "aplay -t wav -f dat --quiet ./resources/output.wav"
        os.system(cmd)
