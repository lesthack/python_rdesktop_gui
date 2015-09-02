from setuptools import setup, find_packages
import os
import sys
import shutil

shutil.copyfile('python_rdesktop_gui.py', 'python_rdesktop_gui')

setup(
    name='python_rdesktop_gui',
    version='1.0.0',
    description='A sample gui for rdesktop',
    scripts = ['python_rdesktop_gui'],
    url='https://github.com/lesthack/python_rdesktop_gui.git',
    author='Spencer McIntyre',
    author_email='',
    maintainer = 'lesthack',
    maintainer_email = 'lesthack@gmail.com',
    license='GPL3',    
    keywords=['rdesktop', 'rdp', 'remote desktop', 'terminal server'],
    packages=find_packages(),
    install_requires=[],
    package_data={},
    zip_safe=False,
    
    data_files = [
        ('/usr/share/applications', ['data/python_rdesktop_gui.desktop']),
        ('/usr/share/icons/hicolor/scalable/apps', ['data/icons/scalable/apps/python_rdesktop_gui.svg']),
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: X11 Applications :: GTK',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    extras_require={
        'dev': [],
        'test': [],
    },

)

