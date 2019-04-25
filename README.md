# Automatic Number Plate Recognition System
Please adhere to your organization's rules for using this code. For [Concordia University](http://www.concordia.ca), these rules can be found [here](http://www.concordia.ca/students/academic-integrity/offences.html).

Uses Opencv to detect the number plate in a static image of vechile.<br/>
Test Data has been scrapped from the following link: http://www.numberplates.com/pr-number-plate-gallery.asp?page=1


## Libraries used
* opencv<br/>
* pandas<br/>

## Steps Performed

### Preprocessing
* Train the KNN Classifier for character recognition.
* The given image is converted into gray-scale for feature extraction.

![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/PreProcessing%201.png?raw=true) ![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Pre%20Processing%202.png?raw=true)

### Feature Extraction
* Smoothing Image and extracting Threshold using GaussianBlur and adaptiveThreshold CV2 Functions.
* With the threshold image we try to figure out all the possible areas of a number plate.

![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Feature%20Extraction%201.png?raw=true) ![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Feature%20Extraction%202.png?raw=true) ![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Feature%20Extraction%203.png?raw=true)

### Classification
* Identify actual number plate area from set of number plates extracted from “Feature Extraction”.
* Perform KNN Classification on the identified number plate by segmenting each character and identifying them.

![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Classification%201.png?raw=true) ![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Classification%202.png?raw=true) ![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Classification%203.png?raw=true) ![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Classification%204.png?raw=true) ![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Classification%205.png?raw=true) ![Alt text](https://github.com/saitejaprasadam/Automatic-Number-Plate-Recognition-System/blob/master/Step%20in%20Images/Classification%206.png?raw=true)

### Post processing
* We calculated the accuracy in this step, and we got 80.5% on a large dataset.
