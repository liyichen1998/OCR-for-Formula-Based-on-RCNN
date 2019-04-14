# OCR-for-Formula-Based-on-RCNN
My HELLO WORLD on Git!

The original structure is based on https://github.com/Sierkinhane/crnn_chinese_characters_rec ,which is an implementation on Chinese Character recognization.

Requirement: Python3, PyTorch 1.0 and lmdb. (cuda is recommended)

This is an implementation dealing with the formula recognization in verification code pictures. You can download the dataset via either Baidu Drive or Google Drive, links are listd below.

Baidu: https://pan.baidu.com/s/1snfs3vB Password: tt63 (Haven't get the label on validate set, you just need to download image_contest_level_1)

Google: uploading...

The verification code pictures is shown as below:


The lenth of these formula is 5 or 7 while only contains " * + - ( ) " and without " / " ! 
To add " / " for more complicated formula please add it into alphabets.py .

The final accuracy on valset is 98% , link of pretrained model is listed below.

Baidu:  https://pan.baidu.com/s/1pLXA5SmuiEGYMnvmllS4Og  Password: spwe

Google: uploading...
