# Delve : 494 rapports SOC 2 identiques, $32M levés, zéro vérification — anatomie d'une fraude à la compliance industrielle

*Article #3 — Strate, 22 mars 2026*

---

## Quand un rapport d'audit ne vaut pas le PDF qui le contient

494 rapports d'audit SOC 2. 455 entreprises clientes. 99,8% de texte identique. Les mêmes erreurs grammaticales. Les mêmes valeurs de test — littéralement "sdf" et "dlkjf", du mashing de clavier copié-collé d'un rapport à l'autre. Et pas un seul régulateur ne s'en est aperçu pendant des mois.

Delve, une startup Y Combinator qui a levé 32 millions de dollars auprès d'Insight Partners pour "automatiser la compliance", n'a pas automatisé la compliance. Elle a automatisé l'APPARENCE de la compliance. Et la différence entre les deux est exactement ce qui fait que cet article n'est pas seulement une histoire de fraude — c'est une histoire sur ce qui arrive quand l'IA réduit à zéro le coût de production d'un signal de confiance.

---

## Les faits : ce que l'enquête a révélé

### La fuite

En décembre 2025, un Google Sheet accessible publiquement a exposé le pipeline de génération de rapports de Delve. Un enquêteur anonyme, sous le pseudonyme DeepDelver, a publié son analyse le 19 mars 2026 sur Substack : "Fake Compliance as a Service — Part I."

Les chiffres sont accablants :

- **494 rapports SOC 2** analysés, tous quasi-identiques
- **251 rapports Type 1**, **198 rapports Type 2**, **84 rapports ISO 27001** — trois types de certifications différents, même template
- **259 rapports Type 2** (les plus rigoureux, censés couvrir une période d'observation de 6 à 12 mois) déclarent **zéro incident de sécurité, zéro changement de personnel, zéro incident cyber** pendant la période d'observation. Pour 259 entreprises différentes. Simultanément.
- Les conclusions de l'auditeur indépendant (Section 1) et les procédures de test (Section 4) étaient **présentes dans les rapports brouillons AVANT que les clients n'aient fourni leur description d'entreprise, leurs diagrammes réseau ou leurs signatures**. L'auditeur avait conclu avant d'avoir quoi que ce soit à auditer.

### Les valeurs fantômes

Le détail le plus révélateur : des valeurs de test comme "sdf" et "dlkjf" — du keyboard mashing, le geste réflexe de quelqu'un qui remplit un champ obligatoire sans réfléchir — apparaissent **identiquement** dans des rapports de clients différents. Ce n'est pas de la standardisation. C'est de la duplication d'artefacts de production.

Quatre contrôles sont systématiquement marqués "non testables" dans les 259 rapports Type 2, avec la même justification : zéro incidents pendant la période d'observation. En audit, "non testable" signifie que le contrôle n'a pas pu être vérifié. Quand 259 entreprises différentes ont exactement le même résultat "non testable" pour les mêmes contrôles, ce n'est pas de la coïncidence. C'est un template.

### Le réseau d'auditeurs

Les rapports de Delve citent des "auditeurs américains indépendants." L'enquête de DeepDelver retrace ces auditeurs — Accorp, Glocert, DKPC — vers des sociétés de certification indiennes opérant via des adresses de domiciliation au Wyoming. Plus de 99% des audits étaient routés vers deux firmes : Accorp et Gradient. Aucune n'est accréditée par l'ANAB ou l'UKAS, les organismes de référence pour l'accréditation des auditeurs.

La description identique des fournisseurs cloud (AWS, GCP, Azure) dans des rapports de clients qui n'utilisent pas les mêmes infrastructures achève le tableau.

---

## Qui est Delve ?

Karun Kaushik (CEO) et Selin Kocalar (COO) se rencontrent en première année au MIT. Ils décrochent en deuxième année. Y Combinator 2024. Seed de 3,3 millions de dollars en janvier 2025. Series A de 32 millions menée par Insight Partners six mois plus tard. Forbes 30 Under 30.

La promesse : **"compliance en 10 heures."**

Pour comprendre l'audace de cette promesse, il faut comprendre ce qu'est un audit SOC 2 normal. Un audit Type 2 couvre une période d'observation de 6 à 12 mois pendant laquelle un auditeur vérifie que les contrôles de sécurité d'une entreprise fonctionnent effectivement. Le coût : 15 000 à 50 000 dollars. La durée : des mois. Delve promettait le même résultat en 10 heures. Le marché, visiblement, n'a pas trouvé cela suspect.

Le marché de l'automatisation SOC 2 pèse 1,3 milliard de dollars en 2026 — une croissance de 53% par rapport aux 850 millions de 2025. La course à la vitesse et au prix bas est structurelle. Terry O'Brien, directeur chez Schellman (un vrai cabinet d'audit), le résumait dans le Journal of Accountancy en février 2026 : *"You just know it's a template. You can compare any five of their reports, they're all exactly the same."* L'article était publié un mois AVANT le scandale Delve. Le problème était visible pour quiconque regardait.

---

## La réponse de Delve : cinq démentis, zéro réponse

Le 20 mars 2026, le jour même de la publication de l'enquête, Delve a publié un communiqué intitulé "Response to Misleading Claims." Cinq points :

1. **"Delve ne produit pas de rapports d'audit."** Delve est une plateforme d'automatisation. Les rapports sont émis par des auditeurs indépendants.
2. **"Nos auditeurs sont accrédités."** Les clients choisissent leurs auditeurs ou utilisent le réseau de Delve.
3. **"La similarité des templates est normale."** Les standards AICPA et ISO imposent une structure commune.
4. **"Les documents pré-remplis sont des brouillons."** Les clients sont responsables de les finaliser.
5. **"Nous avons 120+ intégrations automatisées."** Pas 14 comme l'allègue l'enquête.

Ce que la réponse NE fait PAS : expliquer pourquoi des valeurs de test identiques ("sdf", "dlkjf") apparaissent dans des rapports de clients différents. Expliquer pourquoi les conclusions de l'auditeur sont présentes AVANT la soumission des preuves. Expliquer pourquoi 259 entreprises sur 259 ont zéro incident de sécurité.

La similarité de template est normale. Les valeurs de test identiques ne le sont pas. La distinction est précisément ce que la réponse évite.

---

## 794 points, 286 commentaires : ce que la communauté technique a vu

Le thread Hacker News a atteint 794 points et 286 commentaires — un ratio commentaires/score de 0.36, caractéristique des stories qui déclenchent un vrai débat plutôt qu'un simple vote en passant.

Le commentaire le plus voté résume le consensus avec une précision chirurgicale : *"80% of Compliance has always been a performative box checking exercise. They delivered the product... make the box checking faster."* Le marché n'est pas choqué que Delve ait triché. Il est choqué que Delve ait été PRISE.

Un insider anonyme a décrit son expérience : son entreprise a utilisé Delve en sachant que les rapports étaient des templates. Ils n'avaient pas la bande passante pour réécrire les politiques. Quand des clients ont demandé des preuves réelles, ils ont dû se précipiter vers un vrai audit.

Un professionnel de la sécurité a rapporté avoir rencontré un vendeur majeur dont la certification prestigieuse masquait une implémentation cryptographique **volontairement incorrecte** pour permettre le tracking des utilisateurs.

Le fil révèle un secret de Polichinelle : les professionnels de la compliance savent quels cabinets tamponneront n'importe quoi pour un chèque. Delve n'a pas créé le problème — elle l'a industrialisé.

---

## Le coût-comme-signal : pourquoi cette fraude était inévitable

L'analyse superficielle est : Delve a triché, c'est mal, les régulateurs auraient dû voir. L'analyse intéressante est : pourquoi est-ce que ça a marché aussi longtemps ?

### Le mécanisme

Un rapport SOC 2 est un **credence good** — un bien dont la qualité ne peut pas être évaluée par l'acheteur, ni avant ni après l'achat. Vous ne pouvez pas lire un rapport SOC 2 et déterminer s'il reflète un vrai audit ou un template. Vous ne pouvez pas non plus vérifier après coup, parce que la vérification nécessiterait exactement le même type d'expertise que l'audit lui-même.

Historiquement, le COÛT du rapport servait de signal de qualité. Un audit SOC 2 à 50 000 dollars implique des mois de travail humain. Un auditeur qui facture 50 000 dollars a une réputation à protéger. Le prix n'est pas seulement le coût du travail — c'est un **signal que le travail a été fait**.

Quand l'IA et l'automatisation réduisent le coût de production d'un credence good à quasi-zéro, le signal s'effondre. "Compliance en 10 heures" n'est pas seulement moins cher — c'est un prix qui **ne peut pas** refléter un vrai audit. Mais les acheteurs ne le savent pas, parce que c'est un credence good. Et les intermédiaires (auditeurs, plateformes) n'ont aucun intérêt à le signaler, parce que le volume compense la marge.

Le résultat : le rapport SOC 2 passe de signal de sécurité à **signal de compliance rituelle**. Sa valeur n'est pas dans son contenu (personne ne le lit) mais dans son **existence** (tout le monde l'exige). C'est la trajectoire classique : norme → signal → rituel → inversion. Delve a accéléré le cycle jusqu'au rituel. trustcompliance.xyz force l'inversion : désormais, un rapport Delve est un signal NÉGATIF — son absence est plus informative que sa présence.

### Le précédent concurrent-critique

trustcompliance.xyz, le site qui a indexé les 533 rapports fuités, suit un pattern devenu identifiable. Composio (concurrent d'OpenClaw) avait publié un exposé sécuritaire sur OpenClaw tout en vendant TrustClaw comme alternative. Ici, trustcompliance.xyz indexe les fuites de Delve — et le site, par son nom même, se positionne comme l'alternative de confiance.

Le pattern concurrent-critique : un acteur du marché investit dans l'exposition des failles d'un concurrent. L'exposé est factuellement solide (les données sont réelles), mais le mobile est commercial. Le résultat net est positif (l'information sort) mais le cadrage est biaisé (les failles du critique ne sont pas examinées).

Ce pattern est désormais reproductible. n=2 (OpenClaw/Composio en sécurité des agents, Delve/trustcompliance en compliance). Le signal d'alerte : quand l'exposé vient d'un concurrent, vérifiez ce que le concurrent vend.

---

## Les conséquences réelles

### Pour les 455 entreprises clientes

Les clients de Delve qui ont transmis ces rapports à leurs propres clients et partenaires font face à un problème en cascade :

- **HIPAA** : la conformité frauduleuse expose à des sanctions fédérales de 50 000 dollars par violation, jusqu'à 1,9 million par catégorie et par an. Dans les cas graves : prison.
- **RGPD** : l'Article 83 prévoit des amendes jusqu'à 4% du chiffre d'affaires mondial annuel.
- **Risque réputationnel** : chaque entreprise qui a affiché un badge SOC 2 de Delve doit maintenant expliquer à ses clients que la certification était potentiellement sans valeur.

Lovable, une plateforme de développement web IA, a été le premier client identifié à communiquer publiquement. Ils avaient migré vers Vanta avant le scandale et sont en cours de recertification ISO 27001 indépendante.

### Pour l'industrie de la compliance

Le Journal of Accountancy avait sonné l'alarme en février 2026 sur les promesses de "fast and easy" qui menacent la crédibilité du SOC. Jeff Cook y notait : *"a lackluster report can leave companies unaware of their actual gaps and deficiencies."* L'article identifiait le mécanisme exact (volumes élevés, petits cabinets, templates) sans nommer Delve spécifiquement.

L'AICPA n'a pas encore réagi officiellement. La SEC non plus. Le marché s'auto-régule — ce qui, comme le montrent ces 494 rapports, ne fonctionne pas.

### Ce que l'Europe fait différemment

L'EU AI Act offre un contre-modèle instructif. Les Articles 29-49 établissent un cadre de conformité qui rend structurellement impossible le scénario Delve :

- **Séparation obligatoire des rôles** : l'entité qui génère les preuves ne peut pas rédiger les conclusions de l'évaluateur ni contrôler les communications avec l'organisme de certification.
- **Accréditation des évaluateurs** : les organismes notifiés doivent démontrer leur indépendance, leur compétence technique, et maintenir une assurance de responsabilité professionnelle. L'accréditation peut être retirée — la seule sanction qui fonctionne quand la réputation seule ne suffit pas.
- **Vérification continue** : le système de management de la qualité (Article 17) exige des procédures opérationnelles continues, pas une documentation ponctuelle.
- **Sanctions** : jusqu'à 35 millions d'euros ou 7% du chiffre d'affaires annuel mondial (Article 99).

Le framework n'est pas encore testé en conditions réelles. Mais sa conception structurelle — séparation des rôles, sanctions disproportionnées, surveillance active — est exactement ce que le modèle SOC 2 n'a pas.

---

## La question que personne ne pose

Le marché de la compliance SOC 2 pèse 1,3 milliard de dollars. Il croît de 53% par an. Et il repose sur un modèle où :

1. L'entreprise choisit et paie son propre auditeur
2. L'auditeur s'auto-régule via des standards professionnels
3. Personne ne vérifie les rapports
4. La sanction en cas de fraude est la perte de réputation — pas la prison

C'est exactement le modèle des agences de notation avant 2008. Moody's et S&P attribuaient des AAA à des CDO toxiques parce que les banques les payaient pour le faire. Le conflit d'intérêt était structurel, pas individuel. Delve est le symptôme. Le modèle "l'audité paie l'auditeur" est la maladie.

La question n'est pas "comment empêcher le prochain Delve." Des centaines de startups de compliance offrent des promesses similaires. La question est : **quand le coût de production d'un signal de confiance tombe à zéro, que reste-t-il comme signal ?**

La réponse, probablement, est le monitoring continu. Pas un rapport annuel que personne ne lit, mais une vérification en temps réel, automatisée, que les contrôles fonctionnent effectivement. Le SOC 2 tel qu'il existe est un artefact d'une époque où vérifier était cher. L'IA a rendu la production du document gratuite. Il faudra aussi qu'elle rende la vérification gratuite — sinon, le gap entre production et vérification sera exploité par le prochain Delve.

---

*Sources : DeepDelver (Substack, 19 mars 2026), trustcompliance.xyz, Delve.co (Response to Misleading Claims, 20 mars 2026), Journal of Accountancy (février 2026), ComplianceHub Wiki, Systima AI (analyse EU AI Act), byteiota.com, Hacker News (thread 47444319, 794 pts / 286 commentaires).*

*Conflit d'intérêt déclaré : trustcompliance.xyz, qui a indexé les rapports fuités, est possiblement un concurrent de Delve. L'exposé de DeepDelver est factuellement documenté mais son auteur est anonyme. Delve a publié un démenti que cet article cite et analyse.*
