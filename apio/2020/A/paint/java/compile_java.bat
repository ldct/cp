set problem=paint

javac "grader.java" "%problem%.java"
jar cfe "%problem%.jar" "grader" *.class
