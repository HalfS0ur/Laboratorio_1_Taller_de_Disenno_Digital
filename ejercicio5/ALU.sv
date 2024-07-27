`timescale 1ns / 1ps

module ALU #(
    parameter ANCHO = 4
)(
    input  logic signed [ANCHO-1:0]  ALUa_i,
    input  logic signed [ANCHO-1:0]  ALUb_i,
    input  logic                     ALUflagin_i,
    input  logic        [3:0]        ALUcontrol_i,
    
    output logic        [ANCHO-1:0]  ALUresult_o,
    output logic                     ALUflags_o,
    output logic                     zero_o
    );
    
    logic [ANCHO:0] carry_suma;
    logic [ANCHO:0] carry_resta;
    
    logic [ANCHO-1:0] Ai = 0;
    logic [ANCHO-1:0] As = 0;

    assign carry_suma = ALUa_i + ALUb_i + ALUflagin_i;
    assign carry_resta = ALUa_i - ALUb_i - ALUflagin_i;
    
    always_comb begin
        case(ALUcontrol_i)
            4'h0: begin
                    ALUresult_o = ALUa_i & ALUb_i; //and.
                    ALUflags_o = 0;
                  end
                  
            4'h1: begin
                    ALUresult_o = ALUa_i | ALUb_i; //or
                    ALUflags_o = 0;
                  end
                  
            4'h2: begin
                    ALUresult_o = ALUa_i + ALUb_i + ALUflagin_i; //suma
                    ALUflags_o = carry_suma [ANCHO];
                  end
                  
            4'h3: begin //incremento en 1
                    ALUflags_o = 0;
                    if (ALUflagin_i == 0)
                        ALUresult_o = ALUa_i + 1;
                    else
                        ALUresult_o = ALUb_i + 1;
                  end
                  
            4'h4: begin //decremento en 1
                    ALUflags_o = 0;
                    if (ALUflagin_i == 0)
                        ALUresult_o = ALUa_i - 1;
                    else
                        ALUresult_o = ALUb_i - 1;
                  end
                  
            4'h5: begin //not
                    ALUflags_o = 0;
                    if (ALUflagin_i == 0)
                        ALUresult_o = ~ALUa_i;
                    else
                        ALUresult_o = ~ALUb_i;
                  end
                  
            4'h6: begin //resta
                    ALUresult_o = ALUa_i - ALUb_i - ALUflagin_i;
                    ALUflags_o = carry_resta [ANCHO];
                  end
                  
            4'h7: begin //xor
                    ALUresult_o = ALUa_i ^ ALUb_i; 
                    ALUflags_o = 0;
                  end
                  
            4'h8: begin
                    if (ALUflagin_i == 0)
                        ALUresult_o = ALUa_i << ALUb_i;
                    else begin
                        Ai = ~ALUa_i;
                        As = Ai << ALUb_i;
                        ALUresult_o = ~As;
                    end
                    
                    if (ALUb_i <= ANCHO) //Logica para calcular el ultimo bit que sale
                          ALUflags_o = ALUa_i[((ANCHO)-ALUb_i)];
                    else
                          ALUflags_o = ALUflagin_i;
                  end
                  
            4'h9: begin
                    if (ALUflagin_i == 0)
                        ALUresult_o = ALUa_i >> ALUb_i;
                    else begin
                        Ai = ~ALUa_i;
                        As = Ai >> ALUb_i;
                        ALUresult_o = ~As;
                    end
                    
                    if (ALUb_i <= ANCHO) //Logica para calcular el ultimo bit que sale
                         ALUflags_o = ALUa_i[ALUb_i-1];
                    else
                         ALUflags_o = ALUflagin_i;
                  end
                        
            default: begin
                         ALUresult_o = 'bx;
                         ALUflags_o = 'bx;
                     end
        endcase
        
        if (ALUresult_o == 0)
            zero_o = 1;
        else
            zero_o = 0;
    end
    
endmodule
