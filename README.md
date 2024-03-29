# Задача: Вернуть смещенную и(или) развернутую ступню в исходное положение, по всем восьми ракурсам. 
**Инструмент: GAN pix2pix**\
**Требования: Линейное расхождение по контуру, между оригинальным и сгенерированным изображением, не более 20 пикселей.**\
**Dataset: Изображения ступней, восемь ракурсов (бинарная маска, size 3088 : 2320).**\
![image](https://github.com/SergSof/predict_8_channel/assets/68720384/5519922d-e26c-4730-b4e0-94d34e38433b)

Обучение: На вход нейронной сети, подается восьмиканальный массив, shape (N, 2048, 2048, 8), N - samples. Для подачи входных данных, использовался генератор. В качестве правильного ответа, изображения 8-ми ракурсов ступни в исходном положении.

Пример полученного результата на тестовых данных:
![22222222](https://github.com/SergSof/predict_8_channel/assets/68720384/ee075c67-741d-4af5-8d9b-b4218cd35dfe)

**Метрики (IoU):
Значения в процентах от общей площади оригинала.
Первое значение {red} - площадь красной области, лишние сгенерированные пиксели
Второе значение {green} - площадь зеленой области, не до cгенерированные пиксели
Первое и второе значения, должны стремиться к 0.**

![result](https://github.com/SergSof/GAN_train_8_channels_img/assets/68720384/9804b218-cc86-428f-b9aa-4a8f830e5294)

Часть процесса обучения (видео):

https://github.com/SergSof/GAN_train_8_channels_img/assets/68720384/6d1b6da3-6a6f-45b9-80f8-2f2b8bf9d3a0

Colab, train GAN

https://colab.research.google.com/drive/1zIBuIUVCyfvQZr4zMtGKkdoqdyOy6my0?usp=sharing

Colab, predict GAN

https://colab.research.google.com/drive/1MykwPe7ul2WUidAqZkdft8BGPhr7KuHX?usp=sharing
