import os
import glob

def create_dat_file(folder_name, output_file):
    if not os.path.exists(folder_name):
        print(f"Error: Folder '{folder_name}' does not exist!")
        return False
    
    json_files = sorted(glob.glob(os.path.join(folder_name, "*.json")))
    
    if not json_files:
        print(f"Warning: No JSON files found in '{folder_name}'")
        return False
    
    formatted_paths = [f'"./{json_file}"' for json_file in json_files]
    
    try:
        with open(output_file, 'w') as f:
            f.write('\n'.join(formatted_paths) + '\n')
        
        print(f"Created '{output_file}' with {len(formatted_paths)} JSON files")
        return True
        
    except Exception as e:
        print(f"Error writing '{output_file}': {e}")
        return False

if __name__ == "__main__":
    folder_name = "af3_queries_natbiotech_xray"
    output_file = f"{folder_name}.dat"

    create_dat_file(folder_name, output_file)
