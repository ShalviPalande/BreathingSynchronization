import serial
import os.path
import time
import csv
import keyboard
from switchlang import switch
    
##OPEN PORTS FOR 2 MEGAS
ser101 = serial.Serial('/dev/cu.usbmodem14101')
time.sleep(1)
ser101.flushInput()

ser301 = serial.Serial('/dev/cu.usbmodem14301')
time.sleep(1)
ser301.flushInput()

filename1 = "/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp13/User1.csv"
filename2 = "/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp13/User2.csv"

##Write Headers of Files
with open (filename1,'w') as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["timestamp","value","type"])
        

with open (filename2,'w') as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["timestamp","value","type"])
    
        
##SELECT TEST CONDITION
def ConditionSelect():
    con = input("Enter 1,2,3,4,5 to select test condition ")
    print("Press Ctrl+C to stop data logging and then select next condition")
    
    with switch(con) as s:
        s.case('1', Baseline)
        s.case('2', Visual)
        s.case('3', Vibrotactile)
        s.case('4', VisualVibro)
        s.case('5', InSync)
        s.default(Invalid_Condition)

##DATA LOGGING FOR CONDITIONS  
def Baseline():
    print("Selected Condition : Baseline")
    ser101.write(b'1')          
    ser301.write(b'1')         
    try:
        while True:
            ser101_bytes = ser101.readline()        #read sensor value from arduino101
            ser301_bytes = ser301.readline()        #read sensor value from arduino301
            decoded_bytes101 = float(ser101_bytes[0:len(ser101_bytes)-2].decode("utf-8"))
            decoded_bytes301 = float(ser301_bytes[0:len(ser301_bytes)-2].decode("utf-8"))
            print(decoded_bytes101,decoded_bytes301)
            
            
            #open file and write sensor values
            with open(filename1,'a') as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes101,'Baseline'])
                
               
            with open(filename2,'a') as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes301,'Baseline'])
                
              
    except:
        print("Baseline Data Logging Done")
        pass
        #f.close()   
    ConditionSelect()

def Visual():
    print("Selected Condition : Visual")
    ser101.write(b'2')          
    ser301.write(b'2')         
    try:
        while True:
            ser101_bytes = ser101.readline()        #read sensor value from arduino101
            ser301_bytes = ser301.readline()        #read sensor value from arduino301
            decoded_bytes101 = float(ser101_bytes[0:len(ser101_bytes)-2].decode("utf-8"))
            decoded_bytes301 = float(ser301_bytes[0:len(ser301_bytes)-2].decode("utf-8"))
            print(decoded_bytes101,decoded_bytes301)
            
            #open file and write sensor values
            with open(filename1,"a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes101,'Visual'])

            with open(filename2,"a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes301,'Visual'])
              
    except:
        print("Visual Data Logging Done")
        pass
    #f.close()   
    ConditionSelect()

def Vibrotactile():
    print("Selected Condition : Vibrotactile")
    ser101.write(b'3')
    ser301.write(b'3')
    try:
        while True:
            ser101_bytes = ser101.readline()        #read sensor value from arduino101
            ser301_bytes = ser301.readline()        #read sensor value from arduino301
            decoded_bytes101 = float(ser101_bytes[0:len(ser101_bytes)-2].decode("utf-8"))
            decoded_bytes301 = float(ser301_bytes[0:len(ser301_bytes)-2].decode("utf-8"))
            print(decoded_bytes101,decoded_bytes301)
            
            #open file and write sensor values
            with open(filename1,"a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes101,'Vibrotactile'])
                
            with open(filename2,"a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes301,'Vibrotactile'])
            
    except:
        print("Vibrotactile Data Logging Done")
        pass
    #f.close()   
    ConditionSelect()

def VisualVibro():
    print("Selected Condition : VisualVibro")
    ser101.write(b'4')
    ser301.write(b'4')
    try:
        while True:
            ser101_bytes = ser101.readline()        #read sensor value from arduino101
            ser301_bytes = ser301.readline()        #read sensor value from arduino301
            decoded_bytes101 = float(ser101_bytes[0:len(ser101_bytes)-2].decode("utf-8"))
            decoded_bytes301 = float(ser301_bytes[0:len(ser301_bytes)-2].decode("utf-8"))
            print(decoded_bytes101,decoded_bytes301)
            
            #open file and write sensor values
            with open(filename1,"a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes101,'VisualVibro'])
                
            with open(filename2,"a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes301,'VisualVibro'])
               
    except:
        print("VisualVibro Data Logging Done")
        pass
    #f.close()   
    ConditionSelect()

def InSync():
    print("Selected Condition : InSync")
    ser101.write(b'5') 
    ser301.write(b'5')
    try:
        while True:
            ser101_bytes = ser101.readline()        #read sensor value from arduino101
            ser301_bytes = ser301.readline()        #read sensor value from arduino301
            decoded_bytes101 = float(ser101_bytes[0:len(ser101_bytes)-2].decode("utf-8"))
            decoded_bytes301 = float(ser301_bytes[0:len(ser301_bytes)-2].decode("utf-8"))
            print(decoded_bytes101,decoded_bytes301)
            
            #open file and write sensor values
            with open(filename1,"a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes101,'InSync'])
                
            with open(filename2,"a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([time.asctime(),decoded_bytes301,'InSync'])
                
    except:
        print("InSync Data Logging Done")
        pass
    #f.close()   
    ConditionSelect()

def Invalid_Condition():
    print("Invalid Input : Please Select Valid Condition")
    ConditionSelect()
    

ConditionSelect()
