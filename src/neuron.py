# src/neuron.py
"""
Classe Neuron - Unité de calcul élémentaire

Un neurone effectue une combinaison linéaire des entrées : z = Σ(wi · xi) + b
L'activation est appliquée au niveau du réseau, pas du neurone.
"""

class Neuron:
    """
    Représente un neurone artificiel.
    
    Attributs:
        weights (list): Poids du neurone [w1, w2, ..., wn]
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
    
    def forward(self, inputs):
        """
        Calcule la sortie BRUTE du neurone (sans activation).
        
        Formule : z = Σ(wi · xi) + bias
        
        Args:
            inputs (list): Vecteur d'entrée [x1, x2, ..., xn]
            
        Returns:
            float: Somme pondérée + biais (valeur brute)
        """
        # Calculer le produit scalaire : Σ(wi · xi)
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))
        
        # Ajouter le biais
        return weighted_sum + self.bias
