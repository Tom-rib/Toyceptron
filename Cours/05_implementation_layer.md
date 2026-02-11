# 05 - Implémentation : Layer

> Coder la classe Layer, une collection de neurones

---

## 🎯 Objectif

Créer la classe `Layer` dans le fichier `src/layer.py` qui :
- Contient plusieurs **neurones**
- Applique tous les neurones à un **vecteur d'entrée**
- Retourne un **vecteur de sortie**

---

## 📋 Spécifications

### Attributs de la classe
```python
class Layer:
    def __init__(self, num_neurons, num_inputs):
        self.neurons = []  # Liste de Neuron
        # Créer num_neurons neurones
        # Chaque neurone aura num_inputs poids
```

### Méthode requise
```python
def forward(self, inputs, activation):
    """
    Propage l'entrée à travers tous les neurones.
    
    Args:
        inputs (list): Vecteur d'entrée
        activation (function): Fonction d'activation
        
    Returns:
        list: Vecteur de sortie [y1, y2, ..., yn]
    """
    # À implémenter
```

---

## 🧮 Principe de fonctionnement

### Schéma d'une couche
```
Entrée (3 valeurs)       Couche (4 neurones)     Sortie (4 valeurs)

    x1  ─────────────→  [neurone 1]  ────→  y1
    x2  ─────────────→  [neurone 2]  ────→  y2
    x3  ─────────────→  [neurone 3]  ────→  y3
                        [neurone 4]  ────→  y4
```

**Chaque neurone :**
- Reçoit **la même entrée** `[x1, x2, x3]`
- A ses **propres poids et biais**
- Produit **une sortie**

**La couche :**
- Collecte toutes les sorties
- Retourne `[y1, y2, y3, y4]`

---

## 💡 Algorithme

### Étape 1 : Créer les neurones

Pour une couche avec :
- `num_neurons` = 3 neurones
- `num_inputs` = 2 entrées par neurone

On doit créer 3 neurones, chacun avec 2 poids.

### Étape 2 : Forward pass

Pour chaque neurone dans la couche :
1. Appliquer le neurone à l'entrée
2. Stocker la sortie dans une liste
3. Retourner la liste des sorties

**Pseudo-code :**
```
outputs = []
pour chaque neurone dans la couche:
    output = neurone.compute(inputs, activation)
    outputs.append(output)
retourner outputs
```

---

## 💻 Implémentation pas à pas

### Étape 1 : Squelette de la classe

Ouvre `src/layer.py` :

```python
# src/layer.py
from neuron import Neuron
import random

class Layer:
    """
    Classe représentant une couche de neurones.
    
    Une couche contient plusieurs neurones qui reçoivent
    tous la même entrée et produisent chacun une sortie.
    """
    
    def __init__(self, num_neurons, num_inputs):
        """
        Initialise une couche de neurones.
        
        Args:
            num_neurons (int): Nombre de neurones dans la couche
            num_inputs (int): Nombre d'entrées par neurone
        """
        self.neurons = []
        
        # TODO: Créer num_neurons neurones
        # Chaque neurone aura num_inputs poids
    
    def forward(self, inputs, activation):
        """
        Propage l'entrée à travers la couche.
        
        Args:
            inputs (list): Vecteur d'entrée
            activation (function): Fonction d'activation
            
        Returns:
            list: Vecteur de sortie
        """
        # TODO: Implémenter la propagation
        pass
```

---

### Étape 2 : Créer les neurones dans __init__

Il y a **2 options** pour initialiser les neurones :

#### Option A : Poids aléatoires (recommandé)

```python
def __init__(self, num_neurons, num_inputs):
    """
    Initialise une couche avec des poids aléatoires.
    """
    self.neurons = []
    
    # Créer num_neurons neurones
    for _ in range(num_neurons):
        # Poids aléatoires entre -1 et 1
        weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        bias = random.uniform(-1, 1)
        
        # Créer le neurone et l'ajouter à la couche
        neuron = Neuron(weights, bias)
        self.neurons.append(neuron)
```

#### Option B : Poids fixes (pour debug)

```python
def __init__(self, num_neurons, num_inputs):
    """
    Initialise une couche avec des poids fixes.
    """
    self.neurons = []
    
    for _ in range(num_neurons):
        # Poids fixes (tous à 0.5)
        weights = [0.5] * num_inputs
        bias = 0.0
        
        neuron = Neuron(weights, bias)
        self.neurons.append(neuron)
```

**Choisis l'option A (aléatoire) pour avoir un vrai réseau.**

---

### Étape 3 : Implémenter forward()

```python
def forward(self, inputs, activation):
    """
    Propage l'entrée à travers tous les neurones.
    
    Args:
        inputs (list): Vecteur d'entrée [x1, x2, ..., xn]
        activation (function): Fonction d'activation
        
    Returns:
        list: Vecteur de sortie [y1, y2, ..., ym]
    """
    outputs = []
    
    # Pour chaque neurone dans la couche
    for neuron in self.neurons:
        # Calculer la sortie de ce neurone
        output = neuron.compute(inputs, activation)
        outputs.append(output)
    
    return outputs
```

**Version avec compréhension de liste (plus concise) :**
```python
def forward(self, inputs, activation):
    return [neuron.compute(inputs, activation) for neuron in self.neurons]
```

---

## 📝 Code complet de layer.py

```python
# src/layer.py
from neuron import Neuron
import random

class Layer:
    """
    Classe représentant une couche de neurones.
    
    Attributs:
        neurons (list): Liste des neurones de la couche
    """
    
    def __init__(self, num_neurons, num_inputs):
        """
        Initialise une couche de neurones avec poids aléatoires.
        
        Args:
            num_neurons (int): Nombre de neurones dans la couche
            num_inputs (int): Nombre d'entrées par neurone (= taille du vecteur d'entrée)
        """
        self.neurons = []
        
        # Créer num_neurons neurones
        for _ in range(num_neurons):
            # Initialiser des poids aléatoires entre -1 et 1
            weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
            bias = random.uniform(-1, 1)
            
            # Créer et ajouter le neurone
            neuron = Neuron(weights, bias)
            self.neurons.append(neuron)
    
    def forward(self, inputs, activation):
        """
        Propage le vecteur d'entrée à travers la couche.
        
        Processus:
        1. Pour chaque neurone, calculer sa sortie
        2. Collecter toutes les sorties dans une liste
        
        Args:
            inputs (list): Vecteur d'entrée
            activation (function): Fonction d'activation à appliquer
            
        Returns:
            list: Vecteur de sortie [y1, y2, ..., yn]
        """
        outputs = []
        
        for neuron in self.neurons:
            output = neuron.compute(inputs, activation)
            outputs.append(output)
        
        return outputs
```

---

## 🧪 Tests de validation

Crée `test_layer.py` pour tester ta couche :

```python
# test_layer.py
from layer import Layer

# Fonction d'activation simple
def identity(x):
    return x

def relu(x):
    return max(0, x)

# Test 1 : Création d'une couche
print("=== Test 1 : Création d'une couche ===")
layer = Layer(num_neurons=3, num_inputs=2)
print(f"Nombre de neurones créés : {len(layer.neurons)}")
print(f"Nombre de poids du 1er neurone : {len(layer.neurons[0].weights)}")
print(f"Test {'✅ OK' if len(layer.neurons) == 3 else '❌ FAIL'}\n")

# Test 2 : Forward pass
print("=== Test 2 : Forward pass ===")
layer = Layer(num_neurons=4, num_inputs=3)
inputs = [1.0, 0.5, -0.3]
outputs = layer.forward(inputs, activation=identity)
print(f"Entrée : {inputs}")
print(f"Nombre de sorties : {len(outputs)}")
print(f"Sorties : {outputs}")
print(f"Test {'✅ OK' if len(outputs) == 4 else '❌ FAIL'}\n")

# Test 3 : Taille de sortie
print("=== Test 3 : Taille de sortie ===")
layer = Layer(num_neurons=2, num_inputs=5)
inputs = [1, 2, 3, 4, 5]
outputs = layer.forward(inputs, activation=relu)
print(f"Couche : 2 neurones, 5 entrées")
print(f"Entrée : {inputs} (taille {len(inputs)})")
print(f"Sortie : {outputs} (taille {len(outputs)})")
print(f"Test {'✅ OK' if len(outputs) == 2 else '❌ FAIL'}\n")

# Test 4 : Propagation avec ReLU
print("=== Test 4 : ReLU élimine les négatifs ===")
# Créer une couche avec des poids négatifs
from neuron import Neuron
layer = Layer(num_neurons=2, num_inputs=2)
# Forcer des poids négatifs pour avoir z < 0
layer.neurons[0] = Neuron(weights=[-1, -1], bias=0)
layer.neurons[1] = Neuron(weights=[1, 1], bias=0)

inputs = [1, 1]
outputs = layer.forward(inputs, activation=relu)
print(f"Neurone 1 : poids=[-1,-1], z=-2, ReLU(-2)=0")
print(f"Neurone 2 : poids=[1,1], z=2, ReLU(2)=2")
print(f"Sortie attendue : [0, 2]")
print(f"Sortie obtenue : {outputs}")
print(f"Test {'✅ OK' if outputs == [0, 2] else '❌ FAIL'}\n")

print("=== Tests terminés ===")
```

**Lancer les tests :**
```bash
cd src
python test_layer.py
```

**Sortie attendue :**
```
=== Test 1 : Création d'une couche ===
Nombre de neurones créés : 3
Nombre de poids du 1er neurone : 2
Test ✅ OK

=== Test 2 : Forward pass ===
...
Test ✅ OK

=== Test 3 : Taille de sortie ===
...
Test ✅ OK

=== Test 4 : ReLU élimine les négatifs ===
...
Test ✅ OK

=== Tests terminés ===
```

---

## 🎨 Visualiser le fonctionnement

Ajoute des prints pour voir ce qui se passe :

```python
def forward(self, inputs, activation):
    """Version avec debug"""
    print(f"=== Couche : {len(self.neurons)} neurones ===")
    print(f"Entrée : {inputs}")
    
    outputs = []
    for i, neuron in enumerate(self.neurons):
        output = neuron.compute(inputs, activation)
        print(f"  Neurone {i+1} → sortie = {output:.3f}")
        outputs.append(output)
    
    print(f"Sortie : {outputs}\n")
    return outputs
```

---

## 🐛 Debugging

### Erreur : "NameError: name 'Neuron' is not defined"

**Problème :** Tu n'as pas importé la classe Neuron.

**Solution :**
```python
# Ajouter en haut du fichier
from neuron import Neuron
```

---

### Erreur : "ValueError: Incompatibilité dimensions"

**Problème :** Le nombre d'entrées ne correspond pas au nombre de poids.

**Solution :** Vérifie que `num_inputs` correspond bien à la taille du vecteur d'entrée.

```python
# Exemple
layer = Layer(num_neurons=3, num_inputs=2)
inputs = [1.0, 2.0]  # ✅ 2 entrées → OK
inputs = [1.0, 2.0, 3.0]  # ❌ 3 entrées → ERREUR
```

---

### Sortie vide []

**Problème :** Les neurones ne sont pas créés dans `__init__`.

**Solution :** Vérifie que la boucle `for _ in range(num_neurons)` s'exécute bien.

```python
# Ajouter un print pour debug
def __init__(self, num_neurons, num_inputs):
    self.neurons = []
    print(f"Création de {num_neurons} neurones...")
    
    for i in range(num_neurons):
        weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        bias = random.uniform(-1, 1)
        neuron = Neuron(weights, bias)
        self.neurons.append(neuron)
        print(f"  Neurone {i+1} créé")
```

---

## ✅ Vérification finale

Avant de passer à la suite, vérifie que :

- [ ] La classe `Layer` est dans `src/layer.py`
- [ ] Le constructeur crée bien `num_neurons` neurones
- [ ] Chaque neurone a `num_inputs` poids
- [ ] La méthode `forward()` retourne une liste de `num_neurons` valeurs
- [ ] Tous les tests passent (4/4 ✅)
- [ ] Tu comprends le fonctionnement d'une couche

---

## 🎯 Résumé

Tu as créé une **couche de neurones** capable de :
1. Créer plusieurs neurones avec initialisation aléatoire
2. Propager un vecteur d'entrée à travers tous les neurones
3. Collecter et retourner les sorties

**Ta couche peut maintenant transformer un vecteur [x1, x2, x3] en [y1, y2, y3, y4] !** 🎉

---

## 📚 Pour aller plus loin

### Bonus 1 : Initialisation avec des poids fixés

Ajoute un paramètre optionnel pour passer des poids manuellement :

```python
def __init__(self, num_neurons, num_inputs, fixed_weights=None):
    """
    Args:
        fixed_weights (list of dict): Poids et biais pour chaque neurone
            Exemple: [{'w': [0.5, 0.2], 'b': 0.1}, ...]
    """
    self.neurons = []
    
    if fixed_weights:
        for params in fixed_weights:
            neuron = Neuron(params['w'], params['b'])
            self.neurons.append(neuron)
    else:
        # Poids aléatoires (code existant)
        ...
```

### Bonus 2 : Méthode __str__

```python
def __str__(self):
    return f"Layer({len(self.neurons)} neurones)"
```

---

**Prochaine étape :** [06 - Implémentation Network](06_implementation_network.md)
