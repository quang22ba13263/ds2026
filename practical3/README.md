# Practical Work 3: MPI File Transfer

## Description
This project implements a parallel file transfer system using the Message Passing Interface (MPI), upgrading from a previous TCP-based version. The system follows a Coordinator-Worker architecture to distribute file data across multiple processes.

## Prerequisites
To run this project, you need to have an MPI implementation (like OpenMPI or MPICH) and the `mpi4py` library installed.

**Ubuntu/Debian installation:**
```bash
sudo apt-get update
sudo apt-get install openmpi-bin libopenmpi-dev
pip install mpi4py

## Run with 4 processes
mpirun -np 4 python3 mpi_file_transfer.py --send-file <your_file_name>