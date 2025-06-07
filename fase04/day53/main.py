import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10

# 1. Cargar el conjunto de datos
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 2. Normalizar las imágenes (de 0-255 a 0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Definir las clases
class_names = ['avión', 'auto', 'pájaro', 'gato', 'ciervo',
               'perro', 'rana', 'caballo', 'barco', 'camión']

# 4. Crear el modelo
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 5. Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 6. Entrenar el modelo
history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_test, y_test))

# 7. Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nPrecisión en el conjunto de prueba: {test_acc:.2f}')

# 8. Mostrar una predicción
import numpy as np

predictions = model.predict(x_test)
index = 0
plt.imshow(x_test[index])
plt.title(f"Etiqueta real: {class_names[int(y_test[index])]} | "
          f"Predicción: {class_names[np.argmax(predictions[index])]}")
plt.show()
