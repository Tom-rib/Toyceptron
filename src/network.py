# src/network.py
"""
Classe Network - Réseau de neurones multi-couches

Le réseau gère les couches et applique la fonction d'activation.
"""

from layer import Layer

class Network:
    """
    Représente un réseau de neurones.
    
    Attributs:
        input_size (int): Taille du vecteur d'entrée
        activation (function): Fonction d'activation
        layers (list): Liste des couches du réseau
    """
    
    def __init__(self, input_size, activation):
        """
        Initialise le réseau.
        
        Args:
            input_size (int): Taille du vecteur d'entrée
            activation (function): Fonction d'activation à appliquer
        """
        self.input_size = input_size
        self.activation = activation
        self.layers = []
    
    def add(self, weights, biases):
        """
        Ajoute une couche au réseau.
        
        Args:
            weights (list of list): Poids pour chaque neurone de la couche
                Exemple: [[w1_1, w1_2], [w2_1, w2_2]]
            biases (list): Biais pour chaque neurone
                Exemple: [b1, b2]
        """
        layer = Layer(weights_list=weights, biases_list=biases)
        self.layers.append(layer)
    
    def feedforward(self, inputs):
        """
        Propage l'entrée à travers toutes les couches avec activation.
        
        Args:
            inputs (list): Vecteur d'entrée
            
        Returns:
            list: Sortie du réseau (valeurs activées)
        """
        current = inputs
        
        # Propager à travers chaque couche
        for layer in self.layers:
            # Obtenir les valeurs brutes de la couche
            raw_outputs = layer.forward(current)
            
            # Appliquer l'activation sur chaque sortie
            activated_outputs = [self.activation(z) for z in raw_outputs]
            
            # Les sorties activées deviennent les entrées de la couche suivante
            current = activated_outputs
        
        return current
