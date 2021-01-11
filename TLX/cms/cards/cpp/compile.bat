@echo off

set problem=cards
set grader_name=stub

g++ -std=c++17 -o "%problem%" "%grader_name%.cpp" "%problem%.cpp" -O2 -lm -Wall
