#!/bin/bash

# Run a compositor
picom &

# Run background setter
nitrogen --restore &

# Run session locker
light-locker &
