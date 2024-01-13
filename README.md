# Stackoverflow_Question_Classifier
A multi-label text classifier that can classify Stackoverflow Question Tags given Question Summary.

A text classification model from data collection, model training, and deployment.
The model can classify different types of Stackoverflow Question Tags

# Data Collection
Data was collected from  Stackoverflow Website:https://stackoverflow.com/
The data collection process was done in one single step:scraper/scraper.py and then stored in a csv file data/Stack_Overflow_data.csv.

In total, I scraped 29950 Questions.

# Data Preprocessing

# Model Training
Finetuned a distilrobera-base model from HuggingFace Transformers using Fastai and Blurr. The model training notebook can be viewed [Here](notebooks/text_classifiction_blurr.ipynb)

# Model Compression and ONNX Inference

# Model Deployment
The compressed model is deployed to HuggingFace Spaces Gradio App. The implementation can be found in deployment folder or [Here](https://huggingface.co/spaces/Sadihsn/StackOverflow_Question_Classifier)
