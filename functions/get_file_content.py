import os

def get_file_content(working_directory, file_path):
    working_directory_abspath = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file.startswith(working_directory_abspath):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000

    try:
        with open(target_file, 'r') as file:
            content = file.read(MAX_CHARS + 1)
        if len(content) > MAX_CHARS:
            return content[0:10_000] + f'[...File "{file_path}" truncated at 10000 characters]'
        return content
    except Exception as e:
        return f'Error: unable to read file {e}'