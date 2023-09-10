# config.py
import sys
import ctypes
import subprocess

class Config:
    def __init__(self):
        self.require_admin_rights()

    def require_admin_rights(self):
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    def configure_irig_pre_hd(self):
        self.run_powershell_command('Set-AudioDevice -Input "Microphone (iRig Pre HD)"')
        print("Windows sound settings configured for iRig Pre HD")

    def run_powershell_command(self, command):
        subprocess.run(['powershell', command])