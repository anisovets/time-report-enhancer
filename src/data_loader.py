import json
import csv
import utils as utils
import os as os

def load_json(filepath):
    """
    Load data from a JSON file.
    Returns a Python dictionary or list based on the JSON structure.
    """
    print('Starting mapping loading')
    try:
        with open(filepath,'r') as file:
            data = json.load(file)
            print('Mapping loading completed')
            return data
    except FileNotFoundError:
        print(f'File {filepath} not found.')
        return None
    except Exception as e:
        print (f'Error reading configuration: {e}')
        return None

def load_csv(filepath):
    """
    Load data from a CSV file.
    Returns a Python dictionary or list based on the CSV structure.
    """
    print('Starting row data loading')
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            print('Mapping loading completed')
            return data
    except FileNotFoundError:
        print(f'File {filepath} not found.')
        return None
    except Exception as e:
        print (f'Error reading row data file: {e}')
        return None

def write_csv(filename, list_of_dicts):
    """
    Writes data to a CSV file with a unique filename based on the current date and time.
    Deletes the file if an exception occurs during the writing process.
    """
    filepath = utils.generate_filename(filename)
    print(f'Starting to write data to {filepath}')

    try:

        with open(filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=list_of_dicts[0].keys())
            writer.writeheader()
            for row in list_of_dicts:
                writer.writerow(row)            
            print('Data writing completed successfully')
    except Exception as e:
        print(f'Error writing to CSV file: {e}')
        # Attempt to delete the file if it exists
        try:
            os.remove(filepath)
        except Exception as delete_error:
            print(f'Failed to delete {filepath}: {delete_error}')



