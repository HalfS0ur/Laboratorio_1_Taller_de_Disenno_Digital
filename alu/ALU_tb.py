import cocotb
import random
from cocotb.triggers import Timer

RANGO = 2**4

@cocotb.test()
async def test_AND(dut):
    '''Prueba de la operación AND'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 0

    for valor_a in range(RANGO):
        dut.ALUa_i.value = valor_a
        for valor_b in range(RANGO):
            dut.ALUcontrol_i.value = 0
            dut.ALUb_i.value = valor_b
            await Timer(1, 'ns')
            assert dut.ALUresult_o.value == valor_a & valor_b, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {valor_a & valor_b}"

@cocotb.test()
async def test_OR(dut):
    '''Prueba de la operación OR'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 1

    for valor_a in range(RANGO):
        dut.ALUa_i.value = valor_a
        for valor_b in range(RANGO):
            dut.ALUb_i.value = valor_b
            await Timer(1, 'ns')
            assert dut.ALUresult_o.value == valor_a | valor_b, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {valor_a | valor_b}"

########################### manejar numeros negativos

@cocotb.test()
async def prueba_suma_sin_carry(dut):
    '''Prueba de la operación suma sin carry in'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 2

    for valor_a in range(RANGO):
        dut.ALUa_i.value = valor_a
        for valor_b in range(RANGO):
            dut.ALUb_i.value = valor_b
            resultado_suma = (valor_a + valor_b) & 0xF
            resultado_carry = ((valor_b + valor_a) >> 4) & 1
            await Timer(1, 'ns')
            assert dut.ALUresult_o.value == resultado_suma, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {resultado_suma}"
            assert dut.ALUflags_o.value == resultado_carry, f"El valor de la salida ALUflags_o es incorrecto. Se obtuvo {dut.ALUflags_o.value}, se esperaba {resultado_carry}"

########################### manejar numeros negativos

@cocotb.test()
async def prueba_suma_con_carry(dut):
    '''Prueba de la operación suma con carry in'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 1
    dut.ALUcontrol_i.value = 2

    for valor_a in range(RANGO):
        dut.ALUa_i.value = valor_a
        for valor_b in range(RANGO):
            dut.ALUb_i.value = valor_b
            resultado_suma = (valor_a + valor_b + 1) & 0xF
            resultado_carry = ((valor_a + valor_b + 1) >> 4) & 1
            await Timer(1, 'ns')
            assert dut.ALUresult_o.value == resultado_suma, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {resultado_suma}"
            assert dut.ALUflags_o.value == resultado_carry, f"El valor de la salida ALUflags_o es incorrecto. Se obtuvo {dut.ALUflags_o.value}, se esperaba {resultado_carry}"

@cocotb.test()
async def test_incrementar_1(dut):
    '''Prueba de la operación incrementar en 1'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 3

    for valor_a in range (RANGO):
        dut.ALUa_i.value = valor_a
        dut.ALUflagin_i.value = 0
        resultado_a1 = (valor_a + 1) & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_a1, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {resultado_a1}"

    for valor_b in range (RANGO):
        dut.ALUb_i.value = valor_b
        dut.ALUflagin_i.value = 1
        resultado_b1 = (valor_b + 1) & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_b1, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {resultado_b1}"

@cocotb.test()
async def test_decrementar_1(dut):
    '''Prueba de la operación decrementar en 1'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 4

    for valor_a in range (RANGO):
        dut.ALUa_i.value = valor_a
        resultado_am1 = (valor_a - 1) & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_am1, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {resultado_am1}"

    for valor_b in range (RANGO):
        dut.ALUb_i.value = valor_b
        dut.ALUflagin_i.value = 1
        resultado_bm1 = (valor_b - 1) & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_bm1, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {resultado_bm1}"


@cocotb.test()
async def test_NOT(dut):
    '''Prueba de la operación NOT'''
    dut.ALUa_i.value = 0
    dut.ALUb_i.value = 0
    dut.ALUflagin_i.value = 0
    dut.ALUcontrol_i.value = 5

    for valor_a in range (RANGO):
        dut.ALUa_i.value = valor_a
        resultado_not_a = ~valor_a & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_not_a, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {resultado_not_a}"

    for valor_b in range (RANGO):
        dut.ALUb_i.value = valor_b
        dut.ALUflagin_i.value = 1
        resultado_not_b = ~valor_b & 0xF
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_not_b, f"El valor de la salida ALUresult_o es incorrecto. Se obtuvo {dut.ALUresult_o.value}, se esperaba {resultado_not_b}"

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
        assert dut.ALUresult_o.value == resultado_resta, f"ALU output ALUresult_o was incorrect. Got {dut.ALUresult_o.value}, expeted {(resultado_resta)}"
        assert dut.ALUflags_o.value == resultado_carry_resta, f"ALU output ALUflags_o was incorrect. Got {dut.ALUflags_o.value} expected {(resultado_carry_resta)}"

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
        assert dut.ALUresult_o.value == valor_a ^ valor_b, f"ALU output ALUresult_o was incorrect. Got {dut.ALUresult_o.value}, expected {(valor_a ^ valor_b)}"

@cocotb.test()
async def test_corrimiento_izquierda_ceros(dut):
    for run in range (10):
        dut.ALUcontrol_i.value = 8
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        valor_flag_in = 0
        dut.ALUflagin_i.value = valor_flag_in

        resultado = (valor_a << valor_b) & 0xF
        ultimo_bit = (valor_a >> (valor_b)) & 1
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado
        #assert dut.ALUflags_o.value == ultimo_bit
        print(dut.ALUflags_o.value, ultimo_bit) ##Revisar valores de x

@cocotb.test()
async def test_corrimiento_izquierda_unos(dut):
    for run in range (10):
        dut.ALUcontrol_i.value = 8
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        valor_flag_in = 1
        dut.ALUflagin_i.value = valor_flag_in

        resultado_esperado = ((valor_a << valor_b) | ((1 << valor_b) - 1)) & 0xF
        ultimo_bit = (valor_a >> (valor_b)) & 1
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado_esperado
        #assert dut.ALUflags_o.value == ultimo_bit
        print(dut.ALUflags_o.value, ultimo_bit) ##Revisar valores de x

@cocotb.test()
async def test_corrimiento_derecha_ceros(dut):
    for run in range (10):
        dut.ALUcontrol_i.value = 9
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        valor_flag_in = 0
        dut.ALUflagin_i.value = valor_flag_in

        resultado = (valor_a >> valor_b) & 0xF
        ultimo_bit = (valor_a >> (valor_b)) & 1
        await Timer(1, 'ns')
        assert dut.ALUresult_o.value == resultado
        #assert dut.ALUflags_o.value == ultimo_bit
        print(dut.ALUflags_o.value, ultimo_bit) ##Revisar valores de x

@cocotb.test()
async def test_corrimiento_derecha_unos(dut):
    for run in range (100):
        dut.ALUcontrol_i.value = 9
        valor_a = random.randint(0, 15)
        dut.ALUa_i.value = valor_a
        valor_b = random.randint(0, 15)
        dut.ALUb_i.value = valor_b
        valor_flag_in = 1
        dut.ALUflagin_i.value = valor_flag_in

        resultado = (valor_a >> valor_b) & 0xF
        ultimo_bit = (valor_a >> (valor_b)) & 1
        await Timer(1, 'ns')
        #assert dut.ALUresult_o.value == resultado
        #assert dut.ALUflags_o.value == ultimo_bit
        print(dut.ALUflags_o.value, ultimo_bit) ##Revisar valores de x





'''@cocotb.test()
async def test_corrimiento_izquierda(dut):
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
            assert dut.ALUflags_o.value == valor_flag_out, f"ALU output ALUflags_o was incorrect. Got {dut.ALUflags_o.value}, expected {(valor_flag_out)}"
        
        elif (valor_b > 4):
            valor_flag_out = valor_flag_in
            await Timer(2, 'ns')
            assert dut.ALUflags_o.value == valor_flag_out, f"Mux output ALUflags_o was incorrect. Got {dut.ALUflags_o.value}, expected {(valor_flag_out)}"
        
        if valor_flag_in == 0:
            resultado = (valor_a << valor_b) & 0xF
            await Timer(2, 'ns')
            assert dut.ALUresult_o.value == resultado, f"ALU output ALUresult_o was incorrect. Got {dut.ALUresult_o.value}, expected {(resultado)}"

        elif valor_flag_in == 1:
            resultado = ((valor_a << valor_b) | ((1 << valor_b) - 1))
            resultado &= 0b1111
            await Timer(3, 'ns')
            assert dut.ALUresult_o.value == resultado, f"ALU output ALUresult_o was incorrect. Got {dut.ALUresult_o.value}, expected {resultado}"











@cocotb.test()
async def test_corrimiento_derecha(dut):
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
            assert dut.ALUflags_o.value == valor_flag_out, f"ALU output ALUflags_o was incorrect. Got {dut.ALUflags_o.value}, expected {valor_flag_out}"
        
        elif (valor_b >> 4):
            valor_flag_out = valor_flag_in
            await Timer(2, 'ns')
            assert dut.ALUflags_o.value == valor_flag_out, f"ALU output ALUflags_o was incorrect. Got {dut.ALUflags_o.value}, expected {valor_flag_out}"
        
        if valor_flag_in == 0:
            resultado = (valor_a >> valor_b) & 0xF
            await Timer(2, 'ns')
            assert dut.ALUresult_o.value == resultado, f"ALU output ALUresult_o was incorrect. Got {dut.ALUresult_o.value}, expected {resultado}"

        elif valor_flag_in == 1:
            resultado = ((valor_a >> valor_b) | ((1 >> valor_b) - 1))
            resultado &= 0b1111
            await Timer(3, 'ns')
            assert dut.ALUresult_o.value == resultado, f"ALU output ALUresult_o was incorrect. Got {dut.ALUresult_o.value}, expected {resultado}"'''