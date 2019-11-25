from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'This Command Renames The Django Project Name.'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name.')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        files_to_rename = ['manoz/settings/base.py', 'manoz/wsgi.py', 'manage.py']
        folder_to_rename = 'manoz'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('manoz', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)
        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been renamed successfully to %s' % new_project_name))