import mnist
from keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import numpy as np

test_labels = mnist.test_labels()
test_images = mnist.test_images()
train_labels = mnist.train_labels()
train_images = mnist.train_images()


classifier = KNeighborsClassifier(n_neighbors=3)
# train the classifier - convert the images to 1D arrays
train_images = train_images.reshape((len(train_images), 28 * 28))
classifier.fit(train_images, train_labels)

# test the classifier - convert the images to 1D arrays
test_images = test_images.reshape((len(test_images), 28 * 28))
print(classifier.score(test_images, test_labels))


def predict(image):
    # convert image to grayscale
    image = image.convert("L")
    # resize image to 28x28 pixels
    image = image.resize((28, 28))
    # convert image to numpy array
    image = np.array(image)
    # invert image
    image = 255 - image
    # flatten the image
    image = image.reshape((1, 28 * 28))
    # predict the label
    return classifier.predict(image)[0], list(classifier.predict_proba(image)[0])


image = Image.open("digit.png")
# convert image to grayscale
image = image.convert("L")
# predict the label
print(predict(image))
