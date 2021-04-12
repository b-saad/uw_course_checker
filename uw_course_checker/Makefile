# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3

# PROJECT_NAME defaults to name of the current directory.
PROJECT_NAME = $(notdir $(PWD))

# export such that its passed to shell functions for Docker to pick up.
export PROJECT_NAME

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY: test clean help

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL: help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo ''
	@echo 'Usage: make [TARGET] [EXTRA_ARGUMENTS]'
	@echo 'Targets:'
	@echo '  test     	run tests for applicaton'
	@echo '  clean    	remove created docker image'


# The ${} notation is specific to the make syntax and is very similar to bash's $() 
# This function uses pytest to test our source files
test:
	docker build -f Dockerfile.dev -t ${PROJECT_NAME} .	
	docker run -it --rm ${PROJECT_NAME} ${PYTHON} -m pytest --verbose
	

# Remove all stopped docker containers
clean:
	docker rmi $$(docker images '${PROJECT_NAME}' -a -q)   
