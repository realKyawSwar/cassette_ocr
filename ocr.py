from paddleocr import PaddleOCR, draw_ocr
# import matplotlib.pyplot as plt
from PIL import Image
import logging

# Set the logging level to WARNING or ERROR to suppress DEBUG messages
logging.getLogger().setLevel(logging.WARNING)

# Initialize OCR model
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Perform OCR on an image
img_path = '1970-01-01/4.jpg'
result = ocr.ocr(img_path, cls=True)

# # Print the results
# for line in result:
#     print(line)

# Draw results on the image
image = Image.open(img_path).convert('RGB')
boxes = [elements[0] for elements in result[0]]
txts = [elements[1][0] for elements in result[0]]
# scores = [elements[1][1] for elements in result[0]]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='Roboto-Light.ttf')
# im_show = Image.fromarray(im_show)

# # Display the image with OCR results
# plt.imshow(im_show)
# plt.axis('off')
# plt.show()
print(txts)
