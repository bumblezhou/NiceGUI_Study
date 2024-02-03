from nicegui import ui

with ui.row():
    ui.label(text="Title")
    ui.button(text="Search")

with ui.row():
    # Add a content grid
    with ui.grid(columns=2):
        ui.image(source="img/nicegui.png")
        ui.label(text="Image description")

        ui.label(text="Details:")
        ui.textarea()

with ui.row():
    ui.button(text="Save")
    ui.button(text="Cancel")

ui.run()