import RPi.GPIO as GPIO
import time
import threading


import verification # A python file contains all the secret verification
import twitter
import pandA

print("Program Starts")

t1 = threading.Thread(target=twitter.twitter_thread, args=(verification.twitter_tokens))
t1.start()

t2 = threading.Thread(target=pandA.pandA_thread, args=(verification.pandA_username, verification.pandA_password))
t2.start()
