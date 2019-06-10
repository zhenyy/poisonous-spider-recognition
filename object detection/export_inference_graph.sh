# export the inference graph that can be loaded to make predictions
python export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path "C:/Users/Donghan Yang/Desktop/poisonous-spider-recognition/training/models/model/pipeline.config" \
    --trained_checkpoint_prefix "C:/Users/Donghan Yang/Desktop/poisonous-spider-recognition/training/models/model/train/model.ckpt-14921" \
    --output_directory "C:/Users/Donghan Yang/Desktop/poisonous-spider-recognition/training/models/model/out2"