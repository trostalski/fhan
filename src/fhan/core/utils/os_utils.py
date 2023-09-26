import subprocess
import os


def black_dir(path: str):
    """Run black on the given directory."""
    subprocess.run(["black", path])
