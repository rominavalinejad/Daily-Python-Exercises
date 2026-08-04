'''
Batch image processing script.
Resize images to 800x600 and add a watermark text to the bottom right corner.
The watermark text is "©RVN" and saves the processed images in a new folder
called "output".
'''

import os
from PIL import Image, ImageDraw, ImageFont

Source_folder = "images"
Output_folder = "output"
os.makedirs(Output_folder, exist_ok=True)

new_size = (700, 500)
watermark_text = "©ROMINAVALINEJAD.2026"

try:
    font = ImageFont.truetype("arial.ttf", 24)
except IOError:
    font = ImageFont.load_default()

for filename in os.listdir(Source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(Source_folder, filename)
        
        with Image.open(img_path) as img:
            # 1. Resize image
            resized_img = img.resize(new_size)
            
            # 2. Add text watermark
            draw = ImageDraw.Draw(resized_img)
            draw.text(
                (15, new_size[1] - 50),
                watermark_text,
                fill=(255, 255, 255),
                font=font
                )
            
            # 3. Save processed image
            save_path = os.path.join(Output_folder, f"watermarked_{filename}")
            resized_img.save(save_path)
            print(f"Processed: {filename}")

print("All images processed successfully!")