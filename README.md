## mylabotools

### Des scripts python génériques pour ne pas réinventer la poudre tous les 4 matins.

#### Comment créer et installer son propre package

* [Créer et installer son propre package python](http://ressources.labomedia.org/python/creer_son_propre_package)

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



### Installation
#### Installation de Twisted pour python 3.x
[Créer son propre package python](http://ressources.labomedia.org/python/creer_son_propre_package)


### Utilisation

~~~python
import mylabotools

ou

from mylabotools import labtcpclient
~~~

### Bugs

* Il est possible que j'ai oublié des dépendances

### Version

* 1.42 try sur lecture de fichier

### Merci à La Labomedia
