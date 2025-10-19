import os, shutil, random

base_dir = 'dataset'                 # this will be created automatically
original_data = 'potato_dataset'     


classes = ['Early_Blight', 'Healthy', 'Late_Blight']

# Create train/test folders
for split in ['train', 'test']:
    for cls in classes:
        os.makedirs(os.path.join(base_dir, split, cls), exist_ok=True)

# Split data 80% train, 20% test
for cls in classes:
    cls_dir = os.path.join(original_data, cls)
    images = os.listdir(cls_dir)
    random.shuffle(images)
    
    split_idx = int(0.8 * len(images))
    train_imgs = images[:split_idx]
    test_imgs = images[split_idx:]
    
    for img in train_imgs:
        shutil.copy(os.path.join(cls_dir, img), os.path.join(base_dir, 'train', cls))
    for img in test_imgs:
        shutil.copy(os.path.join(cls_dir, img), os.path.join(base_dir, 'test', cls))

print("✅ Split complete — 'dataset/train' and 'dataset/test' folders created!")
