### LABBE William

# Réponses aux questions du TP_Chat
## Prise en main

### 1.

Il s'agit d'une topologie en étoile. Un unique serveur permet de connecter tous les utilisateurs du chat.

### 2.

On voit apparaître les messages en clair ainsi que les noms des utilisateurs et leur adresse.

### 3.

Cela constitue un problème car le contenu des messages, le nom et l'adresse des utilisateurs puet être visualisé et récupéré sur le serveur. De plus, l'identité des utilisateurs n'est pas vérifiée. Une tierce personne peut donc via le serveur à des données confifentielles et prendre l'identité d'un utilisateur.
Cela viole le principe de Kerckhoffs.

### 4.

Pour éviter cela, on pourrait par exemple mettre en place un mot de passe pour l'accès au chat ou chiffré les échanges.


## Chiffrement

### 1.

urandom n'est pas un bon choix pour la cryptographie car cette fonction fourni une suite de nombre qui dépendent des paramètres du système. Cette suite est donc prévisible ce qui compromets la sécutié de la clé.

### 2.

_______________

### 3.

Malgré le chiffrement qui permet de protéger les informations échangées entre les utilisateurs, les identifiants des utilisateurs restent accessibles et permettent des attaques.

### 4.

On pourrait ajouter une fonction permettant la vérification de l'intégrité des informations qui transitent sur le serveur, car même si celle-ci sont rendues illisibles, elles sont toujours vulnérables à des modifications.

## Authenticated Symetric Encryption

### 1.

Cette méthode est moins risquée car elle permet une meilleure gestion des clés et de leur génération, les rendant moins vulnérables.

### 2.

L'attaque bassée sur la réutilisation de messages envoyés dans le passé s'appelle le rejeu. En réenvoyant un message crypté déjà envoyé, un attaquant peut ensuite accéder aux messages échangés.

### 3.

Le contre du rejeu est le nonce, un nombre unique et aléatoire généré par l'émetteur et que le récepteur ne s'attend à ne recevoir qu'une fois.

## TTL

### 1.


## Regard critique

En utilisant des bibliothèques tiers sans étudier leur fonctionnement en détail, on laisse la possibilité que la génération de clé soit retraçable ce qui compromettrait le chiffrement.

