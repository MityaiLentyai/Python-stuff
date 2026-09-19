# Create a program called construct.py that:
# • Detects whether it is running inside a virtual environment
# • Displays information about the current Python environment
# • Provides instructions for creating and activating a virtual environment if none is
# detected
# • Shows the difference between global and virtual environment package locations
# Your program should work both inside and outside virtual
# environments, providing different outputs for each scenario.
#
# Testing outside virtual environment
# $> python3 construct.py
# # Should detect no virtual environment and provide instructions
# Creating and testing virtual environment
# $> python3 -m venv matrix_env
# $> source matrix_env/bin/activate
# (matrix_env) $> python3 construct.py
# # Should detect virtual environment and show details
# Do not submit your virtual environnement in your repository. You
# must be able to create a new one during review if needed
#
# Expected Output
# When run outside a virtual environment:
# Outside the Matrix
# $> python construct.py
# MATRIX STATUS: You're still plugged in
# Current Python: /usr/bin/python3.11
# Virtual Environment: None detected
# WARNING: You're in the global environment!
# The machines can see everything you install.
# To enter the construct, run:
# python -m venv matrix_env
# source matrix_env/bin/activate # On Unix
# matrix_env\Scripts\activate # On Windows
# Then run this program again.
# When run inside a virtual environment:
# Inside the Construct
# $> python construct.py
# MATRIX STATUS: Welcome to the construct
# Current Python: /path/to/matrix_env/bin/python
# Virtual Environment: matrix_env
# Environment Path: /path/to/matrix_env
# SUCCESS: You're in an isolated environment!
# Safe to install packages without affecting
# the global system.
# Package installation path:
# /path/to/matrix_env/lib/python3.11/site-packages


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
