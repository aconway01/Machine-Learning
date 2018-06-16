import numpy as np

def get_data_from_file(name):
    flag = False

    # absolute path, should probably change in future
    filename = name
    while flag == False:
        try:
            infile = open(filename,"r")
            flag = True
        except:
            print("Filename not valid")
            filename = input("Enter filename: ")

    # read lines into list
    lst = infile.read().split("\n")
    infile.close()

    # Replace line with list of elements in line
    for i in range(0,len(lst)-1):
        lst[i] = [int(e) for e in lst[i].split(",")]


    # returns file data in list
    return lst

# u is a list of predicted values, v is a list of actual values
def mse(u,v):
    mean_squared_error = 0
    for i in range(len(u)):
        mean_squared_error += (1/len(u))*(u[i]-v[i])**2

    return mean_squared_error

def dot_prod(x,y):
    res = 0
    for i in range(len(x)):
        res += x[i]*y[i]

    return res

def activate(x):
    try:
        return (1/(1+np.exp(-1*x)))
    except:
        return 0.0001

def weighted(neurons,example):
    example = example[1:]
    weighted_in = dot_prod(neurons,example)
    return weighted_in

def update(neurons,alpha,delta,ex):
    new_weights = []
    ex = ex[1:]
    for i in range(len(neurons)):
        # print(alpha, err, acti, ex[i])
        new_weights.append(neurons[i] + alpha*delta*ex[i])


    return new_weights

def main():
    # list of examples, 1st index as identifier
    train = get_data_from_file("data/mnist_train_0_1.csv")
    test = get_data_from_file("data/mnist_test_0_1.csv")

    numHidden = 5
    numEpochs = 5
    alpha = 0.05
    w = []
    for i in range(numHidden):
        w.append([np.random.uniform(-1,1) for _ in range(len(train[0])-1)])

    h = [np.random.uniform(-1,1) for i in range(numHidden)]
    weighted_in = [np.random.uniform(-1,1) for i in range(numHidden)]
    activateVals = [np.random.uniform(-1,1) for i in range(numHidden)]
    deltaw = [np.random.uniform(-1,1) for i in range(numHidden)]
    activate_out = 0
    output = 0
    deltaOut = 0

    for i in range(numEpochs):
        for j in range(len(train)-1):
            output = 0
            for k in range(numHidden):
                weighted_in[k] = weighted(w[k],train[j])
                activateVals[k] = activate(weighted_in[k])

                output += (activateVals[k]*h[k])
            activate_out = activate(output)

            # calculate delta at output and hidden layers
            deltaOut = (train[j][0]-activate_out)*activate_out*(1-activate_out)
            for k in range(numHidden):
                deltaw[k] = (activateVals[k]*(1-activateVals[k])*deltaOut*h[k])

                # update weights
                h[k] = h[k] + alpha*activateVals[k]*deltaOut
                w[k] = update(w[k],alpha,deltaw[k],train[j])

    #---------------------------------------------end training

    pred_vals = []
    actual_vals = [test[i][0] for i in range(len(test)-1)]

    # predict on test set
    for i in range(len(test)-1):
        output = 0
        for j in range(numHidden):
            weighted_in[j] = weighted(w[j],test[i])
            activateVals[j] = activate(weighted_in[j])

            output += (activateVals[j]*h[j])
        activate_out = activate(output)
        if activate_out > 0.5:
            activate_out = 1
        else:
            activate_out = 0
        pred_vals.append(activate_out)

    mean_squared_error = mse(pred_vals,actual_vals)
    print(pred_vals)

    # check incorrect values
    correct = 0
    for i in range(len(pred_vals)):
        if pred_vals[i] == actual_vals[i]:
            # print("pred: ",pred_vals[i])
            # print("actual: ",actual_vals[i])
            correct += 1

    print("MSE: ",mean_squared_error)
    print("Percent Correct: ",100*correct/len(pred_vals))

main()
