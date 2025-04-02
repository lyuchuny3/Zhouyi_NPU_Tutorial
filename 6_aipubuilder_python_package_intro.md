# Tutorial 6: AIPUBuilder Python Package Overview

## AIPUBuilder Python package
The python whl package of AIPUBuilder include:
- NN-Compiler Toolchain
- NN library

## AIPUBuilder Tools
The AIPUBuilder provides the following tools:
- LLVM toolchain: aipuoas, aipuocc, aipuold
- NN toolchain: aipuparser, aipugsim, aipuopt, aipugb, ...

The llvm toolchain is assembler, compiler, linker, with `o` mean OpenCL, to distinguish from C language.
The introduction of NN toolchain, see the [Tutorial 2: AIPUBuilder Overview](2_aipubuilder_overview.md)

## AIPUBuilder Python API
The AIPUBuilder provides the following python API:

- Tool level API
- Device API
- Execution API
- Ops API
- Bind API

For detail info about each API, see the [Tutorial 7: AIPUBuilder Python API](7_aipubuilder_python_api.md)