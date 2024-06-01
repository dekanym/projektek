import flet as ft
import random

def main(page: ft.Page):
    questions = [
        {
            "question": "What is the capital of France?",
            "type": "single",
            "options": ["Paris", "London", "Rome", "Berlin"],
            "correct": ["Paris"]
        },
        {
            "question": "Which languages are spoken in Switzerland?",
            "type": "multiple",
            "options": ["German", "French", "Italian", "Spanish"],
            "correct": ["German", "French", "Italian"]
        },
        {
            "question": "What is the largest planet in our Solar System?",
            "type": "single",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct": ["Jupiter"]
        },
        {
            "question": "Which element has the chemical symbol O?",
            "type": "single",
            "options": ["Oxygen", "Gold", "Silver", "Iron"],
            "correct": ["Oxygen"]
        },
        {
            "question": "What is the smallest prime number?",
            "type": "single",
            "options": ["0", "1", "2", "3"],
            "correct": ["2"]
        },
        {
            "question": "Which of the following are programming languages?",
            "type": "multiple",
            "options": ["Python", "Java", "HTML", "CSS"],
            "correct": ["Python", "Java"]
        },
        {
            "question": "Which of the following are fruits?",
            "type": "multiple",
            "options": ["Apple", "Carrot", "Banana", "Potato"],
            "correct": ["Apple", "Banana"]
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "type": "single",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "correct": ["Mars"]
        },
        {
            "question": "Which country is the largest by area?",
            "type": "single",
            "options": ["China", "Russia", "USA", "Canada"],
            "correct": ["Russia"]
        },
        {
            "question": "Which of the following are mammals?",
            "type": "multiple",
            "options": ["Dolphin", "Shark", "Eagle", "Elephant"],
            "correct": ["Dolphin", "Elephant"]
        }
    ]

    random.shuffle(questions)  # Shuffle questions

    user_answers = {}

    def submit(e):
        score = 0
        total = len(questions)
        for i, q in enumerate(questions):
            if q["type"] == "single":
                if user_answers.get(i) in q["correct"]:
                    score += 1
            elif q["type"] == "multiple":
                if set(user_answers.get(i, [])) == set(q["correct"]):
                    score += 1
        result_text.value = f"You scored {score} out of {total}"
        page.update()

    def create_question_ui(q, index):
        if q["type"] == "single":
            options = q["options"]
            random.shuffle(options)  # Shuffle options
            radio_group = ft.RadioGroup(
                content=ft.Column(
                    [ft.Radio(label=o, value=o) for o in options],
                    spacing=10
                ),
                on_change=lambda e: user_answers.update({index: e.control.value})
            )
            return ft.Column([ft.Text(q["question"])] + [radio_group])
        elif q["type"] == "multiple":
            options = q["options"]
            random.shuffle(options)  # Shuffle options
            checkboxes = [
                ft.Checkbox(label=o, on_change=lambda e, o=o: update_multiple_answers(index, o, e.control.value))
                for o in options
            ]
            return ft.Column([ft.Text(q["question"])] + checkboxes)

    def update_multiple_answers(index, option, checked):
        if index not in user_answers:
            user_answers[index] = []
        if checked:
            user_answers[index].append(option)
        else:
            user_answers[index].remove(option)

    question_uis = [create_question_ui(q, i) for i, q in enumerate(questions)]
    submit_button = ft.ElevatedButton(text="Submit", on_click=submit)
    result_text = ft.Text()

    scrollable_column = ft.Column(
        controls=question_uis + [submit_button, result_text],
        scroll="always"
    )

    page.add(scrollable_column)

ft.app(target=main)
