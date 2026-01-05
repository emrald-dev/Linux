from pathlib import Path

from .utils import cons, fs, copy_dir


class Themes:
    def __init__(self):
        self.dev_dir = fs.dev / "themes"
        self.sys_dir = fs.share

    def get_current_theme(self):
        cons.print("Attempting to get the current theme, please wait.")
        try:
            path = self.sys_dir / "themes/.current"

            if Path(path).exists():
                with open(path, "r") as f:
                    return f.read()

            else:
                cons.print("Update themes")

        except Exception as e:
            cons.print(e)

    def set_theme(self, theme):
        cons.print("Attempting theme setting, please wait.")
        try:
            path = self.sys_dir / "themes/.current"

            if Path(path).exists():
                with open(path, "w") as f:
                    f.write(theme)

                cons.print("Success.")

            else:
                cons.print("Update themes")

        except Exception as e:
            cons.print(e)

    def update_themes(self):
        cons.print("Attempting theme update, please wait.")
        try:
            copy_dir(self.dev_dir, self.sys_dir)

            cons.print("Success.")

        except Exception as e:
            cons.print(e)
    
    def switch_theme(self, theme):
        cons.print("Attempting apps theme update, please wait.")
        try:
            pass

        except Exception as e:
            cons.print(e)

themes = Themes()

