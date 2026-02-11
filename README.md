# 🧠 Toyceptron

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-En%20cours-yellow.svg)]()
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()

> *"What I cannot create, I do not understand"* — Richard Feynman

Un **vrai réseau de neurones** codé from scratch, sans bibliothèques externes (numpy, pytorch, sklearn...).  
Projet pédagogique pour comprendre la structure d'un perceptron multi-couches.

---

## 📋 Sommaire du projet

### 📚 Cours & Ressources
Tous les fichiers pédagogiques sont dans le dossier `cours/` :

1. [Introduction](cours/01_introduction.md) — Contexte et objectifs du projet
2. [Concepts théoriques](cours/02_concepts_theoriques.md) — Neurone, couche, réseau, activations
3. [Préparation](cours/03_preparation.md) — Prérequis et setup
4. [Implémentation Neuron](cours/04_implementation_neuron.md) — Classe Neuron
5. [Implémentation Layer](cours/05_implementation_layer.md) — Classe Layer
6. [Implémentation Network](cours/06_implementation_network.md) — Classe Network
7. [Tests & Validation](cours/07_tests_validation.md) — Vérifications
8. [Bonus](cours/08_bonus.md) — Fonctionnalités avancées
9. [Troubleshooting](cours/09_troubleshooting.md) — Résolution de problèmes
10. [Annexes](cours/10_annexes.md) — Formules, commandes, ressources

### 💻 Code source
- `src/neuron.py` — Classe Neuron (unité de calcul élémentaire)
- `src/layer.py` — Classe Layer (collection de neurones)
- `src/network.py` — Classe Network (composition de couches)
- `src/main.py` — Script de test fourni

---

## 🎯 Objectifs

Créer un perceptron multi-couches capable de :
- ✅ Stocker des poids et biais
- ✅ Effectuer une **forward pass** (propagation avant)
- ✅ Utiliser 4 fonctions d'activation : identité, seuil, sigmoïde, ReLU
- ✅ Être initialisé aléatoirement ou avec des paramètres fixes

**Contrainte :** Python pur uniquement, pas de bibliothèques externes !

---

## 🚀 Quick Start

### Installation
```bash
# Cloner le projet
git clone https://github.com/ton-username/toyceptron.git
cd toyceptron

# Vérifier Python (version 3.8+)
python --version
```

### Lancer le projet
```bash
# Exécuter le fichier de test
cd src
python main.py
```

### Structure du dépôt
```
toyceptron/
├── README.md                   # Ce fichier
├── cours/                      # 📚 Fichiers pédagogiques
│   ├── 01_introduction.md
│   ├── 02_concepts_theoriques.md
│   ├── ...
│   └── 10_annexes.md
├── src/                        # 💻 Code source
│   ├── neuron.py
│   ├── layer.py
│   ├── network.py
│   └── main.py
├── tests/                      # 🧪 Tests (optionnel)
│   └── test_examples.py
├── docs/                       # 📊 Schémas et documentation
│   └── schemas/
└── .gitignore
```

---

## 📖 Comment utiliser ce projet

### Pour apprendre
1. Lis les fichiers dans `cours/` dans l'ordre (01 → 10)
2. Regarde les vidéos recommandées (3Blue1Brown)
3. Implémente chaque classe en suivant les guides

### Pour réviser
- Relis les sections théoriques (`02_concepts_theoriques.md`)
- Consulte les annexes pour les formules (`10_annexes.md`)
- Vérifie le troubleshooting en cas de problème (`09_troubleshooting.md`)

### Pour reproduire le projet
1. Suis `03_preparation.md` pour le setup
2. Code `neuron.py`, `layer.py`, `network.py` avec les guides
3. Teste avec `main.py`
4. Ajoute des bonus si tu veux aller plus loin

---

## 🎓 Compétences développées

- **Python** : POO (classes, méthodes, attributs)
- **Structures de données** : listes, manipulation de vecteurs
- **Machine Learning** : architecture de réseau de neurones, forward pass
- **Documentation** : markdown, GitHub, commentaires de code

---

## 🏆 Résultats attendus

À la fin du projet, ton réseau devra :
- Créer un réseau avec N couches de tailles variables
- Propager un vecteur d'entrée à travers toutes les couches
- Retourner une sortie correcte selon les fonctions d'activation
- Fonctionner avec le `main.py` fourni sans modification

---

## 📚 Ressources externes

- [Vidéo 3Blue1Brown - Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk) (EN)
- [Article Wikipédia - Perceptron](https://fr.wikipedia.org/wiki/Perceptron)
- [Playground TensorFlow](https://playground.tensorflow.org/) (tester un réseau)
- [W3Schools - Machine Learning](https://www.w3schools.com/python/python_ml_getting_started.asp)

---

## 👨‍💻 Auteur

**[Ton nom]** — Étudiant en Administration Systèmes et Réseaux (2e année)  
Projet réalisé dans le cadre de [nom de l'école/formation]

---

## 📝 Licence

Projet éducatif libre d'utilisation pour l'apprentissage.

---

## 🔥 Prochaines étapes

- [ ] Implémenter la classe Neuron
- [ ] Implémenter la classe Layer
- [ ] Implémenter la classe Network
- [ ] Tester avec main.py
- [ ] Bonus : ajouter summary()
- [ ] Bonus : gérer les erreurs
- [ ] Bonus : sérialisation du réseau

---

**Bon courage ! 🚀**
