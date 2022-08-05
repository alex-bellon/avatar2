from capstone import *

from .architecture import Architecture

from avatar2.installer.config import QEMU, GDB_MULTI

class M68K(Architecture):
    
    get_qemu_executable = Architecture.resolve(QEMU)
    get_gdb_executable = Architecture.resolve(GDB_MULTI)

    qemu_name = 'm68k'
    gdb_name = 'm68k'

    registers = {'d0': 0,
                 'd1': 1,
                 'd2': 2,
                 'd3': 3,
                 'd4': 4,
                 'd5': 5,
                 'd6': 6,
                 'd7': 7,
                 'a0': 8,
                 'a1': 9,
                 'a2': 10,
                 'a3': 11,
                 'a4': 12,
                 'a5': 13,
                 'a6': 14,
                 'a7': 15,
                 'sp': 15,
                 'pc': 16,
                 'sr': 17,
                 }

    pc_name = 'pc'
    sr_name = 'sr'

    capstone_arch = CS_ARCH_M68K

# Keystone (KS) does not support M68k currently

class M68040(M68K):

    qemu_name = 'm68040'
    gdb_name = 'm68040'

    capstone_mode = CS_MODE_M68K_040
