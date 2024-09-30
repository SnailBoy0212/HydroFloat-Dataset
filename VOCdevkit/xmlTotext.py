import os
import xml.etree.ElementTree as ET

# 设置路径
voc_root = r"E:\Users\HP\Desktop\数据集\VOCdevkit"
annotations_dir = os.path.join(voc_root, "Annotations")
images_dir = os.path.join(voc_root, "JPEGImages")
output_dir = os.path.join(voc_root, "YOLOAnnotations")

# 如果输出文件夹不存在，则创建
os.makedirs(output_dir, exist_ok=True)

# Pascal VOC 类别列表，类别索引与该列表的索引一一对应
classes = ["class1", "class2", "class3"]  # 根据实际的类别填写

# 函数：将 Pascal VOC bounding box 转换为 YOLO 格式
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# 处理每个 XML 文件
for filename in os.listdir(annotations_dir):
    if not filename.endswith(".xml"):
        continue

    xml_path = os.path.join(annotations_dir, filename)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    image_id = root.find('filename').text.replace('.jpg', '')

    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    yolo_file = os.path.join(output_dir, image_id + ".txt")
    with open(yolo_file, 'w') as f:
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            f.write(f"{cls_id} {' '.join([str(a) for a in bb])}\n")

print("转换完成！YOLO 格式的标注文件保存在:", output_dir)
