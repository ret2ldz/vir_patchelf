#!/bin/bash

# Check if the directory exists
TARGET_DIR=~/Desktop/create

# Make sure the script exists before creating the symlink
if [ ! -f "$TARGET_DIR/vir.py" ]; then
    echo "Error: vir.py not found in $TARGET_DIR"
    exit 1
fi

# Create the symbolic link
echo "Creating symbolic link for vir..."
sudo ln -sf "$TARGET_DIR/vir.py" /usr/local/bin/vir

# Confirm the success of the operation
if [ $? -eq 0 ]; then
    echo "Successfully created the symbolic link. You can now run 'vir' from anywhere."
else
    echo "Failed to create the symbolic link."
fi

