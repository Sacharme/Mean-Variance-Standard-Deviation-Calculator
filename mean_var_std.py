import numpy as np

def calculate(list):
    # If the list contains less than 9 elements, print the text "List must contain nine numbers."
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(list).reshape(3, 3)
    
    # Calculate statistics for axis 0 (columns), axis 1 (rows), and flattened (total)
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # mean of columns
            matrix.mean(axis=1).tolist(),  # mean of rows
            matrix.mean().tolist()         # mean of flattened
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # variance of columns
            matrix.var(axis=1).tolist(),   # variance of rows
            matrix.var().tolist()          # variance of flattened
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # standard deviation of columns
            matrix.std(axis=1).tolist(),   # standard deviation of rows
            matrix.std().tolist()          # standard deviation of flattened
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # max of columns
            matrix.max(axis=1).tolist(),   # max of rows
            matrix.max().tolist()          # max of flattened
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # min of columns
            matrix.min(axis=1).tolist(),   # min of rows
            matrix.min().tolist()          # min of flattened
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # sum of columns
            matrix.sum(axis=1).tolist(),   # sum of rows
            matrix.sum().tolist()          # sum of flattened
        ]
    }

    return calculations