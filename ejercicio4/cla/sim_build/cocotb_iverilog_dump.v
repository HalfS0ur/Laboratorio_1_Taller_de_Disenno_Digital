module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/CLA.fst");
    $dumpvars(0, CLA);
end
endmodule
