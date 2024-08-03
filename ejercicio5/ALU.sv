`timescale 1ns / 1ps

module ALU #(
    parameter ANCHO = 4
)(
    input  logic signed [ANCHO-1:0]  ALUA,
    input  logic signed [ANCHO-1:0]  ALUB,
    input  logic                     ALUFlagIn,
    input  logic        [3:0]        ALUControl,
    
    output logic        [ANCHO-1:0]  ALUResult,
    output logic                     ALUFlags,
    output logic                     ALUZero
    );
    
    logic [ANCHO:0] carry_suma;
    logic [ANCHO:0] carry_resta;
    
    logic [ANCHO-1:0] Ai = 0;
    logic [ANCHO-1:0] As = 0;

    assign carry_suma = ALUA + ALUB + ALUFlagIn;
    assign carry_resta = ALUA - ALUB - ALUFlagIn;
    
    always_comb begin
        Ai = 0;
        As = 0;
        
        case(ALUControl)
            4'h0: begin
                    ALUResult = ALUA & ALUB; //and
                    ALUFlags = 0;
                  end
                  
            4'h1: begin
                    ALUResult = ALUA | ALUB; //or
                    ALUFlags = 0;
                  end
                  
            4'h2: begin
                    ALUResult = ALUA + ALUB + ALUFlagIn; //suma
                    ALUFlags = carry_suma [ANCHO];
                  end
                  
            4'h3: begin //incremento en 1
                    ALUFlags = 0;
                    if (ALUFlagIn == 0)
                        ALUResult = ALUA + 1;
                    else
                        ALUResult = ALUB + 1;
                  end
                  
            4'h4: begin //decremento en 1
                    ALUFlags = 0;
                    if (ALUFlagIn == 0)
                        ALUResult = ALUA - 1;
                    else
                        ALUResult = ALUB - 1;
                  end
                  
            4'h5: begin //not
                    ALUFlags = 0;
                    if (ALUFlagIn == 0)
                        ALUResult = ~ALUA;
                    else
                        ALUResult = ~ALUB;
                  end
                  
            4'h6: begin //resta
                    ALUResult = ALUA - ALUB - ALUFlagIn;
                    ALUFlags = carry_resta [ANCHO];
                  end
                  
            4'h7: begin //xor
                    ALUResult = ALUA ^ ALUB; 
                    ALUFlags = 0;
                  end
                  
            4'h8: begin
                    if (ALUFlagIn == 0)
                        ALUResult = ALUA << ALUB;
                    else begin
                        Ai = ~ALUA;
                        As = Ai << ALUB;
                        ALUResult = ~As;
                    end
                    
                    if (ALUB <= ANCHO) //Logica para calcular el ultimo bit que sale
                          ALUFlags = ALUA[((ANCHO)-ALUB)];
                    else
                          ALUFlags = ALUFlagIn;
                  end
                  
            4'h9: begin
                    if (ALUFlagIn == 0)
                        ALUResult = ALUA >> ALUB;
                    else begin
                        Ai = ~ALUA;
                        As = Ai >> ALUB;
                        ALUResult = ~As;
                    end
                    
                    if (ALUB <= ANCHO) //Logica para calcular el ultimo bit que sale
                         ALUFlags = ALUA[ALUB-1];
                    else
                         ALUFlags = ALUFlagIn;
                  end
                        
            default: begin
                         ALUResult = 'bx;
                         ALUFlags = 'bx;
                     end
        endcase
        
        if (ALUResult == 0)
            ALUZero = 1;
        else
            ALUZero = 0;
    end
    
endmodule
