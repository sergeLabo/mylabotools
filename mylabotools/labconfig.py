#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# labconfig.py

# #####################################################################
# Copyright (C) La Labomedia November 2016
#
# This file is part of mylabotools.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# #####################################################################

"""
Le fichier ini doit être défini avec son chemin absolu


Pour un projet python:
    import os
    dossier = os.path.dirname(os.path.abspath(__file__))
    ou
    os.getcwd()

Pour un projet Blender, le chemin complet est trouvé avec:
    bge.logic.expandPath()
"""


import os
import ast
from configparser import SafeConfigParser


class MyConfig():
    """Charge la configuration depuis le fichier *.ini,
    sauve les changement de configuration,
    enregistre les changements par section, clé.
    """

    def __init__(self, ini_file):
        """Charge la config depuis un fichier *.ini

        Le cemin doit être donné avec son chemin absolu.
        """

        self.conf = {}
        self.ini = ini_file
        self.load_config()

    def load_config(self):
        """Lit le fichier *.ini, et copie la config dans un dictionnaire."""

        parser = SafeConfigParser()
        parser.read(self.ini)

        # Lecture et copie dans le dictionnaire
        for section_name in parser.sections():
            self.conf[section_name] = {}
            for key, value in parser.items(section_name):
                self.conf[section_name][key] = ast.literal_eval(value)

        print("\nConfiguration chargée depuis {}".format(self.ini))

    def save_config(self, section, key, value):
        """Sauvegarde dans le fichioer *.ini  avec section, key, value.

        Uniquement int, float, str
        """

        if isinstance(value, int):
            val = str(value)
        if isinstance(value, float):
            val = str(value)
        if isinstance(value, str):
            val = """ + value + """

        config = SafeConfigParser()
        config.read(self.ini)
        config.set(section, key, val)
        with open(self.ini, "w") as f:
            config.write(f)
        f.close()
        print("{1} = {2} saved in {3} in section {0}\n".format(section, key, val, self.ini))


if __name__ == "__main__":

    dossier = os.path.dirname(os.path.abspath(__file__))
    print("dossier", dossier)

    dossier_a = os.getcwd()
    print("dossier_a", dossier_a)

    #/media/data/3D/projets/mylabotools/example.ini
    #/media/data/3D/projets/mylabotools/tools

    ma_config = MyConfig(dossier_a + "/example.ini")
    a = ma_config.conf
    # conf est un dictionnaire avec tous les paramètres
    print(a)
