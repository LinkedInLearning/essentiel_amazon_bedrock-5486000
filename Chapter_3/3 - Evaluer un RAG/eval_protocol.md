## Protocole d'évaluation (exemple)
1. Définir un jeu de questions de référence (golden set).
2. Fournir des *expected facts* (faits attendus) et sources attendues par question.
3. Lancer le pipeline RAG et enregistrer:
   - Réponse générée
   - Passages/citations utilisés
   - Traces (latence, tokens)
4. Calculer les métriques :
   - Groundedness (recouvrement avec expected facts)
   - Hallucination rate (faits non supportés)
   - Qualité des citations (précision/rappel des sources)
   - CSAT (feedback utilisateur)
5. Suivi longitudinal dans un journal versionné.
