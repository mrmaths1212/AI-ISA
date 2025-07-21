import os
def write_file(working_directory, file_path, content):
           # Créer le chemin absolu depuis working_directory et directory
    try:
        # Sécurise le chemin d'accès
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

        # Empêche l'écriture en dehors du répertoire de travail
        if not full_path.startswith(working_directory_abs):
            return print(f"Error: The file '{file_path}' is outside the working directory.")

        # Crée les dossiers parents si nécessaire
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Écrit ou écrase le fichier
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')


    except Exception as e:
        return print(f"Error: {str(e)}")