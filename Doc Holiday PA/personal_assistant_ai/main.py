## main.py

from ui import UI
from voice_interface import VoiceInterface
from file_manager import FileManager
from learning_model import LearningModel

class Main:
    def __init__(self):
        self.voice_interface = VoiceInterface()
        self.file_manager = FileManager()
        self.learning_model = LearningModel()
        self.ui = UI()

    def run(self) -> None:
        """
        Starts the UI and the main loop of the application.
        """
        self.ui.start_ui()

if __name__ == "__main__":
    main_app = Main()
    main_app.run()
