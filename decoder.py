'''
FirmwareDecoder Academic License

This software is licensed for academic use only.

Commercial use (including in proprietary, closed-source, or monetized systems) is strictly prohibited without a separate license agreement.

If you wish to use this software for commercial purposes, please contact the author at: jank.jong@gmail.com

© 2025 [Jank Jong]. All rights reserved.
'''

import re
import shutil
import os
import json
import requests
import subprocess
import py7zr
from elftools.elf.elffile import ELFFile

avr_objdump_path = r"C:\Users\88691\AppData\Local\Arduino15\packages\arduino\tools\avr-gcc\7.3.0-atmel3.6.1-arduino7\bin\avr-objdump.exe"
arm_objdump_path = r"C:\Program Files (x86)\Arm GNU Toolchain arm-none-eabi\13.3 rel1\bin\arm-none-eabi-objdump.exe"

INPUT_FIRMWARES_DIR = "./input/firmwares"
OUTPUT_ASSEMBLY_DIR = "./output/assemblies"

class ElfFileProcessor:
    def __init__(self, avr_objdump_path: str, arm_objdump_path: str):
        self.avr_objdump_path = avr_objdump_path
        self.arm_objdump_path = arm_objdump_path

    def identify_elf_architecture(self, elf_file: str) -> str:
        try:
            with open(elf_file, "rb") as f:
                elf = ELFFile(f)
                machine = elf['e_machine']
                if machine == 'EM_ARM':
                    return "ARM Cortex-M (e.g., STM32)"
                elif machine == 'EM_AVR':
                    return "AVR (Atmel/Microchip)"
                else:
                    return f"Unknown architecture (e_machine={machine})"
        except Exception as e:
            print(f"Failed to identify architecture for {elf_file}: {str(e)}")
            return "Unknown architecture"

    def disassemble_elf_file(self, elf_file: str, disasm_file: str, architecture: str):
        objdump_path = self.arm_objdump_path if "ARM" in architecture else self.avr_objdump_path
        command = [objdump_path, "-D",  elf_file]
        try:
            with open(disasm_file, "w", encoding="utf-8") as outfile:
                subprocess.run(command, stdout=outfile, stderr=subprocess.PIPE, check=True)
            print(f"Disassembled {elf_file} -> {disasm_file}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to disassemble {elf_file}: {e.stderr.decode('utf-8')}")

    def process_elf_file(self, elf_file: str, output_file: str):
        disasm_file = output_file

        if os.path.isfile(disasm_file):
            print(f"Disassembly file already exists: {disasm_file}")
            return disasm_file

        architecture = self.identify_elf_architecture(elf_file)
        print(f"Inferred architecture for {elf_file}: {architecture}")

        self.disassemble_elf_file(elf_file, disasm_file, architecture)
        return disasm_file

def main():
    processor = ElfFileProcessor(avr_objdump_path, arm_objdump_path)

    input_firmware_file = os.path.join(INPUT_FIRMWARES_DIR, "example.elf")
    output_assembly_file = os.path.join(OUTPUT_ASSEMBLY_DIR, "example.asm")
    output_archive_file = os.path.join(OUTPUT_ASSEMBLY_DIR, "example.7z")

    # Step 1: Disassemble ELF to ASM
    disasm_file = processor.process_elf_file(input_firmware_file, output_assembly_file)

    # Step 2: Compress ASM file to 7z
    with py7zr.SevenZipFile(output_archive_file, 'w') as archive:
        archive.write(output_assembly_file, arcname="example.asm")

    # Step 3: Delete the original .asm file
    os.remove(output_assembly_file)

    print(f"Assembly file compressed and cleaned up: {output_archive_file}")

if __name__ == "__main__":
    main()
