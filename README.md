# 🧠 Toyceptron

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Complété-green.svg)]()
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()

> *"What I cannot create, I do not understand"* — Richard Feynman

Un **vrai réseau de neurones** codé from scratch, sans bibliothèques externes (numpy, pytorch, sklearn...).  
Projet pédagogique pour comprendre la structure d'un perceptron multi-couches.

---

## 📋 Sommaire du projet

### 📚 Cours & Ressources

Tous les fichiers pédagogiques sont dans le dossier `cours/` :

| # | Fichier | Contenu |
|---|---------|---------|
| 01 | [Introduction](cours/01_introduction.md) | Contexte, objectifs, philosophie du projet |
| 02 | [Concepts théoriques](cours/02_concepts_theoriques.md) | Neurone, couche, réseau, fonctions d'activation |
| 03 | [Préparation](cours/03_preparation.md) | Prérequis, setup, structure du projet |
| 04 | [Implémentation Neuron](cours/04_implementation_neuron.md) | Coder la classe `Neuron` |
| 05 | [Implémentation Layer](cours/05_implementation_layer.md) | Coder la classe `Layer` |
| 06 | [Implémentation Network](cours/06_implementation_network.md) | Coder la classe `Network` |
| 07 | [Tests & Validation](cours/07_tests_validation.md) | Vérifications et tests |
| 08 | [Bonus](cours/08_bonus.md) | Fonctionnalités avancées (optionnel) |
| 09 | [Troubleshooting](cours/09_troubleshooting.md) | Résolution de problèmes |
| 10 | [Annexes](cours/10_annexes.md) | Formules, commandes Git, ressources |

### 💻 Code source

| Fichier | Rôle |
|---------|------|
| `src/neuron.py` | Classe `Neuron` — Unité de calcul élémentaire |
| `src/layer.py` | Classe `Layer` — Collection de neurones |
| `src/network.py` | Classe `Network` — Composition de couches |
| `src/activation.py` | Fonctions d'activation (identity, threshold, relu) |
| `src/main.py` | Script de test fourni par le sujet |

---

## 🎯 Objectifs

Créer un perceptron multi-couches capable de :
- ✅ Stocker des poids et biais dans chaque neurone
- ✅ Effectuer une **forward pass** complète
- ✅ Utiliser 4 fonctions d'activation : identité, seuil, sigmoïde, ReLU
- ✅ Respecter l'interface imposée par le `main.py` fourni

**Contrainte :** Python pur uniquement — aucune bibliothèque externe !

---

## 🚀 Quick Start

### Prérequis
```bash
# Vérifier Python (version 3.8+)
python --version
```

### Installation
```bash
# Cloner le projet
git clone https://github.com/ton-username/toyceptron.git
cd toyceptron
```

### Lancer le projet
```bash
cd src
python main.py
```

### Résultat attendu
```
Input: [1.0, 2.0, 4.0]

--- Test Neuron ---
Neurone h1 (brut): 1.6
Neurone h2 (brut): 0.7
Neurone h1 (activé): 0.8320183851339245
Neurone h2 (activé): 0.6681877721681662

--- Test Layer ---
Couche (valeurs brutes): [1.6, 0.7]
Couche (valeurs activées): [0.8320183851339245, 0.6681877721681662]

--- Test Network ---
Sorties activées : [0.5309442148001715, 0.494901997674804]
```

---

## 🗂️ Structure du dépôt

```
toyceptron/
├── README.md                       # Ce fichier
├── .gitignore                      # Fichiers ignorés par Git
│
├── cours/                          # 📚 Documentation pédagogique
│   ├── 01_introduction.md
│   ├── 02_concepts_theoriques.md
│   ├── 03_preparation.md
│   ├── 04_implementation_neuron.md
│   ├── 05_implementation_layer.md
│   ├── 06_implementation_network.md
│   ├── 07_tests_validation.md
│   ├── 08_bonus.md
│   ├── 09_troubleshooting.md
│   └── 10_annexes.md
│
└── src/                            # 💻 Code source
    ├── neuron.py                   # Classe Neuron
    ├── layer.py                    # Classe Layer
    ├── network.py                  # Classe Network
    ├── activation.py               # Fonctions d'activation
    └── main.py                     # Script de test (fourni)
```

---

## 🧩 Architecture du code

### Séparation des responsabilités

```
neuron.py         layer.py          network.py        activation.py
──────────        ──────────        ──────────        ──────────────
Neuron            Layer             Network           act_identity()
  ├── weights       ├── neurons[]     ├── layers[]      act_threshold()
  ├── bias          └── forward()     ├── activation    act_relu()
  └── forward()     (valeurs brutes)  ├── add()
  (valeurs brutes)                    └── feedforward()
                                      (applique activation)
```

### Principe clé : séparation brut / activé

```
Neuron.forward()   →  valeur BRUTE  z = Σ(wi·xi) + b
Layer.forward()    →  valeurs BRUTES [z1, z2, ...]
Network.feedforward() →  valeurs ACTIVÉES [f(z1), f(z2), ...]
```

L'activation est appliquée **uniquement** dans le Network, pas dans les neurones ou les couches.

---

## 💻 Exemple d'utilisation

### Neurone individuel
```python
from neuron import Neuron

neuron = Neuron(weights=[0.2, -0.1, 0.4], bias=0.0)
z = neuron.forward([1.0, 2.0, 4.0])
# z = 0.2*1.0 + (-0.1)*2.0 + 0.4*4.0 + 0.0 = 1.6
```

### Couche de neurones
```python
from layer import Layer

layer = Layer(
    weights_list=[[0.2, -0.1, 0.4], [-0.4, 0.3, 0.1]],
    biases_list=[0.0, 0.1]
)
raw = layer.forward([1.0, 2.0, 4.0])
# raw = [1.6, 0.7]  (valeurs brutes)
```

### Réseau complet
```python
from network import Network
from math import exp

def act_sigmoid(x):
    return 1 / (1 + exp(-x))

net = Network(input_size=3, activation=act_sigmoid)

net.add(
    weights=[[0.2, -0.1, 0.4], [-0.4, 0.3, 0.1]],
    biases=[0.0, 0.1]
)
net.add(
    weights=[[0.5, -0.2], [-0.3, 0.4], [0.1, 0.2]],
    biases=[0.0, 0.1, -0.1]
)
net.add(
    weights=[[0.3, -0.1, 0.2], [-0.5, 0.4, 0.1]],
    biases=[-0.1, 0.0]
)

y = net.feedforward([1.0, 2.0, 4.0])
# y = [0.5309442148001715, 0.494901997674804]
```

### Fonctions d'activation disponibles
```python
from activation import act_identity, act_threshold, act_relu

act_identity(x)   # f(x) = x
act_threshold(x)  # f(x) = 1 si x >= 0, sinon 0
act_relu(x)       # f(x) = max(0, x)
# act_sigmoid est définie dans main.py
```

---

## 🎓 Compétences développées

- **Python** : Programmation Orientée Objet (classes, méthodes, attributs)
- **Structures de données** : listes, manipulation de vecteurs
- **Machine Learning** : architecture MLP, forward pass, fonctions d'activation
- **Documentation** : Markdown, GitHub, docstrings

---

## 📚 Ressources externes

- [Vidéo 3Blue1Brown - Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk) (EN, 19min)
- [Article Wikipédia - Perceptron](https://fr.wikipedia.org/wiki/Perceptron)
- [Playground TensorFlow](https://playground.tensorflow.org/) (visualiser un réseau)
- [W3Schools - Machine Learning](https://www.w3schools.com/python/python_ml_getting_started.asp)

---

## 👨‍💻 Auteur

**[Tom Ribero]** — Étudiant en Administration Systèmes et Réseaux (2e année)  
Projet réalisé dans le cadre de [nom de l'école/formation]
**[Romain Jazzar]** — Étudiant en  data IA (2e année)  

---
