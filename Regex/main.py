import hashlib
from getpass import getpass


clear_mdp = b"azerty"
cipher_mdp = hashlib.sha1(clear_mdp).hexdigest()

locked = True
while locked:
    entre = getpass("Tapez le mot de passe : ") 

    entre = entre.encode()
    
    entre_cipher = hashlib.sha1(entre).hexdigest()
    if entre_cipher == cipher_mdp:
        locked = False
    else:
        print("Mot de passe incorrect")

print("Mot de passe accepté...")