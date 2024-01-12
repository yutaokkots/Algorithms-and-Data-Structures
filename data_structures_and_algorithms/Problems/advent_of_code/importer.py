"""Importer module for importing the contents of an external file."""

import os 
import re
from typing import List, Match

class FileReader():
    """Class for setting and getting the contents of an external file."""

    def __init__(self):
        self.input_file_path:str = ""
        self.file_name:str = ""
        self.input_lst: List[str] = []

    def load(self, file_path: str) -> None:
        """Loads a document's contents from file into this class."""
        if os.path.isfile(file_path):
            self.input_file_path = file_path
            self.file_name = self.__file_path_parser(file_path)
            self.input_lst= self.__file_import(file_path)
        else:
            print("File does not exist.")

    def get(self) -> List[str]:
        """Returns the saved list"""
        if self.input_lst == []:
            print("Data is empty.") 
        return self.input_lst

    def save(self) -> None:
        """Saves the current data as a separate python file."""
        file_path = f"./{self.file_name}.py"
        def save_file():
            try:
                with open(file_path, "w") as file:
                    file.write('input_lst = ' + str(self.input_lst))
                print(f"Saved to file as {file_path}")
            except IOError:
                print("Unable to save file.")
        if not os.path.exists(file_path):
            if self.file_name != "":
                save_file()
            else:
                print("No data to save.")
        else:
            prompt = input("Override current file? (y / N)")
            if prompt.lower() == "y":
                save_file()
            else:
                print("Canceled operation.")

    def __file_path_parser(self, file_path: str) -> str:
        """Parses the file path to its name."""
        file_name: str = os.path.basename(file_path)
        pattern: str = r'^(.+)\.[^.]+$'
        match_name: Match = re.match(pattern, file_name)
        return match_name.group(1)
    
    def __file_import(self, input_file_path):
        """Imports the contents of a file and returns the result as a list"""
        input_lst: List[str] = []
        try:
            with open(input_file_path, 'r') as file:
                file_lines = file.readlines()
                for line in file_lines:
                    input_lst.append(str(line))
            print("File loaded.")
            return input_lst
        except FileNotFoundError:
            print("File not found.")
            return input_lst
    
