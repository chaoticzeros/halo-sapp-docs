Initializing SAPP
=================

* Move the sapp.dll file, strings.dll file and the server executable (haloded.exe or haloceded.exe) to a
  safe location. This folder will function as your *Halo dedicated server folder*.



* Create a text file named init.txt in this folder.
  You will need to customize it later. For now place the following commands in it.


    .. code-block::
        :caption: init.txt

        sv_name "!!!@@@_dancing_warthogs_@@@!!!"

        load

* Copy the "maps" folder from your Halo installation directory (You can download it if not available)
  to your Halo dedicated server folder.


* Run the dedicated server to initialize the SAPP files.
  Just run it once, then close it once you see SAPP load.

    .. caution:: It is highly reccomended that you specify the path argument when running the server.
        Otherwise your savegames, logs, and sapp folder will default to your Documents folder and
        you will have trouble managing your files, since they are in two seperate locations. It is explained in detail below.






Command Line arguments
------------------------

You can run the Halo CE dedicated server from a Windows command prompt or from a batch file. 
The following is a list of arguments you may use to start a Halo CE Dedicated server. 
You may use more than one command at a time:

.. code-block:: 

   haloceded.exe -argument [option]

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - **Argument**
     - **Usage**

   * - **-?**
     - Lists all arguments.

   * - **-exec** path\\to\\init.txt
     - Use a init.txt that has a different path or name instead of the init.txt in the server folder.
       The default is the init.txt in the current directory.

   * - **-cpu** cpu-number
     - Have the dedicated server use a specific CPU (0 being first one).

   * - **-path** path\\to\\stuff
     - Specify the path to your savegames, logs, and sapp folder.
       The default path is the Halo or Halo CE folder in your My Games folder in your documents folder.
       Use.
       to refer to the the current directory.


Creating a Batch Script
------------------------

If you are specifying one of more of these arguments, you are better off with opening the server with a batch script.

1. Open notepad (or any text editro)
2. Paste in the following commands. Note that we are using . (root folder) as the path argument.

    .. code-block:: batch

        @echo OFF
        haloceded.exe -path .

3. Save the file as start.bat in your Halo dedicated server folder.
4. You can start the server by running this file.

Common Startup Errors
-----------------------

1. *Requested function "load" cannot be executed now.*

    The SAPP strings.dll file is not present.
    You need to make sure that SAPP's strings.dll is present, and not the Halo dedicated server's strings.dll file.

2. *Failed to load sapp.dll!*

   Check to make sure the sapp.dll file is in the server folder with the server executable.
   If it is, check to make sure it's the correct sapp.dll file and that your file permissions aren't preventing you from opening it.

3.  *### FAILED TO OPEN DATA-CACHE FILE.*
    
    You have not copied the maps folder to your Halo dedicated server folder.