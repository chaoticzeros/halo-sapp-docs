Map Commands
==============

Map Cycle
---------

A map cycle puts the server on a continuous loop of games.
Using the SAPP map cycle is advantageous in that it’s non-volatile (the map cycle is saved into a file), you can edit the map cycle as it’s being
played, you can skip the map cycle, and you can automatically skip map cycle entries if there are too many or not enough players.

.. caution::
    Make sure your map cycle covers your entire possible range of players.
    If SAPP cannot find a game that can be loaded with the current number of players, the minimum or maximum player count may be ignored when picking the
    next game.

.. note:: Enabling the map cycle will disable map voting.

To set up your map cycle, you can edit your mapcycle.txt, or use SAPP’s map cycle commands.
This is how each line in mapcycle.txt file is formatted:

.. code-block::
  
  map:gamevariant:minimumplayers:maximumplayers

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Command Usage
     - Effect

   * - map_next
     - Start the next game in the mapcycle.

   * - map_prev
     - Start the previous game in the mapcycle.

   * - map_spec <index>
     - Skip the mapcycle to a certain point.

   * - mapcycle
     - Get a list of games in the map cycle and their indices.

   * - mapcycle_add <map><game variant>[minimum players][maximum players][index]
     - Insert a new mapcycle entry with a map and gametype variant.
       Optionally, the minimum players and maximum players can be added (by default they’re 0 and 16, respectively), and the game can also be inserted at a
       certain index, moving games at the index and afterwards after the index.

   * - mapcycle_begin
     - Begin the mapcycle from the beginning.

   * - mapcycle_del<index>
     - Remove a mapcycle entry.

   * - sapp_mapcycle[enabled]
     - This will enable SAPP’s mapcycle.
       *mapcycle_begin* will also automatically enable this if it isn’t already enabled.

       *Default: false*


Map Vote
--------

Similar to a map cycle, map voting puts the server on a continuous loop of games, but it also gives players the option to choose their next game.
The map vote is also non-volatile (it’s saved to a file, thus retained when the server is reloaded), and you can edit map votes as they’re being
played.

You can hide map voting entries if there are too many or not enough players.
This will only hide entries, thus the number of votes displayed will be reduced.

.. caution::
    Make sure your map vote covers your entire possible range of players.
    If SAPP cannot find a game that can be loaded with the current number of players, the minimum or maximum player count may be ignored when picking the
    next game.

.. note:: Enabling map voting will disable a running map cycle.

To set up map voting, you can edit your mapvotes.txt, or use SAPP’s map votes commands.
This is how each line in mapvotes.txt file is formatted:

.. code-block::
  
  map:gamevariant:name:minimumplayers:maximumplayers

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Command Usage
     - Effect

   * - mapvote [enabled]
     - Enable map voting at the end of each game.
       *Default: false*

   * - mapvote_add <map><game variant><name> [minimumplayers] [maximumplayers] [index]
     - Optionally, the minimum players and maximum players can be added (by default they’re 0 and 16, respectively), and the game can also be inserted at a
       certain index, moving games at the index and afterwards after the index.

   * - mapvote_del <index>
     - Delete a map vote entry.

   * - mapvotes
     - List map votes.

   * - max_votes [count]
     - This is the maximum displayed votes per round.
       However, if your map voting requires a certain number of players, then there may be less votes displayed if these games are unavailable.
       
       *Default: 5*