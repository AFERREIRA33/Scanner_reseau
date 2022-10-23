# Scanner reseau:

## installation

Afin d'utilisé ce programme il vous fout installez python3, ainsi que pip.

```
dnf install python3
```

```
dnf install pip
```

Il faut ensuite installé les packages suivant:
```
pip3 install netifaces
```
```
pip3 install scapy
```
```
pip3 install netaddr
```

## Utilisation du programme

Pour utilisé le programme il sufit d'effectuer la commande suivante :
```
sudo python scannerreseau.py [command] [optional_argument]
```

Plusieur commande sont disponible :

```
-a : make arp request to all network
-o : find the os of the choose ip
-p : scan port of choose ip
-h : show list of command
```

Il est aussi possible de lancée le programme avec un argument optionel. Si aucun argument n'est donné le programmes en demanderas un.

Ce programme est a utilisé sur une machine avec une distribution linux dû à des problèmes avec scapy sur windows.