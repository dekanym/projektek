import flet as ft
from PIL import Image
import io
import base64

def main(page: ft.Page):

    def select_image(e):
        file_picker.pick_files(allow_multiple=False)

    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            with open(file_path, 'rb') as f:
                img_data = f.read()
            image.src_base64 = base64.b64encode(img_data).decode('utf-8')
            image.width = 300
            image.height = 300
            image.update()

            # Display image metadata
            img = Image.open(io.BytesIO(img_data))
            info_text.value = f"Format: {img.format}\nSize: {img.size}\nMode: {img.mode}"
            page.update()

    def resize_image(e):
        try:
            new_width = int(width_input.value)
            new_height = int(height_input.value)
            img = Image.open(io.BytesIO(base64.b64decode(image.src_base64)))
            img_resized = img.resize((new_width, new_height))
            buf = io.BytesIO()
            img_resized.save(buf, format='PNG')
            image.src_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            image.update()
        except Exception as ex:
            info_text.value = f"Error: {ex}"
            page.update()

    def generate_rgb_images(e):
        img = Image.open(io.BytesIO(base64.b64decode(image.src_base64)))
        r, g, b = img.split()

        def img_to_base64(img):
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            return base64.b64encode(buf.getvalue()).decode('utf-8')

        red_image.src_base64 = img_to_base64(r)
        green_image.src_base64 = img_to_base64(g)
        blue_image.src_base64 = img_to_base64(b)
        page.update()

    # UI Components
    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    select_button = ft.ElevatedButton(text="Select Image", on_click=select_image)
    image = ft.Image()
    info_text = ft.Text()

    width_input = ft.TextField(label="Width", value="300")
    height_input = ft.TextField(label="Height", value="300")
    resize_button = ft.ElevatedButton(text="Resize Image", on_click=resize_image)

    rgb_button = ft.ElevatedButton(text="Generate RGB Images", on_click=generate_rgb_images)
    red_image = ft.Image()
    green_image = ft.Image()
    blue_image = ft.Image()

    page.add(
        select_button,
        image,
        info_text,
        ft.Row([width_input, height_input, resize_button]),
        rgb_button,
        ft.Row([red_image, green_image, blue_image])
    )

ft.app(target=main)
