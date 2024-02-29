`timescale 1ns / 1ps

module ALU #(
    parameter ANCHO = 4
)(
    input  logic signed [ANCHO-1:0] ALUa_i,
    input  logic signed [ANCHO-1:0] ALUb_i,
    input  logic                    ALUflagin_i,
    input  logic        [3:0]       ALUcontrol_i,
    output logic        [ANCHO-1:0] ALUresult_o,
    output logic                    ALUflags_o,
    output logic                    zero_o
);
    logic [ANCHO:0]carry_suma;
    logic [ANCHO:0]carry_resta;
    
    assign carry_suma = ALUa_i + ALUb_i + ALUflagin_i;
    assign carry_resta = ALUa_i - ALUb_i - ALUflagin_i;

    always_comb begin
        case(ALUcontrol_i)
             4'h0: begin //AND bitwise
                    ALUresult_o = ALUa_i & ALUb_i;
                  end
                  
             4'h1: begin //OR bitwise
                    ALUresult_o = ALUa_i | ALUb_i;
                  end
                  
             4'h2: begin //Suma
                    ALUresult_o = ALUa_i + ALUb_i + ALUflagin_i;
                    ALUflags_o = carry_suma[ANCHO];
                  end
                  
              4'h3: begin //Incrementar el operando en 1
                     if (ALUflagin_i == 0)
                         ALUresult_o = ALUa_i + 1;
                     else
                         ALUresult_o = ALUb_i + 1;
                  end
                  
              4'h4: begin //Decrementar operando en 1
                     if (ALUflagin_i == 0)
                         ALUresult_o = ALUa_i - 1;
                     else
                         ALUresult_o = ALUb_i - 1;
                  end
                  
              4'h5: begin //NOT operando
                     if (ALUflagin_i == 0)
                         ALUresult_o = ~ALUa_i;
                     else
                         ALUresult_o = ~ALUb_i;
                  end
                  
              4'h6: begin //Resta
                      ALUresult_o = ALUa_i - ALUb_i - ALUflagin_i;
                      ALUflags_o = carry_resta[ANCHO];
                  end
                  
              4'h7: begin //Xor bitwise
                     ALUresult_o = ALUa_i ^ ALUb_i;
                  end
                  
              4'h8: begin //Corrimiento a la izquierda
                      if (ALUb_i <= ANCHO) //Logica para calcular el ultimo bit que sale
                          ALUflags_o = ALUa_i[((ANCHO)-ALUb_i)];
                      else if (ALUb_i > ANCHO)
                          ALUflags_o = ALUflagin_i;
                          
                      if (ALUflagin_i == 0) 
                          ALUresult_o = ALUa_i << ALUb_i;
                     
                      else if (ALUflagin_i == 1) //Logica para desplazar el registro a la derecha y rellenar con 1
                          begin
                              ALUresult_o = ALUa_i << ALUb_i;
                              for (int n=0; n<ALUb_i; n++)
                                  begin
                                      ALUresult_o[n] = 1;
                                  end
                          end
                 end
                 
             4'h9: begin //Corrimiento a la derecha
                     if (ALUb_i <= ANCHO) //Logica para calcular el ultimo bit que sale
                         ALUflags_o = ALUa_i[ALUb_i-1];
                     else if (ALUb_i > ANCHO)
                         ALUflags_o = ALUflagin_i;
                         
                     if (ALUflagin_i == 0)
                         ALUresult_o = ALUa_i >> ALUb_i;
                         
                     else if (ALUflagin_i == 1) //Logica para desplazar el registro a la derecha y rellenar con 1
                         begin
                             ALUresult_o = ALUa_i >> ALUb_i;
                             for (int k = ANCHO - 1; k>=(ANCHO-ALUb_i); k--)
                                 begin
                                     ALUresult_o[k] = 1;
                                 end
                         end
             end
        endcase
        
    if (ALUresult_o == 0)
        zero_o = 1;
    else
        zero_o = 0;
    end
endmodule