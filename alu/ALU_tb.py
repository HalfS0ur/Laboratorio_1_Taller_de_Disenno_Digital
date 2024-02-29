import cocotb
import random
from cocotb.triggers import Timer

@cocotb.test()
async def test_AND(dut):
    '''Prueba de la operación AND'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for run in range (10):
        dut.ALUcontrol_i.value = 0
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == valor_a & valor_b, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

@cocotb.test()
async def test_OR(dut):
    '''Prueba de la operación OR'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for run in range (10):
        dut.ALUcontrol_i.value = 1
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == valor_a | valor_b, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

@cocotb.test()
async def test_suma(dut):
    '''Prueba de la operación suma'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for run in range (10):
        dut.ALUcontrol_i.value = 2
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        valor_flag = random.randint(0, 1)
        dut.ALUflagin_i.value = valor_flag
        resultado_suma = (valor_b + valor_a + valor_flag) & 0xF
        resultado_carry = ((valor_b + valor_a + valor_flag) >> 4) & 1
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_suma, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"
        assert dut.ALUflags_o.value == resultado_carry, f"Mux output salida_o was incorrect. Got {dut.ALUflags_o.value} expected {(resultado_carry)}"

@cocotb.test()
async def test_incrementar_1(dut):
    '''Prueba de la operación incrementar en 1'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for test_a in range (10):
        dut.ALUcontrol_i.value = 3
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        dut.ALUflagin_i.value = 0
        resultado_a1 = (valor_a + 1) & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_a1, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

    for test_b in range (10):
        dut.ALUcontrol_i.value = 3
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        dut.ALUflagin_i.value = 1
        resultado_b1 = (valor_b + 1) & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_b1, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

@cocotb.test()
async def test_decrementar_1(dut):
    '''Prueba de la operación decrementar en 1'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for test_a in range (10):
        dut.ALUcontrol_i.value = 4
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        dut.ALUflagin_i.value = 0
        resultado_am1 = (valor_a - 1) & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_am1, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

    for test_b in range (10):
        dut.ALUcontrol_i.value = 4
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        dut.ALUflagin_i.value = 1
        resultado_bm1 = (valor_b - 1) & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_bm1, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

@cocotb.test()
async def test_NOT(dut):
    '''Prueba de la operación NOT'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for test_a in range (10):
        dut.ALUcontrol_i.value = 5
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        dut.ALUflagin_i.value = 0
        resultado_not_a = ~valor_a & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_not_a, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

    for test_b in range (10):
        dut.ALUcontrol_i.value = 5
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        dut.ALUflagin_i.value = 1
        resultado_not_b = ~valor_b & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_not_b, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

@cocotb.test()
async def test_resta(dut):
    '''Prueba de la operación resta'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for run in range (10):
        dut.ALUcontrol_i.value = 6
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        valor_flag = random.randint(0, 1)
        dut.ALUflagin_i.value = valor_flag
        resultado_resta = (valor_a - valor_b - valor_flag) & 0xF
        resultado_carry_resta = ((valor_a - valor_b - valor_flag) >> 4) & 1
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_resta, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"
        assert dut.ALUflags_o.value == resultado_carry_resta, f"Mux output salida_o was incorrect. Got {dut.ALUflags_o.value} expected {(resultado_carry_resta)}"

@cocotb.test()
async def test_XOR(dut):
    '''Prueba de la operación XOR'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for run in range (10):
        dut.ALUcontrol_i.value = 7
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == valor_a ^ valor_b, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

@cocotb.test()
async def test_corrimiento_izquierda(dut):
    '''Prueba de la operación corrimiento a la izquierda'''
    for run in range (10):
        dut.ALUcontrol_i.value = 8
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        valor_flag_in = random.randint(0, 1)
        dut.ALUflagin_i.value = valor_flag_in

        if (valor_b <= 4):
            valor_flag_out = ((valor_a) >> (4 - valor_b)) & 0b1
            await Timer(2, 'ns')
            assert dut.ALUflags_o.value == valor_flag_out, f"Mux output salida_o was incorrect. Got {dut.ALUflags_o.value}"
        
        elif (valor_b >> 4):
            valor_flag_out = valor_flag_in
            await Timer(2, 'ns')
            assert dut.ALUflags_o.value == valor_flag_out, f"Mux output salida_o was incorrect. Got {dut.ALUflags_o.value} lmao"
        
        if valor_flag_in == 0:
            resultado = (valor_a << valor_b) & 0xF
            await Timer(2, 'ns')
            assert dut.ALUresult_o.value == resultado, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

        elif valor_flag_in == 1:
            resultado = ((valor_a << valor_b) | ((1 << valor_b) - 1))
            resultado &= 0b1111
            await Timer(3, 'ns')
            assert dut.ALUresult_o.value == resultado, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value} expected {resultado}"

@cocotb.test()
async def test_corrimiento_derecha(dut):
    '''Prueba de la operación corrimiento a la derecha'''
    for run in range (10):
        dut.ALUcontrol_i.value = 9
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        valor_flag_in = random.randint(0, 1)
        dut.ALUflagin_i.value = valor_flag_in

        if (valor_b <= 4):
            valor_flag_out = ((valor_a) >> (valor_b - 1)) & 0b1
            await Timer(2, 'ns')
            assert dut.ALUflags_o.value == valor_flag_out, f"Mux output salida_o was incorrect. Got {dut.ALUflags_o.value}"
        
        elif (valor_b >> 4):
            valor_flag_out = valor_flag_in
            await Timer(2, 'ns')
            assert dut.ALUflags_o.value == valor_flag_out, f"Mux output salida_o was incorrect. Got {dut.ALUflags_o.value} lmao"
        
        if valor_flag_in == 0:
            resultado = (valor_a >> valor_b) & 0xF
            await Timer(2, 'ns')
            assert dut.ALUresult_o.value == resultado, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value}"

        elif valor_flag_in == 1:
            resultado = ((valor_a >> valor_b) | ((1 >> valor_b) - 1))
            resultado &= 0b1111
            await Timer(3, 'ns')
            assert dut.ALUresult_o.value == resultado, f"Mux output salida_o was incorrect. Got {dut.ALUresult_o.value} expected {resultado}"