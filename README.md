# OCR-for-Formula-Based-on-RCNN
My HELLO WORLD on Git!

The original structure is based on https://github.com/Sierkinhane/crnn_chinese_characters_rec ,which is an implementation on Chinese Character recognization.

Requirement: Python3, PyTorch 1.0 and lmdb. (cuda is recommended)

This is an implementation dealing with the formula recognization in verification code pictures. You can download the dataset via either Baidu Drive or Google Drive, links are listd below.

Baidu: https://pan.baidu.com/s/1snfs3vB Password: tt63 (Haven't get the label on validate set, you just need to download image_contest_level_1)

Google: https://drive.google.com/file/d/1EWPxJmXAVj8ZKICgF7bFqItZvC8evqLO/view?usp=sharing

The verification code pictures is shown as below:

![0](https://github.com/liyichen1998/OCR-for-Formula-Based-on-RCNN/blob/master/OCR_for_Formula_Based_on_RCNN/to_lmdb/train_images/0.png)
![0](https://github.com/liyichen1998/OCR-for-Formula-Based-on-RCNN/blob/master/OCR_for_Formula_Based_on_RCNN/to_lmdb/train_images/1.png)
![0](https://github.com/liyichen1998/OCR-for-Formula-Based-on-RCNN/blob/master/OCR_for_Formula_Based_on_RCNN/to_lmdb/train_images/2.png)
![0](https://github.com/liyichen1998/OCR-for-Formula-Based-on-RCNN/blob/master/OCR_for_Formula_Based_on_RCNN/to_lmdb/train_images/3.png)

The lenth of these formula is 5 or 7 while only contains " * + - ( ) " and without " / " ! 
To add " / " for more complicated formula please add it into alphabets.py .

The final accuracy on valset is 98% , link of pretrained model is listed below.

Baidu:  https://pan.baidu.com/s/1pLXA5SmuiEGYMnvmllS4Og  Password: spwe

Google: https://drive.google.com/file/d/1LlBEtJqbsLA03nzMxvxnf1qZkTdrOHp0/view?usp=sharing
