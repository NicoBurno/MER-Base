import renpy.store as store
import renpy.exports as renpy
from mer_utilities import weighted_random


class Wish(object):
    "Wish object simply wraps renpy dict and labels"

    def __init__(self, id_):

        self.id = id_

    def name(self):
        return self.data.get('name', "No name")

    def description(self):
        return self.data.get('description', 'No description')

    def _get_label(self, name):
        return 'lbl_wish_%s_%s' % (self.id, name)

    def _end_label(self):
        return self._get_label('end')

    def _turn_end_label(self):
        return self._get_label('turn_end')

    def _chance_label(self):
        return self._get_label('chance')

    def _fulfill_label(self):
        return self._get_label('fulfill')

    @property
    def data(self):
        return store.wishes_data.get(self.id)

    def activate(self, person):
        # called when whish is fulfilled
        renpy.call_in_new_context(self._end_label(), person=person)

    def turn_end(self, person):
        # called at end of each turn
        renpy.call_in_new_context(self._turn_end_label(), person=person)

    def appearance_chance(self, person):
        # gets chance for wish to appear at this person
        chance = renpy.call_in_new_context(self._chance_label(), person=person)
        return max(0, chance)

    def fulfilled(self, person):
        # checks if wish fulfilled or not
        return renpy.call_in_new_context(self._fulfill_label(), person=person)


class WishesGenerator(object):

    def __init__(self, max_wishes=3):
        self.max_wishes = max_wishes

    def _get_wishes(self):
        return store.wishes_data.keys()

    def make_wishes(self, person):
        wishes_amount = len(person.wishes())
        available_wishes = [Wish(i) for i in self._get_wishes()
                            if not person.has_wish(i)]
        pairs = {}
        for i in available_wishes:
            chance = i.appearance_chance(person)
            if chance > 0:
                pairs[i] = chance
        while wishes_amount < self.max_wishes and len(pairs.keys()) > 0:
            wish = weighted_random(pairs)
            del pairs[wish]
            person.add_wish(wish)