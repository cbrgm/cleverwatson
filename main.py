# /bin/bash/python
# coding=utf-8

from cleverwatson import TextToSpeech, CleverBotConnector


def main():

    active = True
    tts = TextToSpeech()
    clw = CleverBotConnector()

    while active:
        message = raw_input("You: ")

        if message == "Bye":
            tts.say("Bye Bye! Nice to talk with you!")
            quit()
        else:
            reply = clw.talk(message)
            tts.say(reply)


if __name__ == '__main__':
    main()
