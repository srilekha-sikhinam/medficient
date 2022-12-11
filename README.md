# medficient
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
We have included a sample of our input data in our repository and the model that is required to run the output form. The raw data filse are located in the data/raw folder and the models are located in the models/ folder. The code can be run with the preloaded raw data (which the pipeline will process) and models. However, it is advised to use the instructions in the following section to download the entire dataset for results that are closest to our final report..

# Downloading the Data
This project uses two years of data (2017 and 2018) from the New York State Health Department.<br />

Our datafiles can be accessed at the following links: <br />
[Hospital Inpatient Discharges (SPARCS De-Identified): 2017](https://health.data.ny.gov/dataset/Hospital-Inpatient-Discharges-SPARCS-De-Identified/22g3-z7e7) <br />
[Hospital Inpatient Discharges (SPARCS De-Identified): 2018](https://healthdata.gov/State/Hospital-Inpatient-Discharges-SPARCS-De-Identified/apnh-6ij9) <br />

The datasets can also be accessed in this GoogleDrive Folder: https://drive.google.com/drive/folders/16ArFAaK9vJiAV9V8LqEI7vqeHtvA-X2V

Please use either of those resources to download the data files and save them to the data/raw directory.

# Data Pipeline
To run our code please run the pipeline.py notebook. That notebook runs our data pipeline and creates the cleaned datasets, the models, and outputs our form. The pipeline is as follows:<br />
![image](https://user-images.githubusercontent.com/78450547/206885277-6fce9dd0-7fe1-43a8-a4b5-517c4ae6e922.png)

Note: To save runtime, by default, the file only loads the model for knee replacement patients. If you would like to run the model for all conditions (Heart Failure, COPD, Schizophrenia, Kidney/UTI, and Knee Replacement patients), please comment out the lines mentioned in pipeline.py. In addition, comment out the lines training the models in train_length_of_stay_model.py and train_cost_model.py. Running the pipeline for all the models can take around 30-40 minutes for all the models to load in. The model for all patients takes most of the time.

# Modeling Exploration
We have also included some notebooks to show how our team landed on our final models. These notebooks are in the notebook folder. Once the datafiles are in their correct location, these notebooks can be run as is. Please note that these files do take quite a bit of time (over an hour) to run.
