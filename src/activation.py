# src/activation.py
"""
Fonctions d'activation pour le réseau de neurones

Ce module contient les fonctions d'activation courantes :
- act_identity : Fonction identité
- act_threshold : Fonction seuil
- act_relu : ReLU (Rectified Linear Unit)
"""

def act_identity(x):
    """
    Fonction identité : f(x) = x
    
    Args:
        x (float): Valeur d'entrée
        
    Returns:
        float: La même valeur
    """
    return x


def act_threshold(x):
    """
    Fonction seuil (step function) : f(x) = 1 si x >= 0, sinon 0
    
    Args:
        x (float): Valeur d'entrée
        
    Returns:
        int: 1 ou 0
    """
    return 1 if x >= 0 else 0


def act_relu(x):
    """
    ReLU (Rectified Linear Unit) : f(x) = max(0, x)
    
    Args:
        x (float): Valeur d'entrée
        
    Returns:
        float: x si x > 0, sinon 0
    """
    return max(0, x)
