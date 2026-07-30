# 01-Image-Processing
## Challenge: Batch Image Resizer & Watermarker

1. Develop an automated image processing script using the Python Imaging Library (Pillow).
2. Read and dynamically load all compatible image formats (`.jpg`, `.jpeg`, `.png`) from a designated source directory (`images`).
3. Resize each image to a fixed target dimension of 700x500 pixels.
4. Dynamically overlay a custom text watermark (`@ROMINAVALINEJAD.2026`) near the bottom-left edge using `ImageDraw` and `ImageFont`.
5. Implement proper fallback error handling for TrueType font rendering to ensure execution stability across different operating systems.
6. Export the newly processed files to a dedicated output directory (`output`) with a prefixed filename (`watermarked_`) without modifying the original source assets.
