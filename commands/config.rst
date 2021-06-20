Configuration Commands
----------------------

Most of these commands are used for configuring your server rather than being invoked by administrators (though administrators level 4, by default,
can still execute these commands).
These commands do not retain their settings when SAPP is reloaded, so use of the SAPP init.txt file is recommended.

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Command Usage
     - Effect

   * - admin_prefix<prefix>
     - This is the prefix inserted before messages made by administrators who are manually using the *say* command (rcon, console, or through chat commands).
       This differs from *msg_prefix* which is used when a script or event invokes the *say* command.

       *Default: \*\* ADMIN \*\**

   * - adminadd_samelevel[value]
     - Setting this will allow/disallow admins to add other V1 admins at certain levels using the *adminadd* command.

       0 = Admins cannot add other admins.
       1 = Admins can add admins to any lower level.
       2 = Admins can add admins to lower/equal levels.

       *Default: 0 (admins cannot add admins)*

   * - adminban [type]
     - Setting this will allow/disallow admins from banning another admin depending on the level of both admins.

       **This is no substitute for hiring non-abusive, trustworthy admins.**  
       
       0 = Admins can freely kick/ban other admins.
       1 = Admins cannot ban admins with a higher level.
       2 = Admins can only ban admins with a lower level.

       *Default: 0 (admins can ban admins)*

   * - admindel_samelevel[value]
     - Setting this will allow/disallow admins to remove other V1 admins at certain levels using the *admindel* command.

       **This is no substitute for hiring non-abusive, trustworthy admins.**  
       
       0 = Admins cannot delete admins.
       1 = Admins can delete admins of a lower level.
       2 = Admins can delete admins of lower/equal levels.

       *Default: 0 (admins cannot delete admins)*

   * - afk_kick [time]
     - Enabling this will automatically remove AFK players from the server after a specified amount of time.

       *Default: 0 (disabled)*

   * - aimbot_ban [length][type]
     - Enabling this will automatically kick and/or ban aimbotters for a specified length of time in minutes.

       0 = CD-hash ban  1 = IP ban  2 = CD and IP ban  3 = Kick  
       
       *Default: 0 minutes (disabled)*

   * - alias <player expr>
     - Search for an alias recorded in aliases.txt.

   * - anticamp [time][distance]
     - Enabling this will raise event_camp if a player has killed someone while camping a certain area (world units) for a number of seconds.
       1 world unit = 10 feet or ~3.048 meters  Forward speed (default) = 2.25 world units/second  
       
       *Default: 0 seconds (disabled)*

   * - anticaps [enabled]
     - Enabling this will prevent players from typing in excessive caps.

       *Default: false*

   * - anticheat [enabled]
     - Enabling this will require players to use SAPP’s anticheat.
       This command must be specified in SAPP’s init.txt and cannot be disabled.

       *Default: false*

   * - antiglitch[enabled]
     - Enabling this will automatically kill all players who have left the map’s BSP (the ground of the map).
       This is useful in maps such as Danger Canyon and Coldsnap to prevent players from glitching through the map, or when fall damage is disabled to
       prevent players falling forever.
       
       *Default: false*

   * - antihalofp[enabled]
     - Enabling this will IP ban (five minutes) people who attempt to join too often in a short amount of time.
       
       *Default: false*

   * - antilagspawn[enable]
     - Enabling this will prevent players from lag-spawning.
       
       *Default: false*

   * - antispam [type]
     - Enabling this will automatically mute players who send too many chat messages in a short amount of time on your server (spam).
       
       0 = Disabled  1 = CD-key (*textban*)  2 = IP-based (*mute*)  
       
       *Default: 0 (disabled)*

   * - antiwarp [warp_num]
     - Enabling this will raise event_warp if a player has warped warp_num times.
       
       *Default: 0 (disabled)*

   * - auto_update[enabled]
     - Enabling this will have SAPP automatically update when a new update is available.
       When SAPP updates, it will unload, interrupting events and scripts.
       The game itself will continue to function as SAPP is unloaded and loaded.
       
       *Default: true*

   * - network_thread[enabled]
     - Disabling this will prevent the server from being listed on the SAPP server list, disable map downloading and auto update, and disable Anticheat.
       This can be useful if the global Sapp server is down to prevent the server from hanging for up to 30 seconds when using the *reload* command.
       
       *Default: true*

   * - block_tc [enabled]
     - Enabling this blocks team changing, preventing players from changing to a more full team.
       
       *Default: false*

   * - chat_console_echo[enabled]
     - This command will toggle whether or not the chat is output into the console.
       This is recommended if you have access to your server’s console output.
       
       *Default: false*

   * - cmdstart1[character]
     - This is the prefix players and admins must place before commands if they wish to use commands from the chat instead of using rcon.
       
       *Default: “\”*

   * - cmdstart2[character]
     - This is an alternative prefix used before commands in chat.
       
       *Default: “/”*

   * - collect_aliases[enabled] [valid CDkeys only]
     - Enabling this will have aliases be collected into alias.txt.
       
       *Default: false*

   * - console_input[enabled]
     - Enabling this will allow the console to accept input.
       
       *Default: true*

   * - custom_sleep [ms]
     - This command will modify the amount of time Halo’s thread sleeps per cycle (ms).
       
       *Default: 8 (stock: 0)*

   * - disable_backtap[enabled]
     - When this is enabled, backtapping a player (hitting from the back) won’t kill them instantly.
       
       *Default: false*

   * - disable_timer_offsets[enabled]
     - Enabling this will spawn items on a fixed timer as defined by the map, similar to how spawn timers worked on the Xbox version of Halo rather than
       using an arbitrary counter.
       
       *Default: false*

   * - dns [url]
     - This value changes the master server address used when broadcasting.
       
       *Default (as of Halo PC 1.10): s1.master.hosthpc.com*

   * - full_ipban[enabled]
     - Enabling this will block all traffic from banned IPs instead of only server queries and join challenges.
       This may reduce performance with longer ban lists.
       
       *Default: false*

   * - hide_admin[enabled]
     - Enabling this will hide the name of admins who use kick or ban commands (k, b, etc.).
       This setting does not apply to vanilla Halo commands (sv_kick, etc.), which are always silent.
       
       *Default: false*

   * - hill_timer[int_expr]
     - Set the amount of time (in seconds) after the hill changes in the “Crazy King” gametype.
       
       *Default: 60*

   * - log [enabled]
     - Enabling this will log events into a log file.
       
       *Default: false*

   * - log rotation [kb]
     - Set the max log size (kB) before the log is archived.
       
       *Default: 4096*

   * - log_name [name]
     - Set the log file name.
       “.log” is appended.
       
       *Default: log*

   * - lua [enabled]
     - Enabling this will enable Lua scripting.
       
       *Default: false*

   * - lua_api_v
     - Display the current Lua API version.

   * - lua_call <script><function>[arguments…]
     - Manually call a function from <script>.lua.
       The script must be loaded, first.

       All arguments supplied through this command are passed as strings.
       Because SAPP’s lua scripting functions (e.g. timer()) are on set on the script’s global level, you can also use this command to call these functions,
       as well.

   * - lua_load <script>
     - Load <script>.lua if it’s not already loaded.
       This command will also call the script’s OnScriptLoad() function.

   * - lua_unload <script>
     - Unload <script>.lua if it’s not already unloaded.
       This command will also call the script’s OnScriptUnload() function, unregister all of the script’s callbacks, and disable all the script’s timers.

   * - map_skip [%]
     - Enable the use of the *skip* command, skipping when a certain percentage of people want the game to be skipped.
       
       *Default: 0 (disabled)*

   * - mapvote [enabled]
     - Enable map voting at the end of each game.
       
       *Default: false*

   * - max_idle [time]
     - SAPP will restart the mapcycle if the server idle for this many seconds.
       
       *Default: 60 seconds*

   * - max_votes [count]
     - This is the maximum displayed votes per round.
       However, if your map voting requires a certain number of players, then there may be less votes displayed if these games are unavailable.
       
       *Default: 5*

   * - motd [string]
     - Set the server motd.

   * - msg_prefix <string>
     - Set the prefix used in server messages.
       *Default: \*\* SAPP \*\**

   * - mtv [enabled]
     - Enable multi-team vehicles, allowing players to enter vehicles occupied by players in separate teams.
       
       **This will only sync for anticheat and HAC2 users.
       Players that cannot see the modification will lag and probably ragequit.**

   * - no_lead [enabled]
     - Enable no-lead mode.
       This will compensate for ping in terms of aiming.
       Players will not have to lead based on network latency.
       
       **Note that this command does not make ping a non-factor, as players will only see the game as it was <ping> ms ago.**  
       
       *Default: false*

   * - packet_limit[amount]
     - Set the maximum packets per second from an IP address.
       
       *Default: 1000*

   * - ping_kick [ping]
     - Kick players with pings exceeding this value (ms).
       
       *Default: 0 (disabled)*

   * - reload_gametypes
     - This will reload all game variants in the savegames folder, therefore you don’t need to restart the server to use newly created ones.

   * - remote_console[enabled]
     - Enabling this will enable the remote console.
       
       *Default: false*

   * - remote_console_list
     - List all connected remote console clients.

   * - remote_console_port[port]
     - Set the TCP port of the remote console.
       Using this command will require restarting the remote console to take effect.
       
       *Default: Port for the Halo server*

   * - sapp_console[enabled]
     - This will disable the periodic *sv_status* messages that is displayed every few seconds, instead displaying messages when a player leaves/joins or
       when a game begins.
       This is recommended if you have access to your server’s console output.
       
       *Default: false*

   * - sapp_mapcycle[enabled]
     - This will enable SAPP’s mapcycle.
       *mapcycle_begin* will also automatically enable this if it isn’t already enabled.
       
       *Default: false*

   * - sapp_rcon [enabled]
     - Enabling this will require rcon users to be admins.
       “v1” admins must use the rcon password set in sv_rcon_password.
       “v2” admins must use their passwords rather than the set rcon password.
       
       **If a v2 admin has a password that exceeds 8 characters, then that admin cannot use rcon.**  
       
       **This is not an excuse to use a weak rcon password, as
       rcon can be used by anyone when SAPP is unloaded (such as due to an update).
       If this is a problem, use a script that changes the rcon password to “” when the script is unloaded, then changes it back when SAPP is loaded again.**
       
       *Default: false*

   * - save_scores[enabled]
     - Enabling this will prevent a player’s score from being reset when the player leaves the server.
       
       *Default: false*

   * - say_prefix[enabled]
     - Enabling this will enable the \*\* SERVER \*\* prefix on server messages.
       This feature doesn’t work outside of Custom Edition.
       
       *Default: true*

   * - scorelimit[int_expr]
     - Get or edit the score limit for the current game.

   * - scrim_mode[enabled]
     - Enabling this will disable naughty commands and lua scripts while also disallowing sightjacking.
       
       *Default: false*

   * - set_ccolor [value]
     - You can set the console color.
       To calculate the color, add the foreground color to the background color multiplied by 16.
       
       **0123456789abcdef**

   * - setcmd <command><name/level>
     - This command will allow you to change either the name or the required admin level of (almost) any other SAPP commands or custom-defined command.

   * - sj_level [level]
     - This command will set the minimum level to use HAC2’s sightjacker on a server.
       
       *Default: -1 (everybody can use sightjacker)*

   * - spawn_protection[time]
     - Set the length of protection in seconds for a player to be invulnerable upon spawning.
       
       *Default: 0 (disabled)*

   * - timelimit[int_expr]
     - Get or edit the time limit on the fly in minutes.

   * - unlock_console_log<enabled>
     - The console becomes more chatty? It’s CE only.
       
       *Default: false*

   * - v [version]
     - View or modify the Halo version string.

   * - zombies [team]
     - This enables zombies medals for HAC2.
       
       0 = None 1 = Red 2 = Blue 
       
       *Default: 0 (none)*
