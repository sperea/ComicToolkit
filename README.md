# ComicToolkit

Welcome to ComicToolkit, a versatile suite of scripts for comic book enthusiasts and digital librarians. This repository is dedicated to providing tools for efficient management and manipulation of digital comic book files. Whether you need to convert file formats, organize your collections, or batch rename files, ComicToolkit is here to simplify your digital comic handling.

## Features
- Format conversion (CBR to CBZ)
- Batch operations for file management
- Easy-to-use scripts for organizing comic collections
- And more coming soon!



## CBR to CBZ Conversion Script

One of the key features of ComicToolkit is the CBR to CBZ conversion script. This Python script allows you to convert your comic book files from CBR (Comic Book RAR) format to CBZ (Comic Book ZIP) format. It's designed to work recursively, processing files not only in the current directory but also in all subdirectories.

### Usage

To use the CBR to CBZ script, follow these steps:

- Ensure you have Python installed on your system.
- Clone or download this repository to your local machine.
- Navigate to the directory containing cbr2cbz.py.
- Run the script with the command python cbr2cbz.py -d <directory_path_to_cbrs>, where <directory_path_to_cbrs> is the path to your comics.

## cbr2cbz_all

cbr2cbz_all.sh is a shell script crafted to automate the conversion of digital comic files from CBR format to CBZ across multiple subdirectories. This script is an essential tool for those looking to streamline the management of their digital comic collection. Upon execution, cbr2cbz_all.sh recursively searches for all CBR files in each subdirectory of the directory from which it is run, excluding the current directory itself. It then utilizes the cbr2cbz.py script to convert each found file to the CBZ format. This approach simplifies the organization and conversion of large collections, optimizing the process and saving valuable time. Ideal for digital comic libraries, enthusiasts, and collectors wishing to maintain their files in a uniform and accessible format.

## Contributing

I welcome contributions to ComicToolkit! If you have suggestions for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions or feedback, please don't hesitate to reach out.

Happy comic organizing!

