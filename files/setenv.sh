#!/bin/sh
export JAVA_OPTS="$JAVA_OPTS\
  -server\
  -Xms6144m\
  -Xmx14336m\
  -Dcom.sun.management.jmxremote=true\
  -Dcom.sun.management.jmxremote.ssl=false\
  -Dcom.sun.management.jmxremote.access.file=/path/to/jmxremote.access\
  -Dcom.sun.management.jmxremote.password.file=/path/to/jmxremote.password\
  -Dcom.sun.management.jmxremote.authenticate=true"