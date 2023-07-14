import sys
from cx_Freeze import setup, Executable

# Replace "your_script_name.py" with the name of your Python script
executables = [Executable("voice_based_email_for_blind.py", base=None)]

# Replace "YourProjectName" with the name you want for your executable
# Replace "YourProjectVersion" with the version number of your project
setup(
    name="voice_based_email_for_blind",
    version="YourProjectVersion",
    description="Description of your project",
    executables=executables
)
