import numpy as np
import json

# Step 1: Generate a 360x280x100 binary matrix
binary_matrix = np.random.randint(0, 2, size=(1080, 720, 100))

# Step 2: Convert the matrix to a Python list (NumPy arrays are not JSON serializable directly)
binary_matrix_list = binary_matrix.tolist()

# Step 3: Save the matrix as a JSON file
with open('binary_matrix_.json', 'w') as json_file:
    json.dump(binary_matrix_list, json_file)

print("Binary matrix saved as 'binary_matrix.json'.")
