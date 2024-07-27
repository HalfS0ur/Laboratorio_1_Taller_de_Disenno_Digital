`timescale 1ns / 1ps

module RCA #(
  parameter BITS = 8
)(
  input  logic [BITS-1:0] a,
  input  logic [BITS-1:0] b,
  input  logic            cin,
  output logic [BITS-1:0] sum,
  output logic            cout
);

logic [BITS:0] carry; //
assign carry[0] = cin;

generate
    genvar i;

    for (i = 0; i < BITS; i = i + 1) begin
        full_adder fa (
            .a(a[i]),
            .b(b[i]),
            .cin(carry[i]),
            .sum(sum[i]),
            .cout(carry[i+1])
        );
    end
endgenerate

assign cout = carry[BITS];

endmodule
