# -*- coding: UTF-8 -*-
import renpy.store as store
import renpy.exports as renpy

from mer_utilities import Observable, empty_card, get_files


class Command(object):
    """Basic class for commands in mer"""
    # Maybe need special allocator for commands created in modules?

    def run(self):
        raise NotImplementedError()


class Card(object):

    def image(self):
        return empty_card()

    def description(self):
        raise NotImplementedError()

    def name(self):
        raise NotImplementedError()


class WrapperCard(Card, Command):

    def __init__(self, wrapped_item):
        self._wrapped_item = wrapped_item

    def image(self):
        return self._wrapped_item.image()

    def name(self):
        return self._wrapped_item.name()

    def description(self):
        return self._wrapped_item.description()


class SeeCard(WrapperCard):

    def run(self):
        return


class MenuCard(Command, Card):
    """Basic class for card-styled menu cards"""
    def __init__(self, name=None, description=None,
                 label=None, image=None, id=None, **kwargs):
        self._name = name
        self._description = description
        self._image = image
        self._label = label
        self._context_data = dict()
        self._id = id
        self.set_context(**kwargs)

    def get_image(self):
        # testing image getting system
        path = 'images/%s/%s' % (self._image, self._id)
        images = get_files(path)
        try:
            img = images[0]
        except IndexError:
            img = None
        return img

    def image(self):
        img = self.get_image()
        if img is None:
            return empty_card()
        return img

    def description(self):
        return self._description

    def name(self):
        return self._name

    def label(self):
        return self._label

    @Observable
    def run(self):
        return renpy.call_in_new_context(self._label, self)

    def __getattr__(self, key):
        try:
            value = self._context_data[key]
        except KeyError:
            raise AttributeError(key)
        else:
            return value

    def set_context(self, **kwargs):
        # sets not 'static' data if needed in card's label
        # mostly common called before run()
        for key, value in kwargs.items():
            self._context_data[key] = value
        return self


class CardsMaker(Command):
    """Factory for easy cards creation"""
    def __init__(self, dict_=None, card_cls=None):
        self.data = dict()
        self._context_data = dict()
        if card_cls is None:
            self.card_cls = MenuCard
        else:
            self.card_cls = card_cls
        if dict_ is not None:
            for key, value in dict_.items():
                if not value.get('hidden', False):
                    self.add_entry(key, dict_)

    @Observable
    def run(self):
        list_ = []
        for key, value in self.data.items():
            card = self.card_cls(id=key, **value)
            list_.append(card.set_context(**self._context_data))
        return list_

    def add_entry(self, key, value):
        data = value[key]
        self.data[key] = data

    def remove_entry(self, key):
        try:
            del self.data[key]
        except KeyError:
            print 'No entry named %s' % key

    def set_context(self, **kwargs):
        # sets not 'static' data if needed in card's label
        # mostly common called before run()
        for key, value in kwargs.items():
            self._context_data[key] = value


class CardMenu(object):

        def __init__(self, cards_list, current=None, cancel=False, one_action=True):
            if not one_action:
                cancel = True
            self._cards_list = cards_list
            self.current_card = current
            self.cancel = cancel
            self.one_action = one_action

        @property
        def cards_list(self):
            return [i for i in self._cards_list if i != self.current_card]

        def get_sorted(self):
            return sorted(self.cards_list, key=lambda card: card.name)

        def set_card(self, card):
            current = self.current_card
            if current is not None and current not in self._cards_list:
                self._cards_list.append(self.current_card)
            self.current_card = card

        def show(self, call=True, x_size=200, y_size=300, spacing=5):
            call = True
            renpy.call_in_new_context(
                '_lbl_card_menu', self, call, x_size, y_size, spacing,
                self.cancel)

        def run(self):
            card = self.current_card
            card.run()
            if self.one_action:
                renpy.return_statement()
            else:
                self._cards_list.remove(self.current_card)
                self.current_card = None


class SeeCards(CardMenu):

    def __init__(self, cards_list):
        super(SeeCards, self).__init__(cards_list, cancel=True)

    def run(self):
        return


class SatisfySex(Command):

    def __init__(self, target, value):
        self.target = target
        self.value = value

    @Observable
    def run(self):
        pass


class MotivatedAction(Command):

    def __init__(self, person, attribute, difficulty):
        self.person = person
        self.attribute = attribute
        self.difficulty = difficulty

    def run(self):
        if UseMotivation(self.person).run():
            return Skillcheck(
                self.person, self.attribute, self.difficulty).run()
        return False


class Skillcheck(Command):

    def __init__(self, person, attribute, difficulty):

        self.person = person
        self.difficulty = difficulty
        self.attribute = attribute

    @Observable
    def run(self):
        value = self.effort()
        for i in self.person.used_motivations():
            if i.id == 'desperation':
                value -= 1
        return self.difficulty < value

    def effort(self):
        return getattr(self.person, self.attribute)() + self.person.count_modifiers('skillcheck')


class UseMotivation(Command):

    class _WrapMotivation(object):
        def __init__(self, person, motivation):
            self.person = person
            self.motivation = motivation

        def __getattr__(self, key):
            return getattr(self.motivation, key)

        def run(self):
            self.person.use_motivation(self.motivation)

    def __init__(self, person):
        self.person = person

    def run(self):
        if not self.person.has_motivation():
            return False
        cards = [self._WrapMotivation(
            self.person, i) for i in self.person.get_motivations()]
        menu = CardMenu(cards)
        menu.show()
        return True
