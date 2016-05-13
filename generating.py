
from sys import argv
def writeMain( n_bots ,n_cops, way_file, obs_file,int_file,mean_delay,std_delay,loss_percent,timeout):
	writeFile = open("main.java", "wb")
	writeFile.write( "package edu.illinois.mitra.demo.leaderelect;\nimport edu.illinois.mitra.starlSim.main.SimSettings;\nimport edu.illinois.mitra.starlSim.main.Simulation;\n\n")
	writeFile.write("public class Main {\n\n")
	writeFile.write("	public static void main(String[] args) {\n\n")
	writeFile.write("		SimSettings.Builder settings = new SimSettings.Builder();\n")
	writeFile.write("		settings.N_BOTS("+ n_bots+");\n")
	writeFile.write("		settings.N_QUADCOPTERS("+ n_cops+");\n")
	writeFile.write("		settings.WAYPOINT_FILE(\""+way_file+".wpt\");\n")
	writeFile.write("		settings.OBSPOINT_FILE(\""+obs_file+".wpt\");\n")
	writeFile.write("		settings.INITIAL_POSITIONS_FILE(\""+int_file+".wpt\");\n")
	writeFile.write("		settings.MSG_MEAN_DELAY("+ mean_delay+");\n")
	writeFile.write("		settings.MSG_STDDEV_DELAY("+ std_delay+");\n")
	writeFile.write("		settings.MSG_LOSSES_PER_HUNDRED("+ loss_percent+");\n")
	writeFile.write("		settings.TIMEOUT("+ timeout+");\n")
	writeFile.write("		settings.DRAW(false);\n") #disable drawing
	writeFile.write("		settings.DRAWER(new LeaderElectDrawer());\n")
	writeFile.write("		Simulation sim = new Simulation(LeaderElectApp.class, settings.build());\n")
	writeFile.write("		sim.start();\n")
	writeFile.write("	}\n}")
	writeFile.close()
	return;
writeMain(argv[1],argv[2],argv[3],argv[4],argv[5],argv[6],argv[7],argv[8],argv[9])
	


