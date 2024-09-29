import numpy as np
import matplotlib.pyplot as plt
import random
import time

def display_puzzle(image, title="Puzzle"):
    plt.figure(figsize=(10, 10))
    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.title(title)
    plt.axis('off')
    plt.show()

def split_image(image, grid_size):
    h, w = image.shape
    new_h = (h // grid_size) * grid_size
    new_w = (w // grid_size) * grid_size
    image = image[:new_h, :new_w]
    
    tile_h, tile_w = new_h // grid_size, new_w // grid_size
    tiles = []
    for i in range(grid_size):
        for j in range(grid_size):
            tile = image[i*tile_h:(i+1)*tile_h, j*tile_w:(j+1)*tile_w]
            tiles.append(tile)
    return tiles

def reconstruct_image(tiles, grid_size):
    tile_h, tile_w = tiles[0].shape
    reconstructed = np.zeros((tile_h * grid_size, tile_w * grid_size))
    for i in range(grid_size):
        for j in range(grid_size):
            reconstructed[i*tile_h:(i+1)*tile_h, j*tile_w:(j+1)*tile_w] = tiles[i * grid_size + j]
    return reconstructed

def edge_difference(tile1, tile2, edge):
    if edge == 'right':
        return np.sum(np.abs(tile1[:, -1] - tile2[:, 0]))
    elif edge == 'bottom':
        return np.sum(np.abs(tile1[-1, :] - tile2[0, :]))

def fitness_score(tiles, grid_size):
    score = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if j < grid_size - 1:
                score += edge_difference(tiles[i * grid_size + j], tiles[i * grid_size + j + 1], 'right')
            if i < grid_size - 1:
                score += edge_difference(tiles[i * grid_size + j], tiles[(i + 1) * grid_size + j], 'bottom')
    return score

def state_space_search(tiles, grid_size, max_iterations=1000):
    best_order = tiles[:]
    best_score = fitness_score(best_order, grid_size)
    
    for _ in range(max_iterations):
        new_order = tiles[:]
        random.shuffle(new_order)
        new_score = fitness_score(new_order, grid_size)
        
        if new_score < best_score:
            best_order, best_score = new_order, new_score

    return best_order, best_score

def simulated_annealing(tiles, grid_size, max_iterations=1000, initial_temp=100, cooling_rate=0.995):
    current_order = tiles[:]
    current_score = fitness_score(current_order, grid_size)
    best_order, best_score = current_order[:], current_score
    temp = initial_temp

    for i in range(max_iterations):
        new_order = current_order[:]
        
        idx1, idx2 = random.sample(range(len(new_order)), 2)
        new_order[idx1], new_order[idx2] = new_order[idx2], new_order[idx1]
        
        new_score = fitness_score(new_order, grid_size)

        if new_score < current_score or random.random() < np.exp((current_score - new_score) / temp):
            current_order, current_score = new_order, new_score
            if new_score < best_score:
                best_order, best_score = new_order, new_score
        
        temp *= cooling_rate

    return best_order, best_score

def solve_puzzle(image_path, grid_size=4):
    image = plt.imread(image_path)
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)

    tiles = split_image(image, grid_size)
    random.shuffle(tiles)  # Scramble the tiles

    scrambled_image = reconstruct_image(tiles, grid_size)
    display_puzzle(scrambled_image, title="Scrambled Puzzle")

    start_time = time.time()
    state_space_tiles, state_space_score = state_space_search(tiles, grid_size)
    state_space_time = time.time() - start_time
    state_space_image = reconstruct_image(state_space_tiles, grid_size)
    display_puzzle(state_space_image, title=f"State Space Solution - Score: {state_space_score:.2f}, Time: {state_space_time:.2f}s")

    start_time = time.time()
    annealed_tiles, annealed_score = simulated_annealing(tiles, grid_size)
    annealed_time = time.time() - start_time
    annealed_image = reconstruct_image(annealed_tiles, grid_size)
    display_puzzle(annealed_image, title=f"Simulated Annealing Solution - Score: {annealed_score:.2f}, Time: {annealed_time:.2f}s")

    print(f"Comparison Metrics:\n{'-' * 30}")
    print(f"State Space Search - Heuristic Score: {state_space_score:.2f}, Time: {state_space_time:.2f} seconds")
    print(f"Simulated Annealing - Heuristic Score: {annealed_score:.2f}, Time: {annealed_time:.2f} seconds")

    display_puzzle(state_space_image, title="State Space Final Arrangement")
    display_puzzle(annealed_image, title="Simulated Annealing Final Arrangement")

if _name_ == "_main_":
    solve_puzzle('input_image.png', grid_size=4)
