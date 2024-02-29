module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/RCA.fst");
    $dumpvars(0, RCA);
end
endmodule
