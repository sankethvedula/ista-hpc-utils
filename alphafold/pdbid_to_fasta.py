import os
import requests

def download_fasta_files(pdb_ids, output_dir='./fastas/'):
    """Download FASTA files for the given PDB IDs."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_url = "https://www.rcsb.org/fasta/entry/"

    for pdb_id in pdb_ids:
        pdb_id = pdb_id.upper()
        file_name = f"{pdb_id}.fasta"
        url = f"{base_url}{pdb_id}"
        
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, 'w') as file:
                file.write(response.text)
            print(f"Downloaded FASTA: {file_name}")
        else:
            print(f"Failed to download FASTA: {pdb_id}")

def download_pdb_files(pdb_ids, output_dir='./PDBs/'):
    """Download PDB files for the given PDB IDs."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_url = "https://files.rcsb.org/download/"

    for pdb_id in pdb_ids:
        pdb_id = pdb_id.lower()
        file_name = f"{pdb_id}.pdb"
        url = f"{base_url}{file_name}"
        
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded PDB: {file_name}")
        else:
            print(f"Failed to download PDB: {pdb_id}")

def download_structures(pdb_ids):
    """Download both FASTA and PDB files for the given PDB IDs."""
    print(f"Downloading structures for {len(pdb_ids)} PDB IDs...")
    
    # Download FASTA files
    print("\n--- Downloading FASTA files ---")
    download_fasta_files(pdb_ids)
    
    # Download PDB files
    print("\n--- Downloading PDB files ---")
    download_pdb_files(pdb_ids)
    
    print(f"\nCompleted downloading structures for {len(pdb_ids)} PDB IDs")

if __name__ == '__main__':
    # Example PDB IDs - replace this list with your desired PDB IDs
    pdb_ids = [
        '2b3w', '2k3d', '2k75', '2kjr', '2kl6', '2kpn', '2l33', '2lf2', 
        '2lk2', '2lx7', '2mql','2k0m', '2k5d', '2kd1', '2kkl', '2l82',
        '2lgh', '2ltl', '6f3k', '1pqx', '2jt1', '2k3a', '2k5v', '2kkz', 
        '2kzv', '2l8v', '2ltm', '2mk2', '6gt7'
    ] 
    
    download_structures(pdb_ids)
