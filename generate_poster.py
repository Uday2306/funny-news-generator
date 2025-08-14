from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import uuid

def create_poster(headline_text):
    # Poster size
    width, height = 800, 1000
    background_color = (30, 30, 30)
    text_color = (255, 255, 255)

    # Create blank image
    img = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Load font
    font_path = "static/fonts/Montserrat-Bold.ttf"  # Add a font in static/fonts
    font = ImageFont.truetype(font_path, size=40)

    # Wrap text to fit in poster
    wrapped_text = textwrap.fill(headline_text, width=28)

    # Use textbbox to get width & height
    bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Draw centered text
    x = (800 - text_width) // 2
    y = (600 - text_height) // 2
    draw.text((x, y), wrapped_text, font=font, fill='black')

    # Save poster
    poster_name = f"poster_{uuid.uuid4().hex}.png"
    output_path = os.path.join("static/posters", poster_name)
    img.save(output_path)

    return poster_name
