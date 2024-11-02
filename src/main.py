import matplotlib as plot
from Simulation import Simulation

def main():
    for _ in range(10):
        simulation = Simulation()
        stats = simulation.run()


if __name__ == "__main__":
    main()
