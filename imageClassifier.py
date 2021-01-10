from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator


model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(300, 300, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), padding = 'same'))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adagrad',
              metrics = ['accuracy'])

batch_size = 5

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = train_datagen.flow_from_directory('train/', target_size = (300, 300),
                                                    batch_size = batch_size,
                                                    class_mode = 'categorical')

validation_generator = test_datagen.flow_from_directory('test/',
                                                        target_size = (300, 300),
                                                        batch_size = batch_size,
                                                        class_mode = 'categorical')


model.fit_generator(train_generator,
                    epochs = 5,
                    validation_data = validation_generator,
                    verbose = 1)

# Evaluating the model's performance on the test set
loss, accuracy = model.evaluate(validation_generator)

print('\nAccuracy: ', accuracy, '\nLoss: ', loss)
