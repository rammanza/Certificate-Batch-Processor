import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

template_path = "img.png"  

output_dir = "certificates/"
os.makedirs(output_dir, exist_ok=True)

data = pd.read_csv("names1.csv")  # Update with the correct CSV path
names = data['Name']  # Assuming the column is 'Name'

# Adjust font size for larger text (set to a reasonable large size)
font_size =78 # Set a large font size that will render clearly
font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)

# Coordinates for text placement (move the text lower and to the center)
text_y =735 # You can adjust this vertically as needed

# Open the template image and prepare the draw object
for index, name in enumerate(names):
    cert = Image.open(template_path)
    draw = ImageDraw.Draw(cert)

    # Calculate the width and height of the text
    text_bbox = draw.textbbox((0, 0), name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Calculate the x-coordinate to center the text
    text_x = (cert.width - text_width) // 2  # Center the text horizontally
    
    # Draw the text at the new location
    draw.text((text_x, text_y), name, font=font, fill="black")  # Change color if necessary
    
    # Save the certificate with participant's name from CSV
    output_path = os.path.join(output_dir, f"{name}_certificate.png")
    cert.save(output_path)

print(f"Certificates generated and saved in {output_dir}")
