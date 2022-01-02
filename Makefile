SCXML_HOME := $(dir $(lastword $(MAKEFILE_LIST)))

init-local:
	conda env create -p $(SCXML_HOME)/python/scxml_build -f $(SCXML_HOME)/python/devtools/env.yml
