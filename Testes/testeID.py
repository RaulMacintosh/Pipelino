import serial
serial = serial.Serial('/dev/ttyACM0', 9600)
instructionADD  = chr(0)+chr(1)+chr(2)+chr(1)
instructionSUB  = chr(1)+chr(1)+chr(2)+chr(1)
instructionADDI = chr(2)+chr(1)+chr(2)+chr(1)
instructionLW   = chr(3)+chr(1)+chr(2)+chr(1)
instructionSW   = chr(4)+chr(1)+chr(2)+chr(1)
instructionSLL  = chr(5)+chr(1)+chr(2)+chr(1)
instructionSRL  = chr(6)+chr(1)+chr(2)+chr(1)
instructionBEQ  = chr(7)+chr(1)+chr(2)+chr(1)
instructionBNE  = chr(8)+chr(1)+chr(2)+chr(1)
serial.write(instructionADD)
serial.write(instructionSUB)
serial.write(instructionADDI)
serial.write(instructionLW)
serial.write(instructionSW)
serial.write(instructionSLL)
serial.write(instructionSRL)
serial.write(instructionBEW)
serial.write(instructionBNE)


