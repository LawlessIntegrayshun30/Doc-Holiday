## file_manager.py
import os
import shutil
from typing import List

class FileManager:
    def list_files(self, directory: str = '.') -> List[str]:
        """
        Lists all files in the given directory.

        :param directory: The directory to list files from.
        :return: A list of file names.
        """
        try:
            files = os.listdir(directory)
            return [file for file in files if os.path.isfile(os.path.join(directory, file))]
        except FileNotFoundError:
            print(f"The directory {directory} does not exist.")
            return []
        except PermissionError:
            print(f"Permission denied to access the directory {directory}.")
            return []

    def manage_file(self, action: str, file_path: str) -> None:
        """
        Manages a file by performing the specified action.

        :param action: The action to perform on the file ('delete', 'copy', 'move').
        :param file_path: The path to the file to manage.
        """
        # Ensure the file_path is a file
        if not os.path.isfile(file_path):
            print(f"The file path {file_path} is not a file or does not exist.")
            return

        # Perform the action
        try:
            if action == 'delete':
                os.remove(file_path)
                print(f"File {file_path} has been deleted.")
            elif action == 'copy':
                # Set a default destination path for the copy
                destination_path = file_path + '.copy'
                shutil.copy2(file_path, destination_path)
                print(f"File {file_path} has been copied to {destination_path}.")
            elif action == 'move':
                # Set a default destination path for the move
                destination_path = file_path + '.moved'
                shutil.move(file_path, destination_path)
                print(f"File {file_path} has been moved to {destination_path}.")
            else:
                print(f"Action {action} is not supported.")
        except OSError as e:
            print(f"An error occurred while managing the file: {e}")
