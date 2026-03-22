# GrapheneOS dit non : quand un OS refuse de vérifier votre âge

*Article #4 — Strate, 22 mars 2026*

---

## "If GrapheneOS devices can't be sold in a region, so be it"

Le 20 mars 2026, GrapheneOS a publié un statement sur Mastodon : "GrapheneOS will remain usable by anyone around the world without requiring personal information, identification or an account." Si les lois de vérification d'âge rendent ses appareils invendables dans certaines régions — tant pis.

En temps normal, un OS mobile qui refuse de se conformer à une loi, c'est un suicide commercial. Sauf que GrapheneOS n'est pas un OS normal. Et les lois en question ne sont pas normales non plus.

L'histoire a explosé sur deux plateformes simultanément : 3 300+ votes sur Reddit r/technology, 170+ points sur Hacker News. Mais les réactions divergent radicalement. Reddit vote massivement et discute peu (ratio 0.05). HN discute intensément (ratio 0.49). Le grand public applaudit un geste de résistance. Les techniciens débattent de sa faisabilité.

Les deux ont raison. Et les deux passent à côté de l'essentiel.

---

## Deux lois, un même mécanisme

### Le Brésil : depuis cinq jours

La Lei 15.211 — le "Digital ECA" brésilien — est entrée en application le 17 mars 2026. Cinq jours avant le statement de GrapheneOS. Ce n'est pas une coïncidence.

La loi s'applique à tout service numérique "susceptible d'être accédé" par des mineurs au Brésil. En pratique : tout. Les méthodes de vérification acceptées incluent le CPF (identifiant fiscal brésilien, qui retourne la date de naissance), la biométrie faciale avec détection de vivacité, et le téléchargement de documents d'identité. L'auto-déclaration — cocher "j'ai plus de 18 ans" — est explicitement interdite.

Les amendes : jusqu'à 50 millions de reais (~9,5 millions de dollars) ou 10% du chiffre d'affaires brésilien. Par infraction.

Le détail qui a fait réagir la communauté open-source : l'ANPD (l'autorité brésilienne de protection des données) a placé les **distributions Linux** sur sa liste de surveillance, aux côtés d'Epic Games et Valve. Pour la première fois, un régulateur traite un système d'exploitation libre comme un vecteur de non-conformité.

### La Californie : dans neuf mois

L'AB-1043 — le "Digital Age Assurance Act" californien — a été signé par le gouverneur Newsom le 13 octobre 2025. Il entre en vigueur le 1er janvier 2027.

Le mécanisme est plus subtil que le brésilien. Pas de biométrie, pas de documents d'identité. À la place : un **signal d'âge chiffré intégré au niveau de l'OS**. Lors de la configuration d'un appareil, l'utilisateur déclare sa date de naissance. Le système encode un bracket d'âge — "moins de 13 ans", "13-15", "16-17", "18+" — dans un signal cryptographique exposé aux applications via une API. La date de naissance elle-même ne quitte jamais l'appareil.

C'est de la vérification d'âge "privacy-preserving" — un terme que le texte de loi utilise explicitement. La donnée sensible (la date de naissance) reste locale. Seul le bracket est transmis. Aucun document, aucune biométrie, aucun tiers de confiance.

Le problème : recevoir ce signal établit ce que la loi appelle "actual knowledge" de l'âge de l'utilisateur. Pour une application, cela déclenche automatiquement les obligations de conformité COPPA et CCPA. Sanctions : jusqu'à 7 500 dollars par enfant affecté en cas de violation intentionnelle.

L'obligation est imposée aux **fournisseurs d'OS**. Apple, Google, Microsoft, Samsung — et tout projet qui distribue un système d'exploitation mobile.

Y compris GrapheneOS.

---

## Le paradoxe Motorola

Le 2 mars 2026, au Mobile World Congress de Barcelone, Motorola et GrapheneOS ont annoncé un partenariat officiel. Après des années d'exclusivité sur les Google Pixel, GrapheneOS arrive sur du hardware Motorola. Premier appareil prévu pour 2027. Le marché cible : les entreprises et le secteur de la sécurité.

C'était il y a trois semaines.

La contradiction est structurelle. Motorola est un fabricant commercial qui vend des appareils dans des juridictions qui exigent la vérification d'âge — le Brésil et la Californie sont deux de ses marchés majeurs. GrapheneOS refuse catégoriquement d'implémenter une quelconque collecte de données personnelles au niveau de l'OS.

Si l'AB-1043 entre en vigueur en janvier 2027 — la même année que le premier téléphone Motorola/GrapheneOS — le partenariat contient une contradiction irrésolue dès le jour du lancement. Motorola ne peut pas vendre un appareil non conforme en Californie. GrapheneOS ne mettra pas de signal d'âge dans son OS.

Deux scénarios plausibles : un fork régional (Android standard pour les marchés réglementés, GrapheneOS pour le reste), ou une restriction géographique pure. Dans les deux cas, le partenariat est plus fragile qu'il n'en a l'air.

Le projet GrapheneOS, sur son forum, est explicite : "We have no more obligation to filter the internet for California than for China." Si les appareils ne peuvent pas être vendus, ils déménageront leurs serveurs.

---

## Les Crypto Wars, version 2026

En 1991, Phil Zimmermann a publié PGP — Pretty Good Privacy — un logiciel de chiffrement assez puissant pour résister aux gouvernements. Le Department of Justice a ouvert une enquête criminelle qui a duré trois ans, pour "exportation d'armes" : à l'époque, la cryptographie forte était classée comme munition au titre de l'ITAR.

Le parallèle avec 2026 n'est pas métaphorique. C'est structurel.

Dans les deux cas, un gouvernement exige qu'une technologie de protection de la vie privée intègre un mécanisme de surveillance ou de conformité. Dans les deux cas, l'argument avancé est la protection du public (sécurité nationale alors, sécurité des mineurs maintenant). Dans les deux cas, des projets open-source refusent au nom d'un principe : toute porte dérobée, même bien intentionnée, affaiblit la sécurité de tous.

La résolution des Crypto Wars a pris une décennie. L'arrêt Bernstein v. US (1999) a établi que le code source est un discours protégé par le Premier Amendement. Les contrôles à l'export ont été assouplis. Le chiffrement fort est devenu la norme.

Mais les Crypto Wars avaient un avantage structurel que la bataille actuelle n'a pas. Le chiffrement était binaire — soit il est fort, soit il ne l'est pas. Le signal d'âge californien est **gradué**. Il ne casse rien. Il ajoute une couche. Il est opt-in pour l'utilisateur (en théorie — la loi l'impose, mais la donnée reste locale). C'est précisément ce qui le rend plus difficile à combattre que le Clipper Chip.

L'argument de Zimmermann était simple : "Si la privacy est criminalisée, seuls les criminels auront de la privacy." L'argument contre l'AB-1043 est plus nuancé : "Ce n'est pas de la surveillance, mais ça crée l'infrastructure de la surveillance." Les projets comme DB48X et MidnightBSD, qui refusent déjà la conformité brésilienne, font le même pari que Zimmermann : le refus total, quelles que soient les conséquences commerciales.

---

## L'angle mort du "privacy-preserving"

La loi californienne a été saluée par certains analystes de la privacy comme un progrès par rapport aux approches texanes et de Louisiane, qui poussent les plateformes vers la collecte de passeports et de pièces d'identité. L'application Tea et Discord ont tous deux subi des fuites de données après avoir collecté des documents d'identité pour se conformer à ces lois. L'AB-1043 évite ce risque en gardant la donnée sur l'appareil.

Mais "privacy-preserving" ne signifie pas "sans conséquences."

Le signal d'âge crée un précédent technique : les OS mobiles comme couche de conformité réglementaire. Si le bracket d'âge peut être transmis aux applications, d'autres signaux pourraient suivre. Localisation. Nationalité. Identité vérifiée. La plomberie est la même.

La critique de Reason.org est mesurée mais directe : le signal devrait être **opt-in**, pas obligatoire. Un parent devrait pouvoir activer la vérification d'âge. Mais la loi rend le prompt obligatoire pour tous les utilisateurs, pas seulement les parents. Un adulte sans enfant qui configure un iPhone en Californie devra déclarer sa date de naissance, non pas parce qu'il y a un risque, mais parce que le système ne peut pas savoir qu'il n'y en a pas.

C'est le paradoxe de la vérification d'âge : pour savoir qui a besoin de protection, il faut d'abord collecter des données sur tout le monde.

---

## Ce que ça change pour vous

**Si vous utilisez Android :** Votre prochain téléphone, configuré en Californie après janvier 2027, vous demandera votre date de naissance. Si vous refusez, les applications pourront vous traiter comme un mineur par défaut — c'est l'interprétation la plus restrictive de la loi.

**Si vous développez une application :** L'API d'âge californienne sera un signal qu'il faudra intégrer. Recevoir le bracket d'âge d'un utilisateur vous impose des obligations légales que vous n'aviez pas avant. L'ignorance n'est plus une défense : le signal existe, ne pas le lire est un choix documentable.

**Si vous maintenez un projet open-source :** Le Brésil vous surveille peut-être. La loi s'applique à tout service "susceptible d'être accédé" par des mineurs brésiliens, sans distinction entre entreprise commerciale et projet bénévole. L'ANPD a déjà des distributions Linux dans son viseur. Le précédent juridique n'existe pas encore — mais le risque réglementaire, lui, est immédiat.

**Si vous dirigez une entreprise :** Les deux lois créent une pression convergente vers l'intégration de vérification d'âge au niveau OS. Le calendrier est serré : le Brésil est déjà en vigueur, la Californie dans neuf mois. Les entreprises qui vendent des appareils ou des applications dans ces marchés doivent commencer à planifier maintenant, pas en décembre.

GrapheneOS a choisi de refuser. C'est un luxe que seul un projet sans actionnaires, sans revenus publicitaires et sans obligation fiduciaire peut se permettre. Pour le reste de l'industrie, la question n'est pas de savoir s'il faut se conformer, mais comment le faire en minimisant les dommages collatéraux sur la privacy de tous les utilisateurs.

---

*Sources : [Tom's Hardware](https://www.tomshardware.com/software/operating-systems/grapheneos-refuses-to-comply-with-age-verification-laws), [GrapheneOS/Mastodon](https://grapheneos.social/@GrapheneOS/116261301913660830), [California Legislature AB-1043](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1043), [Troutman Privacy](https://www.troutmanprivacy.com/2025/10/analyzing-californias-digital-age-assurance-act/), [Reason.org](https://reason.org/commentary/examining-californias-digital-age-assurance-act/), [Didit — Brazil Digital ECA](https://didit.me/blog/brazil-digital-eca-age-verification/), [VerifyMy](https://verifymy.io/blog/brazil-digital-dca-age-verification-rules/), [Reclaim The Net](https://reclaimthenet.org/brazil-digital-eca-age-verification-law), [Android Authority — Motorola/GrapheneOS](https://www.androidauthority.com/grapheneos-motorola-partnership-announced-3645710/)*
