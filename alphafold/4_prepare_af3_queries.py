import os
import json
import shutil


def read_a3m_sequence(a3m_path):
    """Extract the sequence for ID '101' from an a3m file."""
    with open(a3m_path, 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if line.endswith('>101\n'):
            # Return the next line (sequence) without newline
            return lines[i + 1].strip()

    return None

def create_af3_query(sequence, msa_path, pdb_id):
    """Create an AF3 query dictionary for a given sequence and MSA file."""
    return {
        "name": f"Fold_{pdb_id}",
        "modelSeeds": [42],
        "sequences": [
            {
                "protein": {
                    "id": "A",
                    "sequence": sequence,
                    "modifications": [],
                    "unpairedMsa": None,
                    "unpairedMsaPath": msa_path,
                    "pairedMsa": None,
                    "pairedMsaPath": msa_path,
                    "templates": []
                }
            }
        ],
        "dialect": "alphafold3",
        "version": 2
    }


def main(af3_queries_dir, af3_msas_dir):
    base_dir = af3_msas_dir
    queries_dir = af3_queries_dir
    
    # Create output directory if it doesn't exist
    os.makedirs(queries_dir, exist_ok=True)
    
    # Iterate through all .a3m files in the MSAs directory
    for msa_file in os.listdir(base_dir):
        if not msa_file.endswith('.a3m'):
            continue
            
        msa_path = os.path.join(base_dir, msa_file)
        sequence = read_a3m_sequence(msa_path)
        
        if sequence and "-" in sequence:
            print(f"Warning: Found gaps (-) in sequence for {msa_file}")
        
        # Extract PDB ID from filename (removing .a3m extension)
        pdb_id = msa_file[:-4]
        
        if sequence:
            # Create query with MSA path
            query = create_af3_query(sequence, msa_path, pdb_id)
            
            # Save query to JSON file in the output directory
            output_path = os.path.join(queries_dir, f"{pdb_id}.json")
            with open(output_path, 'w') as f:
                json.dump(query, f, indent=2)
            
            print(f"Created AF3 query for {pdb_id}")
        else:
            print(f"No sequence found for {pdb_id}")

if __name__ == "__main__":
    main("af3_queries_natbiotech_xray", "natbiotech_xray_msas")
    
    # Copy the natbiotech_xray_msas directory to be inside the af3_queries_natbiotech_xray directory
    shutil.copytree("natbiotech_xray_msas", "af3_queries_natbiotech_xray/natbiotech_xray_msas")
