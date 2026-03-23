# Manyana : quand Bram Cohen veut refaire le contrôle de version

*Article #7 | Strate, 23 mars 2026*

---

## L'homme qui redistribue les tuyaux

En avril 2001, un développeur de 25 ans quitte MojoNation, une startup de stockage distribué qui allait mourir quelques mois plus tard, et écrit un programme en Python. Le programme est simple : il découpe un fichier en fragments et les distribue entre tous ceux qui veulent le télécharger. Plus il y a de téléchargeurs, plus le téléchargement est rapide. Le développeur s'appelle Bram Cohen. Le programme s'appelle BitTorrent.

BitTorrent a résolu un problème que personne ne savait formuler. Le partage de fichiers sur Internet était centralisé : un serveur, des milliers de clients. Le serveur tombait, tout le monde s'arrêtait. Cohen a retourné le modèle : chaque client est aussi un serveur. Le fichier n'est nulle part et partout. Le résultat a été si efficace qu'à son apogée, BitTorrent représentait **un tiers du trafic Internet mondial**.

En août 2017, Cohen quitte la société BitTorrent Inc. (dont il avait été évincé de la direction opérationnelle) pour fonder Chia Network. Même architecture intellectuelle, domaine différent : les blockchains sont centralisées autour du proof-of-work, un mécanisme où la puissance de calcul, et donc la consommation d'énergie, détermine qui valide les transactions. Cohen remplace le proof-of-work par le proof-of-space-time : au lieu de brûler de l'électricité, on prouve qu'on dispose d'espace de stockage. La validation de la blockchain devient commutative, n'importe quel disque dur peut participer.

En mars 2026, Cohen publie Manyana. C'est un script Python de 470 lignes, placé dans le domaine public. Il s'attaque au dernier tuyau centralisé du développement logiciel : le contrôle de version. Et il pose une question que 40 millions d'utilisateurs de Git préféreraient ne pas entendre : et si les merge conflicts n'avaient jamais eu besoin d'exister ?

Le pattern est frappant par sa constance. En 25 ans, Cohen a touché à trois domaines entièrement distincts : le partage de fichiers, la blockchain, le contrôle de version : et a appliqué exactement la même opération intellectuelle à chacun : prendre un système centralisé et le rendre **commutatif**. Les opérations peuvent se faire dans n'importe quel ordre, par n'importe qui, et le résultat est le même. BitTorrent : le téléchargement est commutatif (les fragments arrivent dans n'importe quel ordre). Chia : la validation est commutative (n'importe quel stockage participe). Manyana : le merge est commutatif : `merge(A, B) = merge(B, A)`, toujours, sans exception.

---

## Le problème que tout le monde connaît et que personne ne résout

Git est l'infrastructure invisible du logiciel mondial. 100 millions de développeurs l'utilisent. GitHub héberge 420 millions de repositories. Chaque application sur votre téléphone, chaque site web que vous visitez, chaque système embarqué dans votre voiture a probablement été géré par Git à un moment de son existence.

Et Git a un problème fondamental que ses utilisateurs connaissent intimement : les merge conflicts.

Les chiffres sont sans appel. **87% des développeurs** déclarent avoir lutté avec des conflits de merge. La résolution de ces conflits consomme entre **10 et 20% du temps de développement** : un coût invisible qui n'apparaît dans aucun dashboard de productivité. Et le coût ne se limite pas au temps : le code qui passe par une résolution de conflit contient **deux fois plus de bugs** que le code normal. Pour les conflits sémantiques : ceux où le conflit n'est pas un problème de lignes identiques mais de logique incompatible : le multiplicateur monte à **26 fois plus de bugs**.

Le merge conflict est le symptôme d'un choix architectural fait par Linus Torvalds en 2005. Git modélise le code comme des snapshots, chaque commit est une photo de l'ensemble du projet à un instant donné. Quand deux développeurs modifient le même fichier, Git doit comparer les deux snapshots et deviner comment les réconcilier. Il n'a aucune compréhension de ce que le code *fait*, il ne voit que des lignes de texte. Deux modifications de la même ligne = conflit. Stop. Débrouillez-vous.

C'est un modèle qui fonctionne remarquablement bien pour les cas simples. Mais la simplicité a un coût caché : quand le cas n'est pas simple, Git ne dégrade pas gracieusement, il s'arrête. Et il s'arrête exactement au moment où le développeur a le plus besoin d'aide : au milieu d'un merge complexe, avec des dizaines de fichiers en conflit, sans aucun contexte sur *pourquoi* les changements entrent en collision.

L'analogie la plus précise est celle d'un correcteur orthographique qui ne comprendrait que les lettres, pas les mots. Il repère les doublons de caractères, mais quand la vraie erreur est une phrase mal construite, il ne peut rien faire. Et il arrête tout le processus pour vous demander de corriger à la main.

Le paradoxe est que tout le monde sait que c'est un problème, et que personne ne le résout. Pas par manque de compétence, par effet de réseau. Git est le standard de facto. GitHub, GitLab, Bitbucket, Azure DevOps : toute l'infrastructure de CI/CD du monde est construite autour de Git. Changer de système de contrôle de version, c'est comme changer de langue dans un pays de 100 millions d'habitants. Le coût de la migration dépasse le coût du problème, pour chaque individu. Mais le coût agrégé, lui, est colossal.

C'est le scénario classique du "Nobody ever got fired for buying IBM" appliqué à l'infrastructure de développement.

---

## Ce que Manyana propose réellement

La proposition de Cohen tient en une phrase : **les merges ne devraient jamais échouer.**

C'est une affirmation qui, pour quiconque a passé un après-midi à résoudre un merge conflict à 3 voies, sonne comme une provocation. Mais la provocation est mathématique, pas rhétorique. Manyana est construit sur les CRDTs, les Conflict-Free Replicated Data Types, une structure de données formellement prouvée comme convergeant toujours vers le même état, quel que soit l'ordre des opérations.

Le concept est né dans le monde des bases de données distribuées. Quand deux serveurs reçoivent des modifications simultanées et ne peuvent pas se coordonner en temps réel, un CRDT garantit qu'ils convergeront vers le même résultat sans avoir besoin de se mettre d'accord au préalable. C'est la pierre angulaire de Google Docs, des éditeurs collaboratifs, et de tout système qui permet à plusieurs personnes de modifier le même document simultanément.

Cohen applique cette idée au code source. Et la différence architecturale avec Git est fondamentale.

Git stocke des snapshots : des photos de l'état complet du projet à chaque commit. Manyana stocke un **weave** : une structure unifiée qui contient **chaque ligne de code ayant jamais existé dans l'historique du projet**. Les lignes supprimées ne disparaissent pas. Elles sont marquées comme supprimées, avec l'identifiant du commit qui les a supprimées. Les lignes ajoutées portent l'identifiant du commit qui les a créées. L'historique n'est pas une séquence de photos : c'est un tissu où chaque fil est traçable.

Dans ce modèle, un merge n'est plus une comparaison de snapshots. C'est une opération sur l'historique des décisions. Quand deux branches modifient la même ligne, Manyana ne dit pas "conflit" : il dit "deux décisions différentes ont été prises sur cette ligne, voici les deux, voici leur historique, voici le résultat combiné." Le résultat est **toujours** un état valide. Pas d'échec de merge. Pas de marqueurs `<<<<<<<`. Pas de résolution manuelle obligatoire.

"Two states go in, one state comes out, and it's always correct," écrit Cohen.

Les conflits ne disparaissent pas : ils changent de nature. Au lieu d'être des erreurs qui bloquent le processus, ils deviennent des **informations** que le développeur peut traiter à son rythme. Le merge réussit toujours. Le conflit est flaggé comme un point d'attention, pas comme un obstacle.

L'innovation technique clé : celle qui distingue Manyana des systèmes CRDT précédents appliqués au code : est dans la gestion du **local undo**. Annuler des changements sur une branche de feature tout en préservant la possibilité de merger plus tard est, selon Cohen, "the feature which finally makes weave-based version control clearly superior to rebase-based hackery." La solution repose sur des commit-based obviation metadata : au lieu de compteurs simples qui échouent avec le local undo, chaque commit référence explicitement les commits qu'il remplace. C'est plus complexe qu'un compteur, mais c'est correct dans tous les cas.

Et il y a une propriété qui n'est pas technique mais philosophique : la commutativité. `merge(A, B) = merge(B, A)`. L'ordre dans lequel les branches sont fusionnées ne change pas le résultat. Dans Git, l'ordre peut produire des résultats différents, un fait que quiconque a fait un rebase suivi d'un merge sait par expérience douloureuse. Dans Manyana, l'ordre est indifférent. C'est ce qui rend le système adapté à un workflow véritablement décentralisé, pas décentralisé comme GitHub (un serveur central avec des clients locaux), mais décentralisé comme BitTorrent (pas de serveur du tout).

---

## Pourquoi 470 lignes de Python pourraient compter

Manyana n'est pas un produit. C'est un **argument**.

Cohen l'écrit en Python, en 470 lignes, et le place dans le domaine public. Pas de framework, pas de dépendances, pas de licence restrictive. C'est un prototype fonctionnel qui opère sur des fichiers individuels. Il ne gère pas les répertoires, n'a pas d'interface utilisateur, ne s'intègre avec aucun service. En l'état, personne ne peut l'utiliser pour un vrai projet.

Mais BitTorrent aussi était un script Python au départ. Le premier client BitTorrent a été écrit par Cohen seul, présenté à CodeCon en 2002, et a mis deux ans à transformer l'industrie. La distance entre un prototype et une disruption est souvent plus courte qu'on ne le pense, quand le prototype résout le bon problème.

Le domaine public est un choix délibéré. Cohen ne propose pas une alternative à Git : il propose un **fondement** sur lequel d'autres peuvent construire. C'est une invitation, pas un produit. Et l'invitation arrive dans un environnement où les constructeurs sont déjà à l'oeuvre.

**Jujutsu (jj)**, développé chez Google, repense le working copy comme un commit permanent : chaque modification est automatiquement un commit, éliminant le rituel `git add` / `git commit` qui consume un temps mental disproportionné. Les change-IDs restent stables à travers les rebases, résolvant un problème qui génère des erreurs quotidiennes chez les utilisateurs de Git.

**Sapling**, développé chez Meta pour gérer des monorepos de plusieurs millions de fichiers, introduit les stacked commits : des séries de modifications empilées qui peuvent être révisées et modifiées indépendamment, transformant selon ses créateurs "a frustrating hack into an everyday pattern."

**Pijul**, développé indépendamment en Rust, est le plus proche de Manyana sur le plan théorique : il est patch-based et commutatif. Mais son écosystème reste immature : un fil de discussion sur le forum de Pijul comparant les deux approches note que Manyana est "much less mature : barely a Python script." L'observation est factuellement correcte et complètement à côté du point.

La question n'est pas si Manyana va remplacer Git. La question est si la **convergence** de ces alternatives : Google, Meta, un chercheur indépendant en Rust, et maintenant l'inventeur de BitTorrent : signale que le coût caché de Git a atteint un seuil où l'infrastructure commence à se fissurer.

La stratégie pragmatique de 2025-2026 le confirme : les équipes pilotent Jujutsu ou Sapling **localement**, tout en gardant les serveurs Git. L'adoption se fait par infiltration, pas par migration. Et Manyana, avec sa commutativité formellement prouvée et son domaine public, fournit la base théorique qui manquait à cette infiltration.

---

## Le paradoxe Git : trop gros pour tomber, trop cassé pour rester

L'histoire de l'informatique est pavée de technologies "too big to fail" qui ont fini par être remplacées. CVS a dominé le contrôle de version pendant 15 ans avant que Subversion ne le supplante. Subversion a dominé 10 ans avant que Git ne le supplante. À chaque transition, le même pattern : l'ancien système était "good enough" pour la majorité, un petit nombre de pionniers a adopté l'alternative, et un point de bascule a fait basculer la masse.

Le point de bascule, dans chaque cas, n'a pas été un argument technique. C'a été un événement social. Pour Git, c'était GitHub (2008), pas Git lui-même, mais la plateforme qui rendait Git accessible. Pour Subversion, c'était le succès de Linux et la démonstration que les projets distribués pouvaient fonctionner à grande échelle.

Quel serait le point de bascule pour un successeur de Git ? Les candidats les plus plausibles :

**L'adoption par un cloud provider.** Si GitHub, GitLab ou AWS intègre nativement un backend CRDT qui comprend le protocole Git mais ajoute des merges sans conflit, l'adoption serait transparente : les développeurs continueraient d'utiliser `git push` et `git pull` tout en bénéficiant d'un système fondamentalement différent sous le capot.

**Un incident de sécurité lié aux merges.** Les conflits de merge mal résolus sont une source documentée de vulnérabilités. Le jour où un merge conflict mal résolu produira un CVE critique : un OpenSSL, un Log4j, l'argument "good enough" s'effondrera.

**L'échelle.** Les monorepos de Google (milliards de fichiers) et Meta (centaines de millions) ont déjà quitté Git pour des outils internes. Quand ces outils seront disponibles en open source : Jujutsu et Sapling le sont déjà, la pression sur Git viendra du haut.

Cohen a déjà résolu un cold start. BitTorrent est passé de "script Python d'un inconnu" à "un tiers du trafic Internet" en moins de 5 ans. Le mécanisme était le même que celui qu'il propose pour Manyana : le système est meilleur quand il est décentralisé. Chaque nouvel utilisateur rend le réseau plus performant. La commutativité n'est pas seulement une propriété mathématique, c'est une propriété de réseau.

---

## Ce que Manyana dit de l'ingénierie

Il y a quelque chose de frappant dans le fait qu'un des architectes les plus influents de l'infrastructure Internet revienne, à 50 ans, aux fondamentaux. 470 lignes de Python. Domaine public. Opère sur des fichiers individuels. Pas de startup, pas de levée de fonds, pas de pitch deck.

C'est l'anti-thèse du cycle actuel de l'industrie tech, où l'infrastructure est de plus en plus consolidée dans les mains de quelques plateformes, où les outils de développement sont vendus comme des services cloud, et où la valeur est extraite par l'ajout de couches au-dessus d'une fondation qui ne change jamais.

Cohen fait le contraire : il touche à la fondation elle-même. Il ne construit pas un outil au-dessus de Git, il propose une alternative aux hypothèses fondamentales sur lesquelles Git repose. L'historique n'est pas une séquence de snapshots, c'est un tissu. Les conflits ne sont pas des erreurs, ce sont des informations. Les merges ne sont pas des opérations risquées, ce sont des opérations mathématiquement garanties.

Les vrais problèmes d'infrastructure sont invisibles. Ils ne se présentent pas comme des bugs, ils se présentent comme le coût normal de faire les choses. 10% du temps développeur perdu en résolution de conflits ? C'est "normal." Des bugs introduits par des merges mal résolus ? C'est "inévitable." Un système où l'ordre des opérations change le résultat ? C'est "comme ça que Git marche."

"Good enough" calcifie. Le coût s'accumule silencieusement, invisible dans les métriques parce qu'il n'y a pas de métrique pour "temps perdu à cause d'une architecture sous-optimale." Et un jour, quelqu'un regarde le problème avec des yeux neufs et dit : "Two states go in, one state comes out, and it's always correct." Et on se demande pourquoi ce n'a pas toujours été comme ça.

Manyana ne remplacera peut-être jamais Git. Mais l'idée que les merges peuvent ne jamais échouer, cette idée est désormais dans le monde. Et les idées, contrairement aux scripts Python de 470 lignes, ont tendance à persister.

---

*Sources : bramcohen.com (Manyana, How To Do a Local Undo, How To Merge a Single Line of Code, The State of Merging Technology), Wikipedia, debugg.ai, discourse.pijul.org. Données : 87% de devs avec merge conflicts et impact sur les bugs (études citées via debugg.ai/zignuts.com).*
