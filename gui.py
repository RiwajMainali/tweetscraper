import dearpygui.dearpygui as dpg

class GUI:
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()
    with dpg.window(label=""):
        dpg.add_text("test")
    dpg.show_viewport()
    while dpg.is_dearpygui_running():
        print("this will run every frame")
        dpg.handle_events()
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

