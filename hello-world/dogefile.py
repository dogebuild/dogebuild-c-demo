from pathlib import Path

from dogebuild_c.c_plugin import CPlugin, BinaryType


CPlugin(
    binary_type=BinaryType.EXECUTABLE,
    out_name="hello-world",
    src=Path("src").glob('**/*.c'),
    headers=Path("src").glob('**/*.h'),
)
