import getpass
import os
import helpers.dep_functions as dep_functions


def get_logged_in_user():
    return getpass.getuser()





if __name__ == '__main__':
    dep_functions.install_chrome()
