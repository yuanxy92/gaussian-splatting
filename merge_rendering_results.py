import os
import shutil
from pathlib import Path

def merge_image_folders(folder1, folder2, output_folder):
    # Make sure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Helper function to get image paths in a sorted order from a folder and its subfolders
    def get_subfolder_structure(folder):
        subfolders = {}
        for root, dirs, _ in os.walk(folder):
            for dir in dirs:
                subfolder_path = os.path.join(root, dir)
                subfolder_name = os.path.relpath(subfolder_path, folder)
                subfolders[subfolder_name] = []
                # Collect images in this subfolder
                for file in sorted(os.listdir(subfolder_path)):
                    if file.endswith('.png'):
                        subfolders[subfolder_name].append(os.path.join(subfolder_path, file))
        return subfolders

    # Get the subfolder structures for both folders
    folder1_subfolders = get_subfolder_structure(folder1)
    folder2_subfolders = get_subfolder_structure(folder2)

    # Merge images from both folders into the output folder with continuous numbering within each subfolder
    for subfolder_name in folder1_subfolders:
        # Merge images in the current subfolder (folder1)
        output_subfolder = os.path.join(output_folder, subfolder_name)
        os.makedirs(output_subfolder, exist_ok=True)

        # Folder 1 images (first batch, continue numbering in each subfolder)
        image_counter = 1
        for img_path in folder1_subfolders[subfolder_name]:
            new_img_name = f"{image_counter:05d}.png"  # Continue numbering within subfolder
            new_img_path = os.path.join(output_subfolder, new_img_name)
            shutil.copy(img_path, new_img_path)
            print(f"Copied {img_path} to {new_img_path}")
            image_counter += 1

    for subfolder_name in folder2_subfolders:
        # Merge images in the current subfolder (folder2)
        output_subfolder = os.path.join(output_folder, subfolder_name)
        os.makedirs(output_subfolder, exist_ok=True)

        # Folder 2 images (second batch, continue numbering in each subfolder)
        image_counter = len(folder1_subfolders.get(subfolder_name, [])) + 1  # Continue from where folder1 left off
        for img_path in folder2_subfolders[subfolder_name]:
            new_img_name = f"{image_counter:05d}.png"  # Continue numbering within subfolder
            new_img_path = os.path.join(output_subfolder, new_img_name)
            shutil.copy(img_path, new_img_path)
            print(f"Copied {img_path} to {new_img_path}")
            image_counter += 1

if __name__ == "__main__":
    folder1 = "/data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense/3dgs/train/ours_10000_1"  # Set path for folder 1
    folder2 = "/data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense/3dgs/train/ours_10000_2"  # Set path for folder 2
    output_folder = "/data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense/3dgs/train/ours_10000"  # Set output folder path

    merge_image_folders(folder1, folder2, output_folder)
