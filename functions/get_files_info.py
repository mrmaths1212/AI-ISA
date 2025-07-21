import os
from config import MAX_CHARS

def get_files_info(working_directory, directory="."):
    """
    Get information about files in the specified directory.

    Args:
        working_directory (str): The path to the working directory.
        directory (str): The directory to list files from. Defaults to the current directory.

    Returns:
        list: A list of dictionaries containing file names and their sizes.
    """

        # Créer le chemin absolu depuis working_directory et directory
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    working_directory_abs = os.path.abspath(working_directory)

    # Vérification de sécurité : éviter les accès en dehors du dossier autorisé
    if not full_path.startswith(working_directory_abs):
        return f"Error: The directory '{directory}' is outside the working directory."

    # Vérifie si le dossier existe
    if not os.path.isdir(full_path):
        return f"Error: '{directory}' is not a directory"

    # Construit une chaîne décrivant les contenus
    output_lines = []

    for entry in os.scandir(full_path):
        file_size = entry.stat().st_size
        is_dir = entry.is_dir()
        output_lines.append(f"- {entry.name}: file_size={file_size} bytes, is_dir={is_dir}")

    return "\n".join(output_lines)


def get_file_content(working_directory, file_path):
    """
    Get information about files in the specified directory.

    Args:
        working_directory (str): The path to the working directory.
        directory (str): The directory to list files from. Defaults to the current directory.

    Returns:
        list: A list of dictionaries containing file names and their sizes.
    """
    try:
        # Créer le chemin absolu depuis working_directory et directory
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

    # Vérification de sécurité : éviter les accès en dehors du dossier autorisé
        if not full_path.startswith(working_directory_abs):
            return f"Error: The directory '{file_path}' is outside the working directory."

    # Vérifie si le dossier existe
        if not os.path.isfile(full_path):
            return f"Error: '{file_path}' is not a file"
    
        # Lire le contenu
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Si le contenu dépasse la limite, tronque et ajoute le message
        if len(content) > MAX_CHARS:
            truncated_msg = f"\n[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"
            return content[:MAX_CHARS] + truncated_msg
        return content
    except Exception as e:
        return f"Error: {str(e)}"
