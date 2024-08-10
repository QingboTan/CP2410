training_data = [
 [5, 1, 0, 300],
 [3, 1, 1, 225],
 [1, 1, 0, 75],
 [4, 0, 1, 200],
 [4, 0, 0, 150],
 [2, 0, 0, 50],
]


def calculate_distance(feature1, feature2):
    sums = sum([(feature1[i] - feature2[i])**2 for i in range(len(feature1))])
    return sums / 2


def predict_loaves(features_and_loaves, todays_features, k):
    distances = []
    for item in features_and_loaves:
        distance = calculate_distance(item[:-1], todays_features)
        distances.append((distance, item[-1]))
    distances.sort()
    nearest_neighbours = distances[:k]
    return sum([neighbour[1] for neighbour in nearest_neighbours]) / k


test_cases = [
 [5, 1, 0],
 [3, 1, 1],
 [1, 1, 0],
 [4, 0, 1],
 [4, 0, 0],
 [2, 0, 0],
 [4, 1, 0] # This should predict 228.75 loaves!
]

for test in test_cases:
    print(predict_loaves(training_data, test, 3))

"""
Step 4:
The above loop passes each test case to the predict_loaves() function. The outcomes represent 
the predicted number of loaves to be sold. For example, for the test case [4, 1, 0], the 
predict_loaves() function predicts the sale of approximately 228.75 loaves.
"""