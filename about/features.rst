Core Features
++++++++++++++

By default, most of the features provided by SAPP are disabled and have to be manually
enabled. However, there are some improvements and bug fixes applied to Halo just by using
SAPP.


.. rubric:: Passive features

* Commands can be used from within the chat. The default prefix to execute a
  command is either ``\`` or ``/`` and can be changed by using the ``cmdstart1`` and ``cmdstart2``
  commands.

* Message of the Day is now instantly synchronized to all players when updated.
* Certain characters that could cause glitches are eliminated from player names.
* Some missing values are now correctly added to Halo’s query.
* Most ISO 8859-1 characters are allowed in the server name rather than just a limited
  number of ASCII characters.
* Rcon brute-force protection is enabled. After four failed attempts, a malicious player
  will be IP-banned from the server for an hour.

.. rubric:: SAPP features enabled by default
  
* Auto Update
* DoS protection

.. rubric:: Halo Bug Fixes

* Halo’s CPU usage is greatly reduced. This slightly improves network performance.
* A memory leak - Now Halo’s memory usage won’t keep growing forever.
* Combo messages (double kill, triple kill, killtacular) are properly announced
  during the entire game.
* Players will no longer remain in the server if they quit if fall damage has been
  removed.
* Network synchronized objects are now cleaned up properly, this fixes the issue
  when objects stuck in the map and players couldn’t spawn after a while in long
  games with intensive object spawning.