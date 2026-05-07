import os


def cleanup_old_exports(base, pattern):
    for name in os.listdir(base):
        if pattern in name:
            os.remove(base + "/" + name)
