`timescale 1ns / 1ps

module display_7_segmentos(
    //Definición de las entradas y salidas para el multiplexor
    input logic [15:0] sw_pi,
    input logic boton_izquierda_pi,
    input logic boton_derecha_pi,
    //Definición de la salida para el decodificador
    output logic [6:0] LED_o
    );
    logic [3:0] salida_mux_o;
    always_comb begin
        case ({boton_izquierda_pi, boton_derecha_pi})
            2'b00: salida_mux_o = sw_pi[3:0];
            2'b01: salida_mux_o = sw_pi[7:4];
            2'b10: salida_mux_o = sw_pi[11:8];
            2'b11: salida_mux_o = sw_pi[15:12];
        endcase
        
        case (salida_mux_o)
            4'b0000: LED_o = 7'b1000000; // 0
            4'b0001: LED_o = 7'b1111001; // 1
            4'b0010: LED_o = 7'b0100100; // 2
            4'b0011: LED_o = 7'b0110000; // 3
            4'b0100: LED_o = 7'b0011001; // 4
            4'b0101: LED_o = 7'b0010010; // 5
            4'b0110: LED_o = 7'b0000010; // 6
            4'b0111: LED_o = 7'b1111000; // 7
            4'b1000: LED_o = 7'b0000000; // 8
            4'b1001: LED_o = 7'b0010000; // 9
            4'b1010: LED_o = 7'b0001000; // A
            4'b1011: LED_o = 7'b0000011; // B
            4'b1100: LED_o = 7'b0100111; // C
            4'b1101: LED_o = 7'b0100001; // D
            4'b1110: LED_o = 7'b0000110; // E
            4'b1111: LED_o = 7'b0001110; // F
            default: LED_o = 7'b1111111; // Valor inválido
        endcase
        
    end
    
endmodule