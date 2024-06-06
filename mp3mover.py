#import necessary libraries
import os
import shutil
import pandas as pd

#define a function to move files from one folder to another based on the file names in a CSV file
def move_matching_files(csv_file_path, column_name, src_folder, dst_folder):
    #check if the destination folder exists, if not create it
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    #read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)
    #print(df[column_name].head())
    #iterate through the file names in the specified column
    for file_name in df[column_name]:
        #construct the source and destination file paths by joining the folders and file name
        src_file = os.path.join(src_folder, file_name)
        dst_file = os.path.join(dst_folder, file_name)

        #check if the source file exists and is a file
        if os.path.isfile(src_file):
            # Move the file from source folder to destination folder
            shutil.move(src_file, dst_file)
            # Print a message showing the file has been moved
            print(f'Moved {file_name} to {dst_folder}')

if __name__ == '__main__':
    #define the input parameters for the function
    csv_file_path = 'final_project/train-test-data.csv'
    column_name = 'filename'
    src_folder = 'final_project/cv-valid-train'
    dst_folder = 'final_project/mp3_files'
    #call the function with the specified input parameters
    move_matching_files(csv_file_path, column_name, src_folder, dst_folder)