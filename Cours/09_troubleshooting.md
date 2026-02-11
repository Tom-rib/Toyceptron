# 09 - Troubleshooting

> Résoudre les problèmes courants

---

## 🐛 Erreurs Python courantes

### 1. ImportError / ModuleNotFoundError

```
ImportError: No module named 'neuron'
```

**Causes :**
- Le fichier `neuron.py` n'existe pas
- Tu n'es pas dans le bon dossier

**Solutions :**
```bash
# Vérifier que tu es dans le bon dossier
pwd
ls  # Doit afficher neuron.py, layer.py, network.py

# Si tu es dans toyceptron/, aller dans src/
cd src
```

---

### 2. IndexError: list index out of range

```
IndexError: list index out of range
```

**Causes :**
- Le vecteur d'entrée n'a pas la bonne taille
- L'architecture `layers` est mal définie

**Exemple d'erreur :**
```python
# Réseau créé avec layers=[2, 3, 1]
# Donc l'entrée doit avoir 2 valeurs
network = Network([2, 3, 1], 'relu')
network.forward([1])  # ❌ Erreur ! Il faut 2 valeurs
```

**Solution :**
```python
# Vérifier les dimensions
network = Network([2, 3, 1], 'relu')
print(f"Taille d'entrée attendue : {len(network.layers[0].neurons[0].weights)}")

# Utiliser la bonne taille
network.forward([1, 0.5])  # ✅ OK
```

---

### 3. TypeError: 'NoneType' object is not callable

```
TypeError: 'NoneType' object is not callable
```

**Cause :**
La fonction d'activation n'est pas passée correctement.

**Erreur typique :**
```python
# ❌ Mauvais
output = neuron.compute([1, 2], activation=relu())  # () en trop

# ✅ Bon
output = neuron.compute([1, 2], activation=relu)
```

---

### 4. ValueError: Incompatibilité dimensions

```
ValueError: Incompatibilité : 3 entrées, 2 poids
```

**Cause :**
Le nombre d'entrées ne correspond pas au nombre de poids.

**Debug :**
```python
# Ajouter des prints dans compute()
def compute(self, inputs, activation):
    print(f"Nombre d'entrées : {len(inputs)}")
    print(f"Nombre de poids : {len(self.weights)}")
    # ...
```

---

### 5. AttributeError: object has no attribute

```
AttributeError: 'Neuron' object has no attribute 'weights'
```

**Cause :**
Le constructeur `__init__` n'a pas été appelé correctement.

**Solution :**
```python
# Vérifier que __init__ définit bien les attributs
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights  # ✅ Important
        self.bias = bias        # ✅ Important
```

---

## 🔍 Problèmes logiques

### 1. La sortie est toujours la même

**Symptôme :** Peu importe l'entrée, la sortie ne change pas.

**Causes possibles :**
- Les poids sont tous à 0
- L'activation est mal implémentée

**Debug :**
```python
# Vérifier les poids
network = Network([2, 3, 1], 'relu')
for i, layer in enumerate(network.layers):
    print(f"Couche {i+1} :")
    for j, neuron in enumerate(layer.neurons):
        print(f"  Neurone {j+1} : poids={neuron.weights}, biais={neuron.bias}")
```

---

### 2. La sortie est toujours 0 avec ReLU

**Symptôme :** Le réseau retourne toujours 0.

**Explication :**
ReLU met à 0 toutes les valeurs négatives. Si tous les neurones produisent des valeurs négatives, la sortie sera 0.

**C'est normal !** Avec des poids aléatoires, il peut arriver que :
```
z = Σ(wi · xi) + b < 0
ReLU(z) = 0
```

**Solutions :**
1. Essayer d'autres entrées
2. Recréer le réseau (nouveaux poids aléatoires)
3. Utiliser une autre activation (identity, sigmoid)

---

### 3. Sigmoid retourne toujours ~0.5

**Symptôme :** Toutes les sorties sont proches de 0.5.

**Explication :**
Si z est proche de 0, alors `sigmoid(0) ≈ 0.5`.

**C'est normal** si les poids sont très petits ou si les entrées sont nulles.

**Test :**
```python
import math
print(math.exp(-0))  # 1
print(1 / (1 + 1))   # 0.5
```

---

### 4. Les résultats changent à chaque exécution

**Symptôme :** Relancer le programme donne des résultats différents.

**Explication :**
Les poids sont initialisés **aléatoirement** !

**C'est normal !** Si tu veux des résultats reproductibles :

```python
import random
random.seed(42)  # Fixer la seed

# Maintenant les résultats seront toujours les mêmes
network = Network([2, 3, 1], 'relu')
```

---

## 🧪 Méthodes de debugging

### 1. Utiliser des prints

```python
# Dans neuron.py
def compute(self, inputs, activation):
    print(f"[DEBUG] Entrées : {inputs}")
    print(f"[DEBUG] Poids : {self.weights}")
    print(f"[DEBUG] Biais : {self.bias}")
    
    z = self.weighted_sum(inputs)
    print(f"[DEBUG] z (avant activation) : {z}")
    
    y = activation(z)
    print(f"[DEBUG] y (après activation) : {y}")
    
    return y
```

---

### 2. Tester avec des valeurs simples

**Toujours commencer par des valeurs faciles à calculer :**

```python
# Test simple : poids=[1, 1, 1], biais=0, activation=identity
neuron = Neuron([1, 1, 1], 0)
result = neuron.compute([1, 2, 3], lambda x: x)
# Résultat attendu : 1+2+3 = 6

if result == 6:
    print("✅ Neurone fonctionne")
else:
    print(f"❌ Attendu 6, obtenu {result}")
```

---

### 3. Vérifier les dimensions

```python
# Script pour vérifier toutes les dimensions
def check_dimensions(network):
    print("=== Vérification des dimensions ===")
    
    for i, layer in enumerate(network.layers):
        print(f"Couche {i+1} :")
        print(f"  Neurones : {len(layer.neurons)}")
        print(f"  Poids par neurone : {len(layer.neurons[0].weights)}")
    
    print("\nVérification : OK ✅")

network = Network([2, 5, 3, 1], 'relu')
check_dimensions(network)
```

---

### 4. Tester étape par étape

**Ne pas tout coder d'un coup !**

```python
# Étape 1 : Tester le neurone seul
neuron = Neuron([1, 1], 0)
print(neuron.compute([2, 3], lambda x: x))  # Doit afficher 5

# Étape 2 : Tester une couche
layer = Layer(2, 2)
print(len(layer.forward([1, 1], lambda x: x)))  # Doit afficher 2

# Étape 3 : Tester le réseau
network = Network([2, 3, 1], 'relu')
print(network.forward([1, 1]))  # Doit afficher un nombre
```

---

## 🚨 Cas spéciaux

### 1. Overflow avec exponentielles

**Erreur :**
```
OverflowError: math range error
```

**Cause :**
`math.exp(-x)` avec x très grand → overflow

**Solution :**
```python
# Dans get_activation()
def sigmoid(x):
    # Limiter x pour éviter l'overflow
    if x > 500:
        return 1.0
    if x < -500:
        return 0.0
    return 1 / (1 + math.exp(-x))
```

---

### 2. Division par zéro

**Erreur :**
```
ZeroDivisionError: division by zero
```

**Cause :**
Rare, mais peut arriver avec certaines fonctions custom.

**Solution :**
Ajouter des vérifications :
```python
def safe_divide(a, b):
    if b == 0:
        return 0
    return a / b
```

---

## 📊 Checklist de debug

Quand quelque chose ne marche pas, vérifie dans l'ordre :

1. **Imports**
   - [ ] Tous les fichiers .py existent
   - [ ] Les imports sont corrects

2. **Structure des classes**
   - [ ] `__init__` définit tous les attributs
   - [ ] Les méthodes sont bien indentées dans la classe

3. **Dimensions**
   - [ ] Le vecteur d'entrée a la bonne taille
   - [ ] Chaque couche a le bon nombre de poids

4. **Fonctions d'activation**
   - [ ] Les fonctions sont bien des fonctions (pas des appels)
   - [ ] Elles retournent un nombre

5. **Logique**
   - [ ] Le produit scalaire est correct
   - [ ] L'activation est appliquée
   - [ ] Le forward pass propage bien à travers toutes les couches

---

## 🛠️ Outils de debug

### Script de diagnostic complet

```python
# diagnostic.py
"""Script pour diagnostiquer les problèmes"""

def test_neuron():
    try:
        from neuron import Neuron
        n = Neuron([1, 1], 0)
        result = n.compute([1, 1], lambda x: x)
        assert result == 2, f"Attendu 2, obtenu {result}"
        print("✅ Neuron : OK")
        return True
    except Exception as e:
        print(f"❌ Neuron : {e}")
        return False

def test_layer():
    try:
        from layer import Layer
        l = Layer(2, 2)
        result = l.forward([1, 1], lambda x: x)
        assert len(result) == 2, f"Attendu 2 sorties, obtenu {len(result)}"
        print("✅ Layer : OK")
        return True
    except Exception as e:
        print(f"❌ Layer : {e}")
        return False

def test_network():
    try:
        from network import Network
        net = Network([2, 3, 1], 'relu')
        result = net.forward([1, 1])
        assert isinstance(result, (int, float)), f"Attendu un nombre, obtenu {type(result)}"
        print("✅ Network : OK")
        return True
    except Exception as e:
        print(f"❌ Network : {e}")
        return False

if __name__ == "__main__":
    print("=== DIAGNOSTIC TOYCEPTRON ===\n")
    results = [
        test_neuron(),
        test_layer(),
        test_network()
    ]
    
    if all(results):
        print("\n🎉 Tout fonctionne !")
    else:
        print("\n⚠️ Certains composants ont des problèmes")
```

---

## 💡 Conseils généraux

1. **Lis les erreurs attentivement**
   - Python donne souvent la ligne exacte du problème
   - Le dernier message d'erreur est le plus important

2. **Google est ton ami**
   - Cherche le message d'erreur exact
   - Regarde Stack Overflow

3. **Teste par petits morceaux**
   - Ne code pas tout d'un coup
   - Teste chaque fonction dès qu'elle est écrite

4. **Prends des pauses**
   - Si tu bloques, fais une pause
   - Reviens avec un regard frais

5. **Demande de l'aide**
   - À tes camarades
   - À ton prof
   - Sur des forums (discord, reddit, etc.)

---

## 📞 Où trouver de l'aide

- **Documentation Python** : [docs.python.org](https://docs.python.org/fr/3/)
- **Stack Overflow** : Cherche ton erreur
- **Discord de ta promo** : Demande à tes camarades
- **GitHub Issues** : Crée une issue sur ton dépôt

---

**Prochaine étape :** [10 - Annexes](10_annexes.md)
