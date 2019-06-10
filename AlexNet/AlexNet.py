# An example implementation of AlexNet in Keras obtained from:
# https://engmrk.com/alexnet-implementation-using-keras/


# import the necessary packages
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K
from keras import losses


class AlexNet:
	@staticmethod
	def build(width, height, depth, classes):
		# initialize the model along with the input shape to be
		# "channels last" and the channels dimension itself
		model = Sequential()
		inputShape = (height, width, depth)
		chanDim = -1

		# if we are using "channels first", update the input shape
		# and channels dimension
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)
			chanDim = 1

		model = Sequential()

		# 1st Convolutional Layer
		model.add(Conv2D(filters=96, input_shape=(224,224,3), kernel_size=(11,11), strides=(4,4), padding="valid"))
		model.add(Activation("relu"))
		# Max Pooling
		model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding="valid"))

		# 2nd Convolutional Layer
		model.add(Conv2D(filters=256, kernel_size=(11,11), strides=(1,1), padding="valid"))
		model.add(Activation("relu"))
		# Max Pooling
		model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding="valid"))

		# 3rd Convolutional Layer
		model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding="valid"))
		model.add(Activation("relu"))

		# 4th Convolutional Layer
		model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding="valid"))
		model.add(Activation("relu"))

		# 5th Convolutional Layer
		model.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding="valid"))
		model.add(Activation("relu"))
		# Max Pooling
		model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding="valid"))

		# Passing it to a Fully Connected layer
		model.add(Flatten())
		# 1st Fully Connected Layer
		model.add(Dense(4096, input_shape=(224*224*3,)))
		model.add(Activation("relu"))
		# Add Dropout to prevent overfitting
		model.add(Dropout(0.4))

		# 2nd Fully Connected Layer
		model.add(Dense(4096))
		model.add(Activation("relu"))
		# Add Dropout
		model.add(Dropout(0.4))

		# 3rd Fully Connected Layer
		model.add(Dense(1000))
		model.add(Activation("relu"))
		# Add Dropout
		model.add(Dropout(0.4))

		# Output Layer
		model.add(Dense(17))
		model.add(Activation("softmax"))

		# Compile the model
		model.compile(loss=losses.categorical_crossentropy, optimizer="adam", metrics=["accuracy"])

		# return the constructed network architecture
		return model