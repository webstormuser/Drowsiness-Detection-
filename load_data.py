from pymongo import MongoClient
import gridfs
import os

# Connect to MongoDB
client = MongoClient('mongodb+srv://Ashwini:Abhishek-27@cluster0.bb6i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['drowsiness_detection']
fs = gridfs.GridFS(db)

# Paths to your image directories
closed_eye_folder = 'eye_dataset/closed_eye'
open_eye_folder = 'eye_dataset/open_eye'

# Function to store images in MongoDB
def store_images_in_mongodb(folder, label):
    for filename in os.listdir(folder):
        if filename.endswith('.png'):  # Ensure only PNG files are processed
            with open(os.path.join(folder, filename), 'rb') as f:
                data = f.read()
                fs.put(data, filename=filename, label=label)

# Store images in MongoDB
store_images_in_mongodb(closed_eye_folder, 'closed_eye')
store_images_in_mongodb(open_eye_folder, 'open_eye')

