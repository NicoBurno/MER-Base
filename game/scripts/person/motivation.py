# -*- coding: <UTF-8> -*-
import renpy.store as store
import renpy.exports as renpy
from mer_utilities import encolor_text, get_files, empty_card


class Motivation(object):
    _colors = {
        'desperation': 'red',
        'stress': 'magenta',
        'determination': 'green',
        'enthusiams': 'gold'
    }
    _images_bg = {
        'desperation': 'bronze',
        'stress': 'silver',
        'determination': 'silver',
        'enthusiams': 'gold'
    }

    def __init__(self, id):

        self.id = id

    def type(self):
        return self.data().get('type')

    def data(self):
        return store.motivations_data[self.id]

    def image(self):
        return empty_card()
        bg_image = 'images/motivations/' +\
            self._images_bg[self.type()] + '.jpg'
        return renpy.display.im.Composite(
            (0, 0), self.get_image(),
            (0, 0), bg_image)

    def description(self):
        return self.data().get('description', 'No description')

    def get_image(self):
        # testing image getting system
        path = 'images/%s/%s' % (self.data().get('image'), self.id)
        images = get_files(path)
        try:
            img = images[0]
        except IndexError:
            img = None
        return img

    def name(self):
        return encolor_text(self.data().get('name'),
                            self._colors[self.type()])

    def _run_label(self):
        return 'lbl_motivation_%s_run' % self.type()

    def run(self, person):
        renpy.call_in_new_context(
            self._run_label(), motivation=self, person=person)
