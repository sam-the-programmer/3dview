from ursina import *
from ursina.prefabs.file_browser import FileBrowser
from ursina.shaders import *

from .settings import *

app = Ursina()

BLENDER_FILE = "mod.blend"
SCALE = 1

base_model = Entity(
    model=BLENDER_FILE,
    texture="white_cube",
    rotation_z=180,
    scale=SCALE,
    shader=colored_lights_shader,
)
point = Entity(model="sphere", scale=0.1, color=color.clear, parent=base_model)

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

slider_scale = Slider(
    visible=False,
    min=0,
    max=5,
    default=SCALE,
    text="Scale",
    dynamic=True,
    position=(-0.5, 0.0),
)

file_browser = FileBrowser(
    file_types=(".bam", ".ursinamesh", ".obj", ".glb", ".gltf", ".blend"), enabled=False
)


def on_submit_paths(paths):
    global BLENDER_FILE, base_model
    BLENDER_FILE = paths[0].name if paths else "cube"
    base_model.model = BLENDER_FILE


file_browser.on_submit = on_submit_paths


def toggle_file_browser():
    file_browser.enabled = not file_browser.enabled
    slider_x.visible = False
    slider_y.visible = False
    slider_ox.visible = False
    slider_oy.visible = False
    slider_scale.visible = False


change_file_browser = Button(
    text="Change File",
    color=color.orange,
    position=(-0.76, 0.2),
    scale=(0.2, 0.07),
    on_click=toggle_file_browser,
    visible=False,
)


def toggle_ui_visible():
    slider_x.visible = not slider_x.visible
    slider_y.visible = not slider_y.visible
    slider_ox.visible = not slider_ox.visible
    slider_oy.visible = not slider_oy.visible
    slider_scale.visible = not slider_scale.visible
    change_file_browser.visible = not change_file_browser.visible


show_ui = Button(
    text="Show UI",
    color=color.azure,
    position=(-0.76, 0.4),
    scale=(0.2, 0.07),
    on_click=toggle_ui_visible,
)

camera.origin = point.origin
camera.parent = point

sky = Entity(
    model="sky_dome",
    scale=200,
    shader=normals_shader,
    rotation_y=90,
    texture="sky_default",
)
