import cv2
import skimage.feature
import numpy as np
import matplotlib.pyplot as plt

class FeatureTransformer:
    def transform(self, image, method, params=None):
        """
        Transform the input image using the specified feature extraction method.

        :param image: Input image as a NumPy array.
        :param method: A function from skimage.feature (e.g., hog, local_binary_pattern, etc.).
        :param params: Additional parameters specific to the chosen method.
        :return: Transformed image.
        """
        if params is None:
            return method(image)
        else:
            return method(image, **params)

def main():
    # Load an example image using OpenCV
    image = cv2.imread('image_0001.jpg', cv2.IMREAD_GRAYSCALE)

    # Create a FeatureTransformer instance
    transformer = FeatureTransformer()

    # Apply HOG feature extraction
    hog_params = {
        'orientations': 9,
        'pixels_per_cell': (8, 8),
        'cells_per_block': (3, 3),
        'block_norm': 'L2-Hys',
        'visualize': True  # Request visualization
    }
    hog_features = transformer.transform(image, skimage.feature.hog, params=hog_params)

    # Extract the HOG image from the result
    hog_image = hog_features[1]

    # Apply Local Binary Pattern (LBP) feature extraction
    lbp_params = {
        'P': 8,
        'R': 1.0
    }
    lbp_features = transformer.transform(image, skimage.feature.local_binary_pattern, params=lbp_params)

    # Display the original image
    plt.figure()
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Display the HOG image
    plt.figure()
    plt.imshow(hog_image, cmap=plt.cm.gray)
    plt.title('HOG Features')
    plt.axis('off')


    # Display the LBP image
    plt.figure()
    plt.imshow(lbp_features, cmap=plt.cm.gray)
    plt.title('LBP Features')
    plt.axis('off')

    plt.show()

    # Add code to display other transformed images as needed

    plt.show()

if __name__ == "__main__":
    main()
