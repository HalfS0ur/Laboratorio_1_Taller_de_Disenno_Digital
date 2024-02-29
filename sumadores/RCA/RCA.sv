`timescale 1ns / 1ps

module RCA 
#(parameter Bits=8 )
(
  input  logic [Bits-1:0] a,
  input  logic [Bits-1:0] b,
  input  logic            cin,
  output logic [Bits-1:0] sum,
  output logic            cout
);

  logic [Bits-1:0] carry;
  assign carry[0] = cin; 
  generate
    genvar i;
 
    for (i = 0; i < Bits; i = i + 1) 
 
        full_adder fa (.a(a[i]), .b(b[i]), .cin(carry[i]), .sum(sum[i]), .cout(carry[i+1]));       
  endgenerate 
  assign cout = carry[Bits];
endmodule