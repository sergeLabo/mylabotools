#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# labsqlite.py

#############################################################################
# Copyright (C) Labomedia June 2016
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franproplin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#############################################################################


"""
class pour la gestion d'une base de données sqlite3
La db est dans le dossier de ce script
TODO cette classe n'est pas générique
"""

import os
import shutil
import sqlite3


class MyDataBase:
    """TODO: pouvoir définir la dim de la grille"""

    def __init__(self, db_file):
        """Crée l'objet de gestion de la base.
        Si pas de db, elle est créée
        """

        self.db_file = db_file
        if not os.path.isfile(self.db_file):
            self.create_db()

    def create_db(self):
        """Cette fonction est spécifique pour créer une base particulière.
        TODO: trouver une solution générique
        en mettant table en argument
        """

        print("Création de la base demandée", self.db_file)

        # Connection à db
        conn = sqlite3.connect(self.db_file)
        # Curseur
        cur = conn.cursor()
        # Crée la table
        table = """CREATE TABLE grille(X INTEGER, Y INTEGER,
                                   Z INTEGER, C INTEGER)"""
        cur.execute(table)
        # Save
        conn.commit()
        # Ferme
        conn.close()
        print("Nouvell base créée", self.db_file, "\n")

    def record_in_db(self, x, y ,z ,c):
        """Si le point existe, une nouvelle entrée est ajoutée à la base. """

        #print("Insertion dans la base de", x, y ,z , c)
        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()
        try:
            with conn:
                cur.execute("INSERT INTO grille(X, Y, Z, C) VALUES(?,?,?,?)",
                                                                (x, y, z, c))
        except sqlite3.IntegrityError:
            print("Erreur lors de l'ajout d'un cube")

    def delete_in_db(self, x, y ,z):
        """Supprime tous les cubes du point."""

        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()
        try:
            with conn:
                cur.execute("DELETE FROM grille WHERE X=? and Y=? and Z=?",
                                                (x,y,z))
        except sqlite3.IntegrityError:
            print("Erreur lors de la supression d'un cube")




if __name__ == '__main__':

    my_db = MyDataBase("test.sqlite")
