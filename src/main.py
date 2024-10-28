import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time
import re


# Define custom language functions
def press_key(key):
    pyautogui.press(key)


def hold_key(key):
    pyautogui.keyDown(key)


def release_key(key):
    pyautogui.keyUp(key)


def left_mouse_button():
    pyautogui.click(button='left')


def right_mouse_button():
    pyautogui.click(button='right')


def hold_left_mouse(duration):
    pyautogui.mouseDown(button='left')
    time.sleep(duration)
    pyautogui.mouseUp(button='left')


def hold_right_mouse(duration):
    pyautogui.mouseDown(button='right')
    time.sleep(duration)
    pyautogui.mouseUp(button='right')


def move_mouse(x, y):
    pyautogui.moveTo(x, y)


def hotkey(key1, key2):
    pyautogui.hotkey(key1, key2)


def check_rgb(r, g, b, x, y):
    pixel_color = pyautogui.screenshot().getpixel((x, y))
    return pixel_color == (r, g, b)


def wait_time(duration):
    time.sleep(duration)


def repeat_action(count, actions):
    for _ in range(count):
        execute_actions(actions)


def for_loop(var, array, actions):
    for value in array:
        globals()[var] = value  # Assign value to the variable
        execute_actions(actions)


# Define the main parser function
def parse_script(script):
    actions = []
    for line in script.splitlines():
        line = line.strip()
        if not line or line.startswith('//'):  # Ignore comments and empty lines
            continue

        # Parse commands based on your custom syntax
        if line == "lmb;":
            actions.append(("lmb",))
        elif line == "rmb;":
            actions.append(("rmb",))
        elif line.startswith("move("):
            match = re.search(r"move\((\d+), (\d+)\);", line)
            if match:
                x, y = map(int, match.groups())
                actions.append(("move", x, y))
        elif line.startswith("presskey_"):
            key = line.split('_')[1][:-1]
            actions.append(("press", key))
        elif line.startswith("holdkey_"):
            key = line.split('_')[1][:-1]
            actions.append(("hold", key))
        elif line.startswith("releasekey_"):
            key = line.split('_')[1][:-1]
            actions.append(("release", key))
        elif line.startswith("wait("):
            match = re.search(r"wait\((\d+\.?\d*)\);", line)
            if match:
                duration = float(match.group(1))
                actions.append(("wait", duration))
        elif line.startswith("holdlmb("):
            match = re.search(r"holdlmb\((\d+\.?\d*)\);", line)
            if match:
                duration = float(match.group(1))
                actions.append(("holdlmb", duration))
        elif line.startswith("holdrmb("):
            match = re.search(r"holdrmb\((\d+\.?\d*)\);", line)
            if match:
                duration = float(match.group(1))
                actions.append(("holdrmb", duration))
        elif "checkrgb" in line:
            match = re.search(r"checkrgb\((\d+), (\d+), (\d+), (\d+), (\d+)\):\[(.*)\];", line)
            if match:
                r, g, b, x, y, actions_str = match.groups()
                actions.append(("checkrgb", int(r), int(g), int(b), int(x), int(y), actions_str))
        elif line.startswith("repeat"):
            match = re.search(r"repeat\((\d+)\):\[(.*)\];", line)
            if match:
                count, actions_str = match.groups()
                actions.append(("repeat", int(count), actions_str))
        elif line.startswith("for("):
            match = re.search(r"for\((\w+), \w+, {(.*?)}\):\[(.*)\];", line)
            if match:
                var, array_str, actions_str = match.groups()
                array = array_str.split(", ")
                actions.append(("for", var, array, actions_str))
        # Add more parsing as needed
    return actions


# Execute parsed actions
def execute_actions(actions):
    for action in actions:
        cmd = action[0]
        if cmd == "lmb":
            left_mouse_button()
        elif cmd == "rmb":
            right_mouse_button()
        elif cmd == "move":
            move_mouse(action[1], action[2])
        elif cmd == "press":
            press_key(action[1])
        elif cmd == "hold":
            hold_key(action[1])
        elif cmd == "release":
            release_key(action[1])
        elif cmd == "wait":
            wait_time(action[1])
        elif cmd == "holdlmb":
            hold_left_mouse(action[1])
        elif cmd == "holdrmb":
            hold_right_mouse(action[1])
        elif cmd == "checkrgb":
            if check_rgb(action[1], action[2], action[3], action[4], action[5]):
                nested_actions = parse_script(action[6])
                execute_actions(nested_actions)
        elif cmd == "repeat":
            nested_actions = parse_script(action[2])
            repeat_action(action[1], nested_actions)
        elif cmd == "for":
            nested_actions = parse_script(action[3])
            for_loop(action[1], action[2], nested_actions)


# Define the GUI application
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ACTIONPACKED")
        self.geometry("500x400")

        self.label = tk.Label(self, text="Load and Execute .apack Script")
        self.label.pack(pady=10)

        self.load_button = tk.Button(self, text="Load .apack File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.run_button = tk.Button(self, text="Run Script", command=self.run_script, state="disabled")
        self.run_button.pack(pady=10)

        self.script_content = ""

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Apack Files", "*.apack")])
        if file_path:
            with open(file_path, "r") as file:
                self.script_content = file.read()
            self.run_button.config(state="normal")
            messagebox.showinfo("Success", f"Loaded {file_path}")

    def run_script(self):
        if self.script_content:
            actions = parse_script(self.script_content)
            execute_actions(actions)
            messagebox.showinfo("Execution", "Script executed successfully.")


# Run the Tkinter app
if __name__ == "__main__":
    app = App()
    app.mainloop()
