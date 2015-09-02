# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import sys
import shutil

shutil.copyfile('python_rdesktop_gui.py', 'python_rdesktop_gui')

setup(
    name='python_rdesktop_gui',
    version='0.1',
    scripts = ['python_rdesktop_gui'],
    
    platforms = 'linux',
    author='Spencer McIntyre',
    author_email='',
    maintainer = 'Jorge Hernández (lesthack)',
    maintainer_email = 'lesthack@gmail.com',
    description='A sample gui for rdesktop',
    license='GPL3',    
    keywords=['rdesktop', 'rdp', 'remote desktop', 'terminal server'],
    url='https://github.com/lesthack/python_rdesktop_gui.git',
    
    data_files = [
        ('/usr/share/applications', ['data/python_rdesktop_gui.desktop']),
        ('/usr/share/icons/hicolor/scalable/apps', ['data/icons/scalable/apps/python_rdesktop_gui.svg']),
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

)

