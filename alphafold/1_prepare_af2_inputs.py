import os
import glob
from pathlib import Path

def prepare_af2_inputs():
    fastas_dir = "fastas"
    output_base_dir = "af2_predictions"
    dat_file = "af2_inputs.dat"
    
    # Create base output directory
    os.makedirs(output_base_dir, exist_ok=True)
    
    fasta_pattern = os.path.join(fastas_dir, "*.fasta")
    fasta_files = glob.glob(fasta_pattern)
    
    if not fasta_files:
        print(f"No fasta files found in {fastas_dir}/")
        return

    dat_content = []
    
    for fasta_file in sorted(fasta_files):
        pdb_id = Path(fasta_file).stem
        output_subdir = os.path.join(output_base_dir, pdb_id)
        
        abs_fasta_path = os.path.abspath(fasta_file)
        abs_output_path = os.path.abspath(output_subdir)
        
        dat_line = f"{abs_fasta_path};{abs_output_path}"
        dat_content.append(dat_line)
    
    with open(dat_file, 'w') as f:
        f.write('\n'.join(dat_content))
    

if __name__ == "__main__":
    prepare_af2_inputs()
