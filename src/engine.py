from ursina import Entity, Slider, Ursina, color, Button, camera

from .settings import *

app = Ursina()
cube = Entity(model="cube", scale=2, texture="white_cube")
point = Entity(model="sphere", scale=0.1, color=color.clear, parent=cube)

slider_x = Slider(
    visible=False,
    min=0,
    max=5,
    default=MOVE_FACTOR_X,
    text="Factor X",
    dynamic=True,
    position=(-0.5, 0.4),
)

slider_y = Slider(
    visible=False,
    min=0,
    max=5,
    default=MOVE_FACTOR_Y,
    text="Factor Y",
    dynamic=True,
    position=(-0.5, 0.3),
)

slider_ox = Slider(
    visible=False,
    min=0,
    max=1,
    default=OFFSET_X,
    text="Offset X",
    dynamic=True,
    position=(-0.5, 0.2),
)

slider_oy = Slider(
    visible=False,
    min=0,
    max=1,
    default=OFFSET_Y,
    text="Offset Y",
    dynamic=True,
    position=(-0.5, 0.1),
)


def toggle_sliders_visible():
    slider_x.visible = not slider_x.visible
    slider_y.visible = not slider_y.visible
    slider_ox.visible = not slider_ox.visible
    slider_oy.visible = not slider_oy.visible


show_ui = Button(
    text="Show UI",
    color=color.azure,
    position=(-0.76, 0.4),
    scale=(0.2, 0.07),
    on_click=toggle_sliders_visible,
)


camera.origin = point.origin
camera.parent = point
camera.position += camera.back * 120
