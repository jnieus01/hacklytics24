from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer, GPT2TokenizerFast
import torch
from PIL import Image

pretrained_model = "nlpconnect/vit-gpt2-image-captioning"

model = VisionEncoderDecoderModel.from_pretrained(pretrained_model)
tokenizer = GPT2TokenizerFast.from_pretrained(pretrained_model)
image_processor = ViTImageProcessor.from_pretrained(pretrained_model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

def predict_step(image_file):
  img = Image.open(image_file)

  # process the image into a tensor
  pixel_values = image_processor(images=img, return_tensors="pt").pixel_values
  pixel_values = pixel_values.to(device)

  output_ids = model.generate(pixel_values, **gen_kwargs)

  preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
  preds = [pred.strip() for pred in preds]
  
  return preds

# if __name__ == "__main__":
#     image_file = "images/caption_input/sad_sandwich.jpeg" # test image
#     captions = predict_step(image_file)
    
#     print("Generated Captions:")
#     for i, caption in enumerate(captions, start=1):
#         print(f"{i}. {caption}")
