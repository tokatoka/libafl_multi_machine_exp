import os
import shutil

# List of directories to process
directories = ["double-conversion", "libhevc", "libxml2", "sqlite3", "stb"]
# Folder to delete and copy
folder = "queue_power,desyscall,multi_machine"

for dir in directories:
    if os.path.isdir(dir):
        print(f"Processing {dir}...")

        target_path = os.path.join(dir, folder)
        artifact_path = os.path.join("/artifact", dir, folder)

        # Delete the folder if it exists
        if os.path.isdir(target_path):
            print(f"Deleting {target_path}...")
            shutil.rmtree(target_path)

        # Copy the folder from the artifact directory
        if os.path.isdir(artifact_path):
            print(f"Copying {artifact_path} to {dir}...")
            shutil.copytree(artifact_path, target_path)
        else:
            print(f"Source {artifact_path} does not exist, skipping...")

print("Script completed.")