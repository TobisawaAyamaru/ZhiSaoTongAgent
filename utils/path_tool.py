import os


def get_project_root() -> str:
    """返回项目根目录"""
    current_File = os.path.abspath(__file__)

    current_dir = os.path.dirname(current_File)

    project_root = os.path.dirname(current_dir)
    return project_root


def get_abs_path(relative_path: str) -> str:
    """相对路径转绝对路径"""

    project_root = get_project_root()
    return os.path.join(project_root, relative_path).replace("\\", "/")
