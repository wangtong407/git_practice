from pathlib import Path


def delete_files(path):
    """无返回值版本，直接删除指定扩展名的文件"""
    path = Path(path)
    if path.is_file():
        # 检查文件扩展名是否在要删除的列表中（不区分大小写）
        if path.suffix.lower() in {'.png', '.txt', '.json'}:
            path.unlink()
    elif path.is_dir():
        # 递归查找并删除所有指定扩展名的文件
        for ext in {'.png', '.txt', '.json'}:
            [f.unlink() for f in path.rglob(f'*{ext}')]


# delete_png(r"C:\Users\31646\Desktop\1")
