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
