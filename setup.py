from setuptools import setup, find_packages
import os
import sys

setup(
    name='python_rdesktop_gui',
    version='1.0.0',
    description='A sample gui for rdesktop',
    url='https://github.com/',
    author='Spencer McIntyre',
    author_email='',
    license='GPL3',
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: X11 Applications :: GTK',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='development remotedesktop rdesktop',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'dev': [],
        'test': [],
    },

    package_data={
    },
    zip_safe=False,
    data_files=[],

    entry_points={
        'console_scripts': [
            'python_rdesktop_gui=python_rdesktop_gui:main',
        ],
    },
)

