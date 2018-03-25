import csv
from sklearn import linear_model


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
    return data


def linear_interpolation(x0,x,x1,y0,y1):
    return (y0*(x1-x) + y1*(x-x0)) / (x1 - x0)

    
def regression():
    attributes = ['Pclass','Sex','Age','Fare','Survived']
    data = read_data('../titanic_data.csv',attributes)
    for x in data:
        x['Sex'] = 0.0 if x['Sex'] == 'Male' else 1.0
        x['Age'] = 10.0 if x['Age'] == '' else float(x['Age'])
    for x in data:
        for y in attributes:
            x[y] = float(x[y])
    attributes.remove('Survived')
    x_list = []
    y_list = []

    for x in range(int(len(data)*.7)):
        y_list.append(float(data[x].get('Survived')))
        temp_list = []
        for y in attributes:
            temp_list.append(data[x].get(y))
        x_list.append(temp_list)
        temp_list = []
    lr = linear_model.LinearRegression()
    lr.fit(x_list,y_list)
    print('The coefficients are ' + str(lr.coef_))

    test_list = []
    test_answers = []
    thirty_percent = int(len(data)*.3)
    # seventy_percent = int(len(data)*.7)
    for x in range(len(data)-1,len(data) - thirty_percent, -1):
        temp_list = []
        test_answers.append(int(data[x]['Survived']))
        for y in attributes:
            temp_list.append(data[x].get(y))
        test_list.append(temp_list)
        temp_list = []
    predict = lr.predict(test_list)
    count = 0
    print('[Pclass, Sex, Age, Fare]')
    for x in range(len(predict)):
        rounded = int(round(predict[x]))
        temp_string = str(test_list[x])
        print(temp_string + " actual " + str(test_answers[x]) + " predicted " + str(rounded))
        if rounded==test_answers[x]:
            count += 1
    print("Percent correct " + str(count/thirty_percent))


regression()