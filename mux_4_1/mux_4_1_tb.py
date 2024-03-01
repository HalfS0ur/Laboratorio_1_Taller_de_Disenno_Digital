import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_dumb(dut):
    """Test del multiplexor 4 a 1 hecho incorrectamente"""
    entrada_0 = random.randint(00, 255)
    entrada_1 = random.randint(0, 255)
    entrada_2 = random.randint(0, 255)
    entrada_3 = random.randint(0, 255)

    dut.entrada0_i.value = entrada_0
    dut.entrada1_i.value = entrada_1
    dut.entrada2_i.value = entrada_2
    dut.entrada3_i.value = entrada_3

    dut.seleccion_i.value = 0b00
    await Timer(1, 'ns')
    assert dut.salida_o.value == entrada_0, f"Mux output salida_o was incorrect. Got {dut.salida_o.value} expected {entrada_0}"

    dut.seleccion_i.value = 0b01
    await Timer(1, 'ns')
    assert dut.salida_o.value == entrada_1, f"Mux output salida_o was incorrect. Got {dut.salida_o.value} expected {entrada_1}"

    dut.seleccion_i.value = 0b10
    await Timer(1, 'ns')
    assert dut.salida_o.value == entrada_2, f"Mux output salida_o was incorrect. Got {dut.salida_o.value} expected {entrada_2}"

    dut.seleccion_i.value = 0b11
    await Timer(1, 'ns')
    assert dut.salida_o.value == entrada_3, f"Mux output salida_o was incorrect. Got {dut.salida_o.value} expected {entrada_3}"

@cocotb.test()
async def test_mux_proper(dut):
    """Test del multiplexor 4 a 1 hecho más mejor (testbench autoverificable)"""
    #Inicializar variables
    dut.entrada0_i.value = 0b0
    dut.entrada1_i.value = 0b0
    dut.entrada2_i.value = 0b0
    dut.entrada3_i.value = 0b0
    dut.seleccion_i.value = 0b0

    valores_entrada = []

    for n in range (10):
        #Carga valores en las entradas del mux
        for i in range (4):
            valorentrada = random.randint(0,255)
            valores_entrada.append(valorentrada)
            dut.__getattr__(f"entrada{i}_i").value = valorentrada
        #Recorre las entradas y verifica que la salida corresponda a la entrada       
        for sel in range (4):
            dut.seleccion_i.value = sel
            await Timer(1, 'ns')
            assert dut.salida_o.value == valores_entrada[sel], f"Mux output salida_o was incorrect. Got {dut.salida_o.value} expected {valores_entrada[sel]}"
        #Reinicia la lista de valores usados en las entradas
        valores_entrada = []