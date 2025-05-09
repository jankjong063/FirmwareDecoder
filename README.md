# FirmwareDecoder

A Python utility to disassemble ELF firmware files into readable assembly, supporting both ARM Cortex-M (e.g., STM32) and AVR (Atmel/Microchip) architectures. This tool uses `objdump` from official toolchains and `pyelftools` to process ELF files.

---

## 🛠 Features

- Automatically detects ELF architecture (ARM or AVR).
- Selects appropriate `objdump` tool for disassembly.
- Outputs human-readable `.asm` assembly files.
- Designed for firmware analysis, reverse engineering, and academic research.

---

## 📦 Requirements

### ✅ Python Packages

Install via pip:

```bash
pip install pyelftools
```

## Required Toolchains
### 3rd Party tools

#### AVR Toolchain
##### Arduino AVR-GCC: https://www.arduino.cc/en/software
```command shell
REM Example path:
C:\Users\<username>\AppData\Local\Arduino15\packages\arduino\tools\avr-gcc\7.3.0-atmel3.6.1-arduino7\bin\avr-objdump.exe
```

#### ARM Toolchain
##### Arm GNU Toolchain
```command shell
REM Example path:
C:\Program Files (x86)\Arm GNU Toolchain arm-none-eabi\13.3 rel1\bin\arm-none-eabi-objdump.exe
```

## Directory Structure
```command shell
 FirmwareDecoder/
├── input/
│   └── firmwares/          # Place ELF firmware files here
├── output/
│   └── assemblies/         # Disassembled output files saved here
├── FirmwareDecoder_main.py # Main script
├── README.md
```

### 🔧 Configuration (Tested with windows environment only!!!)
In FirmwareDecoder_main.py, update these paths to match your local environment:

```python
avr_objdump_path = r"C:\Users\<username>\AppData\Local\Arduino15\packages\arduino\tools\avr-gcc\7.3.0-atmel3.6.1-arduino7\bin\avr-objdump.exe"
arm_objdump_path = r"C:\Program Files (x86)\Arm GNU Toolchain arm-none-eabi\13.3 rel1\bin\arm-none-eabi-objdump.exe"
```

### Set firmware input and assembly output folders:
```python
INPUT_FIRMWARES_DIR = "./input/firmwares/"
OUTPUT_ASSEMBLY_DIR = "./output/assemblies/"
```

## How to Use
### Make sure your ELF firmware (e.g., example.elf) is placed under ./input/firmwares/.
### Run the decoder:
```bash
python FirmwareDecoder_main.py
```
### The resulting .asm file will appear under ./output/assemblies/.

## 📜 License
### Apache 2.0, patent protected, See LICENSE for details.

## 🤝 Contributions
Open to pull requests, suggestions, and improvements from the community or academia.


