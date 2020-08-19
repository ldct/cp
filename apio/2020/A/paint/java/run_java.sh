#!/bin/bash

problem=paint

java -Xmx512M -Xss64M -jar "${problem}.jar" "grader"
