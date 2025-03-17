import os
import re
import shutil
import datetime
import subprocess
from PIL import Image
import xml.etree.ElementTree as ET


GITHUB_REPO = "https://github.com/Anubhav1421/SeatBookingApp"
LOCAL_DIR = "\\androidAutomate\\androidProject"
NEW_APP_NAME = "TestDemo2"


def run_command(command, cwd=None):
    process = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
    print(process.stdout)
    if process.stderr != 0:
        print(f"error:{process.stderr} ")
    else:
        print(process.stdout)


# def pull_project():

#     # Clone the repository
#     if os.path.exists(LOCAL_DIR) and os.path.isdir(os.path.join(LOCAL_DIR, ".git")):
#         print("Updating the existing project")
#         run_command("git pull origin main", cwd=LOCAL_DIR)
#     else :
#         print("Clone the Project")
#         run_command(f'git clone {GITHUB_REPO} "{LOCAL_DIR}"')
#         print("Cloning Complete")



def change_appName():
    # Change the app name in "D:\personal\androidAutomate\androidProject\android\app\src\main\res\values\strings.xml"

    file_path = os.path.join(LOCAL_DIR, "android", "app", "src", "main", "res", "values", "strings.xml")
    
    if not os.path.exists(file_path):
        print("This file is invalid", file_path)
        return
    
    tree = ET.parse(file_path)
    root = tree.getroot()

    update = False
    for string in root.findall("string"):
        if string.attrib.get("name") == "app_name":
            print(f"Changing app name to {NEW_APP_NAME}")
            string.text = NEW_APP_NAME
            update = True
            break

    if update:
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print("App name change")
    else:
        print(f"No app_name find in ", file_path)



    







if __name__ == "__main__":
    # pull_project()
    change_appName()
