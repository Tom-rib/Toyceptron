# 06 - Implémentation : Network

> Coder la classe Network, le réseau de neurones complet

---

## 🎯 Objectif

Créer la classe `Network` dans le fichier `src/network.py` qui :
- Crée une **architecture complète** de couches
- Fait circuler les données de l'**entrée à la sortie**
- Gère les **fonctions d'activation**

---

## 📋 Spécifications

### Attributs de la classe
```python
class Network:
    def __init__(self, layers, activation='relu'):
        self.layers = []  # Liste de Layer
        self.activation = activation  # Nom de la fonction d'activation
        # Créer l'architecture du réseau
```

### Méthodes requises
```python
def forward(self, inputs):
    """
    Propage l'entrée à travers toutes les couches.
    
    Args:
        inputs (list): Vecteur d'entrée
        
    Returns:
        list: Sortie du réseau
    """
    # À implémenter
```

---

## 🧮 Architecture d'un réseau

### Exemple de réseau
```
Entrée        Couche 1      Couche 2       Couche 3      Sortie
[x1, x2]  →  [3 neurones] → [5 neurones] → [2 neurones] → [y1, y2]
  (2)            (3)            (5)             (2)          (2)
```

**Notation :** `layers = [2, 3, 5, 2]`
- `layers[0]` = taille de l'entrée (2)
- `layers[1]` = taille de la couche 1 (3 neurones)
- `layers[2]` = taille de la couche 2 (5 neurones)
- `layers[3]` = taille de la couche 3 / sortie (2 neurones)

---

## 💡 Algorithme

### Étape 1 : Créer les couches

Pour créer un réseau `[2, 3, 5, 2]` :
- **Couche 1 :** 3 neurones, 2 entrées (= `layers[0]`)
- **Couche 2 :** 5 neurones, 3 entrées (= `layers[1]`)
- **Couche 3 :** 2 neurones, 5 entrées (= `layers[2]`)

**Règle :** Couche `i` a `layers[i]` neurones et `layers[i-1]` entrées.

**Pseudo-code :**
```
pour i allant de 1 à len(layers)-1 :
    num_neurons = layers[i]
    num_inputs = layers[i-1]
    créer Layer(num_neurons, num_inputs)
```

---

### Étape 2 : Forward pass

Faire circuler les données de couche en couche :

```
current = input
pour chaque couche :
    current = couche.forward(current, activation)
retourner current
```

---

## 💻 Implémentation pas à pas

### Étape 1 : Squelette de la classe

Ouvre `src/network.py` :

```python
# src/network.py
from layer import Layer
import math

class Network:
    """
    Classe représentant un réseau de neurones multi-couches.
    
    Le réseau est une composition de couches qui transforment
    progressivement l'entrée jusqu'à produire une sortie.
    """
    
    def __init__(self, layers, activation='relu'):
        """
        Initialise le réseau.
        
        Args:
            layers (list): Architecture du réseau [in, h1, h2, ..., out]
                Exemple: [2, 4, 3, 1] → entrée:2, couche1:4, couche2:3, sortie:1
            activation (str): Nom de la fonction d'activation
                Choix: 'identity', 'step', 'sigmoid', 'relu'
        """
        self.layers = []
        self.activation_name = activation
        
        # TODO: Créer les couches
        
        # TODO: Définir la fonction d'activation
    
    def forward(self, inputs):
        """
        Propage l'entrée à travers le réseau.
        
        Args:
            inputs (list): Vecteur d'entrée
            
        Returns:
            list: Sortie du réseau
        """
        # TODO: Implémenter la propagation
        pass
```

---

### Étape 2 : Créer les couches dans __init__

```python
def __init__(self, layers, activation='relu'):
    """
    Initialise le réseau avec une architecture donnée.
    """
    self.layers = []
    self.activation_name = activation
    
    # Créer les couches
    # On parcourt layers à partir de l'indice 1
    for i in range(1, len(layers)):
        num_neurons = layers[i]      # Taille de la couche actuelle
        num_inputs = layers[i-1]     # Taille de la couche précédente
        
        # Créer la couche et l'ajouter au réseau
        layer = Layer(num_neurons, num_inputs)
        self.layers.append(layer)
    
    # Définir la fonction d'activation
    self.activation = self.get_activation(activation)
```

**Exemple :** Pour `layers = [2, 3, 5, 2]`
```
i=1 : Layer(3 neurones, 2 entrées)
i=2 : Layer(5 neurones, 3 entrées)
i=3 : Layer(2 neurones, 5 entrées)

Résultat : 3 couches créées
```

---

### Étape 3 : Implémenter les fonctions d'activation

Ajoute une méthode pour récupérer la fonction d'activation :

```python
def get_activation(self, name):
    """
    Retourne la fonction d'activation correspondante.
    
    Args:
        name (str): Nom de l'activation
        
    Returns:
        function: Fonction d'activation
    """
    if name == 'identity':
        return lambda x: x
    
    elif name == 'step':
        return lambda x: 1 if x >= 0 else 0
    
    elif name == 'sigmoid':
        return lambda x: 1 / (1 + math.exp(-x))
    
    elif name == 'relu':
        return lambda x: max(0, x)
    
    else:
        raise ValueError(f"Activation inconnue : {name}")
```

---

### Étape 4 : Implémenter forward()

```python
def forward(self, inputs):
    """
    Propage l'entrée à travers toutes les couches.
    
    Processus:
    1. Partir de l'entrée
    2. Pour chaque couche, transformer le vecteur courant
    3. Retourner la sortie de la dernière couche
    
    Args:
        inputs (list): Vecteur d'entrée
        
    Returns:
        list ou float: Sortie du réseau
    """
    current = inputs
    
    # Propager à travers chaque couche
    for layer in self.layers:
        current = layer.forward(current, self.activation)
    
    # Si la sortie est un scalaire (1 neurone), retourner juste la valeur
    if len(current) == 1:
        return current[0]
    
    return current
```

---

## 📝 Code complet de network.py

```python
# src/network.py
from layer import Layer
import math

class Network:
    """
    Classe représentant un réseau de neurones multi-couches.
    
    Attributs:
        layers (list): Liste des couches du réseau
        activation_name (str): Nom de la fonction d'activation
        activation (function): Fonction d'activation
    """
    
    def __init__(self, layers, activation='relu'):
        """
        Initialise le réseau avec une architecture.
        
        Args:
            layers (list): Architecture [entrée, h1, h2, ..., sortie]
                Exemple: [3, 5, 2] → entrée:3, couche1:5, sortie:2
            activation (str): 'identity', 'step', 'sigmoid', 'relu'
        """
        self.layers = []
        self.activation_name = activation
        
        # Créer les couches du réseau
        for i in range(1, len(layers)):
            num_neurons = layers[i]
            num_inputs = layers[i-1]
            layer = Layer(num_neurons, num_inputs)
            self.layers.append(layer)
        
        # Définir la fonction d'activation
        self.activation = self.get_activation(activation)
    
    def get_activation(self, name):
        """
        Retourne la fonction d'activation.
        
        Args:
            name (str): 'identity', 'step', 'sigmoid', 'relu'
            
        Returns:
            function: Fonction d'activation
        """
        if name == 'identity':
            return lambda x: x
        
        elif name == 'step':
            return lambda x: 1 if x >= 0 else 0
        
        elif name == 'sigmoid':
            return lambda x: 1 / (1 + math.exp(-x))
        
        elif name == 'relu':
            return lambda x: max(0, x)
        
        else:
            raise ValueError(f"Activation inconnue : {name}")
    
    def forward(self, inputs):
        """
        Propage l'entrée à travers le réseau.
        
        Args:
            inputs (list): Vecteur d'entrée
            
        Returns:
            list ou float: Sortie du réseau
        """
        current = inputs
        
        # Propager à travers toutes les couches
        for layer in self.layers:
            current = layer.forward(current, self.activation)
        
        # Si sortie scalaire (1 neurone), retourner la valeur
        if len(current) == 1:
            return current[0]
        
        return current
```

---

## 🧪 Tests de validation

Crée `test_network.py` :

```python
# test_network.py
from network import Network

# Test 1 : Création d'un réseau
print("=== Test 1 : Création d'un réseau ===")
network = Network(layers=[2, 3, 1], activation='relu')
print(f"Architecture : [2, 3, 1]")
print(f"Nombre de couches créées : {len(network.layers)}")
print(f"Couche 1 : {len(network.layers[0].neurons)} neurones")
print(f"Couche 2 : {len(network.layers[1].neurons)} neurones")
print(f"Test {'✅ OK' if len(network.layers) == 2 else '❌ FAIL'}\n")

# Test 2 : Forward pass simple
print("=== Test 2 : Forward pass ===")
network = Network(layers=[2, 3, 1], activation='identity')
output = network.forward([1.0, 0.5])
print(f"Entrée : [1.0, 0.5]")
print(f"Sortie : {output}")
print(f"Type : {type(output)}")
print(f"Test {'✅ OK' if isinstance(output, (int, float)) else '❌ FAIL'}\n")

# Test 3 : Réseau avec plusieurs sorties
print("=== Test 3 : Plusieurs sorties ===")
network = Network(layers=[3, 4, 2], activation='relu')
output = network.forward([1.0, 0.5, -0.3])
print(f"Architecture : [3, 4, 2]")
print(f"Entrée : [1.0, 0.5, -0.3] (3 valeurs)")
print(f"Sortie : {output}")
print(f"Taille sortie : {len(output)}")
print(f"Test {'✅ OK' if len(output) == 2 else '❌ FAIL'}\n")

# Test 4 : ReLU élimine les négatifs
print("=== Test 4 : Activation ReLU ===")
network_relu = Network(layers=[2, 1], activation='relu')
network_identity = Network(layers=[2, 1], activation='identity')

inputs = [1.0, 2.0]
output_relu = network_relu.forward(inputs)
output_identity = network_identity.forward(inputs)

print(f"Entrée : {inputs}")
print(f"Sortie avec ReLU : {output_relu} (≥ 0)")
print(f"Sortie avec identité : {output_identity} (peut être < 0)")
print(f"Test {'✅ OK' if output_relu >= 0 else '❌ FAIL'}\n")

# Test 5 : Sigmoid entre 0 et 1
print("=== Test 5 : Activation Sigmoid ===")
network = Network(layers=[2, 3, 1], activation='sigmoid')
output = network.forward([10.0, 5.0])
print(f"Entrée : [10.0, 5.0]")
print(f"Sortie : {output}")
print(f"Sigmoid → sortie entre 0 et 1")
print(f"Test {'✅ OK' if 0 <= output <= 1 else '❌ FAIL'}\n")

# Test 6 : Réseau profond
print("=== Test 6 : Réseau profond ===")
network = Network(layers=[2, 5, 4, 3, 1], activation='relu')
output = network.forward([1.0, 0.5])
print(f"Architecture : [2, 5, 4, 3, 1] (4 couches cachées)")
print(f"Entrée : [1.0, 0.5]")
print(f"Sortie : {output}")
print(f"Test {'✅ OK' if isinstance(output, (int, float)) else '❌ FAIL'}\n")

print("=== Tests terminés ===")
```

**Lancer les tests :**
```bash
cd src
python test_network.py
```

---

## 🎨 Visualisation du réseau

Ajoute une méthode `summary()` pour afficher l'architecture :

```python
def summary(self):
    """
    Affiche un résumé de l'architecture du réseau.
    """
    print("=" * 50)
    print("RÉSUMÉ DU RÉSEAU")
    print("=" * 50)
    print(f"Activation : {self.activation_name}")
    print(f"Nombre de couches : {len(self.layers)}")
    print("-" * 50)
    
    for i, layer in enumerate(self.layers):
        num_neurons = len(layer.neurons)
        num_inputs = len(layer.neurons[0].weights)
        num_params = num_neurons * (num_inputs + 1)  # poids + biais
        
        print(f"Couche {i+1} : {num_neurons} neurones")
        print(f"  Entrées : {num_inputs}")
        print(f"  Paramètres : {num_params}")
        print()
    
    # Total de paramètres
    total_params = sum(
        len(layer.neurons) * (len(layer.neurons[0].weights) + 1)
        for layer in self.layers
    )
    print("-" * 50)
    print(f"TOTAL PARAMÈTRES : {total_params}")
    print("=" * 50)
```

**Usage :**
```python
network = Network([3, 5, 4, 2], activation='relu')
network.summary()
```

**Sortie :**
```
==================================================
RÉSUMÉ DU RÉSEAU
==================================================
Activation : relu
Nombre de couches : 3
--------------------------------------------------
Couche 1 : 5 neurones
  Entrées : 3
  Paramètres : 20

Couche 2 : 4 neurones
  Entrées : 5
  Paramètres : 24

Couche 3 : 2 neurones
  Entrées : 4
  Paramètres : 10

--------------------------------------------------
TOTAL PARAMÈTRES : 54
==================================================
```

---

## 🧪 Test avec le main.py fourni

Maintenant, teste avec le fichier `main.py` du projet :

```bash
cd src
python main.py
```

**Si tout fonctionne :** Tous les tests doivent passer ! ✅

---

## 🐛 Debugging

### Erreur : "IndexError: list index out of range"

**Problème :** L'architecture `layers` est mal définie.

**Solution :** Vérifie que `layers` a au moins 2 éléments :
```python
# ✅ Bon
layers = [2, 3, 1]  # Minimum 2 éléments

# ❌ Mauvais
layers = [2]  # Pas assez d'éléments
```

---

### Erreur : "ValueError: Activation inconnue"

**Problème :** Le nom de l'activation n'est pas reconnu.

**Solution :** Utilise un nom valide : `'identity'`, `'step'`, `'sigmoid'`, `'relu'`

---

### Sortie toujours 0 avec ReLU

**Problème :** Tous les neurones produisent des valeurs négatives.

**Explication :** C'est normal avec des poids aléatoires ! ReLU met à 0 les valeurs négatives.

**Solution :** Réessaye avec d'autres entrées ou recréé le réseau (poids différents).

---

## ✅ Vérification finale

Avant de considérer le projet terminé, vérifie que :

- [ ] La classe `Network` est dans `src/network.py`
- [ ] Le réseau crée le bon nombre de couches
- [ ] Les 4 activations fonctionnent (identity, step, sigmoid, relu)
- [ ] La méthode `forward()` propage correctement
- [ ] Le `main.py` fourni fonctionne sans erreur
- [ ] Tous les tests passent

---

## 🎯 Résumé

Tu as créé un **réseau de neurones complet** capable de :
1. Créer une architecture multi-couches
2. Propager un vecteur de l'entrée à la sortie
3. Utiliser 4 fonctions d'activation différentes
4. Transformer des données complexes

**Tu as maintenant un perceptron fonctionnel ! 🎉🧠**

---

## 🏆 Félicitations !

Tu as terminé la partie obligatoire du projet Toyceptron !

**Tu as codé from scratch :**
- ✅ Un neurone artificiel
- ✅ Une couche de neurones
- ✅ Un réseau multi-couches
- ✅ 4 fonctions d'activation

**Prochaines étapes :**
1. [Tests et validation](07_tests_validation.md)
2. [Bonus](08_bonus.md) (optionnel)

---

**Prochaine étape :** [07 - Tests & Validation](07_tests_validation.md)
