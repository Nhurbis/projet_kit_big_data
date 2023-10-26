import gradio as gr
from controller.task_controller import TaskController

class TaskView:
    def __init__(self):
        self.controller = TaskController()
        self.interface = self.create_interface()

    def create_interface(self):
        with gr.Blocks() as app:
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Add a Task")
                    with gr.Row():
                        title = gr.Textbox(label="Title")
                        status = gr.Radio(["True","False"], label="Completed")
                    output = gr.Textbox(label="Output")
                    gr.Button("Save Task").click(self.controller.add_task, inputs=[title, status], outputs=output)
                with gr.Column():
                    gr.Markdown("### All Tasks")
                    task_list = gr.Textbox(label="Tasks", elem_id="task-list", lines=10)
                    gr.Button("Show Tasks").click(self.controller.show_all_tasks, inputs=[], outputs=task_list)
        return app

    def start(self):
        self.interface.launch()