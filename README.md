# Aerial Object Classification & Detection

Bird vs Drone Classification + YOLOv8 Object Detection  
Name: Amisha Singh

## Project Overview

This project focuses on classifying aerial objects into two categories:
- Bird
- Drone

Additionally, it includes an optional YOLOv8 object detection module to locate and identify objects in real-world aerial images.

The solution is designed for applications in:
- Security Surveillance
- Wildlife Protection
- Airport Runway Safety
- Defense Systems

## Skills Demonstrated

- Deep Learning (CNN, Transfer Learning)
- Computer Vision
- Image Classification
- YOLOv8 Object Detection
- Python, TensorFlow/Keras
- Data Augmentation
- Model Evaluation & Comparison
- Streamlit Deployment

## Dataset Details

### Classification Dataset

- Classes: Bird, Drone
- Image Format: JPG

Folder Structure:
```
classification_dataset/
    train/
    valid/
    test/
```

Class Distribution:
- Train → Bird: 1414, Drone: 1248
- Valid → Bird: 217, Drone: 225
- Test → Bird: 121, Drone: 94

### YOLOv8 Detection Dataset

- Total Images: 3319
- Annotation Format: YOLO
- Splits:
  - Train: 2662
  - Valid: 442
  - Test: 215

## Project Workflow

### 1. Dataset Understanding
- Count images
- Visualize samples
- Check class imbalance

### 2. Data Preprocessing
- Normalize images (1./255)
- Resize to 224×224

### 3. Data Augmentation
- Rotation
- Zoom
- Horizontal Flip
- Brightness adjustments

### 4. Model Building
Models implemented:
1. Custom CNN
2. MobileNetV2
3. ResNet50
4. EfficientNetB0 (Best Performing Model)

### 5. Model Training
- EarlyStopping
- ModelCheckpoint
- Metrics: Accuracy, Precision, Recall, F1-score

### 6. Model Evaluation
- Confusion Matrix
- Classification Report
- Accuracy & Loss graphs

### 7. Model Comparison
All models were compared based on validation accuracy.
EfficientNetB0 achieved the best performance.

### 8. YOLOv8 Object Detection (Optional)
Includes:
- YOLOv8 installation
- Training command
- Validation
- Inference script

### 9. Streamlit Deployment
A web-based application that allows:
- Image upload
- Bird/Drone prediction
- Display of prediction result

Run the app using:
streamlit run app.py

## Project Structure

```
Aerial-Object-Classification/
│── notebook.ipynb
│── app.py
│── best_model.h5
│── README.md
```

(Note: Dataset not included due to large size)

## Best Model

EfficientNetB0 was selected as the final model due to:
- Higher validation accuracy
- Better generalization
- Stable performance

Saved as: best_model.h5

## Future Enhancements

- Cloud deployment (AWS/GCP)
- Real-time drone detection
- Multi-class classification
- Edge deployment (Raspberry Pi / Jetson Nano)

## References

- TensorFlow Documentation
- Streamlit Documentation
- YOLOv8 (Ultralytics)
- Deep Learning Study Material
