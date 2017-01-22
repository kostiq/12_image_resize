# Image Resizer

Скрипт изменяет размеры входного изображения и сохраняет в нужном месте.

Для запуска скрипта, надо установить нужные пакеты:

    pip3 install -r requirements.txt

Скрипт имеет насколько входных параметров:

    --path - путь к изменяемому изображению, обязательный параметр,

    --width, --hieght - размеры создаваемого изображения,

    --scale - масштаб создаваемого изображения,

    --output - путь к выходному файлу.

Для корректной работы, указывайте либо масштаб, либо ширину/высоту выходного файла.

##Пример запуска скрипта:

    python3 image_resize.py --path image001.jpg --width 120 --height 800 --output abc.jpg

    python3 image_resize.py --path image001.jpg --scale 10 

При отсутсвии выходного пути, полученное изображение сохраняется рядом с исходным.


The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
