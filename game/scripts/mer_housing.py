# -*- coding: UTF-8 -*-
import copy
import renpy.store as store
from schedule import Schedule, ScheduleObject, ScheduleJob
from collections import defaultdict


class Housing(object):

    def __init__(self):
        self._dwellers = dict()

    def dweller_house(self, person):
        return self._dwellers.get(person)

    def add_dweller(self, person, house):
        if person in self._dwellers.keys():
            self.remove_dweller(person)
        self._dwellers[person] = house
        house.add_dweller(person)

    def remove_dweller(self, person):
        try:
            house = self._dwellers[person]
            del self._dwellers[person]
        except KeyError:
            pass
        else:
            house.remove_dweller(person)

    @staticmethod
    def get_house(id, data_dict=None):
        if data_dict is None:
            data_dict = store.housing_data
        data = data_dict.get(id)
        cls = globals()[data.get('house_type')]
        return cls(data, id)

    @staticmethod
    def available_premises(type):
        ids = set()
        for key, value in store.housing_updates.items():
            if value.get('type') == type:
                ids.add(key)
        return [Housing.get_house(i, store.housing_updates) for i in ids]


class HouseType(object):

    def __init__(self, data, id):
        self.id = id
        self._data = data
        self._schedule_options = self._init_schedule_options()
        self._dwellers = []

    def add_dweller(self, person):
        self._dwellers.append(person)
        for i in self.schedule_options():
            person.schedule.add_available(i)

    def remove_dweller(self, person):
        self._dwellers.remove(person)
        for i in self.schedule_options():
            person.schedule.remove_available(i)

    def dwellers(self):
        return copy.copy(self._dwellers)

    def schedule_options(self):
        return copy.copy(self._schedule_options)

    def name(self):
        return self._data.get('name', 'No name')

    def description(self):
        return self._data.get('description', "No description")

    def available_schedule_options(self):
        return [i for i in self.schedule_options() if not i.active]

    def _init_schedule_options(self):
        options = list()
        for id, data in self._data.get('schedule_options', list()):
            data = getattr(store, data)
            if data[id].get('slot') == 'job':
                options.append(ScheduleJob(id, data))
            else:
                options.append(ScheduleObject(id, data))
        return options

    def cost(self):
        return self._data.get('cost', 0)

    def used_schedule_options(self):
        return [i for i in self._schedule_options if i.active]

    def available(self, person):
        # every house is available by default
        return True

    def type(self):
        return self._data.get('type')

    def resources(self):
        return defaultdict(int, self._data.get('resources', {}))

    def has_resources(self, used=None):
        if used is None:
            used = self.used_resources()
        resources = self.resources()
        return all(
            [value <= resources.get(key, 0) for key, value in used.items()])

    def used_resources(self):
        resources = defaultdict(int)
        for i in self.dwellers():
            for key, value in i.schedule.used_resources().items():
                resources[key] += value
        return resources

    def resource_overuse(self):
        if self.has_resources():
            return dict()
        else:
            used = self.used_resources()
            available = self.resources()
            for key, value in used.items():
                available[key] -= value
        overused = dict()
        for key, value in available.items():
            if value < 0:
                overused[key] = abs(value)
        return overused


class Hostel(HouseType):
    pass


class PremiseStore(object):

    def __init__(self, type, root, premise=None):
        self.type = type
        self.premise = premise
        self.root = root

    def set_premise(self, premise):
        dwellers = self.root.dwellers()
        if premise is not None:
            premise.root = self.root
            for i in dwellers:
                premise.add_dweller(i)
        else:
            if self.premise is not None:
                for i in dwellers:
                    self.premise.remove_dweller(i)
        self.premise = premise


class Premise(HouseType):

    def __init__(self, data, id):
        super(Premise, self).__init__(data, id)
        self.used_space = 0

    def freespace(self):
        return self._data.get('freespace', 0)

    def upkeep(self):
        return self._data.get('upkeep', 0)

class PremisedHousing(HouseType):

    def __init__(self, data, id, root=None):
        super(PremisedHousing, self).__init__(data, id)
        self._available_premises = self._make_premises(self)
        self._used_space = 0
        self.root = root

    def dwellers(self):
        if self.root is not None:
            return self.root.dwellers()
        else:
            return super(PremisedHousing, self).dwellers()

    def active_premises(self):
        return [i.premise for i in self._available_premises if i.premise is not None]

    def _make_premises(self, root):
        premises = list()
        for i in self._data.get('available_premises', list()):
            premises.append(PremiseStore(i, root, None))
        return premises

    def upkeep(self):
        inner = sum([i.upkeep() for i in self.active_premises()])
        return inner + self._data.get('upkeep', 0)

    def schedule_options(self):
        list_ = super(PremisedHousing, self).schedule_options()
        list_ += [option for i in self.active_premises() for option in i.schedule_options()]
        return list_

    def available_premises(self):
        return copy.copy(self._available_premises)

    @property
    def used_space(self):
        value = sum([i.used_space for i in self.active_premises()])
        return self._used_space + value

    def resources(self):
        resources = super(PremisedHousing, self).resources()
        for i in self.active_premises():
            for key, value in i.resources().items():
                resources[key] += value
        return resources
