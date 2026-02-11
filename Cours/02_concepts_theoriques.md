# 02 - Concepts théoriques

> Comprendre les bases mathématiques avant de coder

---

## 🧩 Les 3 briques fondamentales

Un réseau de neurones est composé de 3 éléments :
1. **Neurone** — L'unité de calcul élémentaire
2. **Couche** — Un groupe de neurones identiques
3. **Réseau** — Un empilement de couches

On va les détailler un par un.

---

## 1️⃣ Le Neurone

### Qu'est-ce qu'un neurone ?

Un neurone artificiel est inspiré du neurone biologique. Il prend plusieurs **entrées**, les combine, et produit une **sortie**.

### Schéma d'un neurone
```
Entrées          Poids          Somme pondérée      Sortie
  x1  ─────────→  w1  ─┐
  x2  ─────────→  w2  ─┼───→ Σ(wi·xi) + b ───→ activation ───→ y
  x3  ─────────→  w3  ─┘
                    +
                  biais (b)
```

### Calcul mathématique

Un neurone effectue **2 opérations** :

#### 1. Combinaison linéaire (produit scalaire)
```
z = w1·x1 + w2·x2 + w3·x3 + b
```

Ou en notation mathématique :
```
z = Σ(wi · xi) + b
```

#### 2. Fonction d'activation
```
y = f(z)
```

Où `f` peut être : identité, seuil, sigmoïde, ReLU, etc.

### Exemple concret

Soit un neurone avec :
- Poids : `w = [0.5, -0.3, 0.2]`
- Biais : `b = 0.1`
- Entrées : `x = [1, 2, 3]`

**Calcul :**
```python
# Étape 1 : Combinaison linéaire
z = 0.5*1 + (-0.3)*2 + 0.2*3 + 0.1
z = 0.5 - 0.6 + 0.6 + 0.1
z = 0.6

# Étape 2 : Activation (par exemple ReLU)
y = max(0, z) = max(0, 0.6) = 0.6
```

### En Python (simplifié)
```python
def neuron(x, w, b, activation):
    # Produit scalaire
    z = sum([x[i] * w[i] for i in range(len(x))]) + b
    
    # Activation
    y = activation(z)
    
    return y
```

---

## 2️⃣ La Couche (Layer)

### Qu'est-ce qu'une couche ?

Une couche est un **groupe de neurones** qui :
- Reçoivent les **mêmes entrées**
- Ont chacun leurs **propres poids et biais**
- Produisent chacun une **sortie**

### Schéma d'une couche
```
Entrée (3 valeurs)       Couche (4 neurones)     Sortie (4 valeurs)

    x1  ─────────────→  [neurone 1]  ────→  y1
    x2  ─────────────→  [neurone 2]  ────→  y2
    x3  ─────────────→  [neurone 3]  ────→  y3
                        [neurone 4]  ────→  y4
```

### Exemple concret

Couche avec **2 neurones**, entrée de taille **3** :

**Neurone 1 :**
- Poids : `[0.5, 0.2, -0.1]`
- Biais : `0.0`

**Neurone 2 :**
- Poids : `[-0.3, 0.4, 0.6]`
- Biais : `0.2`

**Entrée :** `[1.0, 2.0, 0.5]`

**Calcul :**
```python
# Neurone 1
y1 = 0.5*1.0 + 0.2*2.0 + (-0.1)*0.5 + 0.0 = 0.85

# Neurone 2
y2 = (-0.3)*1.0 + 0.4*2.0 + 0.6*0.5 + 0.2 = 1.00

# Sortie de la couche
output = [0.85, 1.00]
```

### Réseau totalement relié (fully-connected)

Dans ce projet, chaque neurone d'une couche est **connecté à TOUTES les sorties** de la couche précédente.

```
Couche 1 (3 neurones)    Couche 2 (2 neurones)

    [n1] ─────┬────────→ [n1]
    [n2] ─────┼────────→ [n2]
    [n3] ─────┘
```

---

## 3️⃣ Le Réseau (Network)

### Qu'est-ce qu'un réseau ?

Un réseau de neurones est une **composition de couches** :
```
Entrée → Couche 1 → Couche 2 → ... → Couche N → Sortie
```

Chaque couche transforme le vecteur qu'elle reçoit et le passe à la suivante.

### Architecture d'exemple
```
Input: [x1, x2, x3]  (3 valeurs)
   ↓
Layer 1: 5 neurones  → [y1, y2, y3, y4, y5]
   ↓
Layer 2: 3 neurones  → [z1, z2, z3]
   ↓
Output: [z1, z2, z3]  (3 valeurs)
```

### Forward Pass (propagation avant)

C'est le processus qui fait circuler les données de l'entrée à la sortie.

**Algorithme :**
```
1. Prendre le vecteur d'entrée
2. Pour chaque couche :
   a. Appliquer tous les neurones de la couche
   b. Obtenir un nouveau vecteur
3. Retourner la sortie de la dernière couche
```

**Exemple en pseudo-code :**
```python
def forward(input):
    current = input
    for layer in layers:
        current = layer.forward(current)
    return current
```

---

## 🎨 Fonctions d'activation

Une fonction d'activation transforme la sortie d'un neurone. Elle introduit de la **non-linéarité** dans le réseau.

### 1. Identité
```
f(x) = x
```
**Graphe :** Ligne droite à 45°  
**Usage :** Couche de sortie pour régression

```
  y
  |     /
  |    /
  |   /
  |  /
  |─/─────── x
```

**Code Python :**
```python
def identity(x):
    return x
```

---

### 2. Seuil (Step)
```
f(x) = 1 si x >= 0
       0 si x < 0
```
**Graphe :** Escalier  
**Usage :** Classification binaire (ancien, peu utilisé)

```
  y
  |  ┌──────
  |  │
  |  │
  |──┘
  |────────── x
```

**Code Python :**
```python
def step(x):
    return 1 if x >= 0 else 0
```

---

### 3. Sigmoïde
```
f(x) = 1 / (1 + e^(-x))
```
**Graphe :** Courbe en S  
**Usage :** Couche de sortie pour probabilités (0 à 1)

```
  y
1 |      ┌────
  |    ╱
  |  ╱
  |╱
0 |────────── x
```

**Code Python :**
```python
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
```

**Propriétés :**
- Sortie entre 0 et 1
- Smooth (dérivable partout)
- Problème : "vanishing gradient" pour x très grand/petit

---

### 4. ReLU (Rectified Linear Unit)
```
f(x) = max(0, x)
```
**Graphe :** Ligne brisée  
**Usage :** Couches cachées (le plus populaire)

```
  y
  |      ╱
  |     ╱
  |    ╱
  |   ╱
  |──┘────── x
```

**Code Python :**
```python
def relu(x):
    return max(0, x)
```

**Propriétés :**
- Simple et efficace
- Pas de vanishing gradient pour x > 0
- Problème : neurones "morts" si x toujours < 0

---

## 📐 Formules importantes

### Produit scalaire (dot product)
```
dot(x, w) = Σ(xi · wi)
          = x1·w1 + x2·w2 + ... + xn·wn
```

**Exemple :**
```python
x = [1, 2, 3]
w = [0.5, -0.2, 0.1]

dot = 1*0.5 + 2*(-0.2) + 3*0.1 = 0.2
```

### Sortie d'un neurone
```
y = activation( Σ(wi · xi) + b )
```

### Sortie d'une couche
```
output = [neuron1(input), neuron2(input), ..., neuronN(input)]
```

---

## 🧪 Exemple complet : Réseau 2 couches

### Architecture
- **Entrée :** 2 valeurs
- **Couche 1 :** 3 neurones, activation ReLU
- **Couche 2 :** 1 neurone, activation identité

### Forward pass avec des valeurs

**Entrée :** `[1.0, 0.5]`

**Couche 1 (3 neurones) :**
```
Neurone 1: w=[0.5, 0.2], b=0.1  → z=0.7  → ReLU(0.7)=0.7
Neurone 2: w=[-0.3, 0.4], b=0.0 → z=-0.1 → ReLU(-0.1)=0.0
Neurone 3: w=[0.1, 0.6], b=0.2  → z=0.6  → ReLU(0.6)=0.6

Sortie couche 1: [0.7, 0.0, 0.6]
```

**Couche 2 (1 neurone) :**
```
Neurone 1: w=[0.5, -0.2, 0.3], b=0.0
z = 0.5*0.7 + (-0.2)*0.0 + 0.3*0.6 + 0.0 = 0.53
y = identity(0.53) = 0.53

Sortie finale: [0.53]
```

**Résultat :** Le réseau transforme `[1.0, 0.5]` en `[0.53]`

---

## ✅ Points clés à retenir

1. **Neurone** = combinaison linéaire + activation
2. **Couche** = plusieurs neurones en parallèle
3. **Réseau** = empilement de couches
4. **Forward pass** = propagation de l'entrée à la sortie
5. **Activation** = fonction non-linéaire (identité, seuil, sigmoïde, ReLU)

---

## 📚 Ressources pour aller plus loin

- [Vidéo 3Blue1Brown - Gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w)
- [Article Wikipédia - Réseau de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels)
- [Playground TensorFlow](https://playground.tensorflow.org/) (visualiser un réseau)

---

**Prochaine étape :** [03 - Préparation](03_preparation.md)
