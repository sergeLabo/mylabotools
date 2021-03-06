#!/usr/bin/env python3

from distutils.core import setup

setup(  name='mylabotools',
        packages = ["mylabotools"],
        version='1.48',
        description='Python Labomedia Utilities',
        author='sergeLabo',
        url='https://labomedia.org',
        download_url='https://github.com/sergeLabo/mylabotools',
        license='GPL Version 3',
        keywords = ["blender", "network", "tools"],
        classifiers = [ "Programming Language :: Python",
                        "Programming Language :: Python :: 3",
                        "Development Status :: 4 - Beta",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
                        "Operating System :: Debian",
                        "Topic :: Blender Game Engine"
                        "Topic :: Network"],
        long_description = """\
        Tools used every day
        --------------------
        Tools used in Blender Game Engine and Python Script
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
                    'OSC3',
                    'mytools']
     )
