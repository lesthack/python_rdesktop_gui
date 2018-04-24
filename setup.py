# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import sys
import shutil

shutil.copyfile('python_rdesktop_gui.py', 'python_rdesktop_gui')

setup(
    name='python_rdesktop_gui',
    version='0.3',
    scripts = ['python_rdesktop_gui'],
    
    platforms = 'linux',
    author='Spencer McIntyre',
    author_email='',
    maintainer = 'Jorge Hernández (lesthack)',
    maintainer_email = 'lesthack@gmail.com',
    description='A sample gui for rdesktop',
    long_description='A sample gui for rdesktop',
    long_description_content_type='text/x-rst',
    license='GPL3',    
    keywords=['rdesktop', 'rdp', 'remote desktop', 'terminal server'],
    url='https://github.com/lesthack/python_rdesktop_gui.git',
    
    data_files = [
        ('/usr/share/applications', ['data/python_rdesktop_gui.desktop']),
        ('/usr/local/share/icons/hicolor/16x16/apps', ['data/icons/16x16/apps/python_rdesktop_gui.png']),
        ('/usr/local/share/icons/hicolor/22x22/apps', ['data/icons/22x22/apps/python_rdesktop_gui.png']),
        ('/usr/local/share/icons/hicolor/24x24/apps', ['data/icons/24x24/apps/python_rdesktop_gui.png']),
        ('/usr/local/share/icons/hicolor/32x32/apps', ['data/icons/32x32/apps/python_rdesktop_gui.png']),
        ('/usr/local/share/icons/hicolor/48x48/apps', ['data/icons/48x48/apps/python_rdesktop_gui.png']),
        ('/usr/local/share/icons/hicolor/64x64/apps', ['data/icons/64x64/apps/python_rdesktop_gui.png']),
        ('/usr/local/share/icons/hicolor/128x128/apps', ['data/icons/128x128/apps/python_rdesktop_gui.png']),
        ('/usr/local/share/icons/hicolor/256x256/apps', ['data/icons/256x256/apps/python_rdesktop_gui.png']),
        ('/usr/local/share/icons/hicolor/scalable/apps', ['data/icons/scalable/apps/python_rdesktop_gui.svg']),
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

