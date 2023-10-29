import gradio as gr
from controller.task_controller import TaskController


def create_gradio_interface():
    with gr.Blocks() as app:
        with gr.Row():
            gr.Markdown("# Gestionnaire de Tâches")

        with gr.Row():
            title_input = gr.Textbox(label="Titre")
            add_tasklist_btn = gr.Button("Ajouter Liste de Tâches")
            add_tasklist_btn.click(add_tasklist, inputs=[
                                   title_input], outputs=gr.Textbox())

        with gr.Row():
            tasklist_id_input = gr.Textbox(label="ID de la Liste de Tâches")
            name_input = gr.Textbox(label="Nom")
            description_input = gr.Textbox(label="Description")
            add_task_btn = gr.Button("Ajouter Tâche")
            add_task_btn.click(add_task, inputs=[
                               tasklist_id_input, name_input, description_input], outputs=gr.Textbox())

        with gr.Row():
            tasklist_id_input = gr.Textbox(label="ID de la Liste de Tâches")
            task_id_input = gr.Textbox(label="ID de la Tâche")
            complete_task_btn = gr.Button("Marquer Tâche comme Terminée")
            complete_task_btn.click(complete_task, inputs=[
                                    tasklist_id_input, task_id_input], outputs=gr.Textbox())

        with gr.Row():
            tasklist_id_input = gr.Textbox(label="ID de la Liste de Tâches")
            task_id_input = gr.Textbox(label="ID de la Tâche")
            delete_task_btn = gr.Button("Supprimer Tâche")
            delete_task_btn.click(delete_task, inputs=[
                                  tasklist_id_input, task_id_input], outputs=gr.Textbox())

        with gr.Row():
            tasklist_id_input = gr.Textbox(label="ID de la Liste de Tâches")
            show_incomplete_tasks_btn = gr.Button("Afficher Tâches en Cours")
            show_incomplete_tasks_btn.click(show_incomplete_tasks, inputs=[
                                            tasklist_id_input], outputs=gr.Textbox())

    return app


def add_tasklist(title: str):
    response = TaskController.create_tasklist(title)
    return response


def add_task(tasklist_id: str, name: str, description: str):
    response = TaskController.add_task_to_tasklist(
        tasklist_id, name, description)
    return response


def complete_task(tasklist_id: str, task_id: str):
    response = TaskController.complete_task(tasklist_id, task_id)
    return response


def delete_task(tasklist_id: str, task_id: str):
    response = TaskController.delete_task(tasklist_id, task_id)
    return response


def show_incomplete_tasks(tasklist_id: str):
    response = TaskController.get_incomplete_tasks(tasklist_id)
    return response
