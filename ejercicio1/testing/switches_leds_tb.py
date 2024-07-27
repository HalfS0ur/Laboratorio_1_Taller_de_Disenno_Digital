import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def prueba_switches_leds_todos_botones(dut):
    """Prueba del módulo switches y leds con todas las combinaciones de botones"""
    for valor_switches in range (2**16):
        dut.switch_pi.value = valor_switches

        for valor_botones in range (16):
            dut.boton_pi.value = valor_botones
            
            if valor_botones == 0:
                await Timer(1, 'ns')
                assert dut.led_po.value == valor_switches, f"LED output salida_o was incorrect." 

            elif valor_botones == 1:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0xFFF0), f"LED output salida_o was incorrect." 

            elif valor_botones == 2:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0xFF0F), f"LED output salida_o was incorrect." 

            if valor_botones == 3:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0xFF00), f"LED output salida_o was incorrect." 

            elif valor_botones == 4:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0xF0FF), f"LED output salida_o was incorrect." 

            elif valor_botones == 5:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0xF0F0), f"LED output salida_o was incorrect." 

            elif valor_botones == 6:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0xF00F), f"LED output salida_o was incorrect." 

            if valor_botones == 7:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0xF000), f"LED output salida_o was incorrect." 

            elif valor_botones == 8:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0x0FFF), f"LED output salida_o was incorrect."

            elif valor_botones == 9:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0x0FF0), f"LED output salida_o was incorrect."

            elif valor_botones == 10:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0x0F0F), f"LED output salida_o was incorrect."

            elif valor_botones == 11:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0x0F00), f"LED output salida_o was incorrect." 

            elif valor_botones == 12:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0x00FF), f"LED output salida_o was incorrect."

            elif valor_botones == 13:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0x00F0), f"LED output salida_o was incorrect." 

            elif valor_botones == 14:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0x000F), f"LED output salida_o was incorrect."

            elif valor_botones == 15:
                await Timer(1, 'ns')
                assert dut.led_po.value == (valor_switches & 0x0000), f"LED output salida_o was incorrect."