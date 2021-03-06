import csv
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

xp = []
fp = []


# this method reads in the csv file
# it returns a list of dictionaries with the attributes specified in the parameter
def read_data(filename,attributes):
    file = open(filename,encoding='UTF-8')
    reader = csv.DictReader(file)
    data = []

    temp_dict = {}
    for x in reader:
        for y in attributes:
            temp_dict[y] = x[y]
        data.append(temp_dict)
        temp_dict = {}
    file.close()
    return data


def linear_interpolation(x):
    z = np.interp(x, xp, fp)
    return z


def run_neural_network(data,attributes):
    for x in data:
        # converts males to 0 females to 1.0
        x['Sex'] = 0.0 if x['Sex'] == 'male' else 1.0
        if x['Age'] == '':
            x['Age'] = round(linear_interpolation(float(x['Fare'])))
    for x in data:
        for y in attributes:
            x[y] = float(x[y])
    x_list = []
    y_list = []

    # train on first 70% of data
    for x in range(int(len(data) * .7)):
        y_list.append(float(data[x].get('Survived')))
        temp_list = []
        for y in attributes:
            temp_list.append(data[x].get(y))
        x_list.append(temp_list)
        temp_list = []

    scaler = StandardScaler()
    scaler.fit(x_list)
    x_list = scaler.transform(x_list)

    mlp = MLPClassifier(hidden_layer_sizes=(4, 4, 4), max_iter=10000)
    mlp.fit(x_list,y_list)

    test_list = []
    test_answers = []
    thirty_percent = int(len(data) * .3)
    # test on last 30% of data
    for x in range(len(data) - 1, len(data) - thirty_percent, -1):
        temp_list = []
        test_answers.append(int(data[x]['Survived']))
        for y in attributes:
            temp_list.append(data[x].get(y))
        test_list.append(temp_list)
        temp_list = []
    test_list = scaler.transform(test_list)
    predict = mlp.predict(test_list)
    count = 0
    print('[Pclass, Sex, Age, Fare] Normalized data')
    for x in range(len(predict)):
        rounded = int(round(predict[x]))
        temp_string = str(test_list[x])
        print(temp_string + " actual " + str(test_answers[x]) + " predicted " + str(rounded))
        if rounded == test_answers[x]:
            count += 1
    print("Percent correct " + str(count / thirty_percent))


def main():
    attributes = ['Pclass', 'Sex', 'Age', 'Fare', 'Survived']
    data = read_data('titanic_data.csv', attributes)
    temp = []
    attributes.remove('Survived')

    # get the data for linear interpolation
    # i am using fare as the x value
    for x in data:
        if x['Age'] != '':
            temp.append([x['Fare'], x['Age']])
    # the fares needs to be sorted in non decreasing order
    temp = sorted(temp)
    # put data in global list to be used every time linear interpolation method is called
    for x in temp:
        xp.append(float(x[0]))
        fp.append(float(x[1]))
    run_neural_network(data,attributes)


main()