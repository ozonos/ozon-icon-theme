UUID=Ozon
INSTALLDIR=$(DESTDIR)/usr/share/icons/$(UUID)

all:

install: local

local: 
	#Create dir if not exist
	mkdir -p $(INSTALLDIR)

	#Clear dir from contents
	-rm -rf $(INSTALLDIR)/*

	#Copy new contents in
	cp -rf Ozon/* $(INSTALLDIR)

uninstall:
	#Uninstall atom-panel
	-rm -rf $(INSTALLDIR)

