Configuration
+++++++++++++

Server Initialization
======================

In order to use a dedicated server, you need to enter commands.
You can enter these commands, yourself, when the dedicated server starts, 
or you can have the dedicated server enter them for you for less of a hassle.
Using an init.txt file is *strongly* recommended.

.. note:: Your dedicated server has **two** init.txt files:
    One is opened when the Halo Dedicated Server starts up, located in the server folder.
    The other file is loaded when SAPP loads, located in the SAPP folder.

Server init.txt
-----------------

This file is opened when the server starts.
The Halo dedicated server (and client) can read init.txt files with LF (Unix) or CRLF (Windows) line endings.
Your server's init.txt file should contain the *load* command so SAPP can be loaded upon startup.

If SAPP is not loaded, the dedicated server will function as a normal dedicated server, with no SAPP features being available.
You may want to have a server name, specify max players, specify whether or not the server is public (broadcasts to lobby), a mapcycle timeout to
reduce time between games, and an rcon password.

.. caution:: You can place the *load* command anywhere in the init.txt file, but SAPP commands will not work unless SAPP is loaded.

.. code-block::
    :caption: Example Server init.txt

    sv_name "!!!@@@_dancing_warthogs_@@@!!!"
    sv_maxplayers 16

    sv_public 1

    sv_mapcycle_timeout 3 
    sv_rcon_password haloce42

    load




SAPP Configuration
===================

After starting up and loading SAPP for the first time, it
will create a number of files and folders ready to be edited. You do
not need to use or know all of the files for a working server.
You can use the *files* command to list these files.


.. _SAPP init.txt:

SAPP init.txt
------------------

This file contains commands that are loaded whenever SAPP is loaded, and it is automatically generated if it is nonexistent when SAPP has loaded.
Most settings in SAPP get destroyed when SAPP is unloaded.
Scripts also need to be loaded via commands; they do not automatically get loaded.
You can further customize SAPP by using many of its commands, then storing these customizations here so they are run every time SAPP is started.
These commands do not have to be SAPP commands.

*Avoid putting commands in here that will end the game, such as mapcycle_begin, sv_mapcycle_begin, sv_map, map, etc.
Players may become frustrated if the game ends prematurely when reloading SAPP.*

A very useful command to include here would be the *no_lead 1* command, to enable no- lead.
Some other useful commands would be *sapp_console 1* to override sv_status and *chat_console_echo 1* to see player chat messages in console.

 

.. code-block::
    :caption: Example SAPP init.txt
        
    no_lead 1

    sapp_console 1

    chat_console_echo 1




Map Cycle
------------

If you are going to use a mapcycle, using SAPP's mapcycle provides more control over when they are available, having some entries work only when a
certain number of players are in-game.
Halo's stock mapcycle is still another option.

Halo's mapcycle requires that you use *sv_mapcycle_add* for each map, then use *sv_mapcycle_begin*.

SAPP's mapcycle only requires that *mapcycle_begin* and *sapp_mapcycle 1* be used, while having the mapcycle stored in mapcycle.txt 
(see :ref:`Map Cycle` and :ref:`Map Vote` for information).


Other SAPP Files
------------------

.. note:: If you
  choose to utilize all of SAPP's features, you should keep your
  modifications as non-gameplay intrusive as possible, or else people
  may get frustrated when playing on your server. I will go over the
  uses of some of these files. 

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - File
     - Usage

   * - admins.txt
     - Stores v2 admin information.
       See :ref:`Admin Management`.

   * - alias.txt
     - Stores aliases of players with same CD hash.
       This requires  *collect_aliases* to be enabled.

   * - areas.txt
     - Stores areas from the *area* command.
       These areas are per-map.

   * - commands.txt
     - Stores custom commands.
       See :ref:`Custom Commands`

   * - events.txt
     - Stores events that run commands when specified requirements are met.
       See :ref:`Events`.

   * - init.txt
     - Stores commands that are executed when SAPP is loaded.
       Not to be confused with the init.txt in the server folder.
       See :ref:`SAPP init.txt`.

   * - ipbans.txt
     - Stores information of IP bans, such as length and time.
       See  :ref:`General Commands`.

   * - locations.txt
     - Stores locations from the *loc* command.
       These are per-map.

   * - lua (folder)
     - Stores lua scripts.
       These scripts can be loaded with the *lua load* command.
       See :ref:`Lua Scripting`

   * - mapcycle.txt
     - Stores your mapcycle.
       Begin the mapcycle with mapcycle_begin.
       See :ref:`Map Cycle`

   * - mapvotes.txt
     - Stores a list of games that players can vote on.
       See :ref:`Map Vote`

   * - sapp.log
     - Created when SAPP's logging feature is enabled.
       This file stores logs.

   * - users.txt
     - Stores v1 admin information.
       See :ref:`Admin Management`.