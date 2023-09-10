import tkinter as tk
from screeninfo import get_monitors

class Display:
    def __init__(self):
        self.root = None
        self.label = None
        self.selected_monitor = None

    def initialize(self):
        """Initialize the Tkinter window."""
        self.root = tk.Tk()
        self.root.title("Bible Verse Display")
        self.label = tk.Label(self.root, text="", font=("Helvetica", 48))
        self.label.pack()

    def show_verse(self, verse_text):
        """Display the given Bible verse on the chosen monitor.
        
        Args:
            verse_text (str): The text of the Bible verse to display.
        """
        if self.root is None:
            self.initialize()
        
        self.label.config(text=verse_text)
        self.root.update()

    def select_monitor(self):
        """Select which monitor to display the Bible verses on."""
        monitors = get_monitors()
        for i, monitor in enumerate(monitors):
            print(f"{i+1}. {monitor.name} ({monitor.width}x{monitor.height})")

        choice = int(input("Select the monitor to display verses on (by number): "))
        self.selected_monitor = monitors[choice - 1]
        
        # Position the Tkinter window on the selected monitor
        if self.root is not None:
            self.root.geometry(f"+{self.selected_monitor.x}+{self.selected_monitor.y}")

    def run(self):
        """Run the Tkinter event loop."""
        self.root.mainloop()

if __name__ == "__main__":
    display = Display()
    display.initialize()
    display.select_monitor()
    display.show_verse("Genesis 1:1 In the beginning God created the heavens and the earth.")
    display.run()
