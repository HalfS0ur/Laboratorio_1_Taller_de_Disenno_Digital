`timescale 1ns / 1ps

module mux_4_1 #(
    parameter int ANCHO = 8
)(
    input  logic [1:0]       seleccion_i,
    input  logic [ANCHO-1:0] entrada0_i,
    input  logic [ANCHO-1:0] entrada1_i, 
    input  logic [ANCHO-1:0] entrada2_i, 
    input  logic [ANCHO-1:0] entrada3_i,  
    output logic [ANCHO-1:0] salida_o
    );
    
    always_comb begin //always_comb se ejecuta una vez en t=0 y es sensible a los cambios en una funcion como seleccion_i
        case (seleccion_i)
            2'b00: salida_o = entrada0_i;
            2'b01: salida_o = entrada1_i;
            2'b10: salida_o = entrada2_i;
            2'b11: salida_o = entrada3_i;
        endcase
    end
endmodule
