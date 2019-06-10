# Poisonous Spider Recognition 
This repository contains scripts for our research project:  
an **iOS application** that recognizes **Australian venomous spiders** in **real-time**

The scripts in this repository are for the **deep learning model development** only

[iOS app repository](https://github.com/zhenyy/SpiderRecognizer)

[Spider Map web app repository](https://github.com/zhenyy/SpiderMap)

## Data
- Our raw training images are located [here](https://drive.google.com/drive/folders/1vSF86zrU9rp9kq2WvM0_ZpAfgH3r2W2K?usp=sharing). (Anyone at The University of Melbourne can access)

- [Training images with annotated xml files in PASCAL VOC format](https://drive.google.com/drive/folders/1xrpwmA6uXws7jNqXTV74DuoQ16MAV3D4?usp=sharing).  

- [Serialized data with label map](https://drive.google.com/drive/folders/1pTdsFcWcS44n-5sBhYGAn4dSNdk_Y2lv?usp=sharing) (ready for use in [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection))


## Things that we used
- The project is not possible without this nice series of tutorials created by [pyimagesearch](https://www.pyimagesearch.com/):  
[How to (quickly) build a deep learning image dataset](https://www.pyimagesearch.com/2018/04/09/how-to-quickly-build-a-deep-learning-image-dataset/)  
[Keras and Convolutional Neural Networks (CNNs)](https://www.pyimagesearch.com/2018/04/16/keras-and-convolutional-neural-networks-cnns/)  
[Running Keras models on iOS with CoreML](https://www.pyimagesearch.com/2018/04/23/running-keras-models-on-ios-with-coreml/)  

- And this blog post written by [Matthijs Hollemans](https://github.com/hollance):  
[MobileNetV2 + SSDLite with Core ML](https://machinethink.net/blog/mobilenet-ssdlite-coreml/)  
with [Source code](https://github.com/hollance/coreml-survival-guide/tree/master/MobileNetV2%2BSSDLite)

- Two handy tools for building image datasets for computer vision:  
[Bing Image Search API](https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/)  
[google-images-download](https://github.com/hardikvasa/google-images-download)

- Image labelling tool:  
[LabelImg](https://github.com/tzutalin/labelImg)