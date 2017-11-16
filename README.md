## mylabotools

### Des scripts python génériques pour ne pas réinventer la poudre tous les 4 matins.

#### Comment créer et installer son propre package

* [Créer et installer son propre package python](https://wiki.labomedia.org/index.php/Cr%C3%A9er_son_propre_package_python)

Téléchrgaer les sources, dans le dossier:

 sudo python3 setup.py install

### Comprend

* Blender: Des scripts spécifiques pour le Blender Game Engine 2.7x et qui ne peuvent tourner que dans Blender
* Twisted: des exemples de twisted en python3
* Network: des sockets simples en python3
* Tools: des outils utilisés fréquement

#### Liste de tous les scripts

Tools:

* labconfig.py La classe MyConfig charge une configuration depuis un fichier .ini
* labfifolist.py La classe PileFIFO permet de faire des statistiques sur dernières valeurs
* labgetmyip.py La fonction get_my_ip retourne l'adresse ip du pc sur le réseau local
* labsqlite.py TODO non fini
* labsometools.py some tools
* labformatter.py Sortie en terminal bien présentée pour les list, tuple, dict

Blender Game Engine:

* labgetobject.py retourne les scènes et objects dans blender
* labsound.py Permet de gérer du son dans Blender facilement
* labtempo.py Permet de gérer des tempos dans Blender facilement
* labtexturechange.py Permet de changer la texture d'un objet dans Blender
* labviewport.py Gestion des vue caméras

Twisted:

* labtcptwisted.py Client et server TCP
* labirctwisted.py Robot IRC
* labmulticasttwisted.py Multicast Server et Client

Network:

* labudpclient.py UDP Client
* labtcpclient.py TCP Client
* labmulticast.py Multicast Client
* OSC3

### Les scripts comprennent la doc pour les utiliser

Ils peuvent être exécuté pour être tester, sauf les scripts du Blender Game Engine qui doivent tourner dans blender.

### TODO
* labsqlite.py n'est pas abouti
* labgetobject le nom est usurpé, il trouve les scénes !!


#### Installation de twisted pour python 3
##### Dépendances

~~~text
sudo apt-get install python3-dev python3-setuptools
~~~

##### Installation

Les sources de twisted comprennent les versions pour python2 et python3.

Télécharger les sources à https://github.com/twisted/twisted

Dans le dossier, ouvrir un terminal:

~~~text
sudo python3 setup.py install
~~~

ou

Dans votre dossier projets, ouvrir un terminal:

~~~text
git clone https://github.com/twisted/twisted.git
cd twisted
sudo python3 setup.py install
~~~

### Utilisation

~~~python
import mylabotools

ou

from mylabotools import labtcpclient.py
~~~

### Merci à La Labomedia
