import os
import numpy as np

# Define the folder to search
folder_path = "/Users/larineouyang/Downloads/sleep_stages/TD_spikes"

# Flag to track if any file matches the condition
file_found = False

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    # Process only .npz files
    if file_name.endswith(".npz"):
        # Get the full file path
        npz_file_path = os.path.join(folder_path, file_name)
        
        # Load the npz file
        data = np.load(npz_file_path)
        
        # Check each array in the file
        for array_name in data.files:
            array = data[array_name]
            
            # Check if it's a 1D array
            if array.ndim == 1:
                # Search for [0, 3, 2] or [2, 3, 0] in the array
                for i in range(1, len(array) - 1):
                    if (array[i-1] == 0 and array[i] == 3 and array[i+1] == 2) or (array[i-1] == 2 and array[i] == 3 and array[i+1] == 0):
                        print(f"File with the sequence found: {file_name}")
                        file_found = True
                        break  # Exit the loop once the condition is met
            if file_found:
                break

# Output if no file has the sequence
if not file_found:
    print("No such file")
