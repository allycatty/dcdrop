DC Drop VMU transfer utility Fork 2023
======================================

Simple HTTP server that facilitates transfer of VMU saves from a Dreamcast to Dreampi or PC, and back to the Dreamcast.


Features
--------

* Transfers VMU saves from Dreamcast to computer (droppy.py)
* Decodes VMU save into a format suitable for emulators (decode.py)
* NEW: Transfer decoded VMU saves by download .VMI back to VMU (dload.py)


Usage
-----

Dreamcast must be connected to host computer with broadband adapter or modem

* Launch droppy.py script
* Using Dreamcast browser disc, navigate to IP address of hosting computer
* Upload the VMU save
* A file starting with tmp will be created, use decode.py to convert that into a VMI/VMS file that will go in the saves dir.
* Launch dload.py to get saves back on dreamcast VMU, or others that you downloaded. Note you'll have to quit droppy.py. 


Notes
-----

I reccomend using the Custom Planetweb 2.6x browser included in XPD Dreams which you can get at psilocybindreams.com.
It may work with other browsers but thats the only one I tested. It also comes with a handy VMS Utility for changing the copy flag from FF to 00 on stuff like PSOv2 saves. You'll have to do that that otherwise it won't show up in the upload form. 


Modem Connection
----------------

The Dreamcast can be connected to the host computer by connecting them together
using modems.  Please check the very useful guide linked below to connect your
Dreamcast to your host pc.

http://www.dreamcast-scene.com/guides/pc-dc-server-guide-win7/


Rationale
---------

I have a ton of great Street Fighter III 3rd Strike replays that I want to keep
for posterity.


Acknowledgments
---------------

This script would not be possible without the efforts in 'droopy.py' by Pierre
Duquesne.  Thank you, and everyone in the Dreamcast community that has
published information on the VMU format.


Python Support
--------------

This fork was developed and tested with:
Linux dreampi 4.9.35-v7+, python 2.7


leif theden (bitcraft), 2012

