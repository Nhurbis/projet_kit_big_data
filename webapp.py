import gradio as gr
from todolist.models.Task import Task
from todolist.models.TaskList import TaskList

# Initialisation de la liste de tâches
task_list = TaskList('liste_test_1')

def manage_tasks(action, task_name="", new_name="", description=None, new_description=""):
    if action == "Afficher toutes les tâches":
        tasks = task_list.collection.find()
        return "\n".join([str(Task.from_dict(task_data)) for task_data in tasks])

    elif action == "Afficher les tâches complétées":
        tasks = task_list.collection.find({"completed": True})
        return "\n".join([str(Task.from_dict(task_data)) for task_data in tasks])

    elif action == "Afficher les tâches en cours":
        tasks = task_list.collection.find({"completed": False})
        return "\n".join([str(Task.from_dict(task_data)) for task_data in tasks])

    elif action == "Ajouter une tâche":
        task_list.add_task(task_name, description)
        return "Tâche ajoutée avec succès!"
    
    elif action == "Modifier la tâche":
        if new_name or new_description:  # Au moins un des deux devrait être non vide
            task_list.update_task(task_name, new_name=new_name, new_description=new_description)
            return f"La tâche '{task_name}' a été modifiée."

    elif action == "Compléter la tâche":
        task_list.complete_task(task_name)
        return f"La tâche '{task_name}' est complétée."

    elif action == "Supprimer la tâche":
        task_list.remove_task(task_name)
        return f"La tâche '{task_name}' a été supprimée."

iface = gr.Interface(
    manage_tasks, 
    [
        gr.Radio([
            "Afficher toutes les tâches", 
            "Afficher les tâches complétées", 
            "Afficher les tâches en cours", 
            "Ajouter une tâche", 
            "Compléter la tâche", 
            "Supprimer la tâche",
            "Modifier la tâche"
        ], label="Action"),
        gr.Textbox(placeholder="Nom de la tâche actuelle", label="Nom actuel"),
        gr.Textbox(placeholder="Nouveau nom de la tâche (pour modification seulement)", label="Nouveau nom"),
        gr.Textbox(placeholder="Description (pour ajout seulement)", label="Description"),
        gr.Textbox(placeholder="Nouvelle description (pour modification seulement)", label="Nouvelle description")
    ], 
    "text",
    clear_on_submit=True
)

iface.launch()
