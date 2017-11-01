#!/usr/bin/env python3

from distutils.core import setup

setup(  name='mylabotools',
        packages = ["mylabotools"],
        version='1.31',
        description='Python Labomedia Utilities',
        author='sergeLabo',
        url='https://labomedia.org',
        download_url='https://github.com/sergeLabo/mylabotools',
        license='GPL Version 2',
        keywords = ["blender", "netwoek", "tools"],
        classifiers = [ "Programming Language :: Python",
                        "Programming Language :: Python :: 3",
                        "Development Status :: 4 - Beta",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
                        "Operating System :: Debian",
                        "Topic :: Blender Game Engine"
                        "Topic :: Network",
                        "Requires: re"],
        long_description = """\
        Tools used every day
        --------------------
        Tools for Blender Game Engine Python Script
        """,

        py_modules=['labfifolist',
                    'labformatter',
                    'labgetmyip',
                    'labconfig',
                    'labgetmyip',
                    'labmulticast',
                    'labtcpclient',
                    'labudpclient',
                    'labsometools',
                    'labsound',
                    'labtempo',
                    'labtexturechange',
                    'labviewport',
                    'labirctwisted',
                    'labmulticasttwisted',
                    'labtcptwisted',
                    'labgetobject',
                    'OSC3']
     )
