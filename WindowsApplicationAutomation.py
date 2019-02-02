from pywinauto.application import Application
import unittest
import string
import random


def generate_random_filename(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class WindowAppAutomation(unittest.TestCase):

    @staticmethod
    def test_automate_notepad(self):
        app = Application().start("notepad.exe")
        app.UntitledNotepad.menu_select("Help -> About Notepad")
        app.AboutNotepad.OK.click()
        app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)
        app.UntitledNotepad.menu_select("File -> Save")
        app.SaveAs.Edit.SetText(generate_random_filename())
        app.SaveAs.Save.click()
        app.UntitledNotepad.menu_select("File -> Exit")
