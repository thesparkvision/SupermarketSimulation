# Supermarket Simulation

This project is a simulation of a supermarket checkout system.

## Installation

To run the supermarket simulation, you need to have Docker installed on your system. If you don't have Docker installed, you can download and install it from the official website: https://www.docker.com/get-started

Once Docker is installed, you can start the Docker container for the supermarket simulation by running the following command:

```bash
docker run -it --rm amanpandya712/supermarket-simulation /bin/bash
```

This command will start a Docker container with the necessary environment for running the simulation.

## Running the Commands

To run the simulation, execute the following command:

```bash
make run
```

To run the tests, execute the following command:

```bash
make test
```

To view the coverage report, execute the following command:

```bash
make coverage
```