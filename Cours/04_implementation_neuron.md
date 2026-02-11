# 04 - Implémentation : Neuron

> Coder la classe Neuron, l'unité de calcul élémentaire

---

## 🎯 Objectif

Créer la classe `Neuron` dans le fichier `src/neuron.py` qui :
- Stocke des **poids** (weights) et un **biais** (bias)
- Calcule une **sortie** à partir d'un vecteur d'entrée
- Applique une **fonction d'activation**

---

## 📋 Spécifications

### Attributs de la classe
```python
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights  # Liste de nombres (poids)
        self.bias = bias        # Nombre (biais)
```

### Méthodes requises
```python
def compute(self, inputs, activation):
    """
    Calcule la sortie du neurone.
    
    Args:
        inputs (list): Vecteur d'entrée [x1, x2, ..., xn]
        activation (function): Fonction d'activation à appliquer
        
    Returns:
        float: Sortie du neurone après activation
    """
    # À implémenter
```

---

## 🧮 Algorithme

### Étape 1 : Produit scalaire + biais
```
z = w1·x1 + w2·x2 + ... + wn·xn + b
```

### Étape 2 : Activation
```
y = activation(z)
```

### Schéma du calcul
```
Entrées      Poids       Somme pondérée    Activation    Sortie
[x1, x2] → [w1, w2] → Σ(wi·xi) + b → f(z) → y
```

---

## 💻 Implémentation pas à pas

### Étape 1 : Squelette de la classe

Ouvre `src/neuron.py` et commence par :

```python
# src/neuron.py

class Neuron:
    """
    Classe représentant un neurone artificiel.
    
    Un neurone effectue une combinaison linéaire de ses entrées,
    ajoute un biais, puis applique une fonction d'activation.
    """
    
    def __init__(self, weights, bias):
        """
        Initialise le neurone.
        
        Args:
            weights (list): Liste des poids [w1, w2, ..., wn]
            bias (float): Biais du neurone
        """
        self.weights = weights
        self.bias = bias
    
    def compute(self, inputs, activation):
        """
        Calcule la sortie du neurone.
        
        Args:
            inputs (list): Vecteur d'entrée [x1, x2, ..., xn]
            activation (function): Fonction d'activation
            
        Returns:
            float: Sortie du neurone
        """
        # TODO: Implémenter le calcul
        pass
```

---

### Étape 2 : Implémenter le produit scalaire

Le produit scalaire est : `Σ(wi · xi) = w1·x1 + w2·x2 + ... + wn·xn`

**Méthode 1 : Avec une boucle for**
```python
def weighted_sum(self, inputs):
    """
    Calcule la somme pondérée des entrées.
    
    Args:
        inputs (list): Vecteur d'entrée
        
    Returns:
        float: Σ(wi · xi) + bias
    """
    total = 0.0
    for i in range(len(inputs)):
        total += self.weights[i] * inputs[i]
    
    return total + self.bias
```

**Méthode 2 : Avec zip() (plus pythonique)**
```python
def weighted_sum(self, inputs):
    """
    Calcule la somme pondérée des entrées.
    """
    total = sum(w * x for w, x in zip(self.weights, inputs))
    return total + self.bias
```

**Méthode 3 : Avec une compréhension de liste**
```python
def weighted_sum(self, inputs):
    """
    Calcule la somme pondérée des entrées.
    """
    total = sum([self.weights[i] * inputs[i] for i in range(len(inputs))])
    return total + self.bias
```

**Choisis la méthode qui te semble la plus claire !**

---

### Étape 3 : Compléter la méthode compute()

```python
def compute(self, inputs, activation):
    """
    Calcule la sortie du neurone.
    
    Args:
        inputs (list): Vecteur d'entrée
        activation (function): Fonction d'activation
        
    Returns:
        float: Sortie du neurone après activation
    """
    # Étape 1 : Calculer la somme pondérée
    z = self.weighted_sum(inputs)
    
    # Étape 2 : Appliquer l'activation
    y = activation(z)
    
    return y
```

---

## 📝 Code complet de neuron.py

Voici le code complet (choisis ta méthode préférée pour le produit scalaire) :

```python
# src/neuron.py

class Neuron:
    """
    Classe représentant un neurone artificiel.
    
    Attributs:
        weights (list): Poids du neurone
        bias (float): Biais du neurone
    """
    
    def __init__(self, weights, bias):
        """
        Initialise le neurone avec des poids et un biais.
        
        Args:
            weights (list): Liste des poids [w1, w2, ..., wn]
            bias (float): Biais du neurone
        """
        self.weights = weights
        self.bias = bias
    
    def weighted_sum(self, inputs):
        """
        Calcule la somme pondérée : Σ(wi · xi) + bias
        
        Args:
            inputs (list): Vecteur d'entrée [x1, x2, ..., xn]
            
        Returns:
            float: Somme pondérée + biais
        """
        # Méthode avec zip() (recommandée)
        total = sum(w * x for w, x in zip(self.weights, inputs))
        return total + self.bias
    
    def compute(self, inputs, activation):
        """
        Calcule la sortie du neurone.
        
        Processus:
        1. Calculer z = Σ(wi · xi) + bias
        2. Appliquer activation: y = f(z)
        
        Args:
            inputs (list): Vecteur d'entrée
            activation (function): Fonction d'activation à appliquer
            
        Returns:
            float: Sortie du neurone après activation
        """
        z = self.weighted_sum(inputs)
        y = activation(z)
        return y
```

---

## 🧪 Tests de validation

Crée un fichier `test_neuron.py` pour tester ton neurone :

```python
# test_neuron.py
from neuron import Neuron

# Fonctions d'activation simples pour les tests
def identity(x):
    return x

def relu(x):
    return max(0, x)

# Test 1 : Neurone simple avec activation identité
print("=== Test 1 : Activation identité ===")
neuron = Neuron(weights=[1, 1, 1], bias=0)
output = neuron.compute([1, 2, 3], activation=identity)
print(f"Entrée : [1, 2, 3]")
print(f"Poids : [1, 1, 1], Biais : 0")
print(f"Sortie attendue : 6.0 (1+2+3)")
print(f"Sortie obtenue : {output}")
print(f"Test {'✅ OK' if output == 6.0 else '❌ FAIL'}\n")

# Test 2 : Neurone avec biais
print("=== Test 2 : Avec biais ===")
neuron = Neuron(weights=[0.5, -0.3, 0.2], bias=0.1)
output = neuron.compute([1, 2, 3], activation=identity)
expected = 0.5*1 + (-0.3)*2 + 0.2*3 + 0.1  # = 0.6
print(f"Entrée : [1, 2, 3]")
print(f"Poids : [0.5, -0.3, 0.2], Biais : 0.1")
print(f"Sortie attendue : {expected}")
print(f"Sortie obtenue : {output}")
print(f"Test {'✅ OK' if abs(output - expected) < 0.001 else '❌ FAIL'}\n")

# Test 3 : ReLU avec valeur négative
print("=== Test 3 : ReLU avec valeur négative ===")
neuron = Neuron(weights=[-1, -1], bias=0)
output = neuron.compute([1, 2], activation=relu)
print(f"Entrée : [1, 2]")
print(f"Poids : [-1, -1], Biais : 0")
print(f"z = -3, ReLU(-3) = 0")
print(f"Sortie attendue : 0")
print(f"Sortie obtenue : {output}")
print(f"Test {'✅ OK' if output == 0 else '❌ FAIL'}\n")

# Test 4 : ReLU avec valeur positive
print("=== Test 4 : ReLU avec valeur positive ===")
neuron = Neuron(weights=[1, 1], bias=0)
output = neuron.compute([1, 2], activation=relu)
print(f"Entrée : [1, 2]")
print(f"z = 3, ReLU(3) = 3")
print(f"Sortie attendue : 3")
print(f"Sortie obtenue : {output}")
print(f"Test {'✅ OK' if output == 3 else '❌ FAIL'}\n")

print("=== Tests terminés ===")
```

**Lancer les tests :**
```bash
cd src
python test_neuron.py
```

**Sortie attendue :**
```
=== Test 1 : Activation identité ===
...
Test ✅ OK

=== Test 2 : Avec biais ===
...
Test ✅ OK

=== Test 3 : ReLU avec valeur négative ===
...
Test ✅ OK

=== Test 4 : ReLU avec valeur positive ===
...
Test ✅ OK

=== Tests terminés ===
```

---

## 🐛 Debugging

### Erreur : "list index out of range"

**Problème :** Les listes `weights` et `inputs` n'ont pas la même longueur.

**Solution :**
```python
# Ajouter une vérification
def weighted_sum(self, inputs):
    if len(inputs) != len(self.weights):
        raise ValueError(f"Incompatibilité : {len(inputs)} entrées, {len(self.weights)} poids")
    # ... reste du code
```

---

### Erreur : "TypeError: 'NoneType' object is not callable"

**Problème :** La fonction d'activation n'est pas passée correctement.

**Solution :** Vérifie que tu passes bien une fonction :
```python
# ✅ Bon
output = neuron.compute([1, 2], activation=relu)

# ❌ Mauvais
output = neuron.compute([1, 2], activation=relu())  # Ne pas mettre ()
```

---

### Résultat incorrect

**Debugging :** Ajoute des prints pour voir les valeurs intermédiaires :
```python
def compute(self, inputs, activation):
    print(f"Inputs : {inputs}")
    print(f"Weights : {self.weights}")
    print(f"Bias : {self.bias}")
    
    z = self.weighted_sum(inputs)
    print(f"z (avant activation) : {z}")
    
    y = activation(z)
    print(f"y (après activation) : {y}")
    
    return y
```

---

## ✅ Vérification finale

Avant de passer à la suite, vérifie que :

- [ ] La classe `Neuron` est dans `src/neuron.py`
- [ ] Le constructeur `__init__()` stocke les poids et le biais
- [ ] La méthode `weighted_sum()` calcule le produit scalaire + biais
- [ ] La méthode `compute()` applique l'activation
- [ ] Tous les tests passent (4/4 ✅)
- [ ] Tu comprends chaque ligne de code

---

## 🎯 Résumé

Tu as créé un **neurone artificiel** capable de :
1. Stocker des poids et un biais
2. Calculer une combinaison linéaire des entrées
3. Appliquer une fonction d'activation
4. Retourner une sortie

**C'est la brique de base de tout réseau de neurones !** 🎉

---

## 📚 Pour aller plus loin

### Bonus 1 : Initialisation aléatoire

Ajoute une méthode pour initialiser des poids aléatoires :
```python
import random

@staticmethod
def random_init(num_inputs):
    """
    Crée un neurone avec des poids aléatoires.
    
    Args:
        num_inputs (int): Nombre d'entrées
        
    Returns:
        Neuron: Neurone avec poids aléatoires
    """
    weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
    bias = random.uniform(-1, 1)
    return Neuron(weights, bias)
```

### Bonus 2 : Méthode __str__

Ajoute une représentation lisible :
```python
def __str__(self):
    return f"Neuron(weights={self.weights}, bias={self.bias})"
```

---

**Prochaine étape :** [05 - Implémentation Layer](05_implementation_layer.md)
