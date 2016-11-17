
from sys import argv
def writeMain( n_bots ,n_cops, way_file, obs_file,int_file,mean_delay,std_delay,loss_percent,timeout):
	writeFile = open("Main.java", "wb")
	writeFile.write( "package edu.illinois.mitra.demo.leaderelect;\nimport edu.illinois.mitra.starlSim.main.SimSettings;\nimport edu.illinois.mitra.starlSim.main.Simulation;\n\n")
	writeFile.write("public class Main {\n\n")
	writeFile.write("	public static void main(String[] args) {\n\n")
	writeFile.write("		SimSettings.Builder settings = new SimSettings.Builder();\n")
        if n_bots is not None:
            writeFile.write("		settings.N_BOTS("+ n_bots+");\n")
	if n_cops is not None:
            writeFile.write("		settings.N_QUADCOPTERS("+ n_cops+");\n")
	if way_file is not None:
            writeFile.write("		settings.WAYPOINT_FILE(\""+way_file+".wpt\");\n")
	if obs_file is not None:
            writeFile.write("		settings.OBSPOINT_FILE(\""+obs_file+".wpt\");\n")
	if int_file is not None:
            writeFile.write("		settings.INITIAL_POSITIONS_FILE(\""+int_file+".wpt\");\n")
	if mean_delay is not None:
            writeFile.write("		settings.MSG_MEAN_DELAY("+ mean_delay+");\n")
	if std_delay is not None:
            writeFile.write("		settings.MSG_STDDEV_DELAY("+ std_delay+");\n")
	if loss_percent is not None:
            writeFile.write("		settings.MSG_LOSSES_PER_HUNDRED("+ loss_percent+");\n")
	if timeout is None:
            timeout = 3000
        writeFile.write("		settings.SIM_TIMEOUT("+ timeout+");\n")
	writeFile.write("		settings.DRAW(false);\n") #disable drawing
	writeFile.write("		settings.DRAWER(new LeaderElectDrawer());\n")
	writeFile.write("		Simulation sim = new Simulation(LeaderElectApp.class, settings.build());\n")
	writeFile.write("		sim.start();\n")
	writeFile.write("	}\n}")
	writeFile.close()
	return;
writeMain(argv[1],argv[2],argv[3],argv[4],argv[5],argv[6],argv[7],argv[8],argv[9])
	


