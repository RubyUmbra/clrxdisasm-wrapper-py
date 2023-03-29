from struct import unpack
from construct import Construct, BitStruct, ByteSwapped, BitsInteger, Padding


class ComputePgmRsrc:
    FORMAT: Construct

    def __init__(self, data: bytes):
        self.__struct = self.FORMAT.parse(data)

    def __getitem__(self, item):
        return self.__struct.__getitem__(item)

    def __str__(self):
        return f'0x{unpack("<I", self.FORMAT.build(self.__struct))[0]:0>8x}'


class ComputePgmRsrc1(ComputePgmRsrc):
    FORMAT = ByteSwapped(BitStruct(
        "GRANULATED_WORKITEM_VGPR_COUNT" / BitsInteger(6),
        "GRANULATED_WAVEFRONT_SGPR_COUNT" / BitsInteger(4),
        "PRIORITY" / BitsInteger(2),
        "FLOAT_ROUND_MODE_32" / BitsInteger(2),
        "FLOAT_ROUND_MODE_16_64" / BitsInteger(2),
        "FLOAT_DENORM_MODE_32" / BitsInteger(2),
        "FLOAT_DENORM_MODE_16_64" / BitsInteger(2),
        "PRIV" / BitsInteger(1),
        "ENABLE_DX10_CLAMP" / BitsInteger(1),
        "DEBUG_MODE" / BitsInteger(1),
        "ENABLE_IEEE_MODE" / BitsInteger(1),
        "BULKY" / BitsInteger(1),
        "CDBG_USER" / BitsInteger(1),
        "FP16_OVFL" / BitsInteger(1),
        Padding(2),
        "WGP_MODE" / BitsInteger(1),
        "MEM_ORDERED" / BitsInteger(1),
        "FWD_PROGRESS" / BitsInteger(1),
    ))


class ComputePgmRsrc2(ComputePgmRsrc):
    FORMAT = ByteSwapped(BitStruct(
        "ENABLE_PRIVATE_SEGMENT" / BitsInteger(1),
        "USER_SGPR_COUNT" / BitsInteger(5),
        "ENABLE_TRAP_HANDLER" / BitsInteger(1),
        "ENABLE_SGPR_WORKGROUP_ID_X" / BitsInteger(1),
        "ENABLE_SGPR_WORKGROUP_ID_Y" / BitsInteger(1),
        "ENABLE_SGPR_WORKGROUP_ID_Z" / BitsInteger(1),
        "ENABLE_SGPR_WORKGROUP_INFO" / BitsInteger(1),
        "ENABLE_VGPR_WORKITEM_ID" / BitsInteger(2),
        "ENABLE_EXCEPTION_ADDRESS_WATCH" / BitsInteger(1),
        "ENABLE_EXCEPTION_MEMORY" / BitsInteger(1),
        "GRANULATED_LDS_SIZE" / BitsInteger(9),
        "ENABLE_EXCEPTION_IEEE_754_FP_INVALID_OPERATION" / BitsInteger(1),
        "ENABLE_EXCEPTION_FP_DENORMAL_SOURCE" / BitsInteger(1),
        "ENABLE_EXCEPTION_IEEE_754_FP_DIVISION_BY_ZERO" / BitsInteger(1),
        "ENABLE_EXCEPTION_IEEE_754_FP_OVERFLOW" / BitsInteger(1),
        "ENABLE_EXCEPTION_IEEE_754_FP_UNDERFLOW" / BitsInteger(1),
        "ENABLE_EXCEPTION_IEEE_754_FP_INEXACT" / BitsInteger(1),
        "ENABLE_EXCEPTION_INT_DIVIDE_BY_ZERO" / BitsInteger(1),
        Padding(1),
    ))


class ComputePgmRsrc3(ComputePgmRsrc):
    FORMAT = ByteSwapped(BitStruct(
        "SHARED_VGPR_COUNT" / BitsInteger(4),
        "INST_PREF_SIZE" / BitsInteger(6),
        "TRAP_ON_START" / BitsInteger(1),
        "TRAP_ON_END" / BitsInteger(1),
        Padding(19),
        "IMAGE_OP" / BitsInteger(1),
    ))
