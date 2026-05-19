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
            fullpath = os.path.join(target_dir, filename)
            size = os.path.getsize(fullpath)
            is_dir = os.path.isdir(fullpath)
            files_info.append(f"{filename}: size={size}, is_dir={is_dir}")
        return "\n".join(files_info)
        
    except Exception as e:
        return f"Error: {e}"



