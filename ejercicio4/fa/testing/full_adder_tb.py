import cocotb
import random
from cocotb.triggers import Timer

@cocotb.test()
async def prueba_full_adder_sin_cin(dut):
    dut.cin.value = 0

    for valor_a in range(2):
        dut.a.value = valor_a
        for valor_b in range (2):
            dut.b.value = valor_b

            resultado = (valor_a + valor_b) & 0b1
            carry_out = ((valor_a + valor_b) >> 1) & 0b1

            await Timer(1, 'ns')

            assert dut.sum.value == resultado, f"Sum output was incorrect. Got {dut.sum.value}, expected {resultado}"
            assert dut.cout.value == carry_out, f"Carry out output was incorrect. Got {dut.cout.value}, expected {carry_out}"

@cocotb.test()
async def prueba_full_adder_con_cin(dut):
    dut.cin.value = 1

    for valor_a in range(2):
        dut.a.value = valor_a
        for valor_b in range (2):
            dut.b.value = valor_b

            resultado = (valor_a + valor_b + 1) & 0b1
            carry_out = ((valor_a + valor_b + 1) >> 1) & 0b1

            await Timer(1, 'ns')

            assert dut.sum.value == resultado, f"Sum output was incorrect. Got {dut.sum.value}, expected {resultado}"
            assert dut.cout.value == carry_out, f"Carry out output was incorrect. Got {dut.cout.value}, expected {carry_out}"