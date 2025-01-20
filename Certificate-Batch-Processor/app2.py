from PIL import Image
import matplotlib.pyplot as plt

# Load the certificate template
template_path = "img.png"  # Your certificate path
img = Image.open(template_path)

# Use Matplotlib to display the image and capture mouse clicks
fig, ax = plt.subplots()

# Display the image
ax.imshow(img)

# Function to get coordinates on mouse click
def onclick(event):
    # Get the x and y coordinates of the mouse click
    print(f"Coordinates: x={event.xdata}, y={event.ydata}")
    plt.close()  # Close the plot after clicking (optional)

# Connect the mouse click event to the function
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()