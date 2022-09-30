# Check if applications are installed
import getpass
import os
import wget




org_identifier = 'com.markforged'
dep_notify_log_path = '/var/tmp/dep_notify.log'
temp_utilities_path = 'usr/local/bin/dep_notify_with_installers'
installer_base_string = f'{org_identifier}.DEPNotify-prestarter'
installer_script_name = f'{installer_base_string}-installer.zsh'
installer_script_path = f'{temp_utilities_path}/{installer_script_name}'


def clean_dock():
    pass


def name_computer():
    pass



def install_1password():
    pass



def install_chrome():
    pass


def install_google_drive():
    pass


def install_slack():
    pass


def install_zoom():
    pass


def configure_printers():
    pass


def install_duo():
    pass


def install_s1():
    pass


def finish_cleanup():
    pass

#########################################################################################
# Task List
#########################################################################################
# The policy array must be formatted "Progress Bar text,Functionname". These will be
# run in the order as they appear below.

policy_list = {f'Cleaning Dock,{clean_dock()}', f'Naming Computer,{name_computer()}',
               f'Installing 1Password, {install_1password()}',
               f'Installing Chrome, {install_chrome()}',
               f'Installing Google Drive, {install_google_drive()}',
               f'Installing Slack, {install_slack()}',
               f'Installing Zoom, {install_zoom()}',
               f'Configuring Printers, {configure_printers()}',
               f'Installing Duo Health App, {install_duo()}',
               f'Installing Sentinel One, {install_s1()}',
               f'Finish Cleanup, {finish_cleanup()}'
               }



for policy in policy_list:
    print(policy)
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


def ask_for_sudo_password():
    input('Please enter your sudo password: ')


def set_user_input_plist():
    dep_notify_user_input_plist = f"/Users/{getpass.getuser()}/Library/Preferences/menu.nomad.DEPNotifyUserInput.plist"
    if os.path.exists(dep_notify_user_input_plist):
        pass
    else:
        os.system(f'touch {dep_notify_user_input_plist} | sudo -s {ask_for_sudo_password()}')



# user notification function
def notify_user(text, dep_notify_log=dep_notify_log_path):
    with open(dep_notify_log, 'a+') as log:
        log.write(f'{text}\n')

    log.close()


def clear_dep_logs():
   with open(dep_notify_log_path, 'w') as log:
       log.write('')
       log.close()

def print_dep_logs():
    with open(dep_notify_log_path, 'r') as log:
        print(log.read())
        log.close()


def launch_dep_notify():
    launch_dep_app_command = f'launchctl asuser {os.getuid()} open -a {set_dep_app_location()} --args -path {dep_notify_log_path}'
    os.system(launch_dep_app_command)

def get_logged_in_user():
    return getpass.getuser()

def kill_dep_notify():
    os.system(f'killall -9 "DEPNotify"')