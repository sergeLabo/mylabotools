#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

## labgetobject.py

#######################################################################
# Copyright (C) La Labomedia November 2016
#
# This file is part of mylabotools.
#
# mylabotools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# mylabotools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mylabotools. If not, see <http://www.gnu.org/licenses/>.
#######################################################################


"""
Utilisation dans blender
"""


from bge import logic as gl


def get_all_objects():
    """Retourne une liste de tous les objets des scènes actives
    TODO à vérifier dans plusieurs projets"""

    activeScenes, scene_name = get_all_scenes()

    all_obj = []
    for scn_name in scene_name:
        scn = get_scene_with_name(scn_name)
        for ob in scn.objects:
            all_obj.append(ob)

    return all_obj

def get_all_scenes():

    # Liste des objets scènes
    activeScenes = gl.getSceneList()

    # Liste des noms de scènes
    scene_name = []
    for scn in activeScenes:
        scene_name.append(scn.name)

    return activeScenes, scene_name

def get_scene_with_name(scn):

    activeScenes, scene_name = get_all_scenes()
    if scn in scene_name:
        return activeScenes[scene_name.index(scn)]
    else:
        print(scn, "pas dans la liste")
        return None
