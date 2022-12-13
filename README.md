# Data Science Approaches in Medicine
## Leveraging novel machine learning techniques to model New York patients’ total hospital costs and length of stay

This project was completed by Mitchell Burke, Urvi Joshi and Srilekha Sikhinam.

# Project Goals
The overall goals of this project are to build a model that can predict length of stay and total costs for patients at New York hospitals at the time of their admission. This project also seeks to find if a hospital should build different models for each condition type or if one general model can suffice. Finally the output of this project is an interactive form where users can enter patient admission information and recieve a prediciton of their estimated length of stay and total cost.

# Getting Started
## Clone the repo
Use the following command to clone the repo
```
git clone https://github.com/srilekha-sikhinam/medficient.git
```
## Install required packages
The following command will install all required libraries for the project
```
pip install -r requirements.txt
```

# A Note About the Data Sample
We have included a sample of our input data in our repository and the model that is required to run the output form. The raw data files are located in the data/raw folder and the models are located in the models/ folder. The code can be run with the preloaded raw data (which the pipeline will process) and models. However, it is advised to use the instructions in the following section to download the entire dataset for results that are closest to our final report.

# Downloading the Data
This project uses two years of data (2017 and 2018) from the New York State SPARCS dataset, which is the entity that owns the dataset.<br />

Our datafiles can be accessed at the following links: <br />
[Hospital Inpatient Discharges (SPARCS De-Identified): 2017](https://health.data.ny.gov/dataset/Hospital-Inpatient-Discharges-SPARCS-De-Identified/22g3-z7e7) <br />
[Hospital Inpatient Discharges (SPARCS De-Identified): 2018](https://healthdata.gov/State/Hospital-Inpatient-Discharges-SPARCS-De-Identified/apnh-6ij9) <br />

After navigating to those links, click 'Export' and select the 'CSV' button. This will start the file download.

The datasets can also be accessed in this GoogleDrive Folder: https://drive.google.com/drive/folders/16ArFAaK9vJiAV9V8LqEI7vqeHtvA-X2V

Please use either of those resources to download the data files and save them to the data/raw directory. Please do not change any default file names. In addition, after you add the files to the data/raw folder please make sure to delete any data and pre-trained model files that are present when cloning the git repository. This includes any files in the data/raw folder, data/processed, and models/ folder. When you download the entire dataset and place the files in data/raw, the pipeline.ipynb file will recreate the datasets that are currently in the data/processed folder.

# Data Pipeline
To run our code please run the pipeline.ipynb notebook. That notebook runs our data pipeline and creates the cleaned datasets, the models, and outputs our form. The pipeline is as follows:<br />
![image](https://user-images.githubusercontent.com/78450547/206885277-6fce9dd0-7fe1-43a8-a4b5-517c4ae6e922.png)

Note: To save runtime, by default, the file only loads the model for knee replacement patients. If you would like to run the model for all conditions (Heart Failure, COPD, Schizophrenia, Kidney/UTI, and Knee Replacement patients), please comment out the lines mentioned in pipeline.py. In addition, comment out the lines training the models in train_length_of_stay_model.py and train_cost_model.py. Running the pipeline for all the models can take around 30-40 minutes for all the models to load in. The model for all patients takes most of the time. Additionally, the non-knee replacement models are not used in the pipeline or in any notebooks.

# Modeling Exploration
We have also included some notebooks to show how our team landed on our final models. These notebooks are in the notebooks folder. Once the datafiles are in their correct location, these notebooks can be run as is. Please note that these files do take quite a bit of time (over an hour) to run.<br />
* notebooks/length_of_stay_classification_model_explorations.ipynb: This notebook walks through how we generated our final classification model for length of stay. The notebook can be used to change model parameters to see how the results change. This notebook generates visualizations that are similar to the ones in our final report. The values may be slightly different as they can change from run to run.
* notebooks/length_of_stay_regression_model_explorations.ipynb: This notebook walks through how we generated our final regression model for length of stay. The notebook can be used to change model parameters to see how the results change. This notebook generates visualizations that are similar to the ones in our final report. The values may be slightly different as they can change from run to run.
* notebooks/Total Cost Classification Model.ipynb: This notebook walks through how we generated our final classification model for total cost. The notebook can be used to change model parameters to see how the results change. This notebook generates visualizations that are similar to the ones in our final report. The values may be slightly different as they can change from run to run.
* notebooks/Total Cost Regression Model.ipynb: This notebook walks through how we generated our final regression model for total cost. The notebook can be used to change model parameters to see how the results change. This notebook generates visualizations that are similar to the ones in our final report. The values may be slightly different as they can change from run to run.
* src/visualizations/visualizations.ipynb: This notebook uses saved scores from a single run of the notebooks above and creates the visualizations with the exact values that are in the final report.

# A note about operating system
We have tried to build and test these notebooks and pipeline so that it works for all operating systems. However, we have found some issues with filepaths. Windows uses the '\\' character and Linux/Darwin uses '/'. We believe we have fixed most of these issues. However, if you encounter a 'FileNotFound' error, please check the filepaths in the notebook you are running and change them to match your operating system if needed. If you encouter the error while running the pipeline, please check the filepaths in the following files:
* src/models/train_cost_model.py
* src/models/train_length_of_stay_model.py
* src/models/predict_model.py
* form.py

We also found that on Linux when running the pipeline notebook, you may get this error:
```
Traceback (most recent call last):
  File "main.py", line 212, in <module>
    root = Tk()
  File "/opt/conda/lib/python3.7/tkinter/__init__.py", line 2023, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable
```
It occurs when the pipeline is trying to display the input form. To remedy this, please run the following:
```
! sudo apt-get install python-tk
! sudo apt-get install -y xvfb
```
```
import os
os.system("Xvfb :1 -screen 0 720x720x16 &")
os.environ['DISPLAY'] = ":1.0"
```
If that does not remedy the issue when running the pipeline, please run the form.py file on it's own after the models and processed data files are generated by pipeline.ipynb.

