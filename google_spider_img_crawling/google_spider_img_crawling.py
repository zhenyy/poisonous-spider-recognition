# This motionScript will give a prediction of input json list
# User can change the prediction frequency: predict for every timeStep's data one time
# Created by Xueyang Ding
# Time: 10/02/2019 23:48

from tensorflow.keras.models import load_model
import json
import predictionToolkit

class motionPrediction:
    def __init__(self, pathToLoadMotion):
        self.motionModel = load_model(pathToLoadMotion)      # currently is DNN

    # can set the different ML model, for future development
    def setMotionModel(self, pathToLoadMotion):
        self.motionModel = load_model(pathToLoadMotion)

    """
    This method input: modtionData is the original json list, and the timeStep is the time of data used for one prediction
    """
    def motionPrediction(self, motionData, timeStep):   
        # data is synchronized and preprocessed from motionData
        data = self.motionDataProcessor(motionData)

        # data is downSampled
        downSampledData = predictionToolkit.getInstance(data)

        # use downSampledData to predict
        # the outcome looks like: [[Num1,Num2],[Num3,Num4],...]
        time, outcome = predictionToolkit.predict_DNN(downSampledData,self.motionModel)

        # voting the outcome based on given timeStep, see details in motionToolkit voting function
        outcome = predictionToolkit.voting(time, outcome, timeStep)   

        return predictionToolkit.showOutcome(outcome)

    """
    This assist method is used in the first step of motionPrediction method
    It will firstly synchronized the json data (see details in motionToolkit)
    And then concatenated the four events (two SALT and two PEPA) as one instance(see details in motionToolkit)
    """
    def motionDataProcessor(self, motionData):
        synchronizedData = predictionToolkit.json_synchronize(motionData)
        concatenatedData = predictionToolkit.processData(synchronizedData)
        return concatenatedData





#--------------------------------------------------------------------------------------------------------------------------------#
# The codes below are just for demo
# load a json file for testing, this is in order to give the json list,
# json list is regarded as the raw input for the motionScript
file = input('input json file: ')
time = input('input the seconds for each prediction: ')
load_f = open('C:\\Users\\vincent916735\\Desktop\\predictionDemo\\'+file,'r')
load_dict = json.load(load_f)

# create the json_list from the json file, the json list looks like this:
# [{"timestamp":...,"event":{"variable":"...","content":[...,...,...,...,...],"metadata":{"validity":...,"timestamp":...}}},
# {"timestamp":...,"event":{"variable":"...","content":[...,...,...,...,...],"metadata":{"validity":...,"timestamp":...}}},
# {"timestamp":...,"event":{"variable":"...","content":[...,...,...,...,...],"metadata":{"validity":...,"timestamp":t}}},...]
json_list = load_dict["data"]

# create an prediction object with instance variable: ML model. The input is the address of DNN model
mP = motionPrediction('C:\\Users\\vincent916735\\Desktop\\predictionDemo\\DNN_100epoches_concatenated_junction_4.h5')

# get the prediction result and print it out. The result is a list of predictions
# the timeStep (second) can be changed, it should be the times of 2 because the time for the unit is 2 second (see Toolkit 134 lines)
result = mP.motionPrediction(json_list,timeStep = int(time))   # one prediction for 2 seconds' data
for i in result:
    print('Event time from',i[0],'to',i[1],'predict as',i[2],'with percentage of believe：',i[3],'\n')