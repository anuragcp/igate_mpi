from mpi4py import MPI
import os
import cv2 as cv

def read_frame():
    try:
        cap = cv.VideoCapture(0)
        ret, frame = cap.read()
        return frame
    except cv.error as e:
        print("No camera module found...")
        return 0

def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
