import gzip
import tarfile
from tarfile import TarFile
import os
from os import listdir
from os.path import isfile, join


path = os.getcwd() + '\\'

file = path + '\\phayes-geoPHP-1.2-20-g6855624.tar.gz'



def extract_tar_file(file):
    tar = TarFile.gzopen(file, mode='r')
    tar.extractall(path='tmp')
    tar.close()
    
def return_all_file_paths(base_path, tar_gz, inner_dir):
    """
    base_path:: base path to location of tar.gz
    tar_gz:: tar.gz file name
    inner_dir:: directory name inside tar.gz file

    return list [all_file_paths]

    example:
    >>>return_all_file_paths(path,
                      'phayes-geoPHP-1.2-20-g6855624.tar.gz',
                      '\\phayes-geoPHP-6855624')
    >>>['.gitignore', '.travis.yml', 'composer.json', 'geoPHP.inc', 'LICENSE', 'README.md']                  
    """
    filenames = []
    new_path = base_path + '\\tmp\\' + inner_dir
    filenames = next(os.walk(new_path))[2]

    return filenames

print(return_all_file_paths(path,
                      'phayes-geoPHP-1.2-20-g6855624.tar.gz',
                      '\\phayes-geoPHP-6855624'))

