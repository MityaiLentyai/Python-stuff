import os
import sys

if __name__ == "__main__":
    if sys.base_prefix == sys.prefix:
        print("\nMATRIX STATUS: You're still plugged in\n\n"
              f"Current Python: {sys.executable}\n"
              f"Virtual Environment: None detected\n\n"
              "WARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n\n"
              "To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n\n"
              "Then run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n\n"
              f"Current Python: {sys.executable}\n"
              f"Virtual Environment: {sys.prefix.split('/')[-1]}'\n"
              f"Environment Path: {os.getcwd()}\n\n"
              "SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.\n\n"
              "Package installation path:\n"
              f"{sys.path[-1]}")
