Run this command to install all lib needed: `pip install -r requirements.txt`

If you want to train model:
- Create a folder name: dataset
- Install 2 folder in drive: https://drive.google.com/drive/folders/1UR6dCBjY1Bhf_NSMpGnobbCT_zoaTAxz and place it to dataset
dataset 
- Create file name and copy follow line to dataset.yaml for train:
`
train: path-to/images/train
val: path-to/images/val

# Number of classes
nc: 15  # Replace with the actual number of classes in your dataset

# Class names
names: ["dua chuot", "tao", "kiwi", "chuoi", "cam", "dua", "dao", "so ri", 
        "le", "luu", "thom", "dua hau", "dua luoi", "nho", "dau"] 
`

If not you can use this model:
- Install model: https://drive.google.com/file/d/1W6qZeutnqnp3YX9w4iYgR44xsoi_64ff/view
- Put that file .pt to folder weights

Run testFruit.py to detect image