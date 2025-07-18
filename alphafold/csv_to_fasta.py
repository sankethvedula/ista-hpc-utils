import csv
import os
from pathlib import Path

def create_fasta_from_csv(csv_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            name = row['name']
            sequence = row['seqres']
            
            fasta_filename = f"{name.upper()}.fasta"
            fasta_path = os.path.join(output_dir, fasta_filename)

            with open(fasta_path, 'w') as fasta_file:
                header = f">{name.upper()}"
                fasta_file.write(header + '\n')
                fasta_file.write(sequence + '\n')
            
            print(f"Created: {fasta_path}")

if __name__ == "__main__":
    out_dir = 'fastas'
    create_fasta_from_csv(
        csv_file='sequences.csv', 
        output_dir=out_dir,
    )

