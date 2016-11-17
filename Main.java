package edu.illinois.mitra.demo.leaderelect;
import edu.illinois.mitra.starlSim.main.SimSettings;
import edu.illinois.mitra.starlSim.main.Simulation;

public class Main {

	public static void main(String[] args) {

		SimSettings.Builder settings = new SimSettings.Builder();
		settings.N_BOTS(4);
		settings.N_QUADCOPTERS(3);
		settings.WAYPOINT_FILE("1.wpt");
		settings.OBSPOINT_FILE("2.wpt");
		settings.INITIAL_POSITIONS_FILE("2.wpt");
		settings.MSG_MEAN_DELAY(15);
		settings.MSG_STDDEV_DELAY(5);
		settings.MSG_LOSSES_PER_HUNDRED(0);
		settings.SIM_TIMEOUT(1000);
		settings.DRAW(false);
		settings.DRAWER(new LeaderElectDrawer());
		Simulation sim = new Simulation(LeaderElectApp.class, settings.build());
		sim.start();
	}
}