#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################################
# Copyright (C) La Labomedia November 2016
#
# This file is part of mylabotools.

# Foobar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
#######################################################################


import os
from pathlib import Path
from json import dumps
import ast

"""Des méthodes souvent appelées par mes scripts."""


class MyTools:

    def __init__(self, debug=0):
        self.debug = debug

    def read_file(self, file_name):
        """Retourne les datas lues dans le fichier avec son chemin/nom
        Retourne None si fichier inexistant ou impossible à lire .
        open est 'r' par défaut.
        """

        try:
            with open(file_name) as f:
                data = f.read()
            f.close()
        except:
            data = None
            print("Fichier inexistant ou impossible à lire:", file_name)

        return data

    def write_file(self, data, fichier, mode='w'):
        """Ecrit les data dans le fichier
        mode =
        'r' when the file will only be read
        'w' write only:
            an existing file with the same name will be erased
        'a' append: any data written to the file is automatically
                           added to the end
        'r+' opens the file for both reading and writing
        """

        with open(fichier, mode) as fd:
            fd.write(data)
        fd.close()

    def create_directory(self, directory):
        """Crée le répertoire avec le chemin absolu.
        ex: /media/data/3D/projets/meteo/meteo_forecast/2017_06
        """

        try:
            Path(directory).mkdir(mode=0o777, parents=False)
            print("Création du répertoire: {}".format(directory))
        except FileExistsError as e:
            print("Le répertoire", directory, "existe")
            pass

    def get_absolute_path(self, a_file_or_a_directory):
        """Retourne le chemin absolu d'un répertoire ou d'un fichier
        n'importe où.
        """

        return os.path.abspath(a_file_or_a_directory)

    def read_json_file(self, fichier):
        """Retourne le json décodé des datas lues
        dans le fichier avec son chemin/nom.
        Retourne None si pas de fichier.
        """

        a = "Fichier inexistant ou impossible à lire ou indécodable:"

        try:
            with open(fichier) as f:
                data = f.read()
                resp = ast.literal_eval(data)
            f.close()
        except:
            if self.debug:
                print(a, fichier)
            resp = None

        return resp

    def write_json_file(self, data, fichier):
        """Enregistre le json des datas dans
        le fichier avec son chemin/nom.
        """

        data = dumps(data)
        # Ecrit en écrasant
        self.write_file(data, fichier)

    def path_walker(self, path):
        """Retourne la liste des fichiers dans le dossier
        et les sous-dossiers.
        """

        all_files = []
        for root, dirs, files in os.walk(path):
            for file_ in files:
                f = os.path.join(root, file_)
                all_files.append(f)

        return all_files

    def scan_path(self, path):
        """Pour test"""

        folders = []
        files = []

        for entry in os.scandir(path):
            if entry.is_dir():
                folders.append(entry.path)
            elif entry.is_file():
                files.append(entry.path)

        print('Folders:')
        print(folders)
        print('Files:')
        print(files)

    def directory_traversal(self, root_dir, file_end):
        """Retourne un dict avec
        clé = répertoires
        valeur =    liste de tous les fichiers avec chemin relatif
                    si les fichiers se termine par file_end

        root_dir = the directory you want to start from
        """

        all_files = {}

        for dir_name, subdirList, fileList in os.walk(root_dir):

            all_files[dir_name] = []
            for file_name in fileList:
                if file_name.endswith(file_end):
                    all_files[dir_name].append(file_name)

        return all_files


def test():
    mt = MyTools(1)

    data = mt.read_file("./example.ini")
    print("data dans ./example.ini \n", data)

    data = {1: "dfsgdfs",
            2: [1,2,3]}

    mt.create_directory('./test')
    mt.write_json_file(data, './test/example_json.txt')
    resp = mt.read_json_file('./test/example_json.txt')
    print("json \n", resp)
    print("type de resp \n", type(resp))

    fichier = "test.txt"
    mt.write_file(str(data), fichier, mode='a')

    print("\n\nTest de path_walker")
    path = "."
    all_files = mt.path_walker(path)
    print("all_files =", all_files)
    print("Fin de test de path_walker\n\n")

    print("\n\nTest de scan_path")
    path = "./"
    mt.scan_path(path)

    print("\n\nTest de scan_path")
    root_dir = "./"
    file_end = ".txt"
    f = mt.directory_traversal(root_dir, file_end)
    print(f)


if __name__ == "__main__":
    test()
