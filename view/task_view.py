import gradio as gr
from controller.task_controller import TaskController


def create_gradio_interface():
    with gr.Blocks() as app:
        with gr.Row():
            gr.Markdown("# Gestionnaire de Tâches")
        
        with gr.Row():
            gr.Markdown("# Ajout Tasklist")
            
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    title_input = gr.Textbox(label="Titre de la tasklist")
                    add_tasklist_btn = gr.Button("Ajouter Liste de Tâches")
                    
            with gr.Column():
                    output_create_tasklist = gr.Textbox(label="ID de la Liste de Tâches", lines=1)
                    add_tasklist_btn.click(add_tasklist, inputs=[
                                        title_input], outputs=output_create_tasklist)
        with gr.Row():
            gr.Markdown("# Ajout Task à une Tasklist")     

        with gr.Row():
            with gr.Row():
                tasklist_id_input = gr.Textbox(label="ID de la Liste de Tâches")
                name_input = gr.Textbox(label="Nom de la tâches")
                description_input = gr.Textbox(label="Description")
            with gr.Row():
                add_task_btn = gr.Button("Ajouter Tâche")
                output_add_task = gr.Textbox(label="ID de la Tâche", lines=1)
                add_task_btn.click(add_task, inputs=[
                            tasklist_id_input, name_input, description_input], outputs=output_add_task)

        with gr.Row():
            gr.Markdown("# Gestion des Tâches") 

        with gr.Row():
            tasklist_id_input = gr.Textbox(label="ID de la Liste de Tâches")
            task_id_input = gr.Textbox(label="ID de la Tâche")
            complete_task_btn = gr.Button("Marquer Tâche comme Terminée")
            output_complete_task = gr.Textbox(label="Tâche Terminée", lines=1)
            complete_task_btn.click(complete_task, inputs=[
                                            tasklist_id_input, task_id_input], outputs=output_complete_task)
        with gr.Column():
            with gr.Row():
                tasklist_id_input = gr.Textbox(label="ID de la Liste de Tâches")
                task_id_input = gr.Textbox(label="ID de la Tâche")
                delete_task_btn = gr.Button("Supprimer Tâche")
                output_delete_task = gr.Textbox(label="Tâche Supprimée", lines=1)
                delete_task_btn.click(delete_task, inputs=[
                                    tasklist_id_input, task_id_input], outputs=output_delete_task)
        with gr.Row():
            gr.Markdown("# Affichages des tâches à faire")

        with gr.Row():
            with gr.Column():
                tasklist_id_input = gr.Textbox(label="ID de la Liste de Tâches")
                show_incomplete_tasks_btn = gr.Button("Afficher Tâches en Cours")
            with gr.Column():
                task_list_incomplete = gr.Textbox(label="Tasks to do", elem_id="task-list-todo", lines=10)
                show_incomplete_tasks_btn.click(show_incomplete_tasks, inputs=[
                                        tasklist_id_input], outputs=task_list_incomplete)

        with gr.Row():
            gr.Markdown("# Affichages des listes de tâches")

        with gr.Row():
            with gr.Column():
                show_tasklists_btn = gr.Button("Afficher les Listes de Tâches")
            with gr.Column():
                task_list = gr.Textbox(label="Tasklists", elem_id="task-list", lines=10)
                show_tasklists_btn.click(TaskController.get_all_tasklists, outputs=task_list)
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
