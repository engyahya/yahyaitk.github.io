from flask import Flask, request, jsonify, send_file
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

# Load the binary matrix when the app starts
binary_matrix = np.load('random_binary_matrix.npy')

@app.route('/process_pixel', methods=['POST'])
def process_pixel():
    data = request.json
    row = data['row']
    column = data['column']
    
    # Validate the row and column
    if row < 0 or row >= binary_matrix.shape[0] or column < 0 or column >= binary_matrix.shape[1]:
        return jsonify({"error": "Invalid indices"}), 400
    
    # Extract the binary values for the selected pixel
    pixel_values = binary_matrix[row, column, :]

    # Count occurrences of ones (1s)
    ones_count = np.sum(pixel_values)

    # Generate the plot
    plt.figure(figsize=(10, 5))
    plt.plot(pixel_values, marker='o', linestyle='-', color='b')
    plt.title(f'Appearance of Ones for Pixel ({row}, {column})')
    plt.xlabel('Slice Index (0-99)')
    plt.ylabel('Value (0 or 1)')
    plt.xticks(range(0, 100, 10))  # Show every 10th slice index
    plt.yticks([0, 1])  # Only 0 and 1 as y-ticks
    plt.grid(True)
    plt.axhline(y=0.5, color='r', linestyle='--')  # Line indicating the threshold

    # Save the plot to a BytesIO object
    img_io = BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    
    plt.close()

    # Return the plot image
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
