import cv2
import os
import pandas as pd
from difflib import SequenceMatcher

from Modules import DetectPlates
from Modules import DetectChars

SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)


def similar(a, b):
    return round(SequenceMatcher(None, a, b).ratio(), 2)


def main(fileName):

    image = cv2.imread(fileName)

    if image is None:
        print("Error: Image Not found \n")
        return

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(image)
    listOfPossiblePlatesChars = DetectChars.detectCharsInPlates(listOfPossiblePlates)

    if len(listOfPossiblePlatesChars) == 0:
        print("Warning: No license plates were detected")
        return ""

    else:
        listOfPossiblePlatesChars.sort(key=lambda possiblePlate: len(possiblePlate.strChars), reverse=True)
        licPlate = listOfPossiblePlatesChars[0]

        if len(licPlate.strChars) == 0:
            print("Warning: No characters were detected")
            return

    return licPlate.strChars


if __name__ == "__main__":

    if not DetectChars.loadKNNDataAndTrainKNN():
        print("Error: KNN traning was not successful\n")

    size = len(os.listdir("Dataset/"))

    accuracy = []
    count = 0

    for fileName in os.listdir("Dataset/"):
        recognizeText = main("Dataset/" + fileName)
        acutalText = os.path.splitext(fileName)[0]
        accuracy.append(similar(acutalText, recognizeText))
        count = count + 1
        print(str(count) + "/" + str(size) + " => " + recognizeText + " (Actual Plate value = " + acutalText + ")")

    print("Accuracy of the algorithm for dataset is " + str(sum(accuracy) / len(accuracy) * 100))