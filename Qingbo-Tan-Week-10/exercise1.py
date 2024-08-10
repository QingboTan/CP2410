labeled_features = [
 [140, 6, "grapefruit"],
 [170, 5.5, "grapefruit"],
 [220, 7, "grapefruit"],
 [260, 7.5, "grapefruit"],
 [300, 9, "grapefruit"],
 [400, 10, "grapefruit"],
 [140, 6.5, "orange"],
 [170, 7, "orange"],
 [200, 8, "orange"],
 [240, 7.5, "orange"],
 [280, 8, "orange"],
 [300, 9, "orange"],
]


def euclidean_distance(feature1, feature2):
    return ((feature1[0] - feature2[0]) ** 2 + (feature1[1] - feature2[1]) ** 2) ** 0.5


def knn_classify(features, chosen_feature, k):
    # create a list of distances
    distances = []

    """
    Step 4: This loop calculates the Euclidean distance between the chosen feature
            and all other features, appending each distance and corresponding label
            to the 'distances' list.
    """
    for feature in features:
        distance = round(euclidean_distance(feature, chosen_feature), 2)
        name = feature[2]
        distances.append((distance, name))

    distances.sort()
    k_nearest_labels = distances[:k]

    return max(set(k_nearest_labels), key=k_nearest_labels.count)


"""
Step 9: Unlike knn_classify() which returns the most frequent label, knn_predict_weight()
        returns the average weight of the k-nearest neighbors.
"""


def knn_predict_weight(features, chosen_feature, k):
    distances = []
    for feature in features:
        distance = round(euclidean_distance(feature, chosen_feature), 2)
        weight = feature[0]
        distances.append((distance, weight))
    distances.sort()
    k_nearest_labels = distances[:k]
    return round(sum([label[1] for label in k_nearest_labels]) / k)
