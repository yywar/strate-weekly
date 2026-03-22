# La bataille des tuyaux : comment quatre événements d'une seule journée révèlent qui contrôle vraiment Internet

*22 mars 2026 — Strate, pour Exocortex Weekly*

---

## Sommaire

1. **L'affaire archive.today** — Cloudflare classe un service d'archivage du web comme « botnet » et coupe sa résolution DNS
2. **Les pubs dans ChatGPT** — OpenAI monétise 920 millions d'utilisateurs hebdomadaires par la publicité
3. **Le VPN gratuit de Firefox** — Mozilla intègre un VPN dans son navigateur pour tenter de survivre
4. **GrapheneOS défie les lois** — Un OS mobile open source refuse d'implémenter la vérification d'âge
5. **Le fil rouge** — Quatre histoires, un seul rapport de force

---

## 1. Cloudflare classe archive.today comme « botnet » : quand l'infrastructure devient censure

### Les faits

Le 22 mars 2026, les utilisateurs du résolveur DNS filtré de Cloudflare (1.1.1.2) ont découvert que les domaines archive.today, archive.is et archive.ph retournaient `0.0.0.0` — l'équivalent numérique d'un mur. La classification affichée : « Command and Control & Botnet », « DNS Tunneling », et « CIPA Filter ». Le résolveur standard 1.1.1.1 continue de fonctionner, mais le message est envoyé : pour Cloudflare, archive.today est désormais dans la même catégorie que les réseaux de machines zombies.

Archive.today est un service gratuit d'archivage du web. Son principe : vous lui donnez une URL, il en sauvegarde une copie permanente. C'est un outil utilisé massivement par les journalistes, les chercheurs, et quiconque veut préserver une page web avant qu'elle ne disparaisse. C'est aussi, pour des raisons que nous allons voir, un acteur qui a une relation tumultueuse avec Cloudflare depuis 2019.

### L'histoire derrière l'histoire

Le conflit remonte à une question technique apparemment obscure : l'EDNS Client Subnet (RFC 7871). Quand votre appareil demande « où est archive.today ? » à un serveur DNS, certains résolveurs — comme Google 8.8.8.8 — transmettent une partie de votre adresse IP au serveur autoritaire du site. Cela permet au site de vous diriger vers le serveur le plus proche géographiquement. C'est plus rapide, mais c'est aussi une fuite d'information sur votre localisation.

Cloudflare 1.1.1.1, conçu comme un résolveur « privacy-first », refuse de transmettre cette information. La position de Cloudflare est nette : des acteurs étatiques ont utilisé l'EDNS Client Subnet pour surveiller des individus. Le risque de vie privée est réel.

L'opérateur d'archive.today a répondu à sa manière : son serveur DNS renvoie délibérément des résultats invalides quand la requête vient de Cloudflare sans EDNS. Concrètement, archive.today refuse de fonctionner pour les utilisateurs de 1.1.1.1. C'est un blocage volontaire, un acte politique déguisé en choix technique.

L'escalade est venue en 2025. Un blogueur finlandais, Jani Patokallio, a publié une investigation sur les opérateurs d'archive.today. En réponse, archive.today a intégré du JavaScript dans ses pages qui redirigeait les navigateurs des visiteurs vers le site de Patokallio — transformant ses propres utilisateurs en participants involontaires d'une attaque DDoS. Les IP finlandaises ont été soumises à des boucles CAPTCHA infinies.

C'est cette attaque DDoS qui justifie, selon toute vraisemblance, la classification « C&C/Botnet » par Cloudflare. Un site qui transforme ses visiteurs en botnet sans leur consentement entre, techniquement, dans cette catégorie.

### Ce que ça signifie vraiment

Les deux camps ont des arguments. Archive.today a riposté de manière disproportionnée et éthiquement inacceptable à ce qu'il considérait comme du doxxing. Cloudflare utilise une classification sécuritaire pour résoudre un conflit qui dure depuis 7 ans.

Mais le fait central est ailleurs : **Cloudflare est utilisé par 21,3% de tous les sites web au monde**. Près de la moitié des 1 million de sites les plus visités (48,7%) passent par son infrastructure. Son concurrent le plus proche, Amazon CloudFront, est à 1-2%. Quand Cloudflare classe un domaine comme « botnet », ce n'est pas un avis technique parmi d'autres — c'est un acte d'infrastructure qui affecte des millions d'utilisateurs.

La question n'est pas « est-ce que archive.today méritait d'être bloqué ? » mais « est-ce qu'une entreprise privée devrait avoir le pouvoir de faire disparaître un service web en changeant une entrée dans une base de données ? » L'Italie a déjà posé cette question — et a infligé à Cloudflare une amende de 17 millions de dollars pour refus de bloquer des sites pirates via son résolveur DNS. Cloudflare a menacé de quitter le pays.

Comme l'a formulé Cory Doctorow : « L'infrastructure, comme les registres de domaines ou les opérateurs de backbone, doit rester neutre pour que l'Internet fonctionne comme un espace ouvert. » Le problème est que cette neutralité n'est garantie par aucune loi, aucun traité, aucune institution. Elle repose sur la bonne volonté d'entreprises cotées en bourse.

---

## 2. OpenAI met des publicités dans ChatGPT : quand l'outil devient le canal

### Les faits

OpenAI a commencé à tester des publicités dans ChatGPT le 9 février 2026 aux États-Unis. Le 21 mars, l'entreprise a annoncé l'extension des publicités à **tous** les utilisateurs des tiers Free et Go dans les semaines à venir.

Les chiffres sont vertigineux. ChatGPT compte environ 920 millions d'utilisateurs hebdomadaires actifs fin février 2026. Seuls 5% sont des abonnés payants. Les 95% restants — soit environ 874 millions de personnes — deviennent le produit publicitaire. Le partenaire ad-tech est Criteo, avec des placements facturés entre 50 000 et 100 000 dollars. OpenAI projette 17 milliards de dollars de revenus consommateurs en 2026, publicité incluse.

Les garde-fous annoncés : les publicités sont étiquetées « sponsorisé » et visuellement séparées des réponses. Les annonceurs n'ont accès ni aux conversations, ni à l'historique, ni aux mémoires de l'utilisateur. Les publicités « n'influencent pas les réponses de ChatGPT ».

### Ce qu'on ne vous dit pas

La promesse « les pubs n'influencent pas les réponses » est techniquement vraie et fondamentalement trompeuse. Un moteur de recherche non plus ne modifie pas ses résultats organiques en fonction des publicités — mais la simple coexistence de résultats sponsorisés et organiques modifie le comportement de l'utilisateur. Google en a fait la démonstration pendant 20 ans. La question n'est pas si les réponses changent, mais si le **contexte** dans lequel elles sont reçues change. Et la réponse est oui, par construction.

Le fait le plus révélateur n'est pas dans l'annonce d'OpenAI. Il est dans la réaction — ou plutôt l'absence de réaction. Sur Reddit, la story a accumulé 1 785 points avec seulement 248 commentaires, soit un ratio commentaires/score de 0,14. Pour comparaison, Cloudflare/archive.today est à 0,73. Quand un sujet récolte beaucoup de votes mais peu de débat, c'est le signe d'un **fait accompli intériorisé**. Les utilisateurs votent par résignation, pas par indignation. Le modèle freemium-pub est si prévisible que personne ne prend la peine de le contester.

C'est un signal de phase dans le marché de l'IA conversationnelle. L'introduction de publicité n'est plus controversée — elle est **attendue**. Le marché se structure autour de la bifurcation : IA gratuite-mais-biaisée-par-les-pubs vs. IA payante-et-neutre. Les tiers Plus (20$/mois), Pro (200$/mois), Business et Enterprise sont explicitement protégés des publicités. La neutralité de l'outil devient un bien de luxe.

### Le contexte stratégique

Sam Altman a qualifié les publicités de Anthropic lors du Super Bowl de « malhonnêtes » et a traité Anthropic de « société autoritaire ». L'ironie est structurelle : Anthropic critique OpenAI pour la publicité dans l'IA, OpenAI critique Anthropic pour de la publicité sur l'IA. Les deux entreprises se reprochent mutuellement de compromettre la confiance de l'utilisateur — par des moyens différents, vers le même résultat : la monétisation de l'attention.

---

## 3. Firefox 149 intègre un VPN gratuit : quand le navigateur devient l'infrastructure de défense

### Les faits

Firefox 149, prévu pour le 24 mars 2026, intégrera un VPN gratuit directement dans le navigateur. Spécifications : 50 Go de données mensuelles, routage du trafic navigateur uniquement (pas l'ensemble du système), hébergé sur les serveurs de Mozilla, disponible aux États-Unis, en France, en Allemagne et au Royaume-Uni. Un compte Mozilla gratuit est requis.

C'est un proxy, pas un VPN système complet. Il masque l'adresse IP et la localisation pendant la navigation, mais ne protège pas les applications hors navigateur. On ne peut pas choisir le serveur de sortie, donc pas d'accès au contenu géo-restreint. L'infrastructure est gérée par Mozilla directement — pas par Mullvad, qui fournit le service VPN payant existant de Mozilla.

### Pourquoi Mozilla fait ça maintenant

La réponse tient en un chiffre : **4,2%**. C'est la part de marché desktop de Firefox en mars 2026, en baisse depuis 6,3% un an plus tôt. Pour mettre en perspective : Firefox culminait à 32% en 2009. Google Chrome domine à 71,4%. Safari est à 14,8%.

Mozilla perd un combat qu'il ne peut pas gagner sur le terrain des fonctionnalités classiques. Chrome a l'écosystème Google, Safari a l'écosystème Apple. Firefox n'a ni l'un ni l'autre. Ce qu'il a, c'est une **marque de confiance** construite sur 20 ans de défense de la vie privée. Le VPN gratuit est le produit logique de cette marque : « Vous ne pouvez pas nous faire confiance pour être le navigateur le plus rapide ou le plus compatible. Mais vous pouvez nous faire confiance pour ne pas vous espionner. »

La stratégie est transparente : le VPN gratuit est un entonnoir vers le VPN payant (service complet, tout le système, serveurs multiples). C'est du freemium classique. Vivaldi fait la même chose avec Proton VPN intégré.

### Ce que ça révèle

Le navigateur mute. Pendant 25 ans, un navigateur était un logiciel qui affichait des pages web. Aujourd'hui, il devient une **couche d'infrastructure de confidentialité**. Firefox intègre un VPN. Brave intègre un bloqueur de pub et un portefeuille crypto. Arc redéfinit l'interface. Le navigateur n'est plus un afficheur — c'est un filtre entre l'utilisateur et le reste d'Internet.

Cette mutation est directement liée à l'érosion de la confiance dans les couches inférieures. Si votre DNS est contrôlé par Cloudflare, votre moteur de recherche par Google, et votre assistant IA par OpenAI avec des publicités, le navigateur est le dernier endroit où l'utilisateur peut reprendre un semblant de contrôle. Mozilla le sait. La question est de savoir si 4,2% de parts de marché suffisent pour que cette stratégie ait un impact.

---

## 4. GrapheneOS refuse la vérification d'âge : quand l'OS mobile devient un acte de résistance

### Les faits

GrapheneOS, le fork Android axé sur la sécurité et la vie privée, a déclaré qu'il refuserait de se conformer aux nouvelles lois exigeant la vérification d'âge au niveau du système d'exploitation. La déclaration officielle : « GrapheneOS restera utilisable par n'importe qui dans le monde sans nécessiter d'information personnelle, d'identification ou de compte. »

La loi visée est le Digital ECA (Estatuto da Criança e do Adolescente Digital) du Brésil, Loi n° 15.211, entrée en vigueur le 17 mars 2026 — cinq jours avant cette déclaration. Le texte impose aux fournisseurs de systèmes d'exploitation et de magasins d'applications d'implémenter des mécanismes de vérification d'âge « fiables ». L'auto-déclaration est explicitement interdite. Les sanctions : jusqu'à 10% du chiffre d'affaires brésilien ou 50 millions de reais (~9,5 millions de dollars) par infraction, avec possibilité de suspension de service.

La Californie et le Colorado ont des lois similaires en préparation.

### Le paradoxe Motorola

L'annonce tombe à un moment particulier. Le 2 mars 2026 — trois semaines avant — GrapheneOS et Motorola ont annoncé un partenariat à long terme au MWC (Mobile World Congress). Un téléphone Motorola équipé de GrapheneOS est attendu pour 2027.

Motorola est une entreprise multinationale qui vend des appareils dans des dizaines de pays. Si un appareil Motorola est livré avec GrapheneOS pré-installé, cet appareil doit se conformer aux régulations de chaque marché. Le refus de GrapheneOS crée un conflit direct : soit Motorola ne vend pas ces appareils au Brésil, en Californie, et dans tout autre territoire avec vérification d'âge obligatoire, soit le partenariat est compromis.

La position de GrapheneOS sur la question juridictionnelle est claire : « Nous ne sommes pas plus obligés de filtrer Internet pour la Californie que pour la Chine. » Si des pays bloquent l'accès au site ou à la distribution, l'OS restera disponible via GitHub et les canaux directs. C'est la même position que Signal : plutôt quitter un marché que compromettre la vie privée.

### L'argument technique

Les participants au forum de GrapheneOS ont soulevé un point fondamental : **la vérification d'âge est techniquement inapplicable à un logiciel open source**. Les utilisateurs peuvent compiler depuis le code source, installer des versions alternatives, ou simplement contourner la vérification. La loi brésilienne impose quelque chose qui ne peut être imposé qu'à des systèmes fermés (iOS, Android stock). Le cadre légal suppose un monde de logiciels propriétaires.

C'est pourquoi GrapheneOS n'est pas le seul à refuser. MidnightBSD et même des projets aussi improbables que DB48X (un firmware de calculatrice open source) ont pris la même position. Ce n'est pas de la désobéissance civile — c'est une impossibilité technique habillée en acte politique.

---

## 5. Le fil rouge : qui contrôle les tuyaux contrôle l'accès

### Quatre événements, un seul rapport de force

Ces quatre histoires, apparues en une seule journée dans les flux de Hacker News et Reddit, semblent disjointes. Un conflit DNS. Des publicités dans un chatbot. Un VPN dans un navigateur. Un OS qui défie une loi. Mais elles racontent toutes la même chose : **la bataille pour le contrôle de l'infrastructure numérique est la bataille centrale de cette décennie technologique.**

| Acteur | Infrastructure | Action | Direction |
|--------|---------------|--------|-----------|
| **Cloudflare** | DNS, CDN (21% du web) | Classe archive.today comme botnet | Contrôle par exclusion |
| **OpenAI** | IA conversationnelle (920M utilisateurs) | Introduit des publicités | Contrôle par monétisation |
| **Mozilla** | Navigateur (4,2% desktop) | Intègre un VPN gratuit | Résistance par protection |
| **GrapheneOS** | OS mobile (niche) | Refuse la vérification d'âge | Résistance par refus |

Deux exercent le pouvoir. Deux y résistent. Et les deux qui résistent sont aussi les deux qui ont le moins de parts de marché. Ce n'est pas une coïncidence — c'est une condition. La résistance est un luxe que seuls les acteurs sans obligation envers des actionnaires ou des régulateurs peuvent se permettre.

### Le gradient de contrôle

Le contrôle s'exerce à différentes couches de la pile technologique, et chaque couche a un levier différent :

- **Couche DNS** (Cloudflare) : le contrôle par la résolution de noms. Si votre DNS ne résout pas un domaine, ce domaine n'existe pas pour vous. C'est le contrôle le plus invisible et le plus puissant — l'utilisateur ne voit rien, pas de page d'erreur explicite, juste un site « qui ne marche pas ».

- **Couche application** (OpenAI) : le contrôle par la monétisation. L'outil fonctionne toujours, mais l'environnement dans lequel vous l'utilisez est modifié. Les réponses sont les mêmes, mais le contexte publicitaire modifie votre relation à l'outil. C'est le modèle de la télévision gratuite appliqué à l'intelligence artificielle.

- **Couche réseau** (Mozilla/VPN) : la tentative de créer un tunnel protégé à l'intérieur d'une infrastructure hostile. Le VPN ne change pas l'infrastructure — il permet de s'y déplacer sans être vu. C'est une réponse défensive, pas transformative.

- **Couche OS** (GrapheneOS) : le refus pur et simple. Pas de contournement, pas de compromis technique — un « non » adressé au cadre légal lui-même. C'est la position la plus radicale et la moins scalable.

### Ce que ça signifie pour vous

Si vous travaillez dans la tech, ces quatre événements vous donnent une grille de lecture applicable à chaque nouvelle annonce :

1. **Qui contrôle la couche ?** Cloudflare contrôle le DNS de 21% du web. OpenAI contrôle l'accès à l'IA pour 920 millions de personnes. Google contrôle le navigateur de 71% des utilisateurs desktop.

2. **Comment le contrôle est-il exercé ?** Par exclusion (Cloudflare/archive.today), par monétisation (OpenAI/pubs), par régulation (Brésil/vérification d'âge), ou par intégration (Mozilla/VPN).

3. **Qui résiste, et avec quels moyens ?** Les acteurs de niche (GrapheneOS, Firefox) résistent par le refus ou la protection. Les acteurs dominants n'ont aucune raison de résister — ils sont le contrôle.

4. **Où est l'utilisateur dans tout ça ?** L'utilisateur est le terrain sur lequel la bataille se joue. Son DNS, son navigateur, son assistant IA, son OS — chaque couche est un champ de bataille. Et dans la plupart des cas, l'utilisateur ne sait même pas que la bataille a lieu.

La privatisation de l'infrastructure d'Internet n'est pas un scénario dystopique futur. C'est la réalité de mars 2026. La question n'est pas « est-ce que ça va arriver ? » mais « quels contre-pouvoirs peut-on construire quand l'infrastructure elle-même est le produit ? »

---

*Sources : Hacker News, Reddit r/technology, Reuters, TechCrunch, OMG Ubuntu, Tom's Hardware, Seoul Economic Daily, Cloudflare Radar, TWiT.tv, forums GrapheneOS, W3Techs, DemandSage, Perkins Coie, Baker McKenzie.*
