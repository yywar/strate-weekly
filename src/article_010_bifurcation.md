# Le Pentagone et la City ont le meme fournisseur de cerveau

*Article #10 | Strate, 23 mars 2026*

---

## Deux contrats, une semaine

Cette semaine, Palantir a signe deux contrats. Le premier : un accord avec la Financial Conduct Authority britannique pour analyser le "data lake" du regulateur financier du Royaume-Uni. Le second : un memo du Pentagone formalisant Maven, le systeme d'IA de Palantir, comme "programme d'enregistrement" officiel de l'armee americaine.

Le meme logiciel, Foundry, traite desormais les donnees de fraude financiere des citoyens britanniques et les images de drones des champs de bataille. Le meme fournisseur facture 30 000 livres par semaine a la City et 1,3 milliard de dollars au Pentagone.

Au meme moment, un developpeur independant a fait tourner un modele de 397 milliards de parametres sur son MacBook Pro. En 24 heures de travail.

Meme technologie. Trajectoires opposees.

---

## Palantir a la FCA : le cerveau du regulateur

La FCA est le gendarme financier britannique. Elle surveille les marches, detecte les fraudes, protege les epargnants. Pour ce faire, elle accumule des quantites massives de donnees : dossiers d'enquete sensibles, signalements de fraude des preteurs, enregistrements d'appels telephoniques, emails, publications sur les reseaux sociaux, plaintes de consommateurs.

Palantir va analyser tout cela avec Foundry, sa plateforme d'IA. Le contrat prevoit un essai de trois mois a plus de 30 000 livres par semaine. La FCA precise que Palantir agira comme "processeur de donnees" et non comme "controleur" : l'entreprise ne peut agir que sur instruction du regulateur. Les cles de chiffrement des fichiers les plus sensibles restent sous controle exclusif de la FCA. Les donnees sont hebergees au Royaume-Uni. Palantir devra les detruire a la fin du contrat.

Les garde-fous existent sur le papier. Mais Christopher Houssemayne, avocat chez Hickman & Rose, pointe un risque structurel : "Si la FCA s'appuie sur un modele de detection par IA, un acteur malveillant pourrait prendre des mesures pour influencer ce systeme quand il examine des documents." Le risque n'est pas la fuite de donnees. C'est la dependance cognitive : quand l'outil de detection devient le cerveau du regulateur, compromettre l'outil compromet la regulation.

Ce contrat s'inscrit dans un engagement plus large de Palantir dans le secteur public britannique : 330 millions de livres avec le NHS, 240 millions avec le ministere de la Defense. Plus de 500 millions de livres au total. Un seul fournisseur pour la sante, la defense et la regulation financiere d'un pays du G7.

---

## Maven au Pentagone : le cerveau du champ de bataille

Le 9 mars 2026, le sous-secretaire a la Defense Steve Feinberg a signe un memo formalisant Maven comme "programme d'enregistrement" du Pentagone. En termes bureaucratiques, cela signifie un financement a long terme, une autorite d'acquisition formelle et un deploiement a travers toutes les branches de l'armee americaine.

Maven n'est pas un outil de bureau. C'est une plateforme de commandement et de controle qui analyse les donnees du champ de bataille : images de drones, imagerie satellite, capteurs radar et rapports de renseignement. Le systeme identifie des cibles, classe des menaces et synthetise des flux de donnees massifs en images operationnelles exploitables. Les humains restent dans la boucle de decision pour toute action letale, selon le Pentagone.

Le contrat initial de 2024 etait plafonne a 480 millions de dollars. En 2025, le Pentagone a releve ce plafond a 1,3 milliard. Maven est deja decrit comme "le systeme operationnel d'IA principal de l'armee americaine." L'integration complete est prevue pour septembre 2026.

Un detail revelateur : Maven utilise Claude, le modele d'IA d'Anthropic. Le Pentagone a recemment classe Anthropic comme "risque de chaine d'approvisionnement" dans le cadre d'un differend sur les garde-fous de securite des modeles d'IA avances. Le systeme de ciblage militaire le plus puissant du monde depend d'un fournisseur d'IA que son propre client considere comme un risque. La dependance est si profonde qu'elle persiste malgre le diagnostic.

Les experts des Nations Unies avertissent que le ciblage assiste par IA augmente les risques lies a des donnees erronees et a des biais potentiels. La question n'est pas abstraite : Maven a soutenu des milliers de frappes dans les dernieres semaines.

---

## Le pattern de concentration

Recapitulons. Une seule entreprise, fondee par Peter Thiel, traite desormais :

- Les donnees financieres des citoyens britanniques (FCA)
- Les dossiers medicaux du systeme de sante britannique (NHS)
- Les renseignements de defense du Royaume-Uni (MoD)
- Le ciblage de champ de bataille de l'armee americaine (Pentagon/Maven)

C'est un niveau de concentration d'infrastructure cognitive sans precedent dans l'histoire des democraties occidentales. Aucun fournisseur de la Guerre froide n'avait simultanement acces aux donnees financieres, medicales et militaires de deux pays allies.

La difference avec un fournisseur d'armes classique (Lockheed Martin, BAE Systems) est structurelle. Un fabricant d'avions livre un produit. Le client l'opere. Le fournisseur peut etre remplace. Palantir ne livre pas un produit : il fournit le cadre d'analyse dans lequel les decisions sont prises. Remplacer Palantir ne signifie pas acheter un autre logiciel. Cela signifie reconstruire la maniere dont l'organisation pense.

C'est du lock-in cognitif. Plus profond que le lock-in technologique. Le temps necessaire pour qu'une organisation retrouve sa capacite operationnelle apres le retrait de la plateforme se mesure en annees, pas en semaines.

---

## Flash-MoE : le cerveau sur un laptop

Pendant que Palantir centralise l'infrastructure cognitive des Etats, un developpeur nomme Dan Woods a publie Flash-MoE : un moteur d'inference qui fait tourner Qwen3.5-397B, un modele de 397 milliards de parametres, sur un MacBook Pro avec 48 Go de RAM.

Les chiffres sont saisissants. Le modele complet pese 209 Go. Flash-MoE n'en charge que 5,5 Go en memoire a tout moment. Le secret : Qwen3.5 est un modele Mixture-of-Experts (MoE). Sur 512 modules "experts" par couche, seuls 4 sont actives pour chaque token. Flash-MoE les charge a la demande depuis le SSD, qui lit a 17,5 Go/s sur le M3 Max d'Apple. Charger quatre modules de 3,9 Mo prend moins d'une milliseconde.

Le resultat : 5,5 tokens par seconde en mode 2 bits, avec un pic a 7 tokens par seconde. C'est utilisable. Pas rapide, mais utilisable. Et entierement local. Pas d'API. Pas d'abonnement. Pas de donnees envoyees a un serveur.

Le code est ecrit en C, Objective-C et Metal (les shaders GPU d'Apple). Pas de Python, pas de frameworks. Environ 5 000 lignes de code de base plus 1 100 lignes de shaders Metal. Le tout construit en 24 heures, en utilisant Claude pour 90 experiences d'optimisation.

L'approche s'appuie sur un article de recherche d'Apple de 2023, "LLM in a Flash", mais c'est la premiere implementation open source qui atteint des vitesses utilisables sur du materiel grand public. Le code est disponible sur GitHub.

Ce qui etait il y a un an le domaine exclusif de clusters GPU coutant des centaines de dollars par heure tourne maintenant sur un portable. La puissance de calcul qui permet a Maven d'identifier des cibles est, structurellement, la meme que celle qui tourne sur le MacBook de Dan Woods.

---

## La bifurcation

Deux trajectoires pour la meme technologie.

D'un cote, la centralisation cognitive : une entreprise privee devient le cerveau d'institutions publiques. Le regulateur financier, le systeme de sante et l'armee sous-traitent leur capacite d'analyse a un fournisseur unique. Le pouvoir de decision reste formellement chez le client, mais le cadre d'analyse appartient au fournisseur.

De l'autre, la democratisation de l'inference : un modele plus puissant que ce que la plupart des entreprises pouvaient deployer il y a 18 mois tourne sur du materiel que n'importe qui peut acheter. L'IA n'est plus un service a louer. C'est une capacite a posseder.

La tension entre ces deux trajectoires definira la prochaine decennie. Si l'inference locale continue a progresser a ce rythme, la centralisation de Palantir devient un choix politique, pas une necessite technique. Les organisations qui sous-traitent leur pensee a un fournisseur unique le font parce qu'elles le decident, pas parce qu'elles n'ont pas d'alternative.

La question n'est pas de savoir si l'IA va penser pour nous. Elle le fait deja. La question est : qui controle la pensee ?

---

*Sources : UKTN, TechStory, AI for Automation, Reuters, CityAM, Simon Willison, GitHub/flash-moe*
