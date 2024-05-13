# X86 Opcode and Instruction Reference

Work-in-progress repository. For more see [ref.x86asm.net](http://ref.x86asm.net).

### Notes on Addressing Methods

#### The `J` method

Might be confusing. For example, `Jbs` actually reads as: "Relative offset to be added to the IP register. The relative offset is sign-extended to the size of of the IP register."

This method is always used as a source operand. To make it completely correct, it should be a destination operand but it would make the byte value also the destination and that doesn't make much sense. This would need to be solved by introducing new types of operands but I don't think it's worth it.

### Notes on Operand Type codes

#### SIMD FP instructions with integer codes

There are several MOV-like SIMD instructions that operate on floating-point data but their operands are indicated as integer ones. For example [`MOVHLPS Vq, Uq`](http://ref.x86asm.net/geek.html#x0F12) means "Move two packed single precision floating-point values from high quadword of source XMM register to low quadword of destination XMM register", however, all the Intel manuals from the pre-AVX era doesn't indicate its operands as packed single FP values (`ps` code) in the opcode map. This is presumably because the operands are treated as integers during the move operation.

The newer manuals from the AVX era indicate this instruction as `VMOVHLPS Vq, Hq, Uq` in the opcode map, making it unclear how the non-AVX version should look like. Anyway, even the AVX version uses integer codes.