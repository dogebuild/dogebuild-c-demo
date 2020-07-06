from pathlib import Path

from dogebuild import dependencies, directory, doge
from dogebuild_c.c_plugin import CPlugin, BinaryType

dependencies(
    doge(directory("../library"))
)

CPlugin(
    binary_type=BinaryType.EXECUTABLE,
    out_name="hello-worlder",
    src=Path("src").glob('**/*.c'),
    headers=Path("src").glob('**/*.h'),
)
