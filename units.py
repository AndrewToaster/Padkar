from basetypes import Unit


class Collectible(Unit):
    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def can_pickup(self, unit: Unit):
        return True

    # noinspection PyMethodMayBeStatic
    def on_pickup(self, unit: Unit):
        # avoids cyclic dependency (I think)
        from mapping import Map
        Map.current.tile_at(unit.position).unit = None

    def on_contact(self, unit: Unit):
        if self.can_pickup(unit):
            self.on_pickup(unit)
