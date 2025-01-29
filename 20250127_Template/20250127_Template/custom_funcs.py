# custom_funcs.py

import matplotlib.pyplot as plt
import os 
import pandas as pd


### Make the plots pretty 
def scatter_plot_template():  
    fig,ax = plt.subplots(figsize=(10,6))
    plt.rc('font', size=20)  # Change all fonts
    # Plot appearance 
    plt.grid(True)
    plt.grid(visible=True, which='minor', axis='both' , linestyle='-',color='k' ,alpha = 0.2)
    plt.grid(visible=True, which='major', axis='both' , linestyle='-',color='k' ,alpha = 0.7)

    plt.minorticks_on() 

    return None

    


### Read PCD files
def pcd_to_dataframe(filename, start_line):
    """
    Creates a pandas DataFrame from a PCD file, starting from a specific line.

    Args:
        filename: Path to the PCD file.
        start_line: Line number from which to start reading data.

    Returns:
        pandas.DataFrame: DataFrame containing the point cloud data.
    """
    if os.path.exists(filename) == True: # Check if the file is in the correct location
        with open(filename, 'r') as file: # Open the pcd file
            lines = file.readlines()[start_line:]  # Read lines from the specified line onwards

        # Extract data (assuming a simple format for demonstration)
        data = [] # Empty list
        for line in lines: # For line is the lines list
            values = line.strip().split(' ')  # Split line into values by looking at the spaces
            if len(values) > 0:  # Check if line contains data
                data.append(values) # Add the lines which have contans data into a list

        # Create DataFrame
        df = pd.DataFrame(data)  
        # change all the numbers from objects to floats
        s = df.select_dtypes(include='object').columns # find the columns that are floats
        df[s] = df[s].astype("int") # change those columns into integers

    else:
        print('The file does not exist')

    return df
