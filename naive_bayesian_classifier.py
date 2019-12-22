import csv
from sklearn.model_selection import train_test_split
import math

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg = mean(numbers)
    return math.sqrt( sum([ pow(x-avg, 2) for x in numbers]) / float(len(numbers)-1) )

def summarize(data):
    separated = {5: [], 10: []}
    for row in data:
        separated[row[-1]].append(row[:-1])
    summary = {5: [], 10: []}
    for key, instances in separated.items():
        summary[key] = [(mean(attribute), stdev(attribute)) for attribute in zip(*instances)]
    return summary

def calculateProbability(x, mean, stdev):
    return 1/(math.sqrt(2*math.pi)*stdev) * math.exp(-math.pow(x-mean, 2)/(2*pow(stdev, 2))) if stdev!=0 else 0

def predict(summary, inp):
    probability = {5: 1, 10: 1}
    for key, summaries in summary.items():
        for x, (mean, stdev) in zip(inp, summaries):
            probability[key] *= calculateProbability(x, mean, stdev)
        print("class:", key, " \t Probability: ", probability[key])
    print()
    return 5 if probability[5]>probability[10] else 10

if __name__=='__main__':
    outlookEnum = {'Sunny': 1, 'Overcast': 2, 'Rain': 3}
    tempEnum = {'Hot': 1, 'Mild': 2, 'Cool': 3}
    humidityEnum = {'High': 1, 'Normal': 2}
    windEnum = {'Weak': 1, 'Strong': 2}
    targetEnum = {'Y': 10, 'N': 5}

    data = []
    lines = csv.reader(open('nb_data.csv'))
    for line in list(lines)[1:]:
        data.append([outlookEnum[line[0]], tempEnum[line[1]], humidityEnum[line[2]], windEnum[line[3]], targetEnum[line[4]] ])
    train_data, test_data = train_test_split(data, test_size=0.25, random_state=4)
    summary = summarize(train_data)
    
    print("{}\n{}\n{}\n{}\n{}\n".format(outlookEnum, tempEnum, humidityEnum, windEnum, targetEnum))
    print("Training data:")
    for x in train_data:
        print(x)
    print("Testing data:")
    for x in test_data:
        print(x)
    print()
    predictions = [predict(summary, x[:-1]) for x in test_data]
    actual = [x[-1] for x in test_data]
    accuracy = sum([1 if x==y else 0 for x, y in zip(predictions, actual)])/len(test_data)*100.0
    print('Actual values:', actual)
    print('predictions: ', predictions)
    print('Accuracy: ', accuracy)