import os

def write_file(working_directory, file_path, content):
    working_directory_abspath = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file.startswith(working_directory_abspath):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
    except Exception as e:
        return f'Error: unable to create directory {e}'
        
    try:
        with open(target_file, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: unable to write file {e}'
        