import os
def get_file_content(working_directory, file_path):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_target_file = os.path.abspath(os.path.join(working_directory, file_path))
        if not abs_target_file.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        MAX_CHARS = 10000
        with open(abs_target_file, "r") as f:
            content = f.read()

        if len(content) > MAX_CHARS:
            truncated_msg = f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            content = content[:MAX_CHARS] + truncated_msg
        return content
    except Exception as e:
        print(f"Error:{e}")