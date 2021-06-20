Player Commands
---------------

Most of these commands are available to all players.
Commands in blue cannot have their levels or names modified with setcmd, nor can they be scripted with the *execute_command* function.

.. list-table::
   :widths: 15 25 5
   :header-rows: 1


   * - Command Usage
     - Effect
     - Level

   * - about
     - This command displays the current version.
     - -1

   * - afk
     - This command marks the player as AFK, disabling the player’s future respawns.
     - 0

   * - clead [ping]
     - This command has player lead at a certain ping rather than at 0 ping.
       *no_lead* has to be enabled and *lead* has to be disabled.
       *Default: 0 ms*
     - -1

   * - info
     - This command displays the server name, the number of players, the current map, and if scrim mode is enabled.
     - -1

   * - lead [enabled]
     - This command toggles leading when no-lead mode is enabled.
       *Default: false*
     - -1

   * - list[“generic/player/custom”]
     - List all commands available to the player.
     - -1

   * - login <password>
     - Log into a name and password based admin account.
     - -1

   * - report [message]
     - Report with a message.
       This command requires *anticheat* to be enabled.
     - -1

   * - stats
     - Show the player’s kills, deaths, and kill/death decimal.
     - -1

   * - stfu
     - Block messages received from the *say* command as well as scripted rcon messages.
     - -1

   * - sv_stats
     - Displays stats about the server, including query count, join attempts, executed command count, executed events count, games played, flags captured,
       kills, betrays, suicides, and chat message count.
       The data is cleared when SAPP is unloaded.
     - -1

   * - unstfu
     - Disables stfu.
       The reason for this command existing instead of just toggling stfu with /stfu 0 is unclear.
     - -1

   * - usage <command>
     - Get the usage for a specified command.
     - -1

   * - whatsnext
     - Get the next game in the mapcycle.
     - -1