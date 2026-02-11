# 03 - Préparation

> Avant de coder, préparons l'environnement et vérifions les prérequis.

---

## ✅ Prérequis

### 1. Python installé

**Vérifier la version :**
```bash
python --version
# ou
python3 --version
```

**Version requise :** Python 3.8 ou supérieur

**Si Python n'est pas installé :**
- **Windows :** [python.org/downloads](https://www.python.org/downloads/)
- **macOS :** `brew install python3`
- **Linux :** `sudo apt install python3`

---

### 2. Éditeur de code

Utilise un éditeur qui te plaît :
- **VS Code** (recommandé) - Extensions Python disponibles
- **PyCharm** - IDE complet pour Python
- **Sublime Text** - Léger et rapide
- **Vim/Nano** - Pour les puristes

---

### 3. Git installé (optionnel mais recommandé)

**Vérifier :**
```bash
git --version
```

**Installer Git :**
- **Windows :** [git-scm.com](https://git-scm.com/)
- **macOS :** `brew install git`
- **Linux :** `sudo apt install git`

---

## 🗂️ Structure du projet

Crée cette arborescence de fichiers et dossiers :

```
toyceptron/
│
├── README.md                   # Présentation du projet
│
├── cours/                      # 📚 Documentation pédagogique
│   ├── 01_introduction.md
│   ├── 02_concepts_theoriques.md
│   ├── 03_preparation.md       ← Tu es ici
│   ├── 04_implementation_neuron.md
│   ├── 05_implementation_layer.md
│   ├── 06_implementation_network.md
│   ├── 07_tests_validation.md
│   ├── 08_bonus.md
│   ├── 09_troubleshooting.md
│   └── 10_annexes.md
│
├── src/                        # 💻 Code source
│   ├── neuron.py               # À créer
│   ├── layer.py                # À créer
│   ├── network.py              # À créer
│   └── main.py                 # Fourni (à copier)
│
├── tests/                      # 🧪 Tests personnalisés (optionnel)
│   └── test_examples.py
│
├── docs/                       # 📊 Schémas (optionnel)
│   └── schemas/
│       └── architecture.txt
│
└── .gitignore                  # Fichiers à ignorer par Git
```

---

## 🚀 Création du projet

### Étape 1 : Créer le dossier principal

```bash
# Créer le dossier du projet
mkdir toyceptron
cd toyceptron
```

---

### Étape 2 : Initialiser Git (optionnel)

```bash
# Initialiser un dépôt Git
git init

# Créer le fichier .gitignore
touch .gitignore
```

**Contenu du `.gitignore` :**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Autres
*.log
.pytest_cache/
```

---

### Étape 3 : Créer la structure

```bash
# Créer les dossiers
mkdir -p cours src tests docs/schemas

# Créer les fichiers Python (vides pour l'instant)
touch src/neuron.py
touch src/layer.py
touch src/network.py

# Créer le README
touch README.md
```

---

### Étape 4 : Récupérer le fichier main.py

**Option A : Copier depuis le PDF du projet**

Crée `src/main.py` et copie le contenu fourni dans le PDF.

**Option B : Exemple de main.py simplifié**

Si tu n'as pas le fichier, voici un exemple basique :

```python
# src/main.py
from neuron import Neuron
from layer import Layer
from network import Network
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def main():
    print("=== Test Toyceptron ===\n")
    
    # Test 1 : Créer un neurone
    print("Test 1 : Neurone simple")
    neuron = Neuron(weights=[0.5, -0.3, 0.2], bias=0.1)
    output = neuron.compute([1.0, 2.0, 3.0], activation=lambda x: max(0, x))
    print(f"Sortie neurone : {output}\n")
    
    # Test 2 : Créer une couche
    print("Test 2 : Couche de neurones")
    layer = Layer(num_neurons=3, num_inputs=2)
    output = layer.forward([1.0, 0.5], activation=sigmoid)
    print(f"Sortie couche : {output}\n")
    
    # Test 3 : Créer un réseau
    print("Test 3 : Réseau complet")
    network = Network(layers=[2, 4, 3, 1], activation='relu')
    output = network.forward([1.0, 0.5])
    print(f"Sortie réseau : {output}\n")
    
    print("=== Tests terminés ===")

if __name__ == "__main__":
    main()
```

---

## 🧪 Vérifier l'environnement

### Test Python

Crée un fichier `test_env.py` :
```python
import sys
print(f"Python version : {sys.version}")
print(f"Python OK ✅")
```

Lance-le :
```bash
cd toyceptron
python src/test_env.py
```

**Sortie attendue :**
```
Python version : 3.x.x
Python OK ✅
```

---

## 📋 Checklist de préparation

Avant de commencer à coder, vérifie que :

- [ ] Python 3.8+ est installé
- [ ] La structure de dossiers est créée
- [ ] Le fichier `main.py` est dans `src/`
- [ ] Le fichier `.gitignore` est créé (si tu uses Git)
- [ ] Ton éditeur de code est configuré
- [ ] Tu as lu les concepts théoriques (`02_concepts_theoriques.md`)

---

## 🎯 Comprendre le fichier main.py

Avant de coder, **lis attentivement le fichier `main.py`** fourni.

Pose-toi ces questions :
1. Quelles classes sont importées ?
2. Quelles méthodes doivent exister dans chaque classe ?
3. Quels sont les paramètres des constructeurs ?
4. Quel est le format des entrées et sorties ?

**Exemple d'analyse :**
```python
# Si tu vois :
neuron = Neuron(weights=[0.5, -0.3], bias=0.1)
output = neuron.compute([1.0, 2.0], activation=relu)

# Cela signifie que la classe Neuron doit avoir :
# - Un constructeur __init__(weights, bias)
# - Une méthode compute(input, activation)
```

---

## 🛠️ Organisation du travail

### Plan de développement recommandé

1. **Jour 1 : Neurone**
   - Implémenter `neuron.py`
   - Tester avec des valeurs simples
   
2. **Jour 2 : Couche**
   - Implémenter `layer.py`
   - Tester avec plusieurs neurones
   
3. **Jour 3 : Réseau**
   - Implémenter `network.py`
   - Implémenter les fonctions d'activation
   
4. **Jour 4 : Tests et debug**
   - Tester avec `main.py`
   - Corriger les bugs
   
5. **Jour 5 : Bonus (optionnel)**
   - Ajouter des fonctionnalités supplémentaires

---

## 📝 Bonnes pratiques de code

### Commenter ton code
```python
# Bon exemple
def compute(self, inputs, activation):
    """
    Calcule la sortie du neurone.
    
    Args:
        inputs (list): Vecteur d'entrée
        activation (function): Fonction d'activation
        
    Returns:
        float: Sortie du neurone
    """
    # ... code ...
```

### Nommer clairement les variables
```python
# ❌ Mauvais
def f(x, w, b):
    return sum([x[i] * w[i] for i in range(len(x))]) + b

# ✅ Bon
def compute_weighted_sum(inputs, weights, bias):
    weighted_sum = sum([inputs[i] * weights[i] for i in range(len(inputs))])
    return weighted_sum + bias
```

### Tester au fur et à mesure
```python
# Ne pas attendre d'avoir tout codé pour tester
# Teste chaque fonction dès qu'elle est écrite

# Exemple :
neuron = Neuron([1, 1], 0)
print(neuron.compute([2, 3], lambda x: x))  # Devrait donner 5
```

---

## 🔍 Debugging tips

### Utiliser des print()
```python
def compute(self, inputs, activation):
    print(f"Inputs : {inputs}")
    print(f"Weights : {self.weights}")
    print(f"Bias : {self.bias}")
    
    z = self.weighted_sum(inputs)
    print(f"Weighted sum : {z}")
    
    output = activation(z)
    print(f"Output : {output}")
    
    return output
```

### Tester avec des valeurs simples
```python
# Valeurs faciles à calculer à la main
weights = [1, 1, 1]  # Somme simple
bias = 0
inputs = [1, 1, 1]

# Résultat attendu : 3 (1+1+1+0)
```

---

## 🎓 Conseils pour réussir

1. **Avance étape par étape** : Ne code pas tout d'un coup
2. **Teste souvent** : Après chaque fonction, teste-la
3. **Lis les erreurs** : Les messages d'erreur Python sont très clairs
4. **Demande de l'aide** : N'hésite pas à chercher sur Google/Stack Overflow
5. **Prends des pauses** : Si tu bloques, fais une pause et reviens plus tard

---

## ✅ Prêt à coder ?

Si tu as :
- ✅ Python installé
- ✅ La structure de fichiers créée
- ✅ Compris les concepts théoriques
- ✅ Lu le fichier main.py

**Tu es prêt(e) à commencer l'implémentation ! 🚀**

---

**Prochaine étape :** [04 - Implémentation Neuron](04_implementation_neuron.md)
