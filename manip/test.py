import hashlib
username="toto"
realm="ESP32 Auth Realm"
nonce="cc9cbac018c0129883d1c524b7af17a1"
uri="/login"
cnonce="ZTFmZTNjZWNkNzdhNGUxODU5MTE1NTI1MGFjN2E2OTE="
nc="00000001"
qop="auth"
response="6baf6d27497be36eb2a1da31361ac4f7"
opaque="a3613940abb23155185997325e98bb73"

mdp ="torototo"
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
#        print("A hash :"+hash3+"| result :"+hash333)
        #--------#
if hash333==response:
    print("Right Login/Password"+mdp)
    quit()
else:
    print("Testé :"+mdp)







