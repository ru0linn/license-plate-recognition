import cv2
import os
def preprocess_image(input_path, output_path):
    # 读取图像并转为灰度图像
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # 检查图像是否成功读取
    if image is None:
        print(f"Failed to read {input_path}")
        return

    # 调整对比度和亮度
    adjusted = cv2.convertScaleAbs(image, alpha=0.8, beta=0)

    # 二值化处理，使用反转二值化，使图像变为白底黑字
    _, binary = cv2.threshold(adjusted, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 保存预处理后的图像
    cv2.imwrite(output_path, binary)
    print(f"Processed and saved: {output_path}")

def batch_preprocess_images(input_dir, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # 仅处理图像文件（根据文件扩展名）
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            preprocess_image(input_path, output_path)

if __name__ == "__main__":
    # 指定输入和输出目录
    input_dir = r'C:/Users/LRL/Desktop/data'
    output_dir = r'C:/Users/LRL/Desktop/data_output'

    # 批量处理图像
    batch_preprocess_images(input_dir, output_dir)
