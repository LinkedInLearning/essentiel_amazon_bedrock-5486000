# 01 — Configuration & Vérification AWS

## Objectifs
- Vérifier l'identité avec **STS**.
- Tester un appel **Bedrock Runtime** (`converse`).

## Exercices
1. Créez un profil CLI `bedrock-course` et exportez `AWS_PROFILE`.
2. Restreignez l'IAM Policy au strict nécessaire (ex: `bedrock:InvokeModel`, `bedrock:Converse`).
3. Testez `converse` avec un simple prompt.

## Solution
Voir `solutions/test_identity.py`.
