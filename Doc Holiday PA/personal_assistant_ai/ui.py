## ui.py

import tkinter as tk
from tkinter import messagebox
from voice_interface import VoiceInterface
from file_manager import FileManager
from learning_model import LearningModel

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Personal Assistant")
        self.voice_interface = VoiceInterface()
        self.file_manager = FileManager()
        self.learning_model = LearningModel()
        self.create_widgets()

    def start_ui(self) -> None:
        """
        Starts the UI loop.
        """
        self.root.mainloop()

    def create_widgets(self) -> None:
        """
        Creates the widgets for the UI.
        """
        # Button to listen for commands
        self.listen_button = tk.Button(self.root, text="Listen", command=self.listen)
        self.listen_button.pack()

        # Label to display the recognized command
        self.command_label = tk.Label(self.root, text="Command will appear here")
        self.command_label.pack()

        # Label to display the action taken
        self.action_label = tk.Label(self.root, text="Action will appear here")
        self.action_label.pack()

    def listen(self) -> None:
        """
        Listens for a voice command and processes it.
        """
        command = self.voice_interface.listen()
        self.command_label.config(text=f"Recognized: {command}")

        if command:
            action = self.learning_model.predict(command)
            self.process_action(action, command)

    def process_action(self, action: str, command: str) -> None:
        """
        Processes the action predicted by the learning model.

        :param action: The action to perform.
        :param command: The original command spoken by the user.
        """
        if action == "manage_file":
            # For simplicity, we assume the command includes the file path and action
            file_path = command.split()[1]  # This is a simplification
            file_action = command.split()[0]  # This is a simplification
            self.file_manager.manage_file(file_action, file_path)
            self.action_label.config(text=f"Performed file action: {file_action} on {file_path}")
        elif action == "speak_response":
            response = "This is a response to your command."
            self.voice_interface.speak(response)
            self.action_label.config(text=f"Spoken response: {response}")
        else:
            messagebox.showerror("Error", "Unknown action.")
            self.action_label.config(text="Error: Unknown action.")
