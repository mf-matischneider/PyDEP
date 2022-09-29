# Check if applications are installed
import os
import wget



# set dep app location
def set_dep_app_location():
    applications_path = '/Applications/'
    app_path = applications_path + 'DEPNotify.app'
    if os.path.exists(app_path):
        return app_path
    else:
        return False 

# Function to check if app is installed
def is_app_installed(app_name):
    applications_path = '/Applications/'
    app_path = applications_path + app_name
    if os.path.exists(app_path):
        print(f'{app_name} is installed')
    else:
        print(f'{app_name} is installed')


# Check standard applications
def check_chrome(app_name='Google Chrome.app'):
    is_app_installed(app_name)
def check_slack(app_name='Slack.app'):
    is_app_installed(app_name)
def check_zoom(app_name='zoom.us.app'):
    is_app_installed(app_name)
def check_duo_health(app_name='Duo Health App.app'):
    is_app_installed(app_name)
def check_sentinel_one(app_name='SentinelOne.app'):
    is_app_installed(app_name)


def install_chrome():
    if wget.download('https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg', '/tmp/googlechrome.dmg'):
        print('Chrome downloaded')
    else:
        print('Chrome not downloaded')


def install_slack():
   pass


def install_zoom():
    pass


def install_duo_health():
    pass


def install_sentinel_one():
    pass


def check_applications():
    
    if not check_chrome():
        install_chrome()
    if not check_slack():
        install_slack()    
    if not check_zoom():
        install_zoom()
    if not check_duo_health():
        install_duo_health()
    if not check_sentinel_one():
        install_sentinel_one()
    
    
    



