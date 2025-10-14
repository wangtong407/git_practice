from pathlib import Path


def delete_png(path):
    """无返回值版本，直接删除"""
    path = Path(path)
    if path.is_file() and path.suffix.lower() == '.png':
        path.unlink()
    elif path.is_dir():
        [f.unlink() for f in path.rglob('*.png')]


# delete_png(r"C:\Users\31646\Desktop\1")
