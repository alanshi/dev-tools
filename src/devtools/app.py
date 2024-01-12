"""
for develop
"""
import json
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class DevTools(toga.App):

    def ecsape_button_handler(self, widget):

        json_value = self.json_text_editor.value
        json_value = json_value.replace("'", '"')
        json_value = json.loads(json_value)
        self.json_text_editor.value = json.dumps(json.dumps(
            json_value
        ))

    def format_button_handler(self, widget):
        json_value = self.json_text_editor.value
        json_value = json_value.replace("'", '"')
        json_value = json.loads(json_value)
        self.json_text_editor.value = json.dumps(
            json_value,
            indent=4,
            ensure_ascii=False
        )

    def startup(self):
        main_box = toga.Box()
        input_box = toga.Box()
        ecsape_button = toga.Button("转义", on_press=self.ecsape_button_handler, style=Pack(height=30))
        format_button = toga.Button("格式化", on_press=self.format_button_handler, style=Pack(height=30))
        self.json_text_editor = toga.MultilineTextInput(placeholder="请输入JSON文本", style=Pack(flex=1, height=600))
        input_box.add(self.json_text_editor)
        input_box.add(ecsape_button)
        input_box.add(format_button)
        main_box.add(input_box)
        main_box.style.update(direction=COLUMN, padding=20)
        self.main_window = toga.MainWindow(title=self.formal_name, size=(800, 600), position=(400, 300))
        self.main_window.content = main_box
        self.main_window.show()



def main():
    return DevTools()
