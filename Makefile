UUID=Icons
INSTALLDIR=$(DESTDIR)/usr/share/icons/

all:

install: local

clear:
	#Clear Install Dir
	-rm -rf $(INSTALLDIR)Ozon
	-rm -rf $(INSTALLDIR)Ozon-Amber
	-rm -rf $(INSTALLDIR)Ozon-Blue
	-rm -rf $(INSTALLDIR)Ozon-Brown
	-rm -rf $(INSTALLDIR)Ozon-Green
	-rm -rf $(INSTALLDIR)Ozon-Grey
	-rm -rf $(INSTALLDIR)Ozon-Orange
	-rm -rf $(INSTALLDIR)Ozon-Purple
	-rm -rf $(INSTALLDIR)Ozon-Red
	-rm -rf $(INSTALLDIR)Ozon-Teal

local:
	#Create dir if not exist
	mkdir -p $(INSTALLDIR)

	clear

	#Copy new contents in
	cp -rf $(UUID)/* $(INSTALLDIR)

uninstall: clear
