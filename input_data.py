from keras.models import load_model

dir_folder = 'C:\\Users\\Lenovo\\PROJECT\\predict_8_channel\\data\\img\\23654right_9_9'
dir_write = 'C:\\Users\\Lenovo\\PROJECT\\predict_8_channel\\result'
RAKURSES = ['0', '35', '90', '145', '180', '215', '270', '325']
dir_model_gan = 'C:\\Users\\Lenovo\\PROJECT\\predict_8_channel\\data\\model\\M_2.h5' # M_(1...101).h5
print('1111......')
g_model = load_model(dir_model_gan)  