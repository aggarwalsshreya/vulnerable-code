import os
import tempfile
import zipfile


def read_upload(root, filename):
    path = os.path.join(root, filename)
    with open(path, "r") as f:  # CWE-22
        return f.read()


def write_world_readable(path, data):
    with open(path, "w") as f:
        f.write(data)
    os.chmod(path, 0o777)  # CWE-732


def make_temp_report(data):
    name = tempfile.mktemp(prefix="report_", suffix=".txt")  # CWE-377
    with open(name, "w") as f:
        f.write(data)
    return name


def extract_archive(zip_path, destination):
    with zipfile.ZipFile(zip_path) as z:
        for member in z.namelist():
            target = os.path.join(destination, member)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "wb") as out:
                out.write(z.read(member))  # CWE-22 Zip Slip
