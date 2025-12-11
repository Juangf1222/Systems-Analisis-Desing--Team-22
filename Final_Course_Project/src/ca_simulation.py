import numpy as np
import pandas as pd

def run_ca(grid_size=60, steps=60, stress=0.3, noise=0.05, seed=42):
    np.random.seed(seed)
    grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.995, 0.005])
    results = []

    for t in range(steps):
        results.append(grid.mean())
        grid = update(grid, stress, noise)

    df = pd.DataFrame({"step": range(steps), "fraction": results})
    df.to_csv("ca_summary.csv", index=False)
    return df

def update(grid, stress, noise):
    n = grid.shape[0]
    new = grid.copy()

    for i in range(n):
        for j in range(n):
            neighborhood = grid[max(0,i-1):min(n,i+2),
                                max(0,j-1):min(n,j+2)]

            frac = neighborhood.mean()
            p = stress * frac + noise * np.random.rand()

            if np.random.rand() < p:
                new[i, j] = 1

    return new
