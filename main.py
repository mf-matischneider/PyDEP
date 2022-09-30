import getpass
import json
import os
import signal

import schedule

import helpers.dep_functions as dep_functions
import psutil




def restart_button():
    dep_functions.notify_user('Command: Restart: Restart')

def



if __name__ == '__main__':

    user = dep_functions.get_logged_in_user().replace(".", " ").capitalize()

    dep_functions.notify_user(f'Command: MainTitle: Hi there {user}!')
    dep_functions.notify_user('Command: Image: /usr/local/techops/logos/logo.png')
    dep_functions.notify_user('Command: MainText: Welcome to the TechOps Department!')
    restart_button()

    dep_functions.notify_user('Status: Installing applications...')
    dep_functions.launch_dep_notify()











