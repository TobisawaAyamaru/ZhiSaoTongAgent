import hashlib, os
from utils.logger_handle import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFDirectoryLoader,
    TextLoader,
)


def get_file_md5_hex(filepath: str):
    # 获取文件md5
    if not os.path.exists(filepath):
        logger.error(f"[md5计算]文件{filepath}不存在")
        return

    if not os.path.isfile(filepath):
        logger.error(f"[md5计算]文件{filepath}不是文件")
        return
    md5_obj = hashlib.md5()

    chunk_size = 4096
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(chunk_size):
                md5_obj.update(chunk)
            md5_hex = md5_obj.hexdigest()
            return md5_hex
    except Exception as e:
        logger.error(f"计算文件{filepath}md5失败")


def listdir_with_allowed_type(path: str, allowed_typed: tuple[str]):
    # 获取文件夹内所有文件
    files = []
    if not os.path.isdir(path):
        logger.error(f"[listdir_with_allowed_type]{path}不是文件夹")
    for f in os.listdir(path):
        files.append(os.path.join(path, f))
    return tuple(files)


def pdf_loader(filepath: str, passwd: None):
    return PyPDFDirectoryLoader(filepath, passwd).load()


def txt_loader(filepath: str):
    return TextLoader(filepath).load()
