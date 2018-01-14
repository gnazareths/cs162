class AbstractSimulation:
    def __init__(self, number_steps):
        self.number_steps = number_steps
        self.show_intermediate_steps = True

    def initialize_sim(self):
        pass

    def run_one_step(self):
        raise NotImplementedError

    def print_sim_state(self):
        pass

    def run(self):
        self.initialize_sim()
        for a in range(self.number_steps):
            self.run_one_step()
            if self.show_intermediate_steps:
                self.print_sim_state()
        if not (self.show_intermediate_steps):
            self.print_sim_state()


class CannonBall(AbstractSimulation):
    def __init__(self, number_steps, velocity, acceleration_m_per_s_s=None):
        super().__init__(number_steps)
        self.velocity = velocity

        if acceleration_m_per_s_s is None:
            self.acceleration_m_per_s_s = [0.0, -9.75]

    def initialize_sim(self):
        self.position = [0, 0]
        self.time = 0

    def run_one_step(self):
        self.time += 1

        self.position[0] = self.position[0] + self.velocity[0]
        self.position[1] = self.position[1] + self.velocity[1]

        self.velocity[0] = self.velocity[0] + self.acceleration_m_per_s_s[0]
        self.velocity[1] = self.velocity[1] + self.acceleration_m_per_s_s[1]

    def print_sim_state(self):
        print("At time {} the cannonball is at position {}".format(
            self.time, repr(self.position)))


cb = CannonBall(20, [50.125, 25.25])
cb.run()
