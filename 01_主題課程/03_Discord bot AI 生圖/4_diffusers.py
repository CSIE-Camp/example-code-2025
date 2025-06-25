import torch
from diffusers import StableDiffusionPipeline

# 初始化 Stable Diffusion
model_id = "" #請填上自己找到的 module
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    allow_pickle=False  # Add this line to prevent unsafe serialization
)
#diffusers reference: https://huggingface.co/docs/diffusers/main/en/quicktour
#from_pretrained reference: https://huggingface.co/docs/diffusers/v0.32.2/en/api/models/overview#diffusers.ModelMixin.from_pretrained
#pipeline reference: https://huggingface.co/docs/diffusers/main/en/api/pipelines/overview

pipe = pipe.to("cuda")
prompt = "a cut cat" #請填入你的prompt
image = pipe(prompt).images[0]
image.save("output.png")
