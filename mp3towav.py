#import necessary libraries
import os
import subprocess

#define a function to convert mp3 files to wav files
def convert_mp3_to_wav(input_folder, output_folder):
    #check if output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    #iterate through all the files in the input folder
    for file_name in os.listdir(input_folder):
        #if the file has a .mp3 extension, proceed with the conversion
        if file_name.endswith('.mp3'):
            #get the full path of the mp3 file
            mp3_file = os.path.join(input_folder, file_name)
            #create the full path for the output wav file
            wav_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.wav')

            #define the command for ffmpeg to convert the mp3 file to wav
            command = f'ffmpeg -i "{mp3_file}" -vn -acodec pcm_s16le -ar 44100 -ac 2 "{wav_file}"'
            #execute the command using subprocess
            subprocess.run(command, shell=True, check=True)
            #print the conversion status
            print(f'Converted {file_name} to {os.path.basename(wav_file)}')

if __name__ == '__main__':
    #define input and output folders, change for your folder
    input_folder = 'final_project/mp3_files'
    output_folder = 'final_project/wav_files'
    #call the convert_mp3_to_wav function with input and output folders
    convert_mp3_to_wav(input_folder, output_folder)