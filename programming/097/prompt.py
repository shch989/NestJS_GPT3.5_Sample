# You are an expert web designer.
# Generate and execute some Python code that produces four color shades (brighter and darker) based on the base color #6014db

from PIL import Image, ImageDraw

def generate_shades(base_color, n_shades=4):
    """Generates brighter and darker shades of a given base color."""
    # Convert the hex color to RGB
    base_color_rgb = tuple(int(base_color[i:i+2], 16) for i in (1, 3, 5))

    # Calculate the shades
    shades = []
    for i in range(1, n_shades // 2 + 1):
        # Brighter shades
        brighter = tuple(min(255, int(c * (1 + 0.2 * i))) for c in base_color_rgb)
        shades.append('#' + ''.join(f'{c:02x}' for c in brighter))

        # Darker shades
        darker = tuple(max(0, int(c * (1 - 0.2 * i))) for c in base_color_rgb)
        shades.append('#' + ''.join(f'{c:02x}' for c in darker))

    return shades

# Base color
base_color = "#6014db"

# Generate shades
shades = generate_shades(base_color)

# Display the base color and its shades
shades.insert(0, base_color)  # Include the base color in the list

# Create an image to display the colors
img = Image.new("RGB", (300, 50 * len(shades)), color="white")
draw = ImageDraw.Draw(img)

# Draw each shade
for i, color in enumerate(shades):
    draw.rectangle([0, i * 50, 300, (i + 1) * 50], fill=color)

# Save the image
img_path = "./color_shades.png"
img.save(img_path)

img_path, shades