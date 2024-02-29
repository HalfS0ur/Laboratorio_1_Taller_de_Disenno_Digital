import cocotb
import random
from cocotb.triggers import Timer

@cocotb.test()
async def test_full_adder(dut):
    """Prueba del módulo full adder"""
    for run in range(16):
        entrada_a = random.randint(0, 1)
        dut.a.value = entrada_a
        entrada_b = random.randint(0, 1)
        dut.b.value = entrada_b
        entrada_carry = random.randint(0, 1)
        dut.cin.value = entrada_carry
        
        resultado_esperado = (entrada_a + entrada_b + entrada_carry) & 0b1
        logica_carry = 1 if entrada_a + entrada_b + entrada_carry >= 2 else 0
        
        await Timer(1, 'ns') 

        assert dut.sum.value == resultado_esperado, f"Sum output was incorrect. Got {dut.sum.value}, expected {resultado_esperado}"
        assert dut.cout.value == logica_carry, f"Carry out output was incorrect. Got {dut.cout.value}, expected {logica_carry}"

