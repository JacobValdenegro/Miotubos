# Myotube Detection and Segmentation Model

This repository contains the scripts necessary to train and use a detection model based on YOLOv11, designed to detect and count myotubes in microscopic images.

## Instructions

1. Organize your data:  
   Place the labeled original images and their corresponding JSON files in the `Labelme` folder.

2. Generate horizontally mirrored images:  
   Run the `mirrorH.py` script to generate horizontally mirrored versions of the images and JSON files:  
   python mirrorH.py  
   This will create a folder named `mirrorH` with the modified images and JSON files.

3. Generate vertically mirrored images:  
   Run the `mirrorV.py` script to generate vertically mirrored versions of the images and JSON files:  
   python mirrorV.py  
   This will create a folder named `mirrorV` with the modified images and JSON files.

4. Merge all files into one folder:  
   Use the `merge_files.py` script to combine the original, horizontal, and vertical files into a folder named `images-json`:  
   python merge_files.py  

5. Convert JSON to YOLO OBB format:  
   Run the `json_to_yolo_obb.py` script to generate the `images` and `labels` folders required for YOLO model training:  
   python json_to_yolo_obb.py  

### 2. Model Training

1. Ensure YOLOv11 is installed locally.  
   You can follow the instructions from the official YOLOv11 repository to set it up.  

2. Place the generated `images` and `labels` folders in the required YOLO structure (inside the `datasets` directory).  

3. Configure the training file with the class names and corresponding paths.  

4. Execute the training using the following command in an Anaconda-configured environment:  
   python train.py --epochs <number_of_epochs> --data <path_to_your_data.yaml> --weights yolov11.pt  

### 3. Detecting New Images

1. Use the `best.pt` file generated after training to perform detections on new images.  
   Run the following command:  
   python detect.py --weights best.pt --source <folder_or_image>  

2. Detection results will be automatically saved in the `runs/detect/` folder.
