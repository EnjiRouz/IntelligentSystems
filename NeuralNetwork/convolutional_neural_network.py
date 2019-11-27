import numpy as np

# импорт набора для обучения и настроек для keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils

# испорт библиотеки для вывода лога
from contextlib import redirect_stdout

# задание seed для повторяемости результатов
np.random.seed(42)

# загрузка данных набора для обучения и тестирования
(input_train, output_train), (input_test, output_test) = cifar10.load_data()

# нормализация данных об интенсивности пикселов изображения (чтобы они находились в диапозоне от 0 до 1)
input_train = input_train.astype("float32")
input_test = input_test.astype("float32")
input_train /= 255
input_test /= 255

# преобразование меток классов в категории
output_train = np_utils.to_categorical(output_train, 10)
output_test = np_utils.to_categorical(output_test, 10)

# создание модели
model = Sequential()

""" создание 2 каскадов свёрточных слоёв """

# создание первого свёрточного слоя
model.add(Convolution2D(32, (3, 3), input_shape=(32, 32, 3), activation="relu", padding="same"))

# создание второго свёрточного слоя
model.add(Convolution2D(32, (3, 3), activation="relu"))

# создание слоя подвыборки (выбор максимального значения)
model.add(MaxPooling2D(pool_size=(2, 2)))

# создание слоя регуляризации
# (предотвращение/снижение переобучения посредством
# случайным образом выключенных нейронов, вероятность передаётся в качестве параметра)
model.add(Dropout(0.25))

# создание третьего свёрточного слоя с увеличенным числом карт признаков
model.add(Convolution2D(64, (3, 3), activation="relu", padding="same"))

# создание четвёртого свёрточного слоя с увеличенным числом карт признаков
model.add(Convolution2D(64, (3, 3), activation="relu"))

# создание второго слоя подвыборки
model.add(MaxPooling2D(pool_size=(2, 2)))

# создание второго слоя регуляризации
model.add(Dropout(0.25))

""" создание классификатора, который по найденным признакам отнесёт изображение к определённому классу """

# преобразование из двумерного вида в плоский
model.add(Flatten())

# создание полносвязного слоя
model.add(Dense(512, activation="relu"))

# создание слоя регуляризации
model.add(Dropout(0.5))

# создание выходного слоя с использованием 10 нейронов (по количеству классов)
model.add(Dense(10, activation="softmax"))

# компиляция сети (используем categorical, поскольку у нас несколько классов, используем Stochastic Gradient Descent)
model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

# обучение сети и определение процента валидационной выборки (10% от той, на которой тренируется сеть при параметре 0.1)
# для повышения качества обучения при градиентном спуске включено перемешивание данных
model.fit(input_train, output_train, batch_size=32, epochs=100, validation_split=0.1, shuffle=True)

# проверка точности модели на тренировочных данных
train_scores = model.evaluate(input_train, output_train, verbose=0)

# проверка точности модели на тестовых данных
test_scores = model.evaluate(input_test, output_test, verbose=0)

# сохранение модели и вывод информации о ней
model.save("cifar10_model.h5")
with open('model_summary.txt', 'w') as f:
    with redirect_stdout(f):
        print("Точность работы на тренировочных данных: %.2f%%" % (train_scores[1] * 100))
        print("Точность работы на тестовых данных: %.2f%%" % (test_scores[1] * 100))
        model.summary()
