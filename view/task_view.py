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
                        completed = gr.Radio(["True","False"], label="Completed")
                    description = gr.Textbox(label="Description")
                    output = gr.Textbox(label="Output")
                    with gr.Row():
                        gr.Button("delete Task").click(self.controller.delete_task, inputs=[title], outputs=output)
                        gr.Button("Save Task").click(self.controller.add_task, inputs=[title, completed,description], outputs=output)
                    
                    gr.Markdown("### Update a Task")
                    with gr.Row():
                        old_title = gr.Textbox(label="Old Title")
                        new_title = gr.Textbox(label="new_Title")
                        new_completed = gr.Radio(["True","False"], label="Completed")
                    new_description = gr.Textbox(label="new Description")
                    output = gr.Textbox(label="Output")
                    gr.Button("update Task").click(self.controller.update_task, inputs=[old_title, new_title, new_completed, new_description], outputs=output)       
                with gr.Column():
                    gr.Markdown("### All Tasks")
                    task_list = gr.Textbox(label="Tasks", elem_id="task-list", lines=10)
                    gr.Button("Show Tasks").click(self.controller.show_all_tasks, inputs=[], outputs=task_list)
        return app

    def start(self):
        self.interface.launch()