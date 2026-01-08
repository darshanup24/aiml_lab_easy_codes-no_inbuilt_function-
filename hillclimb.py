import numpy as np

def hill_climbing(func, x, step=0.01, iters=1000):
    for _ in range(iters):
        # Create an array of 3 points: [x - step, x, x + step]
        neighbors = np.array([x - step, x, x + step])
        values = func(neighbors)
        
        # Find the index of the highest value
        best_idx = np.argmax(values)
        
        # If the best neighbor is the current position (index 1), we've reached a peak
        if best_idx == 1:
            break
            
        x = neighbors[best_idx]
    return x, func(x)

# Inputs
f_str = input("Enter function (e.g., -x**2 + 4*x): ")
func = lambda x: eval(f_str, {"x": x, "np": np})
start = float(input("Enter starting x: "))

# Execution
maxima, val = hill_climbing(func, start)
print(f"\nMaximum found at x = {maxima}, Value = {val}")