from subprocess import run, PIPE
from utils import temp_file


def __dump_text(filename: str, text: bytes):
    with open(filename, 'wb') as file:
        file.write(text)


def __run_clrxdisasm(clrxdisasm: str, arch: str, wavefront_size: int, filename: str) -> list[str]:
    args: list[str] = ["-dCfsr", f"--arch={arch}"]
    if wavefront_size == 32:
        args.append("--wave32")
    output: str = run([clrxdisasm, *args, filename], stdout=PIPE, check=True).stdout.decode()
    return output.splitlines()


def run_clrxdisasm(clrxdisasm: str, arch: str, wavefront_size: int, filename: str, text: bytes) -> list[str]:
    with temp_file(f"{filename}.text") as filename:
        __dump_text(filename, text)
        return __run_clrxdisasm(clrxdisasm, arch, wavefront_size, filename)