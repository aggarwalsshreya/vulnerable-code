import os
import sys

index = sys.argv[1] if len(sys.argv) > 1 else "default"
os.system("echo rebuilding " + index)  # CWE-78
