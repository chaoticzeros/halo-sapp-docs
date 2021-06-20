Stock Halo Commands
-------------------

These commands are Halo’s stock commands.

While this list does not include devmode commands (cheat commands, debug commands, etc.), devmode is automatically enabled by SAPP on both versions of
the dedicated server rather than just Halo Custom Edition.

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Command Usage
     - Effect

   * - quit
     - This command closes the server application.

   * - sv_ban <player>[length]
     - Ban a player.
       Specifying a length will ban a player for that amount of time.
       Otherwise, the player will be banned indefinitely.

   * - sv_ban_penalty [1][2] [3] [4]
     - Display or specify the ban length for a certain number of teamkill bans.
       Up to four ban lengths can be specified before a permanent ban is given.

       *Default: 5m, 1d, 10d, 0 (indefinite)*

   * - sv_banlist
     - Display the ban list.

   * - sv_banlist_file
     - Locate the ban list file.

   * - sv_end_game
     - End the current game without starting a new game.

       **This command will remove all players from the server and prevent players from joining until a new game is started on the server.
       SAPP will try to restart its mapcycle, mapvote, and default Halo mapcycle (in this order) if there is one, or else the server will hang indefinitely.
       Use sv_map_next if you want to skip the current game.**

   * - sv_friendly_fire
     - Set friendly fire parameters.
       This overrides the game variant settings.
       Note that explosion-only friendly fire can only be toggled from the game variant.

       0 = Default (game variant)  1 = Off  2 = Shield only  3 = On  
       
       *Default: 0 (use game variant)*

   * - sv_gamelist
     - List all usable game variants in the savegames folder.
       This can be reloaded with the reload_gametypes command.

   * - sv_kick <player>
     - Remove a player from the game.

   * - sv_log_echo_chat[enabled]
     - Enable or disable chat echoing into the (non-SAPP) server log.

       **This command only works in Halo: Custom Edition.**  
       
       *Default: false*

   * - sv_log_enabled[enabled]
     - Enable or disable the (non-SAPP) server log.

       **This command only works in Halo: Custom Edition.**  
       
       *Default: false*

   * - sv_log_file [path]
     - Get or specify the path to the (non-SAPP) server log.

       **This command only works in Halo: Custom Edition.**  
       
       *Default: haloserver.log*

   * - sv_log_note[string]
     - Write a note into the (non-SAPP) server log.

       **This command only works in Halo: Custom Edition.**

   * - sv_log_rotation_threshold[KiB]
     - Get or specify the minimum file size (in kibibytes) before Halo renames the server log and creates a new one.

       **This command only works in Halo: Custom Edition.**  
       
       *Default: 4096*

   * - sv_map <map> <gamevariant>
     - Change the map and/or game variant.
       The use of this command will suspend any running map cycle and cancel SAPP’s map voting for the current game, if it was enabled.

   * - sv_map_next
     - End the current game, loading the next game.
       If the game is on a map cycle, it’ll load the next game.
       If map voting is enabled, that will take place.
       Otherwise, it’ll repeat the game.

   * - sv_map_reset
     - Reset the game, respawning all objects and players and clearing score, kills, deaths, and assists.

   * - sv_mapcycle
     - Display the current (non-SAPP) map cycle.

   * - sv_mapcycle_add<map> <gamevariant>
     - Add an entry to the (non-SAPP) map cycle.

   * - sv_mapcycle_begin
     - Start the (non-SAPP) map cycle from the beginning.

   * - sv_mapcycle_del <#>
     - Remove an entry from the map cycle.

   * - sv_mapcycle_timeout[time]
     - Gets or sets the time between games.
       Setting it to 0 or less will prevent the next game from being loaded, similar to sv_end_game, essentially kicking all players out.

       *Default: 10 seconds*

   * - sv_maplist
     - Displays all loaded maps.

   * - sv_maxplayers[players]
     - Get or set the maximum players.
       The maximum number of players is 16, and the minimum is 1.
       A warning is shown if the maximum players is set to 1.

       *Default: 16 players*

   * - sv_motd [motd.txt]
     - Specify a path for a text file for the server motd.

       **This command only works in Halo Custom Edition.**  
       
       *Default: “” (disabled)*

   * - sv_name [name]
     - Get or set the server name.
       The maximum character length is 63.

       *Default: “Halo”*

   * - sv_password[password]
     - Get or set the password in order to join the game.
       The maximum character length is 8.
       If players are in-game when a password is added or changed but not removed, they will be kicked after the game.

       *Default: “” (no password)*

   * - sv_players
     - Get a list of players and player indices which can be used in both Halo’s and SAPP’s commands.
       Other information such as team, ping, score, betrayals, and TK timer is also displayed here for each player.

   * - sv_public [public]
     - Set whether or not the server is allowed to broadcast to the master server.
       Making the server non-public effectively makes it a LAN server.

       *Setting sv_public to 0 is somewhat buggy in that it can can occasionally prevent players from joining.
       You’re better off setting a password if possible.*  
       
       *Default: true*

   * - sv_rcon_password[password]
     - Get or set the rcon password.
       The maximum character length is 8.

       *Default: “” (no password - rcon is disabled)*

   * - sv_single_flag_force_reset[enabled]
     - Get or set whether or not the flag can be reset when a player is holding the flag in single-flag games.

       *Default: false*

   * - sv_status
     - Display the current map, number of players, and maximum players.
       This command is automatically executed in the console periodically as the game is running.

   * - sv_timelimit
     - Get or set the time limit for future games in minutes.
       Setting it to 0 results in an indefinite time limit, while setting it to -1 uses the game variant settings.

       *Default: -1 (use game variant time limit)*

   * - sv_tk_ban [bans]
     - Get or set the number of team kills required for a player to be banned from the server.
       Ban length is determined by sv_ban_penalty.

       *Default: 4*

   * - sv_tk_cooldown[time]
     - Set the time required to wait before a player loses a TK point.

       *Default: 300s*

   * - sv_tk_grace [time]
     - Set the grace period between TK points.
     
       *Default: 3s*

   * - sv_unban <#>
     - Unbans a player and removes the player completely from the ban list, bypassing sv_ban_penalty.