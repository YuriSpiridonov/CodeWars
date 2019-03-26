# https://www.codewars.com/kata/extract-file-name/train/python

import re 
class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        regex = re.compile(r'^\d+_([a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+)\.')
        mo = regex.search(dirty_file_name)
        return mo.group(1)

print(FileNameExtractor.extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"))#,"FILE_NAME.EXTENSION")
print(FileNameExtractor.extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"))#,"FILE_NAME.EXTENSION")
