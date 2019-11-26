from keras.models import load_model
from skimage import transform
from PIL import Image
import numpy as np

# метки классов
labels = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck"
}


# загрузка изображения и преобразование его в массив чисел
def load_image(img_file_path):
    np_image = Image.open(img_file_path)
    np_image = np.array(np_image).astype('float32') / 255
    np_image = transform.resize(np_image, (32, 32, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


# вывод результатов распознавания с цветовой пометкой
def check_expectations_and_print_result(expected_class, recognized_class):
    if expected_class == recognized_class:
        print("\033[36m {}".format(labels[recognized_class]))
    else:
        print("\033[31m {}".format(labels[recognized_class]))


if __name__ == "__main__":
    # загрузка изображений и преобразование их в массивы чисел
    ship_array = load_image("photos_from_web/ship.jpg")
    horse_array = load_image("photos_from_web/horse.jpg")
    cat_array = load_image("photos_from_web/cat.jpg")

    # определение ожидаемых классов
    expected_ship_class = 8
    expected_horse_class = 7
    expected_cat_class = 3

    # загрузка модели
    model = load_model("cifar10_model.h5")

    # получение предсказаний модели
    recognized_ship_class = int(model.predict_classes(ship_array))
    recognized_horse_class = int(model.predict_classes(horse_array))
    recognized_cat_class = int(model.predict_classes(cat_array))

    # вывод результатов распознавания с цветовой пометкой
    check_expectations_and_print_result(expected_ship_class, recognized_ship_class)
    check_expectations_and_print_result(expected_horse_class, recognized_horse_class)
    check_expectations_and_print_result(expected_cat_class, recognized_cat_class)
