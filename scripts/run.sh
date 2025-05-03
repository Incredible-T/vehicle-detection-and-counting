#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Step 1: Preprocess the dataset
echo "Preprocessing the dataset..."
python3 src/data_preprocessing.py

# Step 2: Train the model
echo "Training the model..."
python3 src/train_model.py

# Step 3: Evaluate the model
echo "Evaluating the model..."
python3 src/evaluate_model.py

echo "Pipeline execution completed successfully!"