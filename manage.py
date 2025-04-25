#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot_project.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
# This script is the entry point for Django's command-line utility. It sets the default settings module and executes the command line arguments.
# It allows you to run various administrative tasks such as starting the development server, applying migrations, and creating superusers.