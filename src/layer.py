# src/layer.py
"""
Classe Layer - Collection de neurones

Une couche contient plusieurs neurones créés à partir de listes de poids et biais.
Retourne les valeurs BRUTES (sans activation).
"""

from neuron import Neuron

class Layer:
    """
    Représente une couche de neurones.
    
    Attributs:
        neurons (list): Liste des neurones de la couche
    """
    
    def __init__(self, weights_list, biases_list):
        """
        Initialise une couche de neurones avec des poids et biais donnés.
        
        Args:
            weights_list (list of list): Liste des poids pour chaque neurone
                Exemple: [[w1_1, w1_2], [w2_1, w2_2]] pour 2 neurones
            biases_list (list): Liste des biais pour chaque neurone
                Exemple: [b1, b2]
        """
        self.neurons = []
        
        # Créer un neurone pour chaque paire (weights, bias)
        for weights, bias in zip(weights_list, biases_list):
            neuron = Neuron(weights, bias)
            self.neurons.append(neuron)
    
    def forward(self, inputs):
        """
        Propage le vecteur d'entrée à travers la couche.
        
        Retourne les valeurs BRUTES (sans activation).
        
        Args:
            inputs (list): Vecteur d'entrée
            
        Returns:
            list: Vecteur de sorties brutes [z1, z2, ..., zn]
        """
        # Calculer la sortie de chaque neurone
        outputs = []
        for neuron in self.neurons:
            output = neuron.forward(inputs)
            outputs.append(output)
        
        return outputs
