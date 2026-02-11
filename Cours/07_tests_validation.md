# 07 - Tests & Validation

> Vérifier que ton réseau de neurones fonctionne correctement

---

## 🎯 Objectif

S'assurer que toutes les classes fonctionnent individuellement **ET** ensemble dans le réseau complet.

---

## ✅ Checklist de validation

### Neuron ✓
- [ ] Stocke correctement les poids et le biais
- [ ] Calcule le produit scalaire correctement
- [ ] Applique la fonction d'activation
- [ ] Retourne un nombre (float)

### Layer ✓
- [ ] Crée le bon nombre de neurones
- [ ] Chaque neurone a le bon nombre de poids
- [ ] La méthode `forward()` retourne une liste
- [ ] La taille de sortie = nombre de neurones

### Network ✓
- [ ] Crée le bon nombre de couches
- [ ] Les couches sont bien connectées
- [ ] Les 4 activations fonctionnent
- [ ] La sortie finale a la bonne taille

---

## 🧪 Tests unitaires

### Test 1 : Neurone avec valeurs simples

```python
# test_neuron_simple.py
from neuron import Neuron

def identity(x):
    return x

# Test avec des valeurs faciles à calculer
neuron = Neuron(weights=[1, 1, 1], bias=0)
result = neuron.compute([2, 3, 4], activation=identity)

print(f"Test Neuron simple")
print(f"Entrée : [2, 3, 4]")
print(f"Poids : [1, 1, 1], Biais : 0")
print(f"Calcul : 2*1 + 3*1 + 4*1 + 0 = 9")
print(f"Résultat obtenu : {result}")
print(f"{'✅ PASS' if result == 9 else '❌ FAIL'}")
```

---

### Test 2 : Layer avec 2 neurones identiques

```python
# test_layer_fixed.py
from neuron import Neuron
from layer import Layer

def identity(x):
    return x

# Créer une couche manuellement avec des poids fixes
layer = Layer(num_neurons=2, num_inputs=2)

# Remplacer par des neurones avec poids fixes
layer.neurons[0] = Neuron(weights=[1, 1], bias=0)
layer.neurons[1] = Neuron(weights=[2, 2], bias=0)

# Test
result = layer.forward([1, 2], activation=identity)

print(f"Test Layer avec poids fixes")
print(f"Neurone 1 : [1, 1] → 1*1 + 2*1 = 3")
print(f"Neurone 2 : [2, 2] → 1*2 + 2*2 = 6")
print(f"Résultat attendu : [3, 6]")
print(f"Résultat obtenu : {result}")
print(f"{'✅ PASS' if result == [3, 6] else '❌ FAIL'}")
```

---

### Test 3 : Network avec architecture simple

```python
# test_network_simple.py
from network import Network

# Créer un réseau très simple
network = Network(layers=[2, 1], activation='identity')

# Entrée simple
result = network.forward([1, 1])

print(f"Test Network [2→1] avec identité")
print(f"Entrée : [1, 1]")
print(f"Sortie : {result}")
print(f"Type : {type(result)} (doit être float)")
print(f"{'✅ PASS' if isinstance(result, (int, float)) else '❌ FAIL'}")
```

---

## 🔬 Tests d'intégration

### Test complet : AND logique

Crée un réseau qui approxime la fonction AND :

```python
# test_and_gate.py
from network import Network
from neuron import Neuron

# Créer un réseau [2→1]
network = Network(layers=[2, 1], activation='step')

# Remplacer le neurone par des poids fixes pour AND
# AND : sortie = 1 si x1=1 ET x2=1, sinon 0
network.layers[0].neurons[0] = Neuron(weights=[1, 1], bias=-1.5)

# Table de vérité AND
test_cases = [
    ([0, 0], 0),  # 0 AND 0 = 0
    ([0, 1], 0),  # 0 AND 1 = 0
    ([1, 0], 0),  # 1 AND 0 = 0
    ([1, 1], 1),  # 1 AND 1 = 1
]

print("=== Test AND Gate ===")
all_pass = True

for inputs, expected in test_cases:
    output = network.forward(inputs)
    status = '✅' if output == expected else '❌'
    print(f"{inputs} → {output} (attendu: {expected}) {status}")
    if output != expected:
        all_pass = False

print(f"\nRésultat : {'✅ TOUS LES TESTS PASSENT' if all_pass else '❌ ÉCHEC'}")
```

---

### Test complet : OR logique

```python
# test_or_gate.py
from network import Network
from neuron import Neuron

network = Network(layers=[2, 1], activation='step')

# OR : sortie = 1 si x1=1 OU x2=1
network.layers[0].neurons[0] = Neuron(weights=[1, 1], bias=-0.5)

test_cases = [
    ([0, 0], 0),  # 0 OR 0 = 0
    ([0, 1], 1),  # 0 OR 1 = 1
    ([1, 0], 1),  # 1 OR 0 = 1
    ([1, 1], 1),  # 1 OR 1 = 1
]

print("=== Test OR Gate ===")
all_pass = True

for inputs, expected in test_cases:
    output = network.forward(inputs)
    status = '✅' if output == expected else '❌'
    print(f"{inputs} → {output} (attendu: {expected}) {status}")
    if output != expected:
        all_pass = False

print(f"\nRésultat : {'✅ TOUS LES TESTS PASSENT' if all_pass else '❌ ÉCHEC'}")
```

---

## 🎮 Tests avec main.py

### Vérifier que main.py fonctionne

```bash
cd src
python main.py
```

**Sortie attendue :**
- Aucune erreur Python
- Des valeurs numériques en sortie
- Pas de `None` ou de crash

---

## 🔍 Tests de propriétés

### Test 1 : Vérifier les dimensions

```python
# test_dimensions.py
from network import Network

def test_dimensions():
    """Vérifie que les dimensions sont correctes"""
    
    # Test 1 : [2, 3, 1]
    network = Network([2, 3, 1], 'relu')
    output = network.forward([1.0, 0.5])
    assert isinstance(output, (int, float)), "Sortie doit être un scalaire"
    
    # Test 2 : [3, 5, 2]
    network = Network([3, 5, 2], 'relu')
    output = network.forward([1.0, 0.5, -0.3])
    assert len(output) == 2, "Sortie doit avoir 2 valeurs"
    
    # Test 3 : [4, 8, 6, 3]
    network = Network([4, 8, 6, 3], 'sigmoid')
    output = network.forward([1, 2, 3, 4])
    assert len(output) == 3, "Sortie doit avoir 3 valeurs"
    
    print("✅ Tous les tests de dimensions passent")

test_dimensions()
```

---

### Test 2 : Vérifier les activations

```python
# test_activations.py
from network import Network
import math

def test_activations():
    """Vérifie que toutes les activations fonctionnent"""
    
    inputs = [1.0, 0.5]
    
    # Test identity
    net = Network([2, 1], 'identity')
    output = net.forward(inputs)
    print(f"Identity : {output} (peut être n'importe quel nombre)")
    
    # Test step
    net = Network([2, 1], 'step')
    output = net.forward(inputs)
    assert output in [0, 1], "Step doit retourner 0 ou 1"
    print(f"Step : {output} ✅")
    
    # Test sigmoid
    net = Network([2, 1], 'sigmoid')
    output = net.forward(inputs)
    assert 0 <= output <= 1, "Sigmoid doit être entre 0 et 1"
    print(f"Sigmoid : {output:.4f} (entre 0 et 1) ✅")
    
    # Test relu
    net = Network([2, 1], 'relu')
    output = net.forward(inputs)
    assert output >= 0, "ReLU doit être >= 0"
    print(f"ReLU : {output:.4f} (>= 0) ✅")
    
    print("\n✅ Toutes les activations fonctionnent")

test_activations()
```

---

## 📊 Tests de robustesse

### Test avec entrées extrêmes

```python
# test_extreme_inputs.py
from network import Network

network = Network([3, 5, 2], 'relu')

# Test 1 : Valeurs très grandes
output = network.forward([1000, 2000, 3000])
print(f"Entrées grandes : {output}")

# Test 2 : Valeurs très petites
output = network.forward([0.001, 0.002, 0.003])
print(f"Entrées petites : {output}")

# Test 3 : Valeurs négatives
output = network.forward([-10, -20, -30])
print(f"Entrées négatives : {output}")

# Test 4 : Zéros
output = network.forward([0, 0, 0])
print(f"Entrées nulles : {output}")

print("\n✅ Le réseau gère les entrées extrêmes")
```

---

## 🐛 Tests de débogage

### Activer le mode debug

Ajoute des prints dans `forward()` pour voir ce qui se passe :

```python
# Dans network.py
def forward(self, inputs):
    """Version debug"""
    print(f"\n=== Forward pass ===")
    print(f"Entrée : {inputs}")
    
    current = inputs
    
    for i, layer in enumerate(self.layers):
        print(f"\n--- Couche {i+1} ---")
        print(f"  Entrée couche : {current}")
        current = layer.forward(current, self.activation)
        print(f"  Sortie couche : {current}")
    
    print(f"\n=== Sortie finale : {current} ===\n")
    
    if len(current) == 1:
        return current[0]
    return current
```

---

## 🎯 Script de test complet

Crée un fichier `run_all_tests.py` qui lance tous les tests :

```python
# run_all_tests.py
"""
Lance tous les tests du projet Toyceptron
"""

import sys

def run_test(test_name, test_func):
    """Exécute un test et affiche le résultat"""
    try:
        print(f"\n{'='*60}")
        print(f"Test: {test_name}")
        print('='*60)
        test_func()
        print(f"✅ {test_name} RÉUSSI")
        return True
    except Exception as e:
        print(f"❌ {test_name} ÉCHOUÉ")
        print(f"Erreur : {e}")
        return False

# Tests à lancer
def test_neuron():
    from neuron import Neuron
    n = Neuron([1, 1], 0)
    assert n.compute([1, 2], lambda x: x) == 3

def test_layer():
    from layer import Layer
    layer = Layer(3, 2)
    output = layer.forward([1, 1], lambda x: x)
    assert len(output) == 3

def test_network():
    from network import Network
    net = Network([2, 3, 1], 'relu')
    output = net.forward([1, 1])
    assert isinstance(output, (int, float))

# Lancer tous les tests
if __name__ == "__main__":
    tests = [
        ("Neuron", test_neuron),
        ("Layer", test_layer),
        ("Network", test_network),
    ]
    
    results = []
    for name, func in tests:
        results.append(run_test(name, func))
    
    # Résumé
    print(f"\n{'='*60}")
    print(f"RÉSUMÉ DES TESTS")
    print('='*60)
    passed = sum(results)
    total = len(results)
    print(f"Tests réussis : {passed}/{total}")
    
    if passed == total:
        print("🎉 TOUS LES TESTS PASSENT ! 🎉")
        sys.exit(0)
    else:
        print("❌ Certains tests ont échoué")
        sys.exit(1)
```

**Lancer tous les tests :**
```bash
cd src
python run_all_tests.py
```

---

## ✅ Validation finale

### Checklist avant de rendre le projet

- [ ] Tous les fichiers Python sont créés (neuron.py, layer.py, network.py)
- [ ] Le code est commenté et lisible
- [ ] Les tests unitaires passent
- [ ] Le main.py fourni fonctionne
- [ ] Les 4 activations fonctionnent
- [ ] Le README.md est complet
- [ ] Le code est sur GitHub

---

## 🏆 Critères de réussite

| Critère | Points | Validation |
|---------|--------|------------|
| Neuron fonctionne | ⭐⭐ | Tests passent |
| Layer fonctionne | ⭐⭐ | Tests passent |
| Network fonctionne | ⭐⭐⭐ | main.py OK |
| 4 activations implémentées | ⭐ | Toutes testées |
| Code propre et commenté | ⭐ | Lisible |
| Documentation complète | ⭐ | README.md |

**Total : ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10 étoiles)**

---

## 🎓 Conclusion

Si tous tes tests passent, **félicitations** ! 🎉

Tu as créé un réseau de neurones fonctionnel from scratch, sans aucune bibliothèque externe.

**Tu comprends maintenant :**
- Comment un neurone effectue un calcul
- Comment une couche transforme des données
- Comment un réseau propage l'information
- Comment les fonctions d'activation influencent la sortie

---

**Prochaine étape :** [08 - Bonus](08_bonus.md) (optionnel)
