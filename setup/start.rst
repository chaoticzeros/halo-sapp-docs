Setup
=======


1. Move the files sapp.dll, strings.dll and the server executable (haloded.exe or haloceded.exe) to a
   safe location. This folder will function as your *Halo dedicated server folder*.


2. Create a text file named init.txt in this folder.
   This will act as the server init file. This is required for the dedicated server to function.
   You will need to customize it later. For now, use the following commands.


    .. code-block::
        :caption: init.txt

        sv_name "!!!@@@_dancing_warthogs_@@@!!!"

        load

3. Copy the "maps" folder from your Halo installation (or download) directory
   to your Halo dedicated server folder.


4. Run the dedicated server to initialize the SAPP files.
   Just run it once, then close it once you see SAPP load.

    Best practice would be to run it with the *-path* :ref:`command line argument <cmd>` as shown below. 
    Here we have selected the root folder (.) as the path:

        ``> haloceded.exe -path .``


    .. caution:: **It is highly recommended that you specify the path argument when running the server.**
          Otherwise your savegames, logs, and sapp folder will default to your documents folder and
          you will have trouble managing your files, since they are in two separate locations.
    
    .. tip:: You can setup a batch script or shortcut to do this efficiently. See :ref:`Launching`

5. Configure the server as explained in the following sections, and start the server again. Now you should be ready to go!


