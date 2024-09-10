import os
import numpy as np

# Define the folder to search
folder_path = "/Users/larineouyang/Downloads/sleep_stages/TD_spikes"

# Function to count the total number of 3s in the arrays
def count_total_threes(array):
    return np.sum(array == 3)

# Function to count the total number of 3s that are between 0s
def count_threes_between_zeros(array):
    total_threes_between_zeros = 0

    i = 0
    while i < len(array):
        # Check if the current element is a 0
        if array[i] == 0:
            j = i + 1
            count_threes = 0

            # Count the number of 3s until the next 0
            while j < len(array) and array[j] == 3:
                count_threes += 1
                j += 1

            # If we found a 0 after the 3s, add the number of 3s to the total
            if j < len(array) and array[j] == 0:
                total_threes_between_zeros += count_threes

            # Move the index to the second 0
            i = j
        else:
            i += 1

    return total_threes_between_zeros

# Function to count the total number of 2s and 1s in the arrays
def count_twos_and_ones(array):
    return np.sum(array == 2) + np.sum(array == 1)

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    # Process only .npz files
    if file_name.endswith(".npz"):
        # Get the full file path
        npz_file_path = os.path.join(folder_path, file_name)
        
        # Load the npz file
        data = np.load(npz_file_path)
        
        # Initialize the total counts
        total_threes = 0
        threes_between_zeros = 0
        total_twos_and_ones = 0
        
        # Check each array in the file
        for array_name in data.files:
            array = data[array_name]
            
            # Count the number of 3s in the array
            total_threes += count_total_threes(array)
            
            # Count the number of 3s between 0s in the array
            threes_between_zeros += count_threes_between_zeros(array)
            
            # Count the number of 2s and 1s in the array
            total_twos_and_ones += count_twos_and_ones(array)
        
        # Calculate the number of 3s not between 0s
        threes_not_between_zeros = total_threes - threes_between_zeros
        
        # Calculate the probability
        denominator = threes_not_between_zeros + total_twos_and_ones
        if denominator == 0:
            probability = 0  # Avoid division by zero
        else:
            probability = threes_not_between_zeros / denominator
        
        # Output the file name and the calculated probability
        print(f"{file_name}: Probability = {probability:.4f}")


