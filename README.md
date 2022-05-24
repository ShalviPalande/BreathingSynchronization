# BreathingSynchronization
This repository consists of codes for a wearable device used to detect breathing data and 
inturn showcase that breathing data onto a visual and a vibrotactile modality to find if synchronization instances can be seen.

The device needs to have a laptop, 2 arduino mega microcontrollers, 2 stretch sensors, 2 NeoPixel 8*8 LEDs, DRV2605L Vibrotactile motors.

AllData.zip file consists of raw breathing data collected from 15 pairs of participants over 5 modalities namely Baseline, Visual, Vibrotactile, Visual-Vibrotactile, InSync.

The repository consists of 3 branches.
1) Python Codes 
          1.A) InputDataConditionSwitch.py : This python file can be used after connecting the laptop to 2 Arduino Mega Microcontrollers. 
           The code can register the raw breathing data onto excel sheets, along with selecting the condiotion for the modality in which the data is to be             showcased back to the user.
           
           1.B) DataAnalysisPearsonCorrelation.py : This python file is to be used after all the data has been collected from the user1 and user2.
           The code cleans the data, normalises it, finds the respiration rate of the raw breathing data and finally applies pearson correlation to the                    same.
           
           1.C) Data Analysis : This oython files consists of the code using neurokit to find the respiration rate from the raw breathig data. 
           
2) Arduino Codes
          2.A) BreathingInput : Receives input from stretch sensor and normalizes sensor input and sends raw breathing data back to python (1.A)
          2.B) BreathsensingFinal(Main) : Checks if Arduino is available for interaction. Receives condition input from python code (1.A). Sends Condition to Mapping code(2.C)
          2.C) LEDMapping : Maps raw sensor input into digital values to be showcased onto actuators (2.D)
          2.D) Actuation : Sends signal to Visual/Vibrotactile Actuators showcasing breathing data received from sensor input.

3) Graph Plot Codes
          3.A) NMQPlot : Box Plots for networked minds questionnaire. Multiple Y axes for a single X axis.
          3.B) AllCCFPlot : Line graph for CCF values calculated from respiration data.
          3.C) BoxPlotPearsonCorrealtion : Box plot for all modalities calculated from pearson correlation to showcase average.
          3.D) ValueGraphs : Line graphs of breathing data of 2 users for Raw data, Amplitude, and Respiration Rate.
