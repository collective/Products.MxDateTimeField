###############################################################################
##
## copyright	(c) Lovely Systems GmbH
## author:		Harald Friessnegger <friessnegger@lovelysystems.com>
## date:		2005/12
## id:			$Id: Makefile 18606 2006-01-10 11:33:33Z friessnegger $
##
##	This makefile is intended to be used for archetypes based plone product
##  development using ArchGenXML.
##  To run the tests make sure that the PloneTestCase product
##  (http://plone.org/products/plonetestcase) is installed
##	You may need to change the paths for the tools used below.
###############################################################################


###############################################################################
## PATHS
###############################################################################

## TOOLS
ArchGenXML = ArchGenXML.py
i18ndude = i18ndude

###############################################################################




###############################################################################
## Product specific settings
###############################################################################

## the name of the product folder
PRODUCT_NAME = MxDateTimeField


## filename of the poseidon uml model
MODEL_NAME = model.zuml
###############################################################################




all: test doc
	@echo "If the tests pass and the docs are created you should be fine"


doc:
	@${MAKE} -C docs all

test:
	@if [ $(INSTANCE_HOME) ]; then\
       $(INSTANCE_HOME)/bin/zopectl test --libdir=$(INSTANCE_HOME)/Products/$(PRODUCT_NAME) $(TEST) ;\
       echo "You may specify a certain test-module using make TEST=testDummy";\
    else\
       echo "please set 'INSTANCE_HOME'!";\
	fi


## removes compiled python and backup files
clean:
	@find . -name "*.pyc" -exec rm {} \;
	@find . -name "*~" -exec rm {} \;
	@find . -name "*.zuml.bak.*" -exec rm {} \;

## used to generate a product out of a poseidon file
generate:
	@cd .. ;\
	$(ArchGenXML) --message-catalog=NO $(PRODUCT_NAME)/model/$(MODEL_NAME) ;\
	cd -

