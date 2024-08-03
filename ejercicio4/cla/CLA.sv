`timescale 1ns / 1ps

module CLA (
  input  logic [7:0] a,         //tamano de 8-bit.
  input  logic [7:0] b,
  input  logic       c_in,
  output logic [7:0] sum,
  output logic       c_out
);

  logic [8:0] G;    //generador de acarreo
  logic [8:0] P;    //propagador de acarreo
  logic [9:0] C;    //acarreos generados

  always_comb begin
    G = a & b;
    P = a ^ b;
    C[0] = c_in;

    for (int i = 0; i < 8; i++) begin   //generar etapas de cálculo de anticipación de acarreo..
      C[i+1] = G[i] | (P[i] & C[i]);
      sum[i] = P[i] ^ C[i];
    end

    c_out = C[8];
  end

endmodule
