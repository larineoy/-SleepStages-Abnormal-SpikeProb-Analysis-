import os
import numpy as np

# Define the folder to search
folder_path = "/Users/larineouyang/Downloads/sleep_stages/ASD_spikes"

# Function to calculate the probability
def calculate_probability(array):
    total_threes_between_zeros = 0
    number_of_zeros = 0

    i = 0
    while i < len(array):
        # Check if the current element is a 0
        if array[i] == 0:
            number_of_zeros += 1
            j = i + 1
            count_threes = 0

            # Count the number of 3s until the next 0
            while j < len(array) and array[j] == 3:
                count_threes += 1
                j += 1

            # If we found a 0 after the 3s, add the number of 3s to the total
            if j < len(array) and array[j] == 0:
                total_threes_between_zeros += count_threes
                number_of_zeros += 1  # For the closing 0

            # Move the index to the second 0
            i = j
        else:
            i += 1

    if number_of_zeros + total_threes_between_zeros == 0:
        return 0  # Avoid division by zero

    # Calculate the probability
    probability = total_threes_between_zeros / (number_of_zeros + total_threes_between_zeros)
    return probability

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    # Process only .npz files
    if file_name.endswith(".npz"):
        # Get the full file path
        npz_file_path = os.path.join(folder_path, file_name)
        
        # Load the npz file
        data = np.load(npz_file_path)
        
        # Initialize the total probability for the current file
        total_probability = 0
        
        # Check each array in the file
        for array_name in data.files:
            array = data[array_name]
            
            # Check if it's a 1D array
            if array.ndim == 1:
                # Calculate the probability for the current array
                total_probability += calculate_probability(array)
        
        # Output the file name and the calculated probability
        print(f"{file_name}: {total_probability:.4f}")
