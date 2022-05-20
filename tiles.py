from basetypes import Tile, Unit, RenderData, Color


class WallTile(Tile):
    def can_enter(self, unit: Unit):
        return False

    def on_draw(self, data: RenderData):
        data.text = "||"
        data.fg_color = Color(50, 255, 50)
