# Le goulot est toujours à l'interface

*Article #9 | Strate, 23 mars 2026*

---

## Quatre histoires, un seul pattern

Un constructeur automobile chinois redesigne un connecteur de charge. Un légendaire architecte logiciel publie 470 lignes de Python pour réinventer le contrôle de version. Un développeur démontre que le code est un médium de précision, pas d'instruction. Et une étude mesurée sur 246 tâches révèle que les développeurs assistés par IA sont 19% plus lents, mais se croient 20% plus rapides.

Ces quatre histoires n'ont rien en commun. Sauf une chose : dans chaque cas, le goulot d'étranglement n'était pas là où tout le monde regardait. Ce n'était pas la batterie, mais le connecteur. Pas la vitesse de Git, mais le merge. Pas l'écriture du code, mais la spécification. Pas la production, mais la compréhension.

Le goulot est toujours à l'interface, pas au throughput.

---

## BYD : le connecteur, pas la batterie

Depuis dix ans, l'industrie du véhicule électrique investit des milliards dans la chimie des batteries. Densités énergétiques, cathodes nickel-manganèse-cobalt, anodes silicium, batteries solid-state. La course au throughput : plus d'énergie, plus vite, plus longtemps.

BYD vient de démontrer que le vrai goulot était ailleurs.

En mars 2026, le constructeur chinois a présenté un système de recharge qui passe de 10% à 60% en moins de 5 minutes. Pas grâce à une révolution chimique, mais grâce à un redesign complet de l'interface de charge. L'architecture est à 1 000 volts, le pic de puissance atteint 1 002 kW en conditions réelles sur une Han L. La batterie utilise du LFP (lithium-fer-phosphate), une chimie mature et peu coûteuse.

Le vrai travail d'ingénierie est dans le câble et le connecteur. Le nouveau câble pèse 2 kg, refroidi par liquide, suspendu en hauteur sur un dispenseur en T conçu pour atteindre tout port de charge sur tout véhicule sans jamais toucher le sol. Le connecteur est conçu pour être manipulable par n'importe qui. C'est un contraste frappant avec les prises CCS américaines, lourdes, rigides, et hostiles.

Le détail révélateur : la Han L et la Tang L acceptent deux prises DC simultanées. Deux câbles, un véhicule, 500 kW combinés. C'est une solution d'interface, pas de chimie. Quand le câble est le goulot, vous doublez les câbles.

BYD a déjà déployé 500 stations Megawatt en Chine, avec un plan pour en construire 20 000. L'Europe est prévue pour le deuxième trimestre 2026, avec 200 à 300 premières stations. Les bornes intègrent du stockage d'énergie pour compenser les limites du réseau électrique local. Là encore, c'est l'interface entre la borne et le réseau qui est résolue, pas la production d'électricité.

La leçon : l'industrie EV a dépensé une décennie à optimiser le throughput (la batterie) alors que le goulot était l'interface (le connecteur). Le jour où quelqu'un a redesigné le câble, le problème de la recharge s'est évaporé.

---

## Manyana : le merge, pas la vitesse

Git est le logiciel de contrôle de version le plus utilisé au monde. Il est aussi le plus détesté par les gens qui le comprennent vraiment. Pas parce qu'il est lent. Parce que les merges échouent.

Bram Cohen connaît le problème. L'inventeur de BitTorrent, le créateur de Chia, est un architecte qui résout le même problème structurel dans des domaines différents : rendre les opérations commutatives. Dans BitTorrent, il a rendu le transfert de fichiers indifférent à l'ordre des morceaux. Dans Chia, il a rendu la validation de la blockchain indifférente à l'ordre des transactions. Avec Manyana, il veut rendre le contrôle de version indifférent à l'ordre des merges.

Manyana est un prototype de 470 lignes de Python. Son principe : les merges ne failent jamais. Le résultat est toujours le même, quel que soit l'ordre dans lequel les branches sont fusionnées. Les conflits ne bloquent pas le processus. Ils sont affichés informatiquement sur un merge qui a techniquement réussi.

La structure de données est un "weave" qui contient toutes les lignes ayant jamais existé dans l'historique d'un fichier, avec des métadonnées d'ajout et de suppression. Pas besoin de traverser des graphes acycliques dirigés ou de trouver des ancêtres communs. Quand deux branches insèrent au même point, le CRDT (Conflict-Free Replicated Data Type) choisit un ordre stable. Le merge est commutatif : merge(A, B) = merge(B, A).

Michael Toomim a découvert une équivalence mathématique entre la structure de données "weave" et les CRDTs, et entre le "rebase" et l'Operational Transform (OT). Ce ne sont pas des analogies. Ce sont des isomorphismes.

Cohen ne dit pas que Git est mauvais. Il dit que le merge est le goulot. Son post "The State of Merging Technology" recommande d'abord de changer l'algorithme de diff par défaut de Git vers histogram, et d'implémenter l'algorithme weave pour les merges non-rebase. Ce sont des améliorations d'interface, pas de throughput.

Le contexte est important. Google, Meta et Cohen convergent indépendamment vers le même diagnostic. Google a construit Piper (un dépôt unique pour des milliards de fichiers). Meta a construit Sapling (maintenant open source). Les deux ont quitté Git. Jujutsu, le VCS expérimental de Google, est aussi open source. La pression vient du haut : les organisations qui opèrent à l'échelle la plus grande ont déjà décidé que l'interface de Git est le goulot.

---

## Précision : le code n'est pas de l'écriture

Steve Krouse a publié un essai intitulé "Precision" qui pose une question simple : si l'IA peut écrire du code, pourquoi avons-nous encore besoin de programmeurs ?

Sa réponse : parce que le code n'est pas de l'écriture. C'est de la précision.

L'argument part d'un exemple concret. Dan Shipper, un éditeur tech, a voulu construire une application de traitement de texte collaborative avec l'IA. La spec semblait simple : un éditeur de texte avec collaboration en temps réel. L'IA a produit du code. L'application fonctionnait. Puis les cas limites sont apparus. Que se passe-t-il quand deux utilisateurs modifient le même paragraphe simultanément ? Comment gérer les curseurs multiples ? La synchronisation hors ligne ? La résolution de conflits ?

Krouse cite Dijkstra : "The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise." Le code n'est pas un médium d'instruction. C'est un médium de désambiguïsation. Le langage naturel paraît précis jusqu'à ce qu'il soit testé à l'échelle. Le code force la confrontation avec chaque cas limite, chaque état possible, chaque interaction entre composants.

La limitation fondamentale est la mémoire de travail humaine, environ 7 concepts simultanément. La maîtrise de la complexité nécessite la compression récursive en abstractions. Sophie Alpert a simplifié le système de notifications de Slack en créant des abstractions qui rendent le système compréhensible. Ce n'est pas de l'écriture. C'est de l'architecture. Et l'architecture est une compétence d'interface, pas de production.

La conclusion de Krouse est provocatrice : dire que le code est mort, c'est comme dire que le storytelling est mort après l'invention de l'imprimerie. L'imprimerie a accéléré la production (throughput). Mais le goulot n'a jamais été la vitesse de copie. C'était la qualité du récit.

---

## La loi d'Amdahl des interfaces

En juillet 2025, METR, une organisation de recherche en sécurité de l'IA basée à Berkeley, a publié les résultats d'un essai contrôlé randomisé qui aurait dû déclencher un séisme. 16 développeurs expérimentés, 246 tâches sur des codebases matures et complexes. La moitié des tâches avec Cursor Pro et Claude 3.5/3.7 Sonnet. L'autre moitié sans.

Résultat : les développeurs assistés par IA étaient 19% plus lents. Pas plus rapides. Plus lents.

Mais le chiffre le plus frappant n'était pas le ralentissement. C'était la perception. Avant l'étude, les participants prédisaient un gain de 24% de vitesse. Après l'étude, après avoir été mesurés comme plus lents, ils estimaient toujours être 20% plus rapides. Un écart perception-réalité de 39 points.

Comment est-ce possible ? La loi d'Amdahl donne la réponse.

Gene Amdahl a formalisé en 1967 un principe simple : le gain de vitesse d'un système est limité par la fraction qui ne peut pas être accélérée. Si 70% du travail de développement logiciel est de la compréhension, de la conception, de la vérification et de la communication (l'interface entre l'intention et le code), et si l'IA n'accélère que les 30% d'écriture (le throughput), alors même un speedup infini sur l'écriture ne produirait qu'un gain de 43%.

Les données de terrain confirment. Software.com, en analysant 250 000 développeurs, a mesuré que le développeur médian écrit du code 52 minutes par jour, soit 11% d'une semaine de 40 heures. Bain & Company estime que l'écriture et le test de code représentent 25 à 35% du cycle de développement total. Le reste est de la lecture, de la compréhension, de la discussion, de la spécification et de la vérification.

La fraction accélérable est petite. Le gain maximal avec f = 0.30 est 1.43x. Avec f = 0.35, c'est 1.54x. Et ces calculs supposent un speedup infini sur la fraction accélérable. En pratique, l'IA ne produit pas un speedup infini. Elle produit du code qui doit être relu, vérifié et souvent corrigé. Le "dark flow" décrit par Rachel Thomas (fast.ai) est le mécanisme psychologique : l'IA produit du volume à grande vitesse, le cerveau enregistre "tâche accomplie", mais le volume n'est pas de la valeur.

Gergely Orosz, auteur de The Pragmatic Engineer, résume la situation en une phrase : "Speed of typing out code has never been the bottleneck for software development."

L'étude de suivi de METR (août 2025 à début 2026) a tenté d'élargir l'échantillon à 57 développeurs et 800+ tâches. Les résultats préliminaires montrent toujours un ralentissement pour les développeurs de la cohorte originale (-18%) et un effet quasi-nul pour les nouveaux développeurs (-4%). Mais METR déclare les données "unreliable" à cause d'un biais de sélection : 30 à 50% des développeurs évitaient les tâches assignées sans IA, et le recrutement était difficile parce que les développeurs refusaient de travailler sans leurs outils. L'étude mesure un monde qui n'existe plus.

---

## L'interface comme loi universelle

BYD, Cohen, Krouse et METR opèrent dans quatre domaines différents : les véhicules électriques, le contrôle de version, la théorie de la programmation et la productivité logicielle. Ils n'ont aucune relation entre eux. Mais ils convergent vers le même constat.

Le pattern est structurel. Quand un système est optimisé pendant assez longtemps, le throughput cesse d'être le facteur limitant. Le goulot migre vers l'interface entre les composants. L'interface entre le chargeur et le véhicule. L'interface entre deux branches de code. L'interface entre l'intention humaine et l'implémentation. L'interface entre l'outil IA et le processus de développement.

La loi d'Amdahl est la formalisation de ce constat. La fraction sérielle d'un système détermine son accélération maximale, quel que soit l'investissement dans la fraction parallèle. Investir dans la batterie quand le goulot est le connecteur. Investir dans la vitesse de Git quand le goulot est le merge. Investir dans l'écriture de code quand le goulot est la spécification. Investir dans les outils IA quand le goulot est la compréhension.

Les ruptures ne viennent pas de l'accélération du throughput. Elles viennent du redesign de l'interface. BYD n'a pas inventé une nouvelle chimie. Cohen n'a pas accéléré Git. Krouse ne propose pas d'écrire plus vite. METR ne suggère pas de meilleurs prompts. Chacun, à sa manière, dit la même chose : regardez l'interface.

La question pour les décideurs, les investisseurs et les ingénieurs est simple : dans votre système, où est l'interface ? Parce que c'est là que se trouve le goulot. Et c'est là que se trouve la prochaine rupture.

---

*Sources : InsideEVs, BYD, bramcohen.com, stevekrouse.com/precision, METR.org, Software.com, Bain & Company, The Pragmatic Engineer, fast.ai*
