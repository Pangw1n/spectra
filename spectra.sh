#!/bin/bash

# Check for at least 2 arguments
if [ "$#" -lt 2 ]; then
    echo "The input directory and output directory must be specified."
    echo "Usage: spectra <input_dir> <output_dir> [optional args...]"
    exit 1
fi

INPUT_DIR=$1
OUTPUT_DIR=$2

shift 2  # Remove first two args, leaving optional flags

docker run --rm \
    -v "$INPUT_DIR":/input \
    -v "$OUTPUT_DIR":/output \
    pangw1n/spectra --input=/input --output=/output "$@"
