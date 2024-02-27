import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_switches_leds (dut):
    """Prueba del módulo switches y leds"""
    for run in range (16):
        switch_pi = random.randint(0, (1 << 16) - 1)
        boton_pi = random.randint(0, (1 << 4) - 1)
        dut.switch_pi.value = switch_pi
        dut.boton_pi.value = boton_pi

        await Timer(5, 'ns')
        
        if boton_pi == 0:
            assert dut.led_po.value == switch_pi, f"Mux output salida_o was incorrect." 

        assert dut.led_po.value != switch_pi, f"Mux output salida_o was incorrect."