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
