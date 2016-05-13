import os
from sys import argv
def writePlot( filename ,robotnum, robotID, mode):
	writeFile = open(filename +".gy", "wb")
	writeFile.write( "set term png\n")
	writeFile.write( "set output 'output.png'\n")
	writeFile.write("set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 2 ps 1.5   # --- blue\n")
	writeFile.write("set style line 2 lc rgb '#dd181f' lt 1 lw 2 pt 2 ps 1.5   # --- red\n")
	writeFile.write("set style line 3 lc rgb '#00ff80' lt 1 lw 2 pt 2 ps 1.5   # --- green\n")
	writeFile.write("set style line 4 lc rgb '#80ff00' lt 1 lw 2 pt 2 ps 1.5   # --- green\n")
	robotID = int(robotID)
	robotnum = int(robotnum)
	if int(mode) == 1:
		writeFile.write( "set xlabel 't (ms)'\n")
		writeFile.write( "set ylabel 'X (mm)'\n")
		writeFile.write( "set title ' "+filename+" x vs t '\n")
		tmp = robotID
		if robotnum ==1:
			writeFile.write( "plot '"+filename+str(robotID)+".dat' using 1:2 title 'robot" +str(robotID)+ "' with l ls "+str(robotID)+"\n")
			writeFile.close()
			return;
		newID = 1
		for i in range(robotnum):
			while int(tmp) % 2 ==0:
				tmp = tmp/2
				newID=newID+1
			if i == 0:
				writeFile.write( "plot '"+filename+str(newID)+".dat' using 1:2 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+", \\")
				writeFile.write("\n")
			elif i == robotnum-1:
				writeFile.write( "     '"+filename+str(newID)+".dat' using 1:2 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+" \n")
			else:
				writeFile.write( "     '"+filename+str(newID)+".dat' using 1:2 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+", \\")
				writeFile.write("\n")
			tmp = tmp/2
			newID = newID+1

	if int(mode)== 2:
		writeFile.write( "set xlabel 't (ms)'\n")
		writeFile.write( "set ylabel 'Y (mm)'\n")
		writeFile.write( "set title ' "+filename+" y vs t '\n")
		tmp = robotID
		if robotnum ==1:
			writeFile.write( "plot '"+filename+str(robotID)+".dat' using 1:3 title 'robot" +str(robotID)+ "' with l ls "+str(robotID)+"\n")
			writeFile.close()
			return;
		newID = 1
		for i in range(robotnum):
			while int(tmp) % 2 ==0:
				tmp = tmp/2
				newID=newID+1
			if i == 0:
				writeFile.write( "plot '"+filename+str(newID)+".dat' using 1:3 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+", \\")
				writeFile.write("\n")
			elif i == robotnum-1:
				writeFile.write( "     '"+filename+str(newID)+".dat' using 1:3 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+" \n")
			else:
				writeFile.write( "     '"+filename+str(newID)+".dat' using 1:3 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+", \\")
				writeFile.write("\n")
			tmp = tmp/2
			newID = newID+1
	if int(mode)== 3:
		writeFile.write( "set xlabel 'Y (ms)'\n")
		writeFile.write( "set ylabel 'X (mm)'\n")
		writeFile.write( "set title ' "+filename+" y vs x '\n")
		tmp = robotID
		if robotnum ==1:
			writeFile.write( "plot '"+filename+str(robotID)+".dat' using 2:3 title 'robot" +str(robotID)+ "' with l ls "+str(robotID)+"\n")
			writeFile.close()
			return;
		newID = 1
		for i in range(robotnum):
			while int(tmp) % 2 ==0:
				tmp = tmp/2
				newID=newID+1
			if i == 0:
				writeFile.write( "plot '"+filename+str(newID)+".dat' using 2:3 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+", \\")
				writeFile.write("\n")
			elif i == robotnum-1:
				writeFile.write( "     '"+filename+str(newID)+".dat' using 2:3 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+" \n")
			else:
				writeFile.write( "     '"+filename+str(newID)+".dat' using 2:3 title 'robot" +str(newID)+ "' with l ls "+str(i+1)+", \\")
				writeFile.write("\n")
			tmp = tmp/2
			newID = newID+1
	writeFile.close()
	print "success"
writePlot(argv[1],argv[2],argv[3],argv[4])
os.system("gnuplot "+argv[1]+".gy")
