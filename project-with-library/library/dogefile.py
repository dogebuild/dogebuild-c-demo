from pathlib import Path

from dogebuild_c.c_plugin import CPlugin, BinaryType


CPlugin(
    binary_type=BinaryType.STATIC_LIBRARY,
    out_name="greeter",
    src=Path("src").glob('**/*.c'),
    headers=Path("src").glob('**/*.h'),
)
