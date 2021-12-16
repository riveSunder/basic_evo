import unittest
import numpy as np

def max_ones(starting_vector, max_generations, threshold=0.9):

    best_vector = np.copy(starting_vector)
    best_score = np.mean(best_vector)

    for generation in range(max_generations):
        
        mutate_vector = np.random.rand(*np.shape(best_vector))

        temp_vector = 1.0 * best_vector

        temp_vector[np.argmax(mutate_vector)] = 1.0

        score = np.mean(temp_vector)

        if score > best_score:

            best_vector = np.copy(temp_vector)
            best_score = score
            
        
        print(f"generation {generation}, best score = {best_score:.3}")
    
    return best_vector, best_score


if __name__ == "__main__":
    
    starting_vector = np.zeros((32,))

    max_ones(starting_vector, 100)

        
        

    
