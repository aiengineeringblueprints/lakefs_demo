import matplotlib
matplotlib.use('TkAgg')
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt  # Add this import
import cv2
import random
import os
import seaborn as sns

data=[]
data_dir='./data'
folders=os.listdir(data_dir)
# Filter out non-directory items from the folders list
folders = [f for f in folders if os.path.isdir(os.path.join(data_dir, f))]

for folder in folders:
    images=os.listdir(os.path.join(data_dir,folder))
    for image in images:
        data.append(
            {
                'image path': os.path.join(data_dir,folder,image),
                'label': folder
            }
        )
data=pd.DataFrame(data)
data.head()



# Function to display images
def show_sample_images(data, num_images=5):
    plt.figure(figsize=(15, 5))

    # Randomly select images
    sample_data = data.sample(num_images).reset_index(drop=True)

    for i, row in sample_data.iterrows():
        image_path = row['image path']
        label = row['label']

        # Read image using OpenCV
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format

        # Plot image
        plt.subplot(1, num_images, i + 1)
        plt.imshow(image)
        plt.title(f"Label: {label}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()

# Call function to visualize images
# show_sample_images(data, num_images=5)

# resize all images to (224,224)
def resize_image(image_path, size=(224, 224)):
    # Read image
    img = cv2.imread(image_path)
    # Resize image
    resized = cv2.resize(img, size)
    cv2.imwrite(image_path, resized)
    return resized

# Create new column with resized images
print("Resizing images...")
data['resized_image'] = data['image path'].apply(lambda x: resize_image(x))
print("Resizing complete!")

# show_sample_images(data, num_images=5)

print("---")


