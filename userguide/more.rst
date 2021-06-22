Additional Topics
===================

.. _cmd:

Command Line Arguments
------------------------

You can run the Halo CE dedicated server from a Windows command prompt or from a batch file. 
The following is a list of arguments you may use to start a Halo CE Dedicated server. 
You may use more than one command at a time:

.. code-block:: shell

   > haloceded.exe -argument [option]

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




.. _Launching:

Launching the Server with Arguments
-----------------------------------

It is recommended that you open the server with a batch script. Here's how to create one:

1. Open notepad (or any text editor)
2. Type in the needed commands. Note that we are using the root folder (.) as the path argument.

    .. code-block:: batch
      :caption: Example server.bat

        @echo OFF
        haloceded.exe -path . -port 2310

3. Save the file as server.bat in your Halo dedicated server folder. (Note that you need to save it as a .bat file, not a .txt file.)
4. You can start the server by running this file (or calling it from the command prompt).


.. Tip:: The same effect can be obtained by creating a shortcut to the server application and appending the arguments 
          to the shortcut's target field.

Updating SAPP
-------------

Whenever there is a new version, SAPP will attempt to automatically update to the latest version without interrupting the game.
It cannot update itself if you have no writing permissions to the server folder.
If this is the case (and you're on Windows), you should either run the server as an administrator or give yourself the Full Control permission to your
account for the server folder.

You can also manually update SAPP by using the unload command to unload SAPP and replace the older sapp.dll with the newer sapp.dll.
You can then use the load command to reload SAPP.