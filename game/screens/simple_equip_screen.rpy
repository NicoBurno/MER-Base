init python:
    class ItemWrapperCard(Card):

        def __init__(self, item):
            self._item = item

        def name(self):
            return self._item.colored_name()

        def description(self):
            return self._item.description()

        def image(self):
            return self._item.image()

        def get_item(self):
            return self._item


    class UnequipCard(MenuCard):
        def __init__(self, person, slot):
            super(UnequipCard, self).__init__('Unequip', 'Unequip Item')
            self.slot = slot
            self.person = person

        def run(self, *args, **kwargs):
            self.person.equip_on_slot(self.slot, None)


    class EquipCard(ItemWrapperCard, Command):

        def __init__(self, person, item, slot, *args, **kwargs):
            super(EquipCard, self).__init__(item)
            self._person = person
            self._slot = slot

        def run(self):
            self._person.equip_on_slot(self._slot, self.get_item())

    class SellCard(ItemWrapperCard, Command):

        def __init__(self, person, item):
            super(SellCard, self).__init__(item)
            self._person = person

        def run(self):
            self._person.remove_item(self.get_item())
            self._person.add_money(self.get_item().price)

        def description(self):
            text = super(SellCard, self).description()
            text += '\n price: {price}'.format(price=self.get_item().price)
            return text

    class SellItems(Command):

        def __init__(self, person, card_menu):
            self.person = person
            self.card_menu = card_menu
        
        def run(self):
            print 'sell called'
            self.card_menu([SellCard(self.person, i) for i in self.person.unequiped_items()], cancel=True, one_action=False).show()

screen sc_simple_equip(person, look_mode=False, storage=None):
    modal True
    python:
        if storage is None:
            storage = person
    window:
        xfill True
        yfill True
        xsize 1280
        ysize 720
        style 'char_info_window'
        # vbox:
        #     imagebutton:
        #         idle im.Scale(person.avatar, 200, 200)
        #         action Show('sc_character_info_screen', person=person, communicate=True)
        #         hovered Show('sc_info_popup', person=person)
        #         unhovered Hide('sc_info_popup')
        #     text 'Money: %s'%person.money
        textbutton 'Leave':
            yalign 1.0
            action Hide('sc_simple_equip')
        hbox:
            xalign 0.35
            spacing 5
            box_wrap True
            for i in person.inventory.slots():
                python:
                    item = person.get_slot(i).get_item()
                    if item is None:
                        name = i
                        img = im.Scale(card_back(), 200, 300)
                    else:
                        name = item.colored_name()
                        img = im.Scale(item.image(), 200, 300)
                        item = EquipCard(person, person.get_slot(i).get_item(), i)
                    items = [
                        EquipCard(person, j, i) for j in person.available_for_slot(i)]

                    items.append(
                        UnequipCard(person, i))
                vbox:
                    imagebutton:
                        idle img
                        action If(look_mode, NullAction(), false=Function(CardMenu(items,
                            item).show, False))
                    text name:
                        xalign 0.5

