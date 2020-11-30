#!/usr/bin/env bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
cd "$( cd -P "$( dirname "$SOURCE" )" && pwd )"

jre/bin/java -Xmx500M -Xms200M \
     -Xss16M \
     -DentityExpansionLimit=100000000 \
     -Dlogback.configurationFile=conf/logback.xml \
     -Dfile.encoding=UTF-8 \
     -XX:CompileCommand=exclude,javax/swing/text/GlyphView,getBreakSpot \
     -classpath bundles/guava.jar:bundles/logback-classic.jar:bundles/logback-core.jar:bundles/slf4j-api.jar:bin/org.apache.felix.main.jar:bin/maven-artifact.jar:bin/protege-launcher.jar \
     $CMD_OPTIONS org.protege.osgi.framework.Launcher $1



