from nicegui import ui

with ui.column().classes('items-center w-full'):
    ui.label('Task Complete').classes('text-red text-7xl')

ui.run(reload=False)