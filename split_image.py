# pip install opencv-python
import cv2
MIN_SIZE = 16
image = cv2.imread("input.png")
h, w, _ = image.shape
if w >= h:
    cols = 120
    rows = 100
else:
    cols = 100
    rows = 120
square_w = w / cols
square_h = h / rows
scale_w = 1
scale_h = 1
if square_w < MIN_SIZE:
    scale_w = (MIN_SIZE * cols) / w
if square_h < MIN_SIZE:
    scale_h = (MIN_SIZE * rows) / h
scale = max(scale_w, scale_h)
if scale > 1:
    new_w = int(w * scale)
    new_h = int(h * scale)
    image = cv2.resize(image, (new_w, new_h))
    w, h = new_w, new_h
square_w = w / cols
square_h = h / rows
for i in range(1, rows):
    y = int(i * square_h)
    cv2.line(image, (0, y), (w, y), (0, 0, 255), 1)
for j in range(1, cols):
    x = int(j * square_w)
    cv2.line(image, (x, 0), (x, h), (0, 0, 255), 1)
big_rows = rows // 10
big_cols = cols // 10
for i in range(1, big_rows):
    y = int(i * 10 * square_h)
    cv2.line(image, (0, y), (w, y), (0, 0, 0), 1)
for j in range(1, big_cols):
    x = int(j * 10 * square_w)
    cv2.line(image, (x, 0), (x, h), (0, 0, 0), 1)
cv2.imwrite("output.jpg", image)
print('ok')
# python split_image.py input.jpg output.jpg 100 120 10 10