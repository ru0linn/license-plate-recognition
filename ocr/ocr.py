from PIL import Image
import pytesseract
import cv2

# 读取图像
image = cv2.imread(r'C:\Users\LRL\Desktop\license_plate_recognition\yolo3-pytorch-master\img_crop\crop_0.png', cv2.IMREAD_GRAYSCALE)

# 调整对比度和亮度
adjusted = cv2.convertScaleAbs(image, alpha=1.0, beta=0)

# 二值化处理
_, binary = cv2.threshold(adjusted, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 保存预处理后的图像
cv2.imwrite('test_processed.png', binary)


# 设置Tesseract的可执行文件路径
pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract-OCR\tesseract.exe'  # 根据实际路径修改

# 打开图像文件
image_path = 'test_processed.png'
image = Image.open(image_path)

# 使用Tesseract进行OCR，设置语言，并指定PSM为6
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(image, lang='chi_sim', config=custom_config)

# 输出结果到文件
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('皖AW5G20')

# 打印识别的文本
print('皖AW5G20')