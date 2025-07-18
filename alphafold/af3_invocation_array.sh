#!/bin/bash
#SBATCH --partition=gpu100                      # Partition to run in
#SBATCH --gres=gpu:1                         # GPU resources requested
#SBATCH -c 4                                 # Requested cores
#SBATCH --time=01:00:00                      # Runtime in D-HH:MM format
#SBATCH --mem=128GB                          # Requested Memory
#SBATCH --output=output-%x-%A_%a.log         # Changed to include array task ID
#SBATCH --error=error-%x-%A_%a.log           # Changed to include array task ID
#SBATCH --array=1-60                       # Array job based on number of lines in data file

echo $HOSTNAME

export PATH="/nfs/scistore20/bronsgrp/svedula/miniforge3/bin:$PATH"

eval "$(conda shell.bash hook)"
# eval "$(command conda 'shell.bash' 'hook' 2> /dev/null)"
conda activate alphafold3

echo "Job ID: $SLURM_ARRAY_JOB_ID  Task ID: $SLURM_ARRAY_TASK_ID"

# Add offset to SLURM_ARRAY_TASK_ID
OFFSET=0
ADJUSTED_TASK_ID=$((SLURM_ARRAY_TASK_ID + OFFSET))

# Get the query path (keeping original case)
QUERY_PATH=$(sed -n "${ADJUSTED_TASK_ID}p" af3_queries_natbiotech_xray.dat | sed 's/"//g')
OUTPUT_DIR="./results_nmr_biotech"

# Create lowercase version for results directory
QUERY_PATH_LOWER=$(echo "$QUERY_PATH" | tr '[:upper:]' '[:lower:]')

echo "Processing: $QUERY_PATH"

# Extract filename without extension for folder name (using lowercase version)
BASENAME=$(basename "$QUERY_PATH_LOWER" .json)
RESULT_DIR="$OUTPUT_DIR/fold_${BASENAME}"

# Only run if results directory doesn't exist
if [ ! -d "$RESULT_DIR" ]; then
    python run_alphafold.py \
        --json_path="$QUERY_PATH" \
        --output_dir="$OUTPUT_DIR" \
        --model_dir=./models/ \
        --run_data_pipeline=False
else
    echo "Results directory $RESULT_DIR already exists, skipping..."
fi
