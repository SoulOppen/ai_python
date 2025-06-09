import os
def get_files_info(working_directory, directory=None):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_target_directory = os.path.abspath(os.path.join(working_directory, directory))
        if not abs_target_directory.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_target_directory):
            return f'Error: "{directory}" is not a directory'
        result_lines = []
        for entry in os.listdir(abs_target_directory):
            full_path = os.path.join(abs_target_directory, entry)
            try:
                size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                result_lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")
            except Exception as e:
                result_lines.append(f"- {entry}: Error retrieving info: {str(e)}")

        return "\n".join(result_lines)                                     
    except Exeption as e:
        print(f"{e}")                                   