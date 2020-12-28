
import numpy as np
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree, SubElement


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

path = "C:/Object_Detection/yolov5/runs/detect/exp/labels" ## txt 위치
path1 = "C:/Object_Detection/yolov5/convert"   ## xml로 변환할 파일 위치

file_list = os.listdir(path)


for i in file_list:
    txt_name = path + '/' + i
    xml_name = path1 + '/' + i.split('.txt')[0] + '_v001_1.xml'

    text = np.genfromtxt(txt_name, encoding='ascii')
    line_content = []

    myFile = open(txt_name, 'r')

    cnt = 0
    while True:
        if myFile.readline() == '':
            break
        cnt += 1

    if cnt == 1:
        for j in range(6):
            x = text[j]
            if j == 0:
                if x == 0:
                    classs = 'Vehicle'
                elif x == 1:
                    classs = 'Pedestarian'
                elif x == 2:
                    classs = 'TrafficLight'
                elif x == 3:
                    classs = 'TrafficSign'
            if j == 1:
                yolo_x_center = x
            elif j == 2:
                yolo_y_center = x
            elif j == 3:
                yolo_width = x
            elif j == 4:
                yolo_height = x
            elif j == 5:
                yolo_confidence = x

        x_center = yolo_x_center * 1920
        y_center = yolo_y_center * 1080
        box_width = yolo_width * 1920
        box_height = yolo_height * 1080

        x_min = int(x_center - (box_width / 2))
        y_min = int(y_center - (box_height/2))
        x_max = int(x_center + (box_width / 2))
        y_max = int(y_center + (box_height / 2))

        line_content.append(classs)
        line_content.append(x_min)
        line_content.append(y_min)
        line_content.append(x_max)
        line_content.append(y_max)
        line_content.append(yolo_confidence)

        root = Element("annotation")
        node1 = Element("Object")
        root.append(node1)

        node2 = Element("name")
        node2.text = classs
        node1.append(node2)

        node3 = Element("bndbox")
        node1.append(node3)

        node4 = Element("xmin")
        node4.text = str(x_min)
        node3.append(node4)

        node5 = Element("ymin")
        node5.text = str(y_min)
        node3.append(node5)

        node6 = Element("xmax")
        node6.text = str(x_max)
        node3.append(node6)

        node7 = Element("ymax")
        node7.text = str(y_max)
        node3.append(node7)

        node8 = Element("confidence")
        node8.text = str(yolo_confidence)
        node1.append(node8)


        indent(root)
        dump(root)

        tree = ElementTree(root)
        tree.write(xml_name, encoding='utf-8', xml_declaration=True)

    else:
        line_number = text.shape[0]
        for i in range(line_number):
            # 한 라인에 있는 내용을 line_content 배열에 저장
            for j in range(6):
                x = text[i, j]
                if j == 0:
                    if x == 0:
                        classs = 'Vehicle'
                    elif x == 1:
                        classs = 'Pedestarian'
                    elif x == 2:
                        classs = 'TrafficLight'
                    elif x == 3:
                        classs = 'TrafficSign'
                if j == 1:
                    yolo_x_center = x
                elif j == 2:
                    yolo_y_center = x
                elif j == 3:
                    yolo_width = x
                elif j == 4:
                    yolo_height = x
                elif j == 5:
                    yolo_confidence = x

            x_center = yolo_x_center * 1920
            y_center = yolo_y_center * 1080
            box_width = yolo_width * 1920
            box_height = yolo_height * 1080

            x_min = str(int(x_center - (box_width / 2)))
            y_min = str(int(y_center - (box_height / 2)))
            x_max = str(int(x_center + (box_width / 2)))
            y_max = str(int(y_center + (box_height / 2)))
            confidence = str(yolo_confidence)

            line_content.append(classs)
            line_content.append(x_min)
            line_content.append(y_min)
            line_content.append(x_max)
            line_content.append(y_max)
            line_content.append(confidence)

        root = Element("annotation")

        size = text.shape[0] * text.shape[1]
        for i in range(size):
            if i % 6 == 0:
                a = line_content[i]
                b = line_content[i + 1]
                c = line_content[i + 2]
                d = line_content[i + 3]
                e = line_content[i + 4]
                f = line_content[i + 5]

                node1 = Element("Object")
                root.append(node1)

                node2 = Element("name")
                node2.text = a
                node1.append(node2)

                node3 = Element("bndbox")
                node1.append(node3)

                node4 = Element("xmin")
                node4.text = b
                node3.append(node4)

                node5 = Element("ymin")
                node5.text = c
                node3.append(node5)

                node6 = Element("xmax")
                node6.text = d
                node3.append(node6)

                node7 = Element("ymax")
                node7.text = e
                node3.append(node7)

                node8 = Element("confidence")
                node8.text = f
                node1.append(node8)

        indent(root)
        dump(root)
        tree = ElementTree(root)
        tree.write(xml_name, encoding='utf-8', xml_declaration=True)



