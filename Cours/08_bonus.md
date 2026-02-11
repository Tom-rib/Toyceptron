# 08 - Bonus

> Fonctionnalités avancées pour aller plus loin (optionnel)

---

## 🎯 À faire APRÈS la partie obligatoire

Les bonus ne doivent être entrepris **qu'une fois** que :
- ✅ Toutes les classes fonctionnent
- ✅ Le main.py fourni fonctionne
- ✅ Tous les tests passent

**Ces bonus sont classés par difficulté croissante.**

---

## ⭐ Niveau 1 : Facile

### Bonus 1 : Méthode summary()

Ajoute une méthode qui affiche l'architecture du réseau.

**Implémentation :**
```python
# Dans network.py
def summary(self):
    """
    Affiche un résumé de l'architecture du réseau.
    """
    print("=" * 60)
    print("ARCHITECTURE DU RÉSEAU")
    print("=" * 60)
    print(f"Fonction d'activation : {self.activation_name}")
    print(f"Nombre total de couches : {len(self.layers)}")
    print()
    
    for i, layer in enumerate(self.layers):
        num_neurons = len(layer.neurons)
        num_inputs = len(layer.neurons[0].weights)
        num_params = num_neurons * (num_inputs + 1)  # poids + biais
        
        print(f"Couche {i+1}:")
        print(f"  - Neurones : {num_neurons}")
        print(f"  - Entrées par neurone : {num_inputs}")
        print(f"  - Paramètres : {num_params}")
    
    # Total des paramètres
    total = sum(len(l.neurons) * (len(l.neurons[0].weights) + 1) 
                for l in self.layers)
    print()
    print("=" * 60)
    print(f"TOTAL DES PARAMÈTRES : {total}")
    print("=" * 60)
```

**Usage :**
```python
network = Network([2, 5, 3, 1], 'relu')
network.summary()
```

---

### Bonus 2 : Vérifications d'erreurs

Ajoute des validations pour éviter les erreurs silencieuses.

**Dans Neuron :**
```python
def compute(self, inputs, activation):
    # Vérifier les dimensions
    if len(inputs) != len(self.weights):
        raise ValueError(
            f"Incompatibilité : {len(inputs)} entrées, "
            f"{len(self.weights)} poids attendus"
        )
    
    # Vérifier le type d'activation
    if not callable(activation):
        raise TypeError("activation doit être une fonction")
    
    # Calcul normal
    z = self.weighted_sum(inputs)
    return activation(z)
```

**Dans Network :**
```python
def __init__(self, layers, activation='relu'):
    # Vérifier que layers a au moins 2 éléments
    if len(layers) < 2:
        raise ValueError(
            "layers doit avoir au moins 2 éléments "
            "(entrée et sortie)"
        )
    
    # Vérifier que les tailles sont positives
    if any(size <= 0 for size in layers):
        raise ValueError("Toutes les tailles doivent être > 0")
    
    # Suite du constructeur...
```

---

### Bonus 3 : Méthode __str__

Ajoute des représentations textuelles lisibles.

**Dans Neuron :**
```python
def __str__(self):
    return f"Neuron(weights={self.weights}, bias={self.bias})"
```

**Dans Layer :**
```python
def __str__(self):
    return f"Layer({len(self.neurons)} neurones)"
```

**Dans Network :**
```python
def __str__(self):
    sizes = [len(self.layers[0].neurons[0].weights)]
    sizes += [len(layer.neurons) for layer in self.layers]
    return f"Network({sizes}, activation='{self.activation_name}')"
```

---

## ⭐⭐ Niveau 2 : Moyen

### Bonus 4 : Activations différentes par couche

Permet de spécifier une activation différente pour chaque couche.

**Modification de Network :**
```python
def __init__(self, layers, activations):
    """
    Args:
        layers (list): Architecture [in, h1, h2, out]
        activations (list ou str): 
            - str : même activation pour toutes les couches
            - list : une activation par couche
    """
    self.layers = []
    
    # Si activations est un string, le répéter
    if isinstance(activations, str):
        activations = [activations] * (len(layers) - 1)
    
    # Vérifier la longueur
    if len(activations) != len(layers) - 1:
        raise ValueError(
            f"Il faut {len(layers)-1} activations, "
            f"{len(activations)} fournies"
        )
    
    # Créer les couches avec leurs activations
    for i in range(1, len(layers)):
        layer = Layer(layers[i], layers[i-1])
        self.layers.append((layer, activations[i-1]))
    
def forward(self, inputs):
    current = inputs
    for layer, activation_name in self.layers:
        activation = self.get_activation(activation_name)
        current = layer.forward(current, activation)
    
    if len(current) == 1:
        return current[0]
    return current
```

**Usage :**
```python
# Activation différente par couche
network = Network(
    layers=[2, 5, 3, 1],
    activations=['relu', 'relu', 'sigmoid']
)
```

---

### Bonus 5 : forward_debug()

Affiche toutes les valeurs intermédiaires.

```python
def forward_debug(self, inputs):
    """
    Forward pass avec affichage des valeurs intermédiaires.
    """
    print("\n" + "=" * 70)
    print("FORWARD PASS DEBUG")
    print("=" * 70)
    print(f"Entrée initiale : {inputs}\n")
    
    current = inputs
    
    for i, layer in enumerate(self.layers):
        print(f"--- Couche {i+1} ({len(layer.neurons)} neurones) ---")
        print(f"Entrée : {current}")
        
        # Afficher chaque neurone
        outputs = []
        for j, neuron in enumerate(layer.neurons):
            z = neuron.weighted_sum(current)
            y = self.activation(z)
            print(f"  Neurone {j+1}: z={z:.4f}, y={y:.4f}")
            outputs.append(y)
        
        current = outputs
        print(f"Sortie : {current}\n")
    
    print("=" * 70)
    print(f"SORTIE FINALE : {current}")
    print("=" * 70 + "\n")
    
    if len(current) == 1:
        return current[0]
    return current
```

---

### Bonus 6 : Perceptron binaire AND/OR

Crée un perceptron qui approxime AND et OR avec des poids fixés.

```python
# bonus_logic_gates.py
from network import Network
from neuron import Neuron

def create_and_gate():
    """Crée un réseau qui implémente AND"""
    network = Network([2, 1], 'step')
    # AND : w1=1, w2=1, b=-1.5
    # Sortie = 1 ssi x1·1 + x2·1 - 1.5 >= 0
    # => x1 + x2 >= 1.5 => les deux doivent être à 1
    network.layers[0].neurons[0] = Neuron([1, 1], -1.5)
    return network

def create_or_gate():
    """Crée un réseau qui implémente OR"""
    network = Network([2, 1], 'step')
    # OR : w1=1, w2=1, b=-0.5
    network.layers[0].neurons[0] = Neuron([1, 1], -0.5)
    return network

# Tests
print("=== AND Gate ===")
and_gate = create_and_gate()
for x1 in [0, 1]:
    for x2 in [0, 1]:
        output = and_gate.forward([x1, x2])
        print(f"{x1} AND {x2} = {output}")

print("\n=== OR Gate ===")
or_gate = create_or_gate()
for x1 in [0, 1]:
    for x2 in [0, 1]:
        output = or_gate.forward([x1, x2])
        print(f"{x1} OR {x2} = {output}")
```

---

## ⭐⭐⭐ Niveau 3 : Difficile

### Bonus 7 : Démontrer que XOR est impossible

Montre qu'un réseau **sans couche cachée** ne peut pas représenter XOR.

```python
# bonus_xor_impossible.py
"""
Démonstration : un perceptron simple ne peut pas apprendre XOR.

Table de vérité XOR :
0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0

Un seul neurone fait : y = step(w1·x1 + w2·x2 + b)
Cela trace une ligne dans l'espace 2D.
XOR n'est pas linéairement séparable !
"""

from network import Network
from neuron import Neuron

def try_xor_simple():
    """Essaie de faire XOR avec un seul neurone"""
    
    print("=== Tentative XOR avec 1 neurone ===\n")
    
    # Essayer plusieurs combinaisons de poids
    test_configs = [
        ([1, 1], -0.5),   # Comme OR
        ([1, 1], -1.5),   # Comme AND
        ([1, -1], 0),     # Asymétrique
        ([2, 2], -1.5),   # Poids plus grands
    ]
    
    xor_truth = [
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1),
        ([1, 1], 0),
    ]
    
    for weights, bias in test_configs:
        print(f"Test avec poids={weights}, biais={bias}")
        network = Network([2, 1], 'step')
        network.layers[0].neurons[0] = Neuron(weights, bias)
        
        correct = 0
        for inputs, expected in xor_truth:
            output = network.forward(inputs)
            status = '✅' if output == expected else '❌'
            print(f"  {inputs} → {output} (attendu {expected}) {status}")
            if output == expected:
                correct += 1
        
        print(f"Score : {correct}/4\n")
    
    print("Conclusion : AUCUNE configuration ne donne 4/4 !")
    print("XOR nécessite au moins 1 couche cachée.\n")

try_xor_simple()
```

**Puis résous-le avec une couche cachée :**
```python
def create_xor_network():
    """XOR avec une couche cachée [2→2→1]"""
    network = Network([2, 2, 1], 'step')
    
    # Couche cachée : crée AND et NAND
    network.layers[0].neurons[0] = Neuron([1, 1], -1.5)   # AND
    network.layers[0].neurons[1] = Neuron([-1, -1], 0.5)  # NAND
    
    # Couche sortie : AND de (x1 OR x2) ET (NOT(x1 AND x2))
    network.layers[1].neurons[0] = Neuron([1, 1], -1.5)
    
    return network

xor_net = create_xor_network()
print("=== XOR avec couche cachée ===")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        output = xor_net.forward([x1, x2])
        print(f"{x1} XOR {x2} = {output}")
```

---

### Bonus 8 : Traitement par batch

Permet de passer plusieurs vecteurs en même temps.

```python
def forward_batch(self, batch_inputs):
    """
    Propage un batch d'entrées.
    
    Args:
        batch_inputs (list of list): [[x1], [x2], ...]
        
    Returns:
        list: [output1, output2, ...]
    """
    return [self.forward(inputs) for inputs in batch_inputs]
```

**Usage :**
```python
network = Network([2, 3, 1], 'relu')
batch = [
    [1.0, 0.5],
    [0.3, 0.7],
    [-0.2, 1.0]
]
outputs = network.forward_batch(batch)
print(outputs)  # [y1, y2, y3]
```

---

### Bonus 9 : Sérialisation (sauvegarder le réseau)

Permet de sauvegarder et charger les poids du réseau.

**Format simple en CSV :**
```python
# Dans network.py
def save(self, filename):
    """
    Sauvegarde les poids dans un fichier.
    
    Format CSV :
    layer_id,neuron_id,weights,bias
    0,0,"[0.5, -0.3, 0.2]",0.1
    ...
    """
    with open(filename, 'w') as f:
        f.write("layer_id,neuron_id,weights,bias\n")
        
        for i, layer in enumerate(self.layers):
            for j, neuron in enumerate(layer.neurons):
                weights_str = str(neuron.weights)
                f.write(f"{i},{j},\"{weights_str}\",{neuron.bias}\n")
    
    print(f"Réseau sauvegardé dans {filename}")

def load(self, filename):
    """
    Charge les poids depuis un fichier.
    """
    import ast
    
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]  # Skip header
        
        for line in lines:
            layer_id, neuron_id, weights_str, bias = line.strip().split(',')
            layer_id = int(layer_id)
            neuron_id = int(neuron_id)
            
            # Parse weights string
            weights_str = weights_str.strip('"')
            weights = ast.literal_eval(weights_str)
            bias = float(bias)
            
            # Mettre à jour le neurone
            self.layers[layer_id].neurons[neuron_id].weights = weights
            self.layers[layer_id].neurons[neuron_id].bias = bias
    
    print(f"Réseau chargé depuis {filename}")
```

**Usage :**
```python
# Créer et sauvegarder
network = Network([2, 5, 1], 'relu')
network.save('my_network.csv')

# Charger
new_network = Network([2, 5, 1], 'relu')
new_network.load('my_network.csv')
```

---

## ⭐⭐⭐⭐ Niveau 4 : Expert

### Bonus 10 : Utiliser numpy

Refactorise tout le projet pour utiliser numpy (plus efficace).

```python
# neuron_numpy.py
import numpy as np

class Neuron:
    def __init__(self, weights, bias):
        self.weights = np.array(weights)
        self.bias = bias
    
    def compute(self, inputs, activation):
        inputs = np.array(inputs)
        z = np.dot(self.weights, inputs) + self.bias
        return activation(z)
```

**Attention :** Cela change la contrainte du projet (pas de libs externes).  
À faire seulement si tu as d'abord réussi avec des listes !

---

## 🎯 Checklist des bonus

Coche ceux que tu as implémentés :

- [ ] Bonus 1 : `summary()`
- [ ] Bonus 2 : Vérifications d'erreurs
- [ ] Bonus 3 : `__str__()`
- [ ] Bonus 4 : Activations par couche
- [ ] Bonus 5 : `forward_debug()`
- [ ] Bonus 6 : AND/OR gates
- [ ] Bonus 7 : XOR impossible sans couche cachée
- [ ] Bonus 8 : Batch processing
- [ ] Bonus 9 : Sérialisation
- [ ] Bonus 10 : Numpy

---

## 📚 Idées bonus supplémentaires

- Ajouter d'autres activations : tanh, leaky ReLU, softmax
- Implémenter un réseau récurrent (RNN) simple
- Visualiser le réseau avec matplotlib
- Créer une interface graphique (tkinter)
- Implémenter la backpropagation (entraînement) !

---

**Prochaine étape :** [09 - Troubleshooting](09_troubleshooting.md)
