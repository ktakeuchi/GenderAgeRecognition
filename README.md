# Gender and Age Recognition Through Voice Data
## ECE4424 | Group 6
### Noah Bardenstein, Evan Donohoe, Vishakh Subramanian, Kyle Takeuchi

**How to run the iPython notebook using the provided .csv files**
The dataset that we used to train and test our model is 'full_dataset_label.csv'
The dataset that we used to test our own voices is 'custom_input.csv'

*In order to run the notebook with our supplied files:*
1. pip install necessary packages: numpy, pandas, matplotlib, seaborn, sklearn
2. Replace the .read_csv(../full_dataset_label.csv) parameters used for the model with YOUR absolute path of 'full_dataset_label.csv'
3. Replace the .read_csv(../custom_input.csv) parameters used for testing/predicting with YOUR absolute path of 'custom_input.csv' 

**How to run the iPython notebook using your custom .mp3 files**
The dataset that we used to train and test our model is 'full_dataset_label.csv'

*In order to obtain .wav files*
1. Place your .mp3 file(s) into a folder
2. Create a folder where the .wav file(s) will be stored
3. In order to run the script 'mp3towav.py', you will need to install ffmpeg
4. After installing ffmpeg, open 'mp3towav.py'
5. Correctly path the input and output folders where specified at the bottom of the script; Input folder should be the relative path to your .mp3 folder, output folder should be the relative path to your .wav folder
6. Run the script
7. Confirm that all .mp3 files have been converted into the .wav folder

*In order to obtain audio properties / .csv files*
Using RStudio and the provided GitHub repository: https://github.com/primaryobjects/voice-gender/blob/master/sound.R
1. Set the working R directory to the one containing the .wav folder (not inside the .wav folder)
2. Run all code from GitHub repository up until line 172 (end of processFolder function, ensuring all packages are installed)
3. Start the feature extraction process by calling processFolder and placing in a dataframe:
    E.g: yourDataFrameName <- processFolder('yourWavFolder')
4. After completion of extraction, use write.csv to write the dataframe data into a csv file
    E.g: write.csv(yourDataFrameName, 'yourfile.csv')
5. Open 'yourfile.csv' and remove the very first column, then remove the following: sound.files, selec, duration, peakf
6. Add the following columns after 'modindx': 'age', 'gender' (in that order)
    Add the correct values to newly created labels, so the model will know if it was accurate or not
7. Save 'yourfile.csv'

*In order to use .csv files into iPython notebook*
Observe cell #2 containing an absolute path of 'full_dataset_label.csv' & 'custom_input.csv'
1. Replace the .read_csv(../full_dataset_label.csv) parameters used for the model with YOUR absolute path of 'full_dataset_label.csv'
2. Replace the .read_csv(../custom_input.csv) parameters used for testing/predicting with YOUR absolute path of 'yourfile.csv' 
    *Your custom csv file produced from the steps before*
