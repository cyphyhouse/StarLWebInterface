package edu.illinois.mitra.demo.leaderelect;
import edu.illinois.mitra.starlSim.main.SimSettings;
import edu.illinois.mitra.starlSim.main.Simulation;

public class Main {

	public static void main(String[] args) {

		SimSettings.Builder settings = new SimSettings.Builder();
		settings.N_BOTS(3);
		settings.N_QUADCOPTERS(0);
		settings.WAYPOINT_FILE("x.wpt");
		settings.OBSPOINT_FILE("y.wpt");
		settings.INITIAL_POSITIONS_FILE("z.wpt");
		settings.MSG_MEAN_DELAY(15);
		settings.MSG_STDDEV_DELAY(5);
		settings.MSG_LOSSES_PER_HUNDRED(0);
		settings.TIMEOUT(0);
		settings.DRAW(false);
		settings.DRAWER(new LeaderElectDrawer());
		Simulation sim = new Simulation(LeaderElectApp.class, settings.build());
		sim.start();
	}
}