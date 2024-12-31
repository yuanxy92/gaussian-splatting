import os
import shutil
from pathlib import Path

def is_image_file(filename):
    """Check if the file is an image by its extension."""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def copy_images(src_dir, dist_dir):
    """Recursively copy image files from src_dir to dist_dir with subfolder name prefix."""
    # Create the destination directory if it doesn't exist
    Path(dist_dir).mkdir(parents=True, exist_ok=True)

    # Walk through the source directory recursively
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if is_image_file(file):
                # Get the relative subfolder name (excluding the main src_dir path)
                relative_subfolder = os.path.relpath(root, src_dir).replace(os.sep, "_")

                # Construct the new filename with the subfolder name as a prefix
                new_filename = f"{relative_subfolder}_{file}" if relative_subfolder != '.' else file

                # Full paths for the source file and the destination file
                src_file = os.path.join(root, file)
                dist_file = os.path.join(dist_dir, new_filename)

                # Copy the image to the destination folder with the new name
                shutil.copy(src_file, dist_file)
                print(f"Copied: {src_file} -> {dist_file}")

# Example usage:
src_dir = "/data/hdd/Data/SkinSight_video/UVC_cam_undis/depths"  # Replace with your source folder path
dist_dir = "/data/hdd/Data/SkinSight_video/UVC_cam_undis2/depths"  # Replace with your destination folder path

copy_images(src_dir, dist_dir)