def run_python_file(working_directory, file_path):
    import os
    import subprocess

    working_directory_abspath = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(working_directory_abspath):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    
    file_extension = target_file.split(".")
    if file_extension[-1] != 'py':
        return f'Error: File "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(['python', target_file], capture_output=True, text=True, cwd=working_directory, timeout=30)

        output = []
        if result.stdout:
            output.append(f"STDOUT:{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:{result.stderr}") 

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f'Error: unable to run file {e}'