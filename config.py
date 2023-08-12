"""
config.py: 
Manages application settings and configurations, possibly reading from config.json and .env.
"""

import ctypes
import subprocess

class Config:
    def __init__(self):
        self.require_admin_rights()

    def require_admin_rights(self):
        # Check for admin rights and request if not present
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    def configure_tascam_model_24(self):
        # Set TASCAM Model 24 as default input and output devices using PowerShell commands
        self.run_powershell_command('Set-AudioDevice -Input "Microphone (Model 24)"')
        self.run_powershell_command('Set-AudioDevice -Output "Speakers (Model 24)"')
        print("Windows sound settings configured for TASCAM Model 24")

    def run_powershell_command(self, command):
        # Run the specified PowerShell command
        subprocess.run(['powershell', command])

