.. _General Commands:

General Commands
----------------

These commands are intended to be used by administrators to moderate the server or otherwise don’t fall under the other categories.

.. list-table::
   :widths: 15 25 5
   :header-rows: 1


   * - Command Usage
     - Effect
     - Level

   * - afks
     - Display a list of AFK players.
     - 0

   * - b <player_expr>[reason] [time]
     - This command kicks and issues a ban on a player and announces this to the server.
       *Time* uses the same format as the *sv_ban* command.
     - 3

   * - balance_teams
     - Balance teams based on stats.
       This may not always make the teams even in player count.
     - 2

   * - bans
     - This command is equivalent to *sv_banlist*.
     - 3

   * - beep [Hz] [ms]
     - Play a beeping sound on the host.
       By default, this is 1000 Hz at 1000 milliseconds.
     - 4

   * - cpu
     - Display information about the server’s CPU, CPU load, memory usage, and operating system.
     - 4

   * - d <player_expr>
     - Display a player’s name, team, admin level, player table index, and machine index.
       If the player is alive, then also display the object address, object ID, shield, health, speed, invisibility info, as well as the player’s coordinates.
       If the player has a weapon, then also display the weapon address and weapon object ID, if in a vehicle then also the vehicle address and vehicle
       object ID.
     - 4

   * - files
     - Locate all SAPP txt files.
     - 4

   * - ipban <player_expr>[time] [reason]
     - Temporarily ban a player by IP.
       If ban time is 0 or no ban time is given, then the ban is indefinite.
     - 3

   * - ipbans
     - Display all IP bans and their indices.
     - 3

   * - iprangeban <name><IP range> [reason][time]
     - Ban an IP by range using CIDR IP addressing (X.X.X.X/YY).
       If no time is given, then the ban is indefinite.
       This may not immediately remove players from the server unless *full_ipban* is enabled.
     - 3

   * - ipunban <index>
     - Unban an IP.
     - 3

   * - inf <player_expr>
     - Display a player’s CD-key hash, IP address, and index.
     - 3

   * - k <player_expr>[reason]
     - This command kicks a player on a player and announces this to the server.
     - 2

   * - kdr <player_expr>
     - Display a player’s kill/death ratio.
     - 0

   * - log_note [message]
     - Make a note in SAPP’s log.
     - 4

   * - map <map><gametype>
     - This is an alias for *sv_map*.
     - 3

   * - maplist
     - This command is equivalent to *sv_maplist*, but displays maps in three columns.
     - 3

   * - mute <player_expr>[time]
     - Ban a player’s IP from the chat.
       If time is unspecified, the ban is indefinite.
       Mutes are volatile and are cleared when SAPP is reloaded.
     - 2

   * - mutes
     - List mutes.
     - 2

   * - unmute <index>
     - Remove a mute.
     - 2

   * - pl
     - This command is similar to *sv_players* just the players are ordered in multiple columns for better readability.
     - 2

   * - skips
     - List players who voted to skip the current map.
     - 0

   * - teamup
     - Group clan members together based on their name.
     - 2

   * - textban<player_expr>[time]
     - Ban a player’s CD-key from the chat.
       If time is unspecified, the ban is indefinite.
       Textbans are volatile and are cleared when SAPP is reloaded.
     - 2

   * - textbans
     - List textbans.
     - 2

   * - textunban <index>
     - Remove a textban.
     - 2

   * - uptime
     - Display how long the server and operating system have been running.
     - 0