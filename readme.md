DC Drop VMU Transfer Utility Fork 2023
======================================

Simple HTTP server that facilitates transfer of VMU saves from a Dreamcast to Dreampi or PC, and back to the Dreamcast.


Features
--------

* Transfers VMU saves from Dreamcast to computer (droppy.py)
* Decodes VMU save into a format suitable for emulators (decode.py)
* NEW: Transfer decoded VMU saves by downloading .VMI files back to your VMU (dload.py)


Usage
-----

Dreamcast must be connected to host computer with broadband adapter or modem.

* chmod +x *.py in dcdrop dir and launch droppy.py script. python droppy.py
* Using Dreamcast browser, navigate to the IP address of host i.e. http://192.168.0.2:8000
* Upload the VMU save, a file starting with tmp will be created.
* Use decode.py to convert that tmp file into a .VMI/.VMS files that will automatically go in the saves dir.
* Launch dload.py to get saves back on dreamcast VMU, or others that you downloaded. Just put the .VMI & .VMS in saves.
  * You'll have to quit out of droppy.py before launching dload.py.
  * Make sure you're selecting the .VMI file and not the .VMS file when downloading.


Notes
-----

I recommend using the Custom Planetweb 2.6x browser included in XPD Dreams which you can get at psilocybindreams.com.
It may work with other browsers but thats the only one I tested. It also comes with a handy VMS Utility for changing the copy flag from FF to 00 on stuff like PSOv2 saves. You'll have to do that that otherwise it won't show up in the upload form. 


Modem Connection
----------------

The Dreamcast can be connected to the host computer by connecting them together
using modems.  Please check the very useful guide linked below to connect your
Dreamcast to your host pc.

https://www.dreamcast-talk.com/forum/app.php/page/ryochanpart1

Also there is of course the wodnerful dreampi project, which is by far the easiest way to get your Dreamcast online with no BBA. 

https://dreamcastlive.net/shop/


Rationale
---------

I have a ton of great Street Fighter III 3rd Strike replays that I want to keep
for posterity.

Sometimes I just wanna use Flycast if I'm going to a friend's. This makes it easy to move the save file for my character back and fourth. 


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
Ally Cat, 2023

