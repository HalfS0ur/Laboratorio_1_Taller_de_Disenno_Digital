import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def prueba_switches_leds_todos_botones(dut):
    """Prueba del módulo switches y leds con todas las combinaciones de botones"""
    mask_map = {
        0: 0xFFFF,
        1: 0xFFF0,
        2: 0xFF0F,
        3: 0xFF00,
        4: 0xF0FF,
        5: 0xF0F0,
        6: 0xF00F,
        7: 0xF000,
        8: 0x0FFF,
        9: 0x0FF0,
        10: 0x0F0F,
        11: 0x0F00,
        12: 0x00FF,
        13: 0x00F0,
        14: 0x000F,
        15: 0x0000
    }

    for valor_switches in range(2**16):
        dut.switch_pi.value = valor_switches

        for valor_botones in range(16):
            dut.boton_pi.value = valor_botones
            await Timer(1, 'ns')
            expected_value = valor_switches & mask_map[valor_botones]
            assert dut.led_po.value == expected_value, f"LED output was incorrect for switches: {valor_switches}, buttons: {valor_botones}. Expected: {expected_value}, Got: {dut.led_po.value}"