# Object_Detection

1.모델 생성 코드 : python train.py --img 640 --batch 32 --epochs 200 --data data.yaml --cfg models/yolov5m.yaml --adam --weights yolov5m.pt --name OD_MODEL --device 0


2.모델 test 코드 : python inference.py --source test/20200602_151227/3 --weights runs/train/OD_MODEL/weights/best.pt --save-conf --save-txt 

(test 데이터는 도심로_주간일출_맑음_120_전방의 20200602_151227 폴더만 넣었습니다.) 

(다른 폴더도 확인하고 싶으시면 추가 부탁드립니다!)


3.txt에서 xml로 변환 코드 : python convert.py

(convert.py 에서 변환할 txt폴더위치, 변환된 xml 폴더위치 변경 부탁드립니다.)

(github 내에서 txt 위치 : runs/detect/exp/labels)

(github 내에서 xml 위치 : convert)
