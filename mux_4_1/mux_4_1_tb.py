import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def prueba_mux(dut):
    """Prueba de todas las combinaciones del multiplexor 4 a 1 de 8 bits"""
    dut.entrada0_i.value = 0
    dut.entrada1_i.value = 0
    dut.entrada2_i.value = 0
    dut.entrada3_i.value = 0
    dut.seleccion_i.value = 0
    
    for prueba in range (2**8):
        for i in range (4):
            dut.__getattr__(f"entrada{i}_i").value = prueba
        for sel in range (4):
            dut.seleccion_i.value = sel
            await Timer(1, 'ns')
            assert dut.salida_o.value == prueba, f"Mux output salida_o was incorrect. Got {dut.salida_o.value} expected {prueba}"

@cocotb.test()
async def test_mux_proper(dut):
    """Prueba del multiplexor 4 a 1 con valores aleatorios en las entradas"""
    #Inicializar variables.
    dut.entrada0_i.value = 0
    dut.entrada1_i.value = 0
    dut.entrada2_i.value = 0
    dut.entrada3_i.value = 0
    dut.seleccion_i.value = 0

    valores_entrada = []

    for n in range (4096):
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

