# Le goulot est toujours a l'interface

*Article #9 | Strate, 23 mars 2026*

---

## Quatre histoires, un seul pattern

Un constructeur automobile chinois redesigne un connecteur de charge. Un legendaire architecte logiciel publie 470 lignes de Python pour reinventer le controle de version. Un developpeur demontre que le code est un medium de precision, pas d'instruction. Et une etude mesuree sur 246 taches revele que les developpeurs assistes par IA sont 19% plus lents, mais se croient 20% plus rapides.

Ces quatre histoires n'ont rien en commun. Sauf une chose : dans chaque cas, le goulot d'etranglement n'etait pas la ou tout le monde regardait. Ce n'etait pas la batterie, mais le connecteur. Pas la vitesse de Git, mais le merge. Pas l'ecriture du code, mais la specification. Pas la production, mais la comprehension.

Le goulot est toujours a l'interface, pas au throughput.

---

## BYD : le connecteur, pas la batterie

Depuis dix ans, l'industrie du vehicule electrique investit des milliards dans la chimie des batteries. Densites energetiques, cathodes nickel-manganese-cobalt, anodes silicium, batteries solid-state. La course au throughput : plus d'energie, plus vite, plus longtemps.

BYD vient de demontrer que le vrai goulot etait ailleurs.

En mars 2026, le constructeur chinois a presente un systeme de recharge qui passe de 10% a 60% en moins de 5 minutes. Pas grace a une revolution chimique, mais grace a un redesign complet de l'interface de charge. L'architecture est a 1 000 volts, le pic de puissance atteint 1 002 kW en conditions reelles sur une Han L. La batterie utilise du LFP (lithium-fer-phosphate), une chimie mature et peu couteuse.

Le vrai travail d'ingenierie est dans le cable et le connecteur. Le nouveau cable pese 2 kg, refroidi par liquide, suspendu en hauteur sur un dispenseur en T concu pour atteindre tout port de charge sur tout vehicule sans jamais toucher le sol. Le connecteur est concu pour etre manipulable par n'importe qui. C'est un contraste frappant avec les prises CCS americaines, lourdes, rigides, et hostiles.

Le detail revelateur : la Han L et la Tang L acceptent deux prises DC simultanees. Deux cables, un vehicule, 500 kW combines. C'est une solution d'interface, pas de chimie. Quand le cable est le goulot, vous doublez les cables.

BYD a deja deploye 500 stations Megawatt en Chine, avec un plan pour en construire 20 000. L'Europe est prevue pour le deuxieme trimestre 2026, avec 200 a 300 premieres stations. Les bornes integrent du stockage d'energie pour compenser les limites du reseau electrique local. La encore, c'est l'interface entre la borne et le reseau qui est resolue, pas la production d'electricite.

La lecon : l'industrie EV a depense une decennie a optimiser le throughput (la batterie) alors que le goulot etait l'interface (le connecteur). Le jour ou quelqu'un a redesigne le cable, le probleme de la recharge s'est evapore.

---

## Manyana : le merge, pas la vitesse

Git est le logiciel de controle de version le plus utilise au monde. Il est aussi le plus deteste par les gens qui le comprennent vraiment. Pas parce qu'il est lent. Parce que les merges echouent.

Bram Cohen connait le probleme. L'inventeur de BitTorrent, le createur de Chia, est un architecte qui resout le meme probleme structurel dans des domaines differents : rendre les operations commutatives. Dans BitTorrent, il a rendu le transfert de fichiers indifferent a l'ordre des morceaux. Dans Chia, il a rendu la validation de la blockchain indifferente a l'ordre des transactions. Avec Manyana, il veut rendre le controle de version indifferent a l'ordre des merges.

Manyana est un prototype de 470 lignes de Python. Son principe : les merges ne failent jamais. Le resultat est toujours le meme, quel que soit l'ordre dans lequel les branches sont fusionnees. Les conflits ne bloquent pas le processus. Ils sont affiches informatiquement sur un merge qui a techniquement reussi.

La structure de donnees est un "weave" qui contient toutes les lignes ayant jamais existe dans l'historique d'un fichier, avec des metadonnees d'ajout et de suppression. Pas besoin de traverser des graphes acycliques diriges ou de trouver des ancetres communs. Quand deux branches inserent au meme point, le CRDT (Conflict-Free Replicated Data Type) choisit un ordre stable. Le merge est commutatif : merge(A, B) = merge(B, A).

Michael Toomim a decouvert une equivalence mathematique entre la structure de donnees "weave" et les CRDTs, et entre le "rebase" et l'Operational Transform (OT). Ce ne sont pas des analogies. Ce sont des isomorphismes.

Cohen ne dit pas que Git est mauvais. Il dit que le merge est le goulot. Son post "The State of Merging Technology" recommande d'abord de changer l'algorithme de diff par defaut de Git vers histogram, et d'implementer l'algorithme weave pour les merges non-rebase. Ce sont des ameliorations d'interface, pas de throughput.

Le contexte est important. Google, Meta et Cohen convergent independamment vers le meme diagnostic. Google a construit Piper (un depot unique pour des milliards de fichiers). Meta a construit Sapling (maintenant open source). Les deux ont quitte Git. Jujutsu, le VCS experimental de Google, est aussi open source. La pression vient du haut : les organisations qui operent a l'echelle la plus grande ont deja decide que l'interface de Git est le goulot.

---

## Precision : le code n'est pas de l'ecriture

Steve Krouse a publie un essai intitule "Precision" qui pose une question simple : si l'IA peut ecrire du code, pourquoi avons-nous encore besoin de programmeurs ?

Sa reponse : parce que le code n'est pas de l'ecriture. C'est de la precision.

L'argument part d'un exemple concret. Dan Shipper, un editeur tech, a voulu construire une application de traitement de texte collaborative avec l'IA. La spec semblait simple : un editeur de texte avec collaboration en temps reel. L'IA a produit du code. L'application fonctionnait. Puis les cas limites sont apparus. Que se passe-t-il quand deux utilisateurs modifient le meme paragraphe simultanement ? Comment gerer les curseurs multiples ? La synchronisation hors ligne ? La resolution de conflits ?

Krouse cite Dijkstra : "The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise." Le code n'est pas un medium d'instruction. C'est un medium de desambiguisation. Le langage naturel parait precis jusqu'a ce qu'il soit teste a l'echelle. Le code force la confrontation avec chaque cas limite, chaque etat possible, chaque interaction entre composants.

La limitation fondamentale est la memoire de travail humaine, environ 7 concepts simultanement. La maitrise de la complexite necessite la compression recursive en abstractions. Sophie Alpert a simplifie le systeme de notifications de Slack en creant des abstractions qui rendent le systeme comprehensible. Ce n'est pas de l'ecriture. C'est de l'architecture. Et l'architecture est une competence d'interface, pas de production.

La conclusion de Krouse est provocatrice : dire que le code est mort, c'est comme dire que le storytelling est mort apres l'invention de l'imprimerie. L'imprimerie a accelere la production (throughput). Mais le goulot n'a jamais ete la vitesse de copie. C'etait la qualite du recit.

---

## La loi d'Amdahl des interfaces

En juillet 2025, METR, une organisation de recherche en securite de l'IA basee a Berkeley, a publie les resultats d'un essai controle randomise qui aurait du declencher un seisme. 16 developpeurs experimentes, 246 taches sur des codebases matures et complexes. La moitie des taches avec Cursor Pro et Claude 3.5/3.7 Sonnet. L'autre moitie sans.

Resultat : les developpeurs assistes par IA etaient 19% plus lents. Pas plus rapides. Plus lents.

Mais le chiffre le plus frappant n'etait pas le ralentissement. C'etait la perception. Avant l'etude, les participants predisaient un gain de 24% de vitesse. Apres l'etude, apres avoir ete mesures comme plus lents, ils estimaient toujours etre 20% plus rapides. Un ecart perception-realite de 39 points.

Comment est-ce possible ? La loi d'Amdahl donne la reponse.

Gene Amdahl a formalise en 1967 un principe simple : le gain de vitesse d'un systeme est limite par la fraction qui ne peut pas etre acceleree. Si 70% du travail de developpement logiciel est de la comprehension, de la conception, de la verification et de la communication (l'interface entre l'intention et le code), et si l'IA n'accelere que les 30% d'ecriture (le throughput), alors meme un speedup infini sur l'ecriture ne produirait qu'un gain de 43%.

Les donnees de terrain confirment. Software.com, en analysant 250 000 developpeurs, a mesure que le developpeur median ecrit du code 52 minutes par jour, soit 11% d'une semaine de 40 heures. Bain & Company estime que l'ecriture et le test de code representent 25 a 35% du cycle de developpement total. Le reste est de la lecture, de la comprehension, de la discussion, de la specification et de la verification.

La fraction accelerable est petite. Le gain maximal avec f = 0.30 est 1.43x. Avec f = 0.35, c'est 1.54x. Et ces calculs supposent un speedup infini sur la fraction accelerable. En pratique, l'IA ne produit pas un speedup infini. Elle produit du code qui doit etre relu, verifie et souvent corrige. Le "dark flow" decrit par Rachel Thomas (fast.ai) est le mecanisme psychologique : l'IA produit du volume a grande vitesse, le cerveau enregistre "tache accomplie", mais le volume n'est pas de la valeur.

Gergely Orosz, auteur de The Pragmatic Engineer, resume la situation en une phrase : "Speed of typing out code has never been the bottleneck for software development."

L'etude de suivi de METR (aout 2025 a debut 2026) a tente d'elargir l'echantillon a 57 developpeurs et 800+ taches. Les resultats preliminaires montrent toujours un ralentissement pour les developpeurs de la cohorte originale (-18%) et un effet quasi-nul pour les nouveaux developpeurs (-4%). Mais METR declare les donnees "unreliable" a cause d'un biais de selection : 30 a 50% des developpeurs evitaient les taches assignees sans IA, et le recrutement etait difficile parce que les developpeurs refusaient de travailler sans leurs outils. L'etude mesure un monde qui n'existe plus.

---

## L'interface comme loi universelle

BYD, Cohen, Krouse et METR operent dans quatre domaines differents : les vehicules electriques, le controle de version, la theorie de la programmation et la productivite logicielle. Ils n'ont aucune relation entre eux. Mais ils convergent vers le meme constat.

Le pattern est structurel. Quand un systeme est optimise pendant assez longtemps, le throughput cesse d'etre le facteur limitant. Le goulot migre vers l'interface entre les composants. L'interface entre le chargeur et le vehicule. L'interface entre deux branches de code. L'interface entre l'intention humaine et l'implementation. L'interface entre l'outil IA et le processus de developpement.

La loi d'Amdahl est la formalisation de ce constat. La fraction serielle d'un systeme determine son acceleration maximale, quel que soit l'investissement dans la fraction parallele. Investir dans la batterie quand le goulot est le connecteur. Investir dans la vitesse de Git quand le goulot est le merge. Investir dans l'ecriture de code quand le goulot est la specification. Investir dans les outils IA quand le goulot est la comprehension.

Les ruptures ne viennent pas de l'acceleration du throughput. Elles viennent du redesign de l'interface. BYD n'a pas invente une nouvelle chimie. Cohen n'a pas accelere Git. Krouse ne propose pas d'ecrire plus vite. METR ne suggere pas de meilleurs prompts. Chacun, a sa maniere, dit la meme chose : regardez l'interface.

La question pour les decideurs, les investisseurs et les ingenieurs est simple : dans votre systeme, ou est l'interface ? Parce que c'est la que se trouve le goulot. Et c'est la que se trouve la prochaine rupture.

---

*Sources : InsideEVs, BYD, bramcohen.com, stevekrouse.com/precision, METR.org, Software.com, Bain & Company, The Pragmatic Engineer, fast.ai*
