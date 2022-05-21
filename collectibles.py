from basetypes import RenderData, Unit
from units import Collectible


class KeyPickup(Collectible):
    def on_draw(self, data: RenderData):
        data.text = "⎆⏔"

    def on_pickup(self, unit: Unit):
        super().on_pickup(unit)
