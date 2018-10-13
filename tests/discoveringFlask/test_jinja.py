
import unittest

import jinja2

from pyMicroservices.discoveringFlask import resources


class TestJinja2Utils(unittest.TestCase):

    def test_item_list(self):
        with open(resources.path('itemList.txt'), 'r') as fp:
            text = fp.read()
        template = jinja2.Template(text)
        t = template.render(items=[
            {'name': 'ak47c', 'price': '400'},
            {'name': 'm16a4', 'price': '800'},
            {'name': 'xm12', 'price': '1200'},
        ])
        print t


if __name__ == '__main__':
    unittest.main()
