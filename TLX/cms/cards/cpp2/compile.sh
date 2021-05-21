#!/bin/bash

problem=cards
grader_name=stub

g++ -std=c++17 -o "${problem}" "${grader_name}.cpp" "assistant.cpp" "magician.cpp" -O2 -lm -Wall
