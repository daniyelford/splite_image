# pip install opencv-python
import cv2

MIN_SIZE = 2
image = cv2.imread("input.png")
h, w, _ = image.shape

# tedad matraha
cols = 120
rows = 100
big_step = 10  # har 10 square

# hesab kardan size square dorost
square_size = max(w / cols, h / rows)

# scale ax
scale = 1
if square_size < MIN_SIZE:
    scale = MIN_SIZE / square_size

if scale > 1:
    new_w = int(w * scale)
    new_h = int(h * scale)
    image = cv2.resize(image, (new_w, new_h))
    w, h = new_w, new_h

square_size = max(w / cols, h / rows)  # square dorost

# keshidan line haye koochik
for i in range(1, rows):
    y = int(i * square_size)
    cv2.line(image, (0, y), (w, y), (0, 0, 0), 1)

for j in range(1, cols):
    x = int(j * square_size)
    cv2.line(image, (x, 0), (x, h), (0, 0, 0), 1)

# keshidan line haye bozorg (har 10 square)
for i in range(1, rows // big_step):
    y = int(i * big_step * square_size)
    cv2.line(image, (0, y), (w, y), (0, 0, 255), 1)

for j in range(1, cols // big_step):
    x = int(j * big_step * square_size)
    cv2.line(image, (x, 0), (x, h), (0, 0, 255), 1)

cv2.imwrite("output.jpg", image)
print('ok')


# python split_image.py input.jpg output.jpg 100 120 10 10
