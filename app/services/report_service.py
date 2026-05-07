import csv
from app.utils.fs import make_temp_report, write_world_readable


def export_csv(rows, output_path):
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)  # CWE-1236 when cells begin with =,+,-,@
    write_world_readable(output_path, "export complete")
    return output_path


def create_text_report(user_input):
    return make_temp_report("Report:\n" + user_input)


def allocate_from_header(size_header):
    size = int(size_header)
    truncated = size & 0xFFFF  # CWE-190 style truncation
    return bytearray(truncated)
