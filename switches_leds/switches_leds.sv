`timescale 1ns / 1ps

module switches_leds(
    input  logic [15:0] switch_pi,
    input  logic [3:0]  boton_pi,
    output logic [15:0] led_po //
    );
    
    assign led_po[0] = switch_pi[0] && !boton_pi[0];
    assign led_po[1] = switch_pi[1] && !boton_pi[0];
    assign led_po[2] = switch_pi[2] && !boton_pi[0];
    assign led_po[3] = switch_pi[3] && !boton_pi[0];

    assign led_po[4] = switch_pi[4] && !boton_pi[1];
    assign led_po[5] = switch_pi[5] && !boton_pi[1];
    assign led_po[6] = switch_pi[6] && !boton_pi[1];
    assign led_po[7] = switch_pi[7] && !boton_pi[1];
    
    assign led_po[8] = switch_pi[8] && !boton_pi[2];
    assign led_po[9] = switch_pi[9] && !boton_pi[2];
    assign led_po[10] = switch_pi[10] && !boton_pi[2];
    assign led_po[11] = switch_pi[11] && !boton_pi[2];
    
    assign led_po[12] = switch_pi[12] && !boton_pi[3];
    assign led_po[13] = switch_pi[13] && !boton_pi[3];
    assign led_po[14] = switch_pi[14] && !boton_pi[3];
    assign led_po[15] = switch_pi[15] && !boton_pi[3];
endmodule