import numpy as np
import cv2

# Genetic Algorithm Parameters
POPULATION_SIZE = 10
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1

# Load the original image
original_image = cv2.imread('input3d.jpg', cv2.IMREAD_GRAYSCALE)

# Flatten the original image into a 1D array
original_image_flat = original_image.flatten()


# Define fitness function (for demonstration purposes, just sum of pixel values)
def fitness(image_flat):
    return np.sum(image_flat)


# Initialize population
population = [np.random.permutation(original_image_flat) for _ in range(POPULATION_SIZE)]

# Genetic Algorithm
for generation in range(NUM_GENERATIONS):
    # Evaluate fitness of each individual in the population
    fitness_scores = [fitness(individual) for individual in population]

    # Select parents based on fitness scores
    parents_indices = np.argsort(fitness_scores)[-2:]  # Select top 2 individuals as parents

    # Crossover
    crossover_point = np.random.randint(1, len(original_image_flat))
    offspring1 = np.concatenate((population[parents_indices[0]][:crossover_point],
                                 population[parents_indices[1]][crossover_point:]))
    offspring2 = np.concatenate((population[parents_indices[1]][:crossover_point],
                                 population[parents_indices[0]][crossover_point:]))

    # Mutation
    if np.random.rand() < MUTATION_RATE:
        mutation_point = np.random.randint(0, len(original_image_flat))
        offspring1[mutation_point] = 255 - offspring1[mutation_point]  # Example mutation
        offspring2[mutation_point] = 255 - offspring2[mutation_point]  # Example mutation

    # Replace worst individuals in the population with offspring
    worst_indices = np.argsort(fitness_scores)[:2]
    population[worst_indices[0]] = offspring1
    population[worst_indices[1]] = offspring2

# Select the best individual as the encrypted image
best_individual_index = np.argmax([fitness(individual) for individual in population])
encrypted_image_flat = population[best_individual_index]
encrypted_image = np.reshape(encrypted_image_flat, original_image.shape)

# Decryption process using the original image
decrypted_image_flat = np.array(encrypted_image_flat)
decrypted_image = np.reshape(decrypted_image_flat, original_image.shape)

# Save or display the encrypted, decrypted, and original images
cv2.imwrite('encrypted_image.jpg', encrypted_image)
cv2.imwrite('decrypted_image.jpg', decrypted_image)
cv2.imshow('Original Image', original_image)
cv2.imshow('Encrypted Image', encrypted_image)
cv2.imshow('Decrypted Image', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
