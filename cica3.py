import flet as ft

def main(page: ft.Page):
    text_field = ft.TextField(label="Name")
    switch = ft.Switch(value=False, label="Agree to terms")
    radio_options = ["Option 1", "Option 2", "Option 3"]
    dropdown_options = ["Option A", "Option B", "Option C"]
    slider = ft.Slider(value=50, min=0, max=100)

    radio_group = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value=option, label=option)
                for option in radio_options
            ]
        )
    )

    dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(option) for option in dropdown_options],
        value=dropdown_options[0]
    )

    def validate_form():
        errors = []
        if not text_field.value:
            errors.append("Name is required")
        if not switch.value:
            errors.append("You must agree to terms")
        if not radio_group.value:
            errors.append("You must select an option")
        return errors

    def submit_form(e):
        errors = validate_form()
        if errors:
            result_text.value = "Validation errors:\n" + "\n".join(errors)
        else:
            result_text.value = (
                f"Name: {text_field.value}\n"
                f"Agreed to terms: {switch.value}\n"
                f"Selected option: {radio_group.value}\n"
                f"Dropdown selection: {dropdown.value}\n"
                f"Slider value: {slider.value}"
            )
        page.update()

    submit_button = ft.ElevatedButton(text="Submit", on_click=submit_form)

    result_text = ft.Text()

    form_layout = ft.Column(
        controls=[
            text_field,
            switch,
            ft.Text("Select an option:"),
            radio_group,
            ft.Text("Select from dropdown:"),
            dropdown,
            ft.Text("Slider value:"),
            slider,
            submit_button
        ],
        spacing=10
    )

    page.add(form_layout)

    page.add(result_text)

ft.app(target=main)
