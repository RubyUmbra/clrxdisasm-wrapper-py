from struct import unpack
from utils import Bits


class ComputePgmRsrc1:
    def __init__(self, compute_pgm_rsrc1: bytes):
        bits: Bits = Bits(unpack("<I", compute_pgm_rsrc1)[0], 32)
        self.FWD_PROGRESS: int = bits.pop_end(1)
        self.MEM_ORDERED: int = bits.pop_end(1)
        self.WGP_MODE: int = bits.pop_end(1)
        _: int = bits.pop_end(2)
        self.FP16_OVFL: int = bits.pop_end(1)
        self.CDBG_USER: int = bits.pop_end(1)
        self.BULKY: int = bits.pop_end(1)
        self.ENABLE_IEEE_MODE: int = bits.pop_end(1)
        self.DEBUG_MODE: int = bits.pop_end(1)
        self.ENABLE_DX10_CLAMP: int = bits.pop_end(1)
        self.PRIV: int = bits.pop_end(1)
        self.FLOAT_DENORM_MODE_16_64: int = bits.pop_end(2)
        self.FLOAT_DENORM_MODE_32: int = bits.pop_end(2)
        self.FLOAT_ROUND_MODE_16_64: int = bits.pop_end(2)
        self.FLOAT_ROUND_MODE_32: int = bits.pop_end(2)
        self.PRIORITY: int = bits.pop_end(2)
        self.GRANULATED_WAVEFRONT_SGPR_COUNT: int = bits.pop_end(4)
        self.GRANULATED_WORKITEM_VGPR_COUNT: int = bits.pop_end(6)
        assert bits.size == 0

    def __str__(self):
        bits: Bits = Bits()
        bits.push_end(self.GRANULATED_WORKITEM_VGPR_COUNT, 6)
        bits.push_end(self.GRANULATED_WAVEFRONT_SGPR_COUNT, 4)
        bits.push_end(self.PRIORITY, 2)
        bits.push_end(self.FLOAT_ROUND_MODE_32, 2)
        bits.push_end(self.FLOAT_ROUND_MODE_16_64, 2)
        bits.push_end(self.FLOAT_DENORM_MODE_32, 2)
        bits.push_end(self.FLOAT_DENORM_MODE_16_64, 2)
        bits.push_end(self.PRIV, 1)
        bits.push_end(self.ENABLE_DX10_CLAMP, 1)
        bits.push_end(self.DEBUG_MODE, 1)
        bits.push_end(self.ENABLE_IEEE_MODE, 1)
        bits.push_end(self.BULKY, 1)
        bits.push_end(self.CDBG_USER, 1)
        bits.push_end(self.FP16_OVFL, 1)
        bits.push_end(0, 2)
        bits.push_end(self.WGP_MODE, 1)
        bits.push_end(self.MEM_ORDERED, 1)
        bits.push_end(self.FWD_PROGRESS, 1)
        assert bits.size == 32
        return f"0x{bits.num:0>8x}"


class ComputePgmRsrc2:
    def __init__(self, compute_pgm_rsrc2: bytes):
        bits: Bits = Bits(unpack("<I", compute_pgm_rsrc2)[0], 32)
        _: int = bits.pop_end(1)
        self.ENABLE_EXCEPTION_INT_DIVIDE_BY_ZERO: int = bits.pop_end(1)
        self.ENABLE_EXCEPTION_IEEE_754_FP_INEXACT: int = bits.pop_end(1)
        self.ENABLE_EXCEPTION_IEEE_754_FP_UNDERFLOW: int = bits.pop_end(1)
        self.ENABLE_EXCEPTION_IEEE_754_FP_OVERFLOW: int = bits.pop_end(1)
        self.ENABLE_EXCEPTION_IEEE_754_FP_DIVISION_BY_ZERO: int = bits.pop_end(1)
        self.ENABLE_EXCEPTION_FP_DENORMAL_SOURCE: int = bits.pop_end(1)
        self.ENABLE_EXCEPTION_IEEE_754_FP_INVALID_OPERATION: int = bits.pop_end(1)
        self.GRANULATED_LDS_SIZE: int = bits.pop_end(9)
        self.ENABLE_EXCEPTION_MEMORY: int = bits.pop_end(1)
        self.ENABLE_EXCEPTION_ADDRESS_WATCH: int = bits.pop_end(1)
        self.ENABLE_VGPR_WORKITEM_ID: int = bits.pop_end(2)
        self.ENABLE_SGPR_WORKGROUP_INFO: int = bits.pop_end(1)
        self.ENABLE_SGPR_WORKGROUP_ID_Z: int = bits.pop_end(1)
        self.ENABLE_SGPR_WORKGROUP_ID_Y: int = bits.pop_end(1)
        self.ENABLE_SGPR_WORKGROUP_ID_X: int = bits.pop_end(1)
        self.ENABLE_TRAP_HANDLER: int = bits.pop_end(1)
        self.USER_SGPR_COUNT: int = bits.pop_end(5)
        self.ENABLE_PRIVATE_SEGMENT: int = bits.pop_end(1)
        assert bits.size == 0

    def __str__(self):
        bits: Bits = Bits()
        bits.push_end(self.ENABLE_PRIVATE_SEGMENT, 1)
        bits.push_end(self.USER_SGPR_COUNT, 5)
        bits.push_end(self.ENABLE_TRAP_HANDLER, 1)
        bits.push_end(self.ENABLE_SGPR_WORKGROUP_ID_X, 1)
        bits.push_end(self.ENABLE_SGPR_WORKGROUP_ID_Y, 1)
        bits.push_end(self.ENABLE_SGPR_WORKGROUP_ID_Z, 1)
        bits.push_end(self.ENABLE_SGPR_WORKGROUP_INFO, 1)
        bits.push_end(self.ENABLE_VGPR_WORKITEM_ID, 2)
        bits.push_end(self.ENABLE_EXCEPTION_ADDRESS_WATCH, 1)
        bits.push_end(self.ENABLE_EXCEPTION_MEMORY, 1)
        bits.push_end(self.GRANULATED_LDS_SIZE, 9)
        bits.push_end(self.ENABLE_EXCEPTION_IEEE_754_FP_INVALID_OPERATION, 1)
        bits.push_end(self.ENABLE_EXCEPTION_FP_DENORMAL_SOURCE, 1)
        bits.push_end(self.ENABLE_EXCEPTION_IEEE_754_FP_DIVISION_BY_ZERO, 1)
        bits.push_end(self.ENABLE_EXCEPTION_IEEE_754_FP_OVERFLOW, 1)
        bits.push_end(self.ENABLE_EXCEPTION_IEEE_754_FP_UNDERFLOW, 1)
        bits.push_end(self.ENABLE_EXCEPTION_IEEE_754_FP_INEXACT, 1)
        bits.push_end(self.ENABLE_EXCEPTION_INT_DIVIDE_BY_ZERO, 1)
        bits.push_end(0, 1)
        assert bits.size == 32
        return f"0x{bits.num:0>8x}"


class ComputePgmRsrc3:
    def __init__(self, compute_pgm_rsrc3: bytes):
        bits: Bits = Bits(unpack("<I", compute_pgm_rsrc3)[0], 32)
        self.IMAGE_OP: int = bits.pop_end(1)
        _: int = bits.pop_end(19)
        self.TRAP_ON_END: int = bits.pop_end(1)
        self.TRAP_ON_START: int = bits.pop_end(1)
        self.INST_PREF_SIZE: int = bits.pop_end(6)
        self.SHARED_VGPR_COUNT: int = bits.pop_end(4)
        assert bits.size == 0

    def __str__(self):
        bits: Bits = Bits()
        bits.push_end(self.SHARED_VGPR_COUNT, 4)
        bits.push_end(self.INST_PREF_SIZE, 6)
        bits.push_end(self.TRAP_ON_START, 1)
        bits.push_end(self.TRAP_ON_END, 1)
        bits.push_end(0, 19)
        bits.push_end(self.IMAGE_OP, 1)
        assert bits.size == 32
        return f"0x{bits.num:0>8x}"
