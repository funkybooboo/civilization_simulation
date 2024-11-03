import matplotlib as plot
from simulation import Simulation


def main():
    for _ in range(10):
        simulation = Simulation()
        stats = simulation.run()
        # TODO display stats


if __name__ == "__main__":
    main()
