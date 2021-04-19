import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["tkinter", "PIL", "sys"],
                     "include_files":['run/assets/closedpr.PNG', 
                         'run/assets/forks.PNG',
                         'run/assets/ico.ico',
                         'run/assets/lines.png',
                         'run/assets/mit.PNG',
                         'run/assets/size.PNG',
                         'run/assets/stars.PNG',
                         'run/populate.py',
                         'run/saveas.py'
                     ]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="EZ-README",
      version="1.0",
      description="An easy README generator",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="run/main.py", base=base)])