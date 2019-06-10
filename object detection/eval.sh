# Run this script from tensorflow/models/research to evaluate: 
python object_detection/eval.py \
    --pipeline_config_path="C:/Users/Donghan Yang/Desktop/poisonous-spider-recognition/labelled_dataset/models/model/faster_rcnn_inception_v2_coco_2018_01_28.config" \
    --checkpoint_dir="C:/Users/Donghan Yang/Desktop/poisonous-spider-recognition/labelled_dataset/models/model/train" \
    --eval_dir="C:/Users/Donghan Yang/Desktop/poisonous-spider-recognition/labelled_dataset/models/model/eval" \
    --logtostderr