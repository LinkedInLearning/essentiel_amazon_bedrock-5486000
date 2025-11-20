# L'essentiel d'Amazon Bedrock

Ce dossier (repository) est lié au cours `L'essentiel d'Amazon Bedrock`. Le cours entier est disponible sur [LinkedIn Learning][lil-course-url].

![Nom final de la formation][lil-thumbnail-url] 

Que vous soyez débutant en cloud, passionné d’IA ou développeur confirmé, cette formation vous guide pas à pas dans l’exploration d’Amazon Bedrock et de son riche catalogue de modèles (Claude, Llama, Mistral, Titan, etc.). Vous apprendrez à tester rapidement vos prompts, appeler les API en Python, orchestrer vos flux avec LangChain, concevoir une approche RAG pour des réponses contextualisées et créer une interface Streamlit pour vos démonstrations. Animée par Jean Sébastien Mambou, docteur en informatique et architecte cloud, cette formation vous permet de transformer vos idées en mini-applications GenAI fonctionnelles, tout en intégrant bonnes pratiques de sécurité, gestion des coûts et nettoyage des ressources.

## Instructions

Le dossier (Repository) contient différents dossiers correspondant aux chapitres avec exercices.
Dans chaque dossier de chapitre, vous trouverez une série de sous-dossiers associés aux vidéos.
À l’intérieur de chacun de ces sous-dossiers, un fichier README.md est présent et fournit les instructions nécessaires pour réaliser l’exercice.

### la structure

```
.
├── 01_Verifier l'acces a AWS via python3
│   ├── README.md
│   ├── solutions
│   │   └── test_identity.py
│   └── test_identity.py
├── 02_Comparer des prompts
│   ├── compare_prompts.py
│   ├── README.md
│   └── solutions
│       └── compare_prompts.py
├── 03_introduction_a_LangChain
│   ├── chain_example.py
│   └── README.md
├── 04_Flux de travail LangChain simple
│   └── from_playground.py
└── 05_Defi_ Premier appel Claude via boto3
    ├── README.md
    ├── solutions
    │   └── tests.py
    └── translate.py
```


## Installation

### Créer un environnement Python et installer les dépendances

Ce guide explique comment mettre en place un environnement Python isolé et installer les bibliothèques nécessaires à partir du fichier `requirements.txt`.

### Étapes

1. Vérifier l’installation de Python :  
   ```bash
   python --version
   # ou
   python3 --version
   ```

2. Créer un environnement virtuel :  

   ```bash
   python -m venv venv
   ```

3. Activer l’environnement virtuel :  
   - **Windows (PowerShell)** : `venv\Scripts\Activate.ps1`  
   - **Windows (CMD)** : `venv\Scripts\activate.bat`  
   - **macOS / Linux** : `source venv/bin/activate`

4. Installer les dépendances :  

   ```bash
   pip install -r requirements.txt
   ```

5. Vérifier l’installation :  

   ```bash
   pip list
   ```

6. Désactiver l’environnement virtuel (si besoin) :  

   ```bash
   deactivate
   ```

Vous disposez maintenant d’un environnement Python isolé avec toutes les dépendances nécessaires pour exécuter le projet.


### Formateur

**Sébastien Mambou** 

Retrouvez mes autres formations sur [LinkedIn Learning][lil-URL-trainer].

[0]: # (Replace these placeholder URLs with actual course URLs)
[lil-course-url]: https://www.linkedin.com
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQG0eDHsyOSqTA/learning-public-crop_675_1200/B4EZVdqqdwHUAY-/0/1741033220778?e=2147483647&v=beta&t=FxUDo6FA8W8CiFROwqfZKL_mzQhYx9loYLfjN-LNjgA
[lil-URL-trainer]: https://www.linkedin.com/learning/instructors/sebastien-mambou

[1]: # (End of FR-Instruction ###############################################################################################)
