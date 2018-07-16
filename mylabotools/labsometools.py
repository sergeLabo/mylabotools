#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#######################################################################
# Copyright (C) La Labomedia November 2016
#
# This file is part of mylabotools.

# mylabotools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# mylabotools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with mylabotools.  If not, see <https://www.gnu.org/licenses/>.
#######################################################################

import inspect


def scene_change(sceneOld, sceneNew):
    '''
    End of sceneOld, load sceneNew.
    Scene must be str: if scene = scene python object, name is scene.name
    '''
    scenes = gl.getSceneList()
    print("Scenes list in scene_change() =", scenes)
    # Check name
    scnName = []
    for scn in scenes:
        scnName.append(scn.name)
    if not sceneOld in scnName:
        print("  {} isn't in scenes list".format(sceneOld))
    else:
        gl.tempoDict["scene_change"].unlock()
        gl.tempoDict["scene_change"].reset()
        print("  Tempo scene_change reset and unlock")

        for scn in scenes:
            if scn.name == sceneOld:
                scn.end()
                print("  End of scene: {}".format(scn))
        try:
            gl.addScene(sceneNew)
            print("  Scene {0} added".format(sceneNew))
        except:
            print("  Scene {0} doesn't exist: Can't be set.".format(sceneNew))



def print_str_args(*args):
    ''' Imprime en terminal les variables en argument
        Les variables doivent être sous forme de string,
        par exemple
        print_str_args("a")
        imprime la variable a qui a une valeur 42
        a = 42
        '''
    for i in args:
        record=inspect.getouterframes(inspect.currentframe())[1]
        frame=record[0]
        val=eval(i,frame.f_globals,frame.f_locals)
        print('{0} = {1}'.format(i, val))


if __name__ == '__main__':
    # Only to test
    spam = 42
    a = 42
    c = [0,0]
    d = {"g":1, "1":2}

    ip =get_my_ip()

    print_str_args("a", "spam", "c", "d", "ip")
    ##print(droiteAffine(0, -30, 0.7, -20))
