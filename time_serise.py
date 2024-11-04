import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the binary matrix from the .npy file
binary_matrix = np.load('random_binary_matrix.npy')

# Check the shape of the loaded array
print(f"Loaded array shape: {binary_matrix.shape}")

# Step 2: User inputs for pixel selection
row = int(input("Enter the row index (0-359): "))
column = int(input("Enter the column index (0-279): "))

# Check for valid indices
if row < 0 or row >= binary_matrix.shape[0] or column < 0 or column >= binary_matrix.shape[1]:
    print("Invalid indices. Please enter values within the specified range.")
else:
    # Step 3: Extract the binary values for the selected pixel
    pixel_values = binary_matrix[row, column, :]

    # Step 4: Count occurrences of ones (1s)
    ones_count = np.sum(pixel_values)

    # Step 5: Create a plot
    plt.figure(figsize=(10, 5))
    plt.plot(pixel_values, marker='o', linestyle='-', color='b')
    plt.title(f'Appearance of Ones for Pixel ({row}, {column})')
    plt.xlabel('Slice Index (0-99)')
    plt.ylabel('Value (0 or 1)')
    plt.xticks(range(0, 100, 10))  # Show every 10th slice index
    plt.yticks([0, 1])  # Only 0 and 1 as y-ticks
    plt.grid(True)
    plt.axhline(y=0.5, color='r', linestyle='--')  # Line indicating the threshold

    # Step 6: Save the plot as an image with pixel coordinates in the filename
    image_filename = f'ones_plot_pixel_{row}_{column}.png'
    plt.savefig(image_filename)

    # Show the plot
    plt.show()

    # Print the count of ones and the saved filename
    print(f"Total number of 1s at pixel ({row}, {column}): {ones_count}")
    print(f"Plot saved as '{image_filename}'")
