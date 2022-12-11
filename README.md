# medficient
# Project Goals
The overall goals of this project are to build a model that can predict length of stay and total costs for patients at New York hospitals at the time of their admission. This project also seeks to find if a hospital should build different models for each condition type or if one general model can suffice. Finally the output of this project is an interactive form where users can enter patient admission information and recieve a prediciton of their estimated length of stay and total cost.

# A Note About the Data Sample
We have included a sample of our input data in our repository. The code can be run with this data alone. However, it is advised to use the instructions in the following section to download the entire dataset for results that are closest to our final report. In addition, our models used for our final deliverable are also in the repository.

# Downloading the Data
This project uses two years of data (2017 and 2018) from the New York State Health Department.<br />

Our datafiles can be accessed at the following links: <br />
[Hospital Inpatient Discharges (SPARCS De-Identified): 2017](https://health.data.ny.gov/dataset/Hospital-Inpatient-Discharges-SPARCS-De-Identified/22g3-z7e7) <br />
[Hospital Inpatient Discharges (SPARCS De-Identified): 2018](https://healthdata.gov/State/Hospital-Inpatient-Discharges-SPARCS-De-Identified/apnh-6ij9) <br />

The datasets can also be accessed in this GoogleDrive Folder: https://drive.google.com/drive/folders/16ArFAaK9vJiAV9V8LqEI7vqeHtvA-X2V

Please use either of those resources to download the data files and save them to the data/raw directory.

# Data Pipeline
To run our code please run the pipeline.py notebook. That notebook runs our data pipeline and creates the cleaned datasets, the models, and outputs our form. The pipeline is as follows:<br />

# Modeling Exploration
We have also included some notebooks to show how our team landed on our final models. These notebooks are in the notebook folder. Once the datafiles are in their correct location, these notebooks can be run as is.
