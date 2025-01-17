# Projet_assurance

# Introduction

Ce projet a pour objectif de créer une solution d'estimation de primes d'assurance pour un assureur, **Assur'Aimant**, qui souhaite s'implanter aux États-Unis. En tant que consultants en **data** et **intelligence artificielle**, nous avons été sollicités pour développer un modèle permettant de prédire la prime d'assurance des souscripteurs en fonction de différentes caractéristiques démographiques. Nous devons également fournir une analyse exploratoire des données pour aider l'équipe dirigeante à mieux comprendre ses clients.

---

# Contexte

## Lancement de la Société

Vous venez de lancer votre société de conseil spécialisée en **data** et **IA**. Après avoir effectué un travail de prospection, vous avez décroché un premier appel d’offres avec **Assur'Aimant**, un assureur français. Cette entreprise veut automatiser l’estimation des primes d’assurance pour ses clients aux États-Unis, un marché qui lui est encore inconnu.

## Mission

La mission consiste à :

1. **Réaliser une étude exploratoire des données** : comprendre les relations entre les variables et décrire les caractéristiques principales du jeu de données.
2. **Construire un modèle de machine learning** pour prédire la prime d’assurance à partir des données démographiques des souscripteurs.

## Collecte des Données

### Variables disponibles

Les données sont constituées des éléments suivants :

- **BMI (Indice de Masse Corporelle)** : Rapport entre la taille et le poids. Idéalement, un BMI compris entre 18.5 et 24.9 est considéré comme sain.
- **Sex (Sexe)** : Genre de la personne (homme ou femme).
- **Age (Âge)** : Âge du souscripteur principal.
- **Children (Nombre d’enfants à charge)** : Nombre d’enfants couverts par l’assurance.
- **Smoker (Fumeur)** : Indicateur si la personne est fumeuse ou non.
- **Region (Région)** : Zone résidentielle aux États-Unis (Nord-Est, Sud-Est, Sud-Ouest, Nord-Ouest).
- **Charges (Prime d’assurance)** : La prime d'assurance que l'assuré doit payer. Cela constitue la cible à prédire.

## Objectifs

### 1. Analyse Exploratoire des Données (EDA)

L'objectif est de réaliser une analyse des données pour identifier des tendances et des relations importantes. Voici les principales étapes :

- Inspection des données manquantes.
- Analyse des distributions de chaque variable.
- Visualisation des corrélations entre les variables.
- Identification des éventuelles anomalies ou erreurs dans les données.

### 2. Construction d'un Modèle de Machine Learning

Nous allons créer un modèle prédictif pour estimer la prime d'assurance (variable cible **Charges**) en fonction des variables d’entrée (**BMI**, **Sexe**, **Âge**, **Nombre d’enfants à charge**, **Fumeur**, **Région**). Les étapes suivantes seront suivies :

- **Prétraitement des données** : gestion des valeurs manquantes, encodage des variables catégorielles (par exemple, Sexe, Smoker, Region), normalisation des données.
- **Modélisation** : utilisation de modèles de régression (par exemple, Régression Linéaire, Arbres de Décision, Forêts Aléatoires, ou Réseaux de Neurones).

## Résultats Attendus

L'objectif final de ce projet est d'avoir un modèle de machine learning capable de prédire avec précision la prime d’assurance des clients d'**Assur'Aimant**. Ce modèle devra être intégré dans une solution opérationnelle pour automatiser l’estimation des primes, ce qui permettra de réduire les coûts et d'améliorer l'efficacité du processus d’estimation.
