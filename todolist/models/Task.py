from datetime import datetime

class TagError(Exception):
    pass

class Task:
    def __init__(self, name:str, description:str, tags=None):
        if not isinstance(name, str) or not isinstance(description, str):
            debug_logger.debug("Le nom et la description doivent être des chaînes de caractères.")
            raise TypeError("Le nom et la description doivent être des chaînes de caractères.")
            
        if not name or not description:
            debug_logger.debug("Le nom et la description ne peuvent pas être vides.")
            raise ValueError("Le nom et la description ne peuvent pas être vides.")
               

        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.completed = False
        self.last_modified = datetime.now()
        self.completion_date = None
        self.tags = tags if tags else []

    def mark_completed(self):
        if self.completed:
            debug_logger.debug("La tâche est déjà marquée comme complétée.")
            raise TaskAlreadyCompletedError("La tâche est déjà marquée comme complétée.")

        self.completed = True
        self.completion_date = datetime.now()

    def update_task(self, new_name=None, new_description=None):
        if new_name:
            if not isinstance(new_name, str):
                debug_logger.debug("Le nouveau nom doit être une chaîne de caractères.")
                raise TypeError("Le nouveau nom doit être une chaîne de caractères.")
                        
            general_logger.info("Modification du nom d'une tâche : " + self.name + " -> " + new_name)
            self.name = new_name
            self.last_modified = datetime.now()

        if new_description:
            if not isinstance(new_description, str):
                debug_logger.debug("La nouvelle description doit être une chaîne de caractères.")
                raise TypeError("La nouvelle description doit être une chaîne de caractères.")
                        
            general_logger.info("Modification de la description d'une tâche : " + self.name + " -> " + new_description)
            self.description = new_description
            self.last_modified = datetime.now()
        if not new_name and not new_description:
            debug_logger.debug("Aucun paramètre de modification n'a été fourni.")
            raise ValueError("Aucun paramètre de modification n'a été fourni.")

    def add_tag(self, tag:str):
        if not isinstance(tag, str):
            debug_logger.debug("Le tag doit être une chaîne de caractères.")
            raise TypeError("Le tag doit être une chaîne de caractères.")
        
        if tag in self.tags:
            debug_logger.debug(f"Le tag '{tag}' existe déjà pour cette tâche.")
            raise TagError(f"Le tag '{tag}' existe déjà pour cette tâche.")
            
        
        if tag not in self.tags:
            general_logger.info("Ajout d'un tag à une tâche : " + self.name + " -> " + tag)
            self.tags.append(tag)
            self.last_modified = datetime.now()

    def remove_tag(self, tag:str):
        if tag not in self.tags:
            debug_logger.debug(f"Le tag '{tag}' n'existe pas pour cette tâche.")
            raise TagError(f"Le tag '{tag}' n'existe pas pour cette tâche.")
         
        if tag in self.tags:
            general_logger.info("Suppression d'un tag à une tâche : " + self.name + " -> " + tag)
            self.tags.remove(tag)
            self.last_modified = datetime.now()

    def __str__(self):
        return f"{self.name} - {self.description} (Completed: {self.completed})"

