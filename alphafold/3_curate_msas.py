import os
import shutil
from pathlib import Path

def copy_a3m_files(af2_preds_dir, msas_dir):
    """
    Copy a3m files from each subfolder in natbiotech_xray_af2 to natbiotech_xray_msas
    """
    source_dir = Path(af2_preds_dir)
    dest_dir = Path(msas_dir)
    
    # Create destination directory if it doesn't exist
    dest_dir.mkdir(exist_ok=True)
    print(f"Created destination directory: {dest_dir}")
    
    # Check if source directory exists
    if not source_dir.exists():
        print(f"Error: Source directory {source_dir} does not exist!")
        return
    
    copied_files = []
    missing_files = []
    
    # Iterate through all subdirectories in the source directory
    for subfolder in source_dir.iterdir():
        if subfolder.is_dir():
            # Look for a3m file in the subfolder
            # Assuming the a3m file is named after the folder (e.g., 7NMO/7NMO.a3m)
            a3m_file = subfolder / f"{subfolder.name}.a3m"
            
            if a3m_file.exists():
                # Copy the a3m file to destination directory
                dest_file = dest_dir / a3m_file.name
                try:
                    shutil.copy2(a3m_file, dest_file)
                    copied_files.append(a3m_file.name)
                    print(f"Copied: {a3m_file} -> {dest_file}")
                except Exception as e:
                    print(f"Error copying {a3m_file}: {e}")
            else:
                missing_files.append(subfolder.name)
                print(f"Warning: No a3m file found in {subfolder}")
    
    
    if missing_files:
        print(f"\nFolders without a3m files:")
        for folder in missing_files:
            print(f"  - {folder}")

if __name__ == "__main__":
    copy_a3m_files("natbiotech_xray_af2", "natbiotech_xray_msas")
