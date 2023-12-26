#!/usr/bin/env python

import shlex
import sys
import os
import getopt
import tempfile
import fnmatch

def execute(command):
    os.system(command)

def print_err(message):
    execute(">&2 echo \""+message+"\"")

def print_usage():
    usage="cbr2cbz A script utility to convert CBR files into CBZ files"
    usage+="\n\t Usage: cbr2cbz -f <filename_without_spaces.cbr>"
    usage+="\n\t                -d <directory_path_to_cbrs>"
    usage+="\n\t\n\t (Please don't use non-free formats like RAR/CBR)"
    print_err(usage)

#Extract images from a CBR file into a directory
def uncompress(filename, directory):
    UNRAR="unrar e"
    command=" ".join([UNRAR, "\""+filename+"\"", directory])
    execute(command)

#Compress a folder with images into a CBZ/ZIP file
def compress(directory, zip_filename):
    ZIP = "zip -r"  # Agregar -r para comprimir recursivamente
    # Comprimir todos los archivos en el directorio
    command = " ".join([ZIP, shlex.quote(zip_filename), "*"])
    # Cambiar al directorio y ejecutar el comando
    old_dir = os.getcwd()  # Guardar el directorio actual
    os.chdir(directory)    # Cambiar al directorio de trabajo
    execute(command)
    os.chdir(old_dir)      # Volver al directorio original

def get_filename_without_extension(filename):
    return filename[:-4]

def cbr2cbz(cbr_filename):
    # cbr_filename=file
    cbz_filename=get_filename_without_extension(cbr_filename)+".cbz"
    # use the TemporaryDirectory() methode that auto cleans/deletes files after use
    with tempfile.TemporaryDirectory() as temp_dir:
        print_err("Processing "+cbr_filename)
        #Extract images from CBR/RAR into a directory
        uncompress(cbr_filename, temp_dir)
        #Compress images and put them into a CBZ/ZIP
        compress(temp_dir, cbz_filename)

def cbr2cbzdir(cbr_dir):
    directory=os.path.abspath(cbr_dir)
    for f in os.listdir(directory):
        # check file extension
        # if .cbr, then continue 
        if fnmatch.fnmatch(f, '*.cbr'):
            filename_with_path=os.path.join(directory, f)
            print(filename_with_path)
            # calls cbr2cbz() for each individual cbr
            cbr2cbz(filename_with_path)
        else:
            # if other, print error message
            print_err("\n\twrong file type: " + f+"\n")

try:
    # sys.argv[1:] is need for all of this to work
    # TODO: check why !
  opts, args = getopt.getopt(sys.argv[1:],"hf:d:",["file=","dir="])
except getopt.GetoptError:
    print("-->\tError in parameters ! \ncbr2cbz.py -i <inputfile> -o <outputfile> -h")
    sys.exit(2)
for opt, arg in opts:
    # Help section, called by -h
    if opt == '-h':
        print("cbr2cbz.py -f <inputfile> -d <inputdirectory> -h")
        sys.exit()
    # argument parsing
    elif opt in ("-f", "--file"):
         #Call single file convert def
         print("Starting file processing..."+arg)
         cbr2cbz(arg)
    elif opt in ("-d", "--dir"):
        # Call dir convert def
        print("Starting directory processing..."+arg)
        cbr2cbzdir(arg)
print("Finished !")
