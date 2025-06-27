import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    working_directory_abspath = os.path.abspath(working_directory)
    target_dir = working_directory_abspath
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(working_directory_abspath):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    else:
        items_in_directory = os.listdir(target_dir)
        string_list = []
        for item in items_in_directory:
            item_error = None
            item_path = os.path.join(target_dir, item)
            try:
                item_size = os.path.getsize(item_path)
            except Exception as e:
                item_error = f"{e}"
            try:
                is_dir = os.path.isdir(item_path)
            except Exception as e:
                item_error = f"{e}"
            if item_error is None:
                string_list.append(f"- {item}: file_size={item_size}, is_dir={is_dir}")
            else:
                string_list.append(f"Error: {item_error}")
        joined_list = "\n".join(string_list)
        return joined_list
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
