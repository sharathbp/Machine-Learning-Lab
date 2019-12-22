import pandas as pd
import math
import operator
from sklearn.model_selection import train_test_split

def euclidean_distance(instance1, instance2):
	distance = 0
	for x1, x2 in zip(instance1, instance2):
		distance += pow((x1-x2),2)
	return math.sqrt(distance)
	
def predict(training_set, test_instance, k):
	distances = []
	for row in training_set:
		distances.append( (row[-1], euclidean_distance(test_instance[:-1], row[:-1])) )
	distances.sort(key=operator.itemgetter(1))	
	class_votes = {}
	for x in distances[:k+1]:
		class_votes[x[0]] = class_votes.get(x[0], 0) + 1
	sorted_votes = sorted(class_votes.items(),key=operator.itemgetter(1),reverse=True)
	return sorted_votes[0][0]

if __name__=='__main__':
	
    data = pd.read_csv('KNN-input.csv', header=None)
    train_set, test_set = train_test_split(data, test_size=0.33, random_state=4)
    
    predictions = []
    k = 3
    print("The predictions are:")
    for x in test_set.values.tolist():
        result = predict(train_set.values.tolist(), x, k)
        predictions.append(result)
        print('predicted =', result, ' \t, actual=', x[-1])
    
    accuracy = sum([1 if x==y else 0 for x, y in zip(test_set.iloc[:, -1].values.tolist(), predictions)])/len(test_set)*100
    print('\nThe accuracy is:', accuracy, '%')	
