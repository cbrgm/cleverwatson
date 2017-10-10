# CleverWatson - Talk with CleverBot using natural language

[![Build Status](http://dev.cynthek.de/api/badges/cbrgm/cleverwatson/status.svg)](http://dev.cynthek.de/cbrgm/cleverwatson)

## Description

**CleverWatson** is a great way to have a conversation with [CleverBot][03bdac3a]. IBM Watson Text To Speech converts your messages and CleverBot's replies into natural language to represent a real conversation. Try it yourself!

  [03bdac3a]: http://cleverbot.com "cleverbot.com"

## Installation

**Please note that at the moment CleverWatson can only be used in Linux environments, because the program `aplay` is used!**  

Clone to project using `git clone https://github.com/cbrgm/cleverwatson`.

To run locally or outside of Bluemix you need the `username` and `password` credentials for each service. (Service credentials are different from your Bluemix account email and password.)

### Bluemix Service Credentials

To get your **service credentials**:

Copy your credentials from the **Service details** page. To find the the Service details page for an existing service, navigate to your Bluemix dashboard and click the service name.

* On the Service **Details page**, click **Service Credentials**, and then **View credentials**.
* Copy the content to `resources/sample-credentials.json` and replace `password` and `username` with your credentials

```json
{
  "url": "https://stream.watsonplatform.net/text-to-speech/api",
  "username": "INSERT BLUEMIX CREDENTIALS",
  "password": "INSERT BLUEMIX CREDENTIALS"
}

```

Rename `resources/sample-credentials.json` to **credentials.json**.

### Install Dependencies using pip

To install the dependencies correctly, you can use `pip`. All dependencies are stored in `requirements.txt`.

`pip install -r requirements.txt`

You can also use `virtualenv` to install dependencies in an isolated environment. Make sure you have `virtualenv` installed and run the following commands:

```bash
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Install Selenium geckodrivers

CleverWatson uses Selenium to communicate with CleverBot. The geckodriver is used, which must be downloaded and added to the path. Latest `geckodriver` release can be found [here][b2537cd7].

  [b2537cd7]: https://github.com/mozilla/geckodriver/releases "geckodriver"

## Examples

Start the script using `python main.py` command. All services are automatically loaded and you can start the conversation with Cleverbot by typing in a message.

### Python Version

The script has been successfully tested with Python2.7

### Dependencies

* `watson-developer-cloud (0.26.1)`
* `selenium (3.6.0)`

### Motivation

This script was developed by [Christian Bargmann][b9824663] for practice purposes to learn how to use IBM Watson Services.

  [b9824663]: http://cbrgm.de "blog"
