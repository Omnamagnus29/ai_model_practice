import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if not os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        # else:
        #     return f'Success: "{directory}" is within the working directory'
        files_info = []
        for filename in os.listdir(target_dir):
            full_path = os.path.join(target_dir, filename)
            size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            files_info.append(f"{filename}: file_size={size}, is_dir={is_dir}")
        
            if is_dir:
                for subfile in os.listdir(full_path):
                    sub_path = os.path.join(full_path, subfile)
                    sub_size = os.path.getsize(sub_path)
                    sub_is_dir = os.path.isdir(sub_path)
                    files_info.append(f"{subfile}: file_size={sub_size}, is_dir={sub_is_dir}")
        
        return "\n".join(files_info)

    except Exception as e:
        return f"Error: {e}"



print(get_files_info("calculator", "."))
print(get_files_info("calculator", "/bin"))
print(get_files_info("calculator", "../"))
print(get_files_info("calculator", "main.py"))
