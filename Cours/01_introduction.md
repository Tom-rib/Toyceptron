# 01 - Introduction

> *"What I cannot create, I do not understand"* — Richard Feynman

---

## 🎯 Objectif du projet

L'objectif de ce projet est de **démystifier et comprendre les principes d'un réseau de neurones** en le construisant de zéro, sans aucune bibliothèque externe.

Et quelle meilleure façon de comprendre qu'en **faisant** ?

---

## 🧠 Qu'est-ce qu'un perceptron multi-couches ?

Un **perceptron multi-couches** (ou MLP - Multi-Layer Perceptron) est un modèle de **réseau de neurones artificiels** composé de :
- Une **couche d'entrée** (les données brutes)
- Une ou plusieurs **couches cachées** (transformations intermédiaires)
- Une **couche de sortie** (le résultat final)

C'est la brique de base du Deep Learning moderne.

### Schéma simplifié
```
Entrée          Couche cachée       Sortie
  [x1]              [n1]              [y]
  [x2]     →        [n2]       →    
  [x3]              [n3]              
```

Chaque cercle est un **neurone** qui effectue un calcul simple.

---

## 📦 Ce que tu vas construire

Un réseau de neurones en Python qui :
1. Prend un **vecteur en entrée** (liste de nombres)
2. Le fait passer à travers plusieurs **couches de neurones**
3. Retourne une **sortie finale** (un ou plusieurs nombres)

**Important :** Pas d'entraînement dans ce projet ! On se concentre uniquement sur la **structure** et la **propagation avant** (forward pass).

---

## 🛠️ Les 3 classes à implémenter

Tu devras coder **3 classes Python** :

### 1️⃣ Neuron (neuron.py)
Une unité de calcul élémentaire qui :
- Stocke des **poids** (weights) et un **biais** (bias)
- Calcule une **sortie** à partir d'entrées

### 2️⃣ Layer (layer.py)
Une couche qui contient plusieurs neurones et :
- Applique tous ses neurones à un vecteur d'entrée
- Retourne un vecteur de sortie

### 3️⃣ Network (network.py)
Le réseau complet qui :
- Empile plusieurs couches
- Fait circuler les données de l'entrée à la sortie
- Applique des fonctions d'activation

---

## 🎓 Compétences développées

Ce projet te permettra de maîtriser :
- ✅ **Python** : Programmation Orientée Objet (POO)
- ✅ **Structures de données** : manipulation de listes, vecteurs
- ✅ **Machine Learning** : comprendre comment fonctionne un réseau de neurones
- ✅ **Documentation** : écrire du code lisible et bien commenté

---

## 📜 Contraintes du projet

### ✅ Autorisé
- Python (version 3.8+)
- Listes Python comme vecteurs
- Module `random` pour l'initialisation aléatoire
- Module `math` pour les fonctions mathématiques (exp, max, etc.)

### ❌ Interdit
- `numpy`, `pytorch`, `tensorflow`, `sklearn`
- Toute bibliothèque de machine learning
- Utilisation de réseaux pré-entraînés

**Pourquoi ?** Pour **vraiment** comprendre ce qui se passe sous le capot !

---

## 🚀 Résultat attendu

À la fin du projet, ton réseau devra :
- Être **initialisé** avec des paramètres aléatoires ou fixes
- Effectuer une **forward pass** (propagation avant)
- Fonctionner avec le fichier `main.py` fourni

### Exemple d'utilisation
```python
# Créer un réseau avec 3 couches
network = Network(layers=[3, 5, 2], activation='relu')

# Faire une prédiction
input_vector = [1.0, 0.5, -0.3]
output = network.forward(input_vector)

print(output)  # [0.42, -0.15]
```

---

## 📅 Organisation suggérée

| Étape | Fichier à lire | Durée |
|-------|----------------|-------|
| 1. Théorie | `02_concepts_theoriques.md` | 1h |
| 2. Setup | `03_preparation.md` | 30min |
| 3. Neuron | `04_implementation_neuron.md` | 2h |
| 4. Layer | `05_implementation_layer.md` | 2h |
| 5. Network | `06_implementation_network.md` | 3h |
| 6. Tests | `07_tests_validation.md` | 1h |
| 7. Bonus | `08_bonus.md` | Optionnel |

---

## 💡 Philosophie du projet

> "La meilleure façon de comprendre quelque chose, c'est de le construire soi-même."

Ce projet n'est pas là pour te faire gagner du temps, mais pour te faire **comprendre en profondeur** comment fonctionnent les réseaux de neurones.

En codant chaque neurone, chaque couche, chaque calcul à la main, tu vas développer une **intuition** que tu n'aurais jamais avec une simple utilisation de PyTorch ou TensorFlow.

---

## 📚 Ressources recommandées

Avant de commencer, regarde cette vidéo (30min) :
- [**3Blue1Brown - But what is a neural network?**](https://www.youtube.com/watch?v=aircAruvnKk) (EN, sous-titres FR disponibles)

C'est la meilleure introduction visuelle aux réseaux de neurones.

---

## ✅ Checklist avant de commencer

- [ ] J'ai Python 3.8+ installé
- [ ] J'ai cloné/créé le dépôt GitHub
- [ ] J'ai regardé la vidéo de 3Blue1Brown
- [ ] J'ai lu cette introduction
- [ ] Je suis prêt(e) à coder ! 🚀

---

**Prochaine étape :** [02 - Concepts théoriques](02_concepts_theoriques.md)
