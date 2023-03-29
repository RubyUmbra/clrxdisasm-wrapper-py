from typing import BinaryIO

from elftools.elf.elffile import ELFFile
from elftools.elf.sections import NoteSection, Section

__EF_AMDGPU_MACH_MASK: int = 0x0ff
__EF_AMDGPU_MACH: dict[int, str] = {
    # RDNA
    0x033: 'gfx10',  # gfx1010
    0x034: 'gfx10',  # gfx1011
    0x035: 'gfx10',  # gfx1012
    0x042: 'gfx10',  # gfx1013
    # RDNA2
    0x036: 'gfx10',  # gfx1030
    0x037: 'gfx10',  # gfx1031
    0x038: 'gfx10',  # gfx1032
    0x039: 'gfx10',  # gfx1033
    0x03e: 'gfx10',  # gfx1034
    0x03d: 'gfx10',  # gfx1035
    0x045: 'gfx10',  # gfx1036
    # RDNA3
    0x041: 'gfx11',  # gfx1100
    0x046: 'gfx11',  # gfx1101
    0x047: 'gfx11',  # gfx1102
    0x044: 'gfx11',  # gfx1103
}


def __extract_arch(elf: ELFFile) -> str:
    e_flags: int = elf.header['e_flags']
    mach: int = e_flags & __EF_AMDGPU_MACH_MASK
    arch: str | None = __EF_AMDGPU_MACH.get(mach)
    assert arch is not None, f'unknown target arch: {mach}'
    return arch


def __extract_metadata(elf: ELFFile) -> bytes:
    note_section: NoteSection = elf.get_section_by_name('.note')
    assert isinstance(note_section, NoteSection), \
        'bad binary format: missed ".note" section'
    notes: list[bytes] = [note.n_desc
                          for note in note_section.iter_notes()
                          if note.n_name == 'AMDGPU']
    assert len(notes) == 1
    return notes[0]


def __extract_section(elf: ELFFile, name: str) -> bytes:
    section: Section = elf.get_section_by_name(name)
    assert isinstance(section, Section), \
        f'bad binary format: missed {name} section'
    return section.data()


def __extract_rodata(elf: ELFFile) -> bytes:
    return __extract_section(elf, '.rodata')


def __extract_text(elf: ELFFile) -> bytes:
    return __extract_section(elf, '.text')


def extract_elf(stream: BinaryIO) -> (str, bytes, bytes, bytes):
    elf: ELFFile = ELFFile(stream)
    assert isinstance(elf, ELFFile), 'bad binary format: not an ELF'
    arch: str = __extract_arch(elf)
    metadata: bytes = __extract_metadata(elf)
    rodata: bytes = __extract_rodata(elf)
    text: bytes = __extract_text(elf)
    return arch, metadata, rodata, text
