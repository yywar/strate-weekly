# Le Pentagone et la City ont le même fournisseur de cerveau

*Article #10 | Strate, 23 mars 2026*

---

## Deux contrats, une semaine

Cette semaine, Palantir a signé deux contrats. Le premier : un accord avec la Financial Conduct Authority britannique pour analyser le "data lake" du régulateur financier du Royaume-Uni. Le second : un mémo du Pentagone formalisant Maven, le système d'IA de Palantir, comme "programme d'enregistrement" officiel de l'armée américaine.

Le même logiciel, Foundry, traite désormais les données de fraude financière des citoyens britanniques et les images de drones des champs de bataille. Le même fournisseur facture 30 000 livres par semaine à la City et 1,3 milliard de dollars au Pentagone.

Au même moment, un développeur indépendant a fait tourner un modèle de 397 milliards de paramètres sur son MacBook Pro. En 24 heures de travail.

Même technologie. Trajectoires opposées.

---

## Palantir à la FCA : le cerveau du régulateur

La FCA est le gendarme financier britannique. Elle surveille les marchés, détecte les fraudes, protège les épargnants. Pour ce faire, elle accumule des quantités massives de données : dossiers d'enquête sensibles, signalements de fraude des prêteurs, enregistrements d'appels téléphoniques, emails, publications sur les réseaux sociaux, plaintes de consommateurs.

Palantir va analyser tout cela avec Foundry, sa plateforme d'IA. Le contrat prévoit un essai de trois mois à plus de 30 000 livres par semaine. La FCA précise que Palantir agira comme "processeur de données" et non comme "contrôleur" : l'entreprise ne peut agir que sur instruction du régulateur. Les clés de chiffrement des fichiers les plus sensibles restent sous contrôle exclusif de la FCA. Les données sont hébergées au Royaume-Uni. Palantir devra les détruire à la fin du contrat.

Les garde-fous existent sur le papier. Mais Christopher Houssemayne, avocat chez Hickman & Rose, pointe un risque structurel : "Si la FCA s'appuie sur un modèle de détection par IA, un acteur malveillant pourrait prendre des mesures pour influencer ce système quand il examine des documents." Le risque n'est pas la fuite de données. C'est la dépendance cognitive : quand l'outil de détection devient le cerveau du régulateur, compromettre l'outil compromet la régulation.

Ce contrat s'inscrit dans un engagement plus large de Palantir dans le secteur public britannique : 330 millions de livres avec le NHS, 240 millions avec le ministère de la Défense. Plus de 500 millions de livres au total. Un seul fournisseur pour la santé, la défense et la régulation financière d'un pays du G7.

---

## Maven au Pentagone : le cerveau du champ de bataille

Le 9 mars 2026, le sous-secrétaire à la Défense Steve Feinberg a signé un mémo formalisant Maven comme "programme d'enregistrement" du Pentagone. En termes bureaucratiques, cela signifie un financement à long terme, une autorité d'acquisition formelle et un déploiement à travers toutes les branches de l'armée américaine.

Maven n'est pas un outil de bureau. C'est une plateforme de commandement et de contrôle qui analyse les données du champ de bataille : images de drones, imagerie satellite, capteurs radar et rapports de renseignement. Le système identifie des cibles, classe des menaces et synthétise des flux de données massifs en images opérationnelles exploitables. Les humains restent dans la boucle de décision pour toute action létale, selon le Pentagone.

Le contrat initial de 2024 était plafonné à 480 millions de dollars. En 2025, le Pentagone a relevé ce plafond à 1,3 milliard. Maven est déjà décrit comme "le système opérationnel d'IA principal de l'armée américaine." L'intégration complète est prévue pour septembre 2026.

Un détail révélateur : Maven utilise Claude, le modèle d'IA d'Anthropic. Le Pentagone a récemment classé Anthropic comme "risque de chaîne d'approvisionnement" dans le cadre d'un différend sur les garde-fous de sécurité des modèles d'IA avancés. Le système de ciblage militaire le plus puissant du monde dépend d'un fournisseur d'IA que son propre client considère comme un risque. La dépendance est si profonde qu'elle persiste malgré le diagnostic.

Les experts des Nations Unies avertissent que le ciblage assisté par IA augmente les risques liés à des données erronées et à des biais potentiels. La question n'est pas abstraite : Maven a soutenu des milliers de frappes dans les dernières semaines.

---

## Le pattern de concentration

Récapitulons. Une seule entreprise, fondée par Peter Thiel, traite désormais :

- Les données financières des citoyens britanniques (FCA)
- Les dossiers médicaux du système de santé britannique (NHS)
- Les renseignements de défense du Royaume-Uni (MoD)
- Le ciblage de champ de bataille de l'armée américaine (Pentagon/Maven)

C'est un niveau de concentration d'infrastructure cognitive sans précédent dans l'histoire des démocraties occidentales. Aucun fournisseur de la Guerre froide n'avait simultanément accès aux données financières, médicales et militaires de deux pays alliés.

La différence avec un fournisseur d'armes classique (Lockheed Martin, BAE Systems) est structurelle. Un fabricant d'avions livre un produit. Le client l'opère. Le fournisseur peut être remplacé. Palantir ne livre pas un produit : il fournit le cadre d'analyse dans lequel les décisions sont prises. Remplacer Palantir ne signifie pas acheter un autre logiciel. Cela signifie reconstruire la manière dont l'organisation pense.

C'est du lock-in cognitif. Plus profond que le lock-in technologique. Le temps nécessaire pour qu'une organisation retrouve sa capacité opérationnelle après le retrait de la plateforme se mesure en années, pas en semaines.

---

## Flash-MoE : le cerveau sur un laptop

Pendant que Palantir centralise l'infrastructure cognitive des États, un développeur nommé Dan Woods a publié Flash-MoE : un moteur d'inférence qui fait tourner Qwen3.5-397B, un modèle de 397 milliards de paramètres, sur un MacBook Pro avec 48 Go de RAM.

Les chiffres sont saisissants. Le modèle complet pèse 209 Go. Flash-MoE n'en charge que 5,5 Go en mémoire à tout moment. Le secret : Qwen3.5 est un modèle Mixture-of-Experts (MoE). Sur 512 modules "experts" par couche, seuls 4 sont activés pour chaque token. Flash-MoE les charge à la demande depuis le SSD, qui lit à 17,5 Go/s sur le M3 Max d'Apple. Charger quatre modules de 3,9 Mo prend moins d'une milliseconde.

Le résultat : 5,5 tokens par seconde en mode 2 bits, avec un pic à 7 tokens par seconde. C'est utilisable. Pas rapide, mais utilisable. Et entièrement local. Pas d'API. Pas d'abonnement. Pas de données envoyées à un serveur.

Le code est écrit en C, Objective-C et Metal (les shaders GPU d'Apple). Pas de Python, pas de frameworks. Environ 5 000 lignes de code de base plus 1 100 lignes de shaders Metal. Le tout construit en 24 heures, en utilisant Claude pour 90 expériences d'optimisation.

L'approche s'appuie sur un article de recherche d'Apple de 2023, "LLM in a Flash", mais c'est la première implémentation open source qui atteint des vitesses utilisables sur du matériel grand public. Le code est disponible sur GitHub.

Ce qui était il y a un an le domaine exclusif de clusters GPU coûtant des centaines de dollars par heure tourne maintenant sur un portable. La puissance de calcul qui permet à Maven d'identifier des cibles est, structurellement, la même que celle qui tourne sur le MacBook de Dan Woods.

---

## La bifurcation

Deux trajectoires pour la même technologie.

D'un côté, la centralisation cognitive : une entreprise privée devient le cerveau d'institutions publiques. Le régulateur financier, le système de santé et l'armée sous-traitent leur capacité d'analyse à un fournisseur unique. Le pouvoir de décision reste formellement chez le client, mais le cadre d'analyse appartient au fournisseur.

De l'autre, la démocratisation de l'inférence : un modèle plus puissant que ce que la plupart des entreprises pouvaient déployer il y a 18 mois tourne sur du matériel que n'importe qui peut acheter. L'IA n'est plus un service à louer. C'est une capacité à posséder.

La tension entre ces deux trajectoires définira la prochaine décennie. Si l'inférence locale continue à progresser à ce rythme, la centralisation de Palantir devient un choix politique, pas une nécessité technique. Les organisations qui sous-traitent leur pensée à un fournisseur unique le font parce qu'elles le décident, pas parce qu'elles n'ont pas d'alternative.

La question n'est pas de savoir si l'IA va penser pour nous. Elle le fait déjà. La question est : qui contrôle la pensée ?

---

*Sources : UKTN, TechStory, AI for Automation, Reuters, CityAM, Simon Willison, GitHub/flash-moe*
