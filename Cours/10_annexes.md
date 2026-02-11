# 10 - Annexes

> Formules mathématiques, commandes utiles et ressources

---

## 📐 Formules mathématiques

### Produit scalaire (dot product)

**Formule :**
```
dot(x, w) = Σ(xi · wi) = x1·w1 + x2·w2 + ... + xn·wn
```

**Exemple :**
```
x = [1, 2, 3]
w = [0.5, -0.2, 0.1]

dot = 1×0.5 + 2×(-0.2) + 3×0.1
    = 0.5 - 0.4 + 0.3
    = 0.4
```

**En Python :**
```python
def dot_product(x, w):
    return sum(xi * wi for xi, wi in zip(x, w))
```

---

### Sortie d'un neurone

**Formule :**
```
y = f(Σ(wi · xi) + b)
```

Où :
- `xi` = entrées
- `wi` = poids
- `b` = biais
- `f` = fonction d'activation

**Décomposé :**
```
1. z = w1·x1 + w2·x2 + ... + wn·xn + b
2. y = f(z)
```

---

### Fonctions d'activation

#### 1. Identité
```
f(x) = x
f'(x) = 1
```

#### 2. Seuil (Step)
```
f(x) = { 1 si x ≥ 0
       { 0 si x < 0
```

#### 3. Sigmoïde
```
f(x) = 1 / (1 + e^(-x))
f'(x) = f(x) · (1 - f(x))
```

**Propriétés :**
- Sortie entre 0 et 1
- `f(0) = 0.5`
- `f(∞) = 1`
- `f(-∞) = 0`

#### 4. ReLU (Rectified Linear Unit)
```
f(x) = max(0, x) = { x si x ≥ 0
                    { 0 si x < 0
f'(x) = { 1 si x > 0
        { 0 si x ≤ 0
```

---

## 💻 Commandes Python utiles

### Gestion de listes

```python
# Créer une liste de N éléments
liste = [0] * 5  # [0, 0, 0, 0, 0]

# Liste avec range
liste = list(range(5))  # [0, 1, 2, 3, 4]

# Compréhension de liste
carres = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Somme d'une liste
total = sum([1, 2, 3, 4])  # 10

# Longueur d'une liste
taille = len([1, 2, 3])  # 3

# Zip deux listes
for x, w in zip([1, 2], [0.5, 0.3]):
    print(x * w)
```

---

### Module random

```python
import random

# Nombre aléatoire entre 0 et 1
r = random.random()

# Nombre aléatoire entre a et b
r = random.uniform(-1, 1)

# Fixer la seed (résultats reproductibles)
random.seed(42)

# Liste de N nombres aléatoires
liste = [random.uniform(-1, 1) for _ in range(5)]
```

---

### Module math

```python
import math

# Exponentielle
e_x = math.exp(2)  # e^2

# Maximum
max_val = max(0, -5)  # 0

# Valeur absolue
abs_val = abs(-3)  # 3

# Puissance
pow_val = math.pow(2, 3)  # 8
```

---

## 🔧 Commandes Git

### Initialiser un dépôt

```bash
# Créer un nouveau dépôt
git init

# Vérifier le statut
git status

# Ajouter tous les fichiers
git add .

# Faire un commit
git commit -m "Initial commit"
```

---

### Pousser sur GitHub

```bash
# Lier au dépôt distant
git remote add origin https://github.com/username/toyceptron.git

# Pousser
git push -u origin main

# Vérifier les remotes
git remote -v
```

---

### Workflow typique

```bash
# 1. Modifier des fichiers
# 2. Voir ce qui a changé
git status

# 3. Ajouter les changements
git add .

# 4. Commit avec message
git commit -m "Implémentation de la classe Neuron"

# 5. Pousser sur GitHub
git push
```

---

## 📚 Ressources externes

### Vidéos

**3Blue1Brown - Neural Networks (EN, sous-titres FR)**
1. [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) (19min)
2. [Gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) (21min)
3. [Backpropagation](https://www.youtube.com/watch?v=Ilg3gGewQ5U) (14min)

**En français**
- [Machine Learnia - Réseaux de neurones](https://www.youtube.com/watch?v=09e8-A5xkQE)
- [Science4All - Comment marchent les IA](https://www.youtube.com/watch?v=5EV9qPNfhWI)

---

### Articles et docs

**Wikipédia**
- [Perceptron](https://fr.wikipedia.org/wiki/Perceptron)
- [Réseau de neurones artificiels](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels)
- [Fonction d'activation](https://fr.wikipedia.org/wiki/Fonction_d%27activation)

**Autres ressources**
- [Neural Networks from Scratch](https://nnfs.io/) (EN)
- [Playground TensorFlow](https://playground.tensorflow.org/) (visualiser)
- [Distill.pub](https://distill.pub/) (articles visuels)

---

### Livres

**Gratuits**
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) (EN, online)
- [Deep Learning](https://www.deeplearningbook.org/) (EN, online)

**Payants**
- "Make Your Own Neural Network" - Tariq Rashid
- "Neural Networks from Scratch in Python" - Harrison Kinsley

---

## 🗂️ Templates de fichiers

### .gitignore pour Python

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Virtual environments
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# Tests
.pytest_cache/
*.log

# Autres
*.egg-info/
dist/
build/
```

---

### README.md template

```markdown
# Toyceptron

Réseau de neurones from scratch en Python pur.

## Installation

```bash
git clone https://github.com/username/toyceptron.git
cd toyceptron/src
python main.py
```

## Architecture

- `neuron.py` : Classe Neuron
- `layer.py` : Classe Layer
- `network.py` : Classe Network

## Usage

```python
from network import Network

network = Network([2, 5, 3, 1], activation='relu')
output = network.forward([1.0, 0.5])
print(output)
```

## Auteur

[Ton nom] - [ton email]
```

---

## 🧮 Exemples de calculs

### Exemple 1 : Neurone simple

**Données :**
- Poids : `[0.5, -0.3, 0.2]`
- Biais : `0.1`
- Entrées : `[1, 2, 3]`
- Activation : identité

**Calcul :**
```
z = 0.5×1 + (-0.3)×2 + 0.2×3 + 0.1
  = 0.5 - 0.6 + 0.6 + 0.1
  = 0.6

y = identity(0.6) = 0.6
```

---

### Exemple 2 : Couche avec 2 neurones

**Couche :**
- Neurone 1 : poids `[1, 1]`, biais `0`
- Neurone 2 : poids `[2, -1]`, biais `0.5`

**Entrée :** `[2, 3]`

**Calculs :**
```
Neurone 1:
  z1 = 1×2 + 1×3 + 0 = 5
  y1 = ReLU(5) = 5

Neurone 2:
  z2 = 2×2 + (-1)×3 + 0.5 = 1.5
  y2 = ReLU(1.5) = 1.5

Sortie : [5, 1.5]
```

---

### Exemple 3 : Réseau complet [2→3→1]

**Architecture :** 2 entrées, 3 neurones cachés, 1 sortie

**Simplification (poids = 1, biais = 0, activation = identité) :**

```
Entrée : [1, 2]

Couche 1 (3 neurones) :
  Neurone 1 : z = 1×1 + 1×2 = 3 → y = 3
  Neurone 2 : z = 1×1 + 1×2 = 3 → y = 3
  Neurone 3 : z = 1×1 + 1×2 = 3 → y = 3
  Sortie couche 1 : [3, 3, 3]

Couche 2 (1 neurone) :
  Neurone 1 : z = 1×3 + 1×3 + 1×3 = 9 → y = 9

Sortie finale : 9
```

---

## 📝 Glossaire

**Neurone (Neuron)**
: Unité de calcul élémentaire qui effectue une combinaison linéaire de ses entrées suivie d'une activation.

**Couche (Layer)**
: Ensemble de neurones qui reçoivent les mêmes entrées et produisent chacun une sortie.

**Réseau (Network)**
: Composition de plusieurs couches permettant de transformer des données complexes.

**Poids (Weights)**
: Paramètres multiplicatifs d'un neurone. Détermine l'importance de chaque entrée.

**Biais (Bias)**
: Paramètre additif d'un neurone. Permet de décaler la fonction d'activation.

**Activation (Activation)**
: Fonction non-linéaire appliquée à la sortie d'un neurone (ReLU, sigmoid, etc.).

**Forward Pass**
: Propagation des données de l'entrée vers la sortie à travers toutes les couches.

**Backpropagation**
: Algorithme d'apprentissage qui ajuste les poids pour minimiser l'erreur (pas dans ce projet).

**Perceptron**
: Modèle de réseau de neurones simple, souvent à une seule couche.

**MLP (Multi-Layer Perceptron)**
: Perceptron avec plusieurs couches cachées.

---

## 🎓 Pour aller plus loin

### Concepts avancés

1. **Entraînement** : Ajuster automatiquement les poids pour minimiser une erreur
2. **Backpropagation** : Algorithme pour calculer les gradients
3. **Gradient descent** : Méthode d'optimisation des poids
4. **Loss function** : Fonction mesurant l'erreur du réseau
5. **Overfitting / Underfitting** : Problèmes de généralisation

### Types de réseaux

- **CNN (Convolutional Neural Networks)** : Pour les images
- **RNN (Recurrent Neural Networks)** : Pour les séquences
- **Transformer** : Architecture moderne (GPT, BERT)
- **GAN (Generative Adversarial Networks)** : Pour générer des données

---

## 💡 Conseils pour la suite

1. **Comprend avant d'utiliser des libs**
   - Maintenant que tu sais comment ça marche, utiliser PyTorch/TensorFlow sera plus clair

2. **Pratique régulièrement**
   - Code d'autres projets ML
   - Participe à des compétitions Kaggle

3. **Reste curieux**
   - Lis des papers
   - Regarde des vidéos
   - Expérimente !

---

## 📞 Contact et feedback

**Projet Toyceptron**
- GitHub : [github.com/ton-username/toyceptron](https://github.com)
- Email : ton-email@example.com

**La Plateforme**
- Site : [laplateforme.io](https://laplateforme.io)

---

## 🏆 Conclusion

**Félicitations !** 🎉

Tu as maintenant une **compréhension profonde** des réseaux de neurones.

Tu sais :
- ✅ Comment un neurone effectue un calcul
- ✅ Comment une couche transforme des données
- ✅ Comment un réseau propage l'information
- ✅ Comment les activations influencent la sortie

**Cette connaissance est précieuse** et te servira pour :
- Utiliser des frameworks (PyTorch, TensorFlow)
- Comprendre les architectures avancées
- Débugger des modèles de ML
- Expliquer le deep learning à d'autres

---

**Bon courage pour la suite ! 🚀🧠**
