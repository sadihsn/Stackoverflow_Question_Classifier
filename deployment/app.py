import gradio as gr
import onnxruntime as rt
from transformers import AutoTokenizer
import torch, json

tokenizer = AutoTokenizer.from_pretrained("distilroberta-base")

with open("/Users/sadihossain/Desktop/Question_Classifier/tags_types_encoded.json", "r") as fp:
  encode_tags_types = json.load(fp)

Tags = list(encode_tags_types.keys())

inf_session = rt.InferenceSession('/Users/sadihossain/Desktop/Question_Classifier/Question-classifier-quantized.onnx')
input_name = inf_session.get_inputs()[0].name
output_name = inf_session.get_outputs()[0].name

def classify_Question_tags(Summary):
  input_ids = tokenizer(Summary)['input_ids'][:512]
  logits = inf_session.run([output_name], {input_name: [input_ids]})[0]
  logits = torch.FloatTensor(logits)
  probs = torch.sigmoid(logits)[0]
  return dict(zip(Tags, map(float, probs))) 

label = gr.outputs.Label(num_top_classes=5)
iface = gr.Interface(fn=classify_Question_tags, inputs="text", outputs=label)
iface.launch(inline=False)
					