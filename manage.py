#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#C id     : LmvBCy2EQZcIctmy62vrytmITTSAwKn7y22h8oO7
#C secret : Xe5HUlwOqrPGS9Mb4gqrcZtRyHpeiQgsM6hRFDWWCCUPoq89rWVDDDaGYQgym7Pc1d3vFmSLpCCTB03Pr6uiZJJ6UrxKFvi0rTdXkHlU1oD6ijRQaKLsXaFc0qdRgNqe

#curl -X POST -d "grant_type=authorization_code&username=annan&password=qazwsxedc" -u"LmvBCy2EQZcIctmy62vrytmITTSAwKn7y22h8oO7:Xe5HUlwOqrPGS9Mb4gqrcZtRyHpeiQgsM6hRFDWWCCUPoq89rWVDDDaGYQgym7Pc1d3vFmSLpCCTB03Pr6uiZJJ6UrxKFvi0rTdXkHlU1oD6ijRQaKLsXaFc0qdRgNqe" http://localhost:8000/o/token/

#My epic app
#cid : L1WwL9EKPiorV5znjx0e2G8CToyuORBEYb9b9Z4A
#cs  : yjviyDicKDmyKsvpWAGlRm1QRtxA4X0yGgGhC4oudT28Hg88CKIJsZTkfySVnF5dQtBnchEtuhZFsOqV8yhlLExO41Q0EIQvWfpF8uwyfm8uEFwZ41HJBM4zQiy7Ty5b
