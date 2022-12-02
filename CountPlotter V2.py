import os
import csv
import matplotlib.pyplot as plot



fileName = "COM9_174803_21_11_2022.log"
rawPlot, errorPlot, deltaPlot, ccvalPlot, statusPlot = [], [], [], [], []
raw, error, delta, ccval, status = [],[],[],[],[]
prevStat = 0

for i in range(12):
    raw.append([])
    error.append([])
    delta.append([])
    ccval.append([])
    status.append([])

with open(os.getcwd() + "\\" + fileName , "r") as logFile:

        reader = csv.reader(logFile)

        for line in logFile:
            line = line.strip('\n')
            line = line.split("\t")
            try:
                if line[1] == 'raw:' :
                    if len(line) == 14:
                        line = line[2:]
                        rawPlot.append(line)
                if line[1] == 'baseline:' :
                    if len(line) == 14:
                        line = line[2:]
                        errorPlot.append(line)
                if line[1] == 'delta:' :
                    if len(line) == 14:
                        line = line[2:]
                        deltaPlot.append(line)
                if line[1] == 'ccval:' :
                    if len(line) == 14:
                        line = line[2:]
                        ccvalPlot.append(line)
                if line[1] == 'status:' :
                    if len(line) == 14:
                        
                        line = line[2:]
                        statusPlot.append(line)

            except: IndexError

rawPlot = rawPlot[20:]
errorPlot = errorPlot[20:]
deltaPlot = deltaPlot[20:]
ccvalPlot = ccvalPlot[20:]
statusPlot = statusPlot[20:]



fig, axis = plot.subplots(5,1, figsize=(16,7), constrained_layout = True)
fig.suptitle("HPDS Serial Output Decoded - " + fileName)


for j in range(12):
    for i in range(len(rawPlot)):
        try:
            if int(rawPlot[i][j]) >0:
                raw[j].append(int(rawPlot[i][j]))
        except ValueError:
            pass
    for i in range(len(deltaPlot)):
        try:
            delta[j].append(int(deltaPlot[i][j]))
        except ValueError:
            pass    
    for i in range(len(statusPlot)):
        try:
            if int(statusPlot[i][j]) < 5:
                status[j].append(int(statusPlot[i][j]))
        except ValueError:
            pass  
    for i in range(len(errorPlot)):
        try:
            error[j].append(int(errorPlot[i][j]))
        except ValueError:
            pass
    for i in range(len(ccvalPlot)):
        try:
            if int(ccvalPlot[i][j]) >1000:
                 if int(ccvalPlot[i][j]) < 100000:
                    ccval[j].append(int(ccvalPlot[i][j]))
        except ValueError:
            pass

        

    for q in range(len(status[j])):
        if status[j][q] == 1: 
            if prevStat == 0:
                debug = status[j][q]
                status[j][q] = -1
        prevStat = status[j][q]

    axis[0].plot(range(len(raw[j])),raw[j] )
    axis[0].set_ylabel("Raw")
    axis[1].plot(range(len(delta[j])),delta[j] )
    axis[1].axhline(y=50, color = 'r', linestyle = 'dashed')
    axis[1].set_ylabel("Delta")
    axis[2].plot(range(len(status[j])),status[j] )
    axis[2].set_ylabel("Status")
    axis[3].plot(range(len(error[j])),error[j] )
    axis[3].set_ylabel("Baseline")
    axis[4].plot(range(len(ccval[j])),ccval[j] )
    axis[4].set_ylabel("CC Value")


plot.show()        
