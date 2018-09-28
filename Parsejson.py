import unittest
import HtmlTestRunner
import json


class TestParseJson(unittest.TestCase):
    def test_parser(self):
        with open('data/distros.json') as f:
            distros_dict = json.load(f)
            print()
        for distro in distros_dict:
            print(distro['Name'], ' : ', distro['Owner'])


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
