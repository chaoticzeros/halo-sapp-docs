Events
------

Events allow for basic scripting without needing a full-sized Lua script.
It was introduced before Lua scripting, though both continue to be updated.

Events are placed in events.txt and each line has this format:

event_name *‘conditional statement 1’* *‘conditional statement 2...’* ‘command1;command2;etc...’

Quotations are not required except when spaces are being used in a section of the event (a conditional statement or the command sequence).
Conditional statements are optional, but can be used to add logic to your events.

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - **Command Usage**
     - **Effect**

   * - cevent <name>[player number]
     - Raises event_custom, setting $ename and optionally the player that triggered the custom event.
       Custom events can be used for additional logic, such as to add logic to custom commands.

   * - events
     - List all events and their indices.

   * - eventsdel <index>
     - Delete an event by its index.

   * - w8 <seconds>
     - Delay the current event by a specified number of seconds.
       **This command can only be executed by an event.**

   * - wait <milliseconds>
     - Delay the current event by a specified number of milliseconds.
       **This command can only be executed by an event.**


Event Types
~~~~~~~~~~~

There are numerous types of events.
Some of them have additional variables to them in addition to custom variables (next section).

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - **Event**
     - **Description**

   * - event_aenter
     - A player has entered a custom area.
       *$area - This is the area the player has entered.*

   * - event_aexit
     - A player has exited a custom area.
       *$area - This is the area the player has exited.*

   * - event_alive
     - A player is alive (executed every second).

   * - event_assist
     - A player has gained an assist.

   * - event_camp
     - A player has killed someone while camping.

   * - event_custom
     - The *cevent* command has been used.
       *$ename - This is the name specified in the first argument of cevent.*

   * - event_die
     - A player has died.
       *$killer - This is the index of the killer.
       -1 if “died”; 0 if killed by a non-player.*

   * - event_end
     - The game has ended.

   * - event_join
     - A player has joined.

   * - event_kill
     - A player has made a kill.
       *$killed - This is the index of the victim.*

   * - event_leave
     - A player has disconnected.

   * - event_login
     - An admin has logged in with the *login* command.

   * - event_prejoin
     - A player has joined, but players have not been notified yet.
       Consequently, kicking the player with sv_kick or sv_ban will remove the player from the game without notifying players.

   * - event_prespawn
     - A player has spawned, but players have not been notified yet.

   * - event_reset
     - *sv_map_reset* has been executed.

   * - event_score
     - A player has scored.

   * - event_snap
     - A player has snapped while aimbot banning is enabled.
       *$snapscore - Aimbot score gained from snapping.*

   * - event_spawn
     - A player has spawned.

   * - event_start
     - The game has started.

   * - event_suicide
     - A player died from suicide.

   * - event_teamswitch
     - A player has switched teams.

   * - event_tick
     - A tick has occurred.
       This is done once every 1/30 seconds.

   * - event_tk
     - A player has team killed.
       *$killed - This is the index of the victim.*

   * - event_venter
     - A player has entered a vehicle.

   * - event_vexit
     - A player has exited a vehicle.

   * - event_warp
     - A player has warped while antiwarp was enabled.\ *.*

   * - event_wdrop
     - A player has dropped a weapon.
       *$index - This is the index of the dropped weapon.*

   * - event_wpickup
     - A player has picked up a weapon.
       *$type* *- This is the type of object picked up.
       1 for weapon, 2 for grenade*  *$index - This is the index of the picked up weapon*


Event Variables
~~~~~~~~~~~~~~~

There are numerous variables used in events, and can also be retrieved using *get_var()* when doing Lua scripting.

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **Variable**
     - **Type**
     - **Description**

   * - $afk
     - Player
     - This is the number of seconds a player has been AFK.

   * - $app
     - Player
     - Bitfield.
       Application(s) the player is using client-side.

       - 0 = None
       - 1 = SAPP
       - 2 = Anticheat
       - 4 = HAC2
       - 8 = RefleX

   * - $assists
     - Player
     - This is the number of assists a player has.

   * - $blues
     - Global
     - This is the number of players on Blue Team.

   * - $bluescore
     - Global
     - This is the total score of Blue Team.

   * - $botscore
     - Player
     - This is the player’s total aimbot score.

   * - $campkills
     - Player
     - This is the total number of kills a player has made while camping.

   * - $combo
     - Player
     - This is the current kill combo count for a player.
       It is reset to 0 if the player hasn’t made any kills in the past four seconds.

   * - $deaths
     - Player
     - This is the number of times a player has died this game.

   * - $ffa
     - Global
     - This variable is 1 if the game is FFA, or it’s 0 if teams are enabled.

   * - $gt
     - Global
     - This is the current gametype (ctf, slayer, king, race, oddball).

   * - $hash
     - Player
     - This is the player’s CD key hash.

   * - $hp
     - Player
     - This is the player’s total health expressed as a decimal.

   * - $invis
     - Player
     - This is 1 if the player has an active camouflage.
       Otherwise it’s 0.

   * - $ip
     - Player
     - This is the IP:Port of the player.

   * - $kills
     - Player
     - This is the number of kills a player has made this game.

   * - $lvl
     - Player
     - This is the administrator level of the player.

   * - $map
     - Global
     - This is the currently loaded map.

   * - $mode
     - Global
     - This is the name of the game variant loaded (CTF, Team Slayer, etc.)

   * - $n
     - Player
     - This is the player’s index.

   * - $name
     - Player
     - This is the name of the player.

   * - $oteam
     - Player
     - This is the name of the player’s opposite team.

   * - $ping
     - Player
     - This is the ping of the player.

   * - $pn
     - Global
     - This is the number of players on the server.

   * - $rand
     - Global
     - This is a random number between 1 and 16.

   * - $reds
     - Global
     - This is the number of players on Red Team.

   * - $redscore
     - Global
     - This is the total score of Red Team.

   * - $running
     - Global
     - This variable is 1 if the game is running, 0 otherwise (aka before the first game is started or shortly after the *sv_end_game* command was executed).

   * - $score
     - Player
     - This is the player’s score.

   * - $sh
     - Player
     - This is the player’s shield expressed as a decimal.

   * - $streak
     - Player
     - This is the number of kills the player has made since respawning.

   * - $suicides
     - Player
     - This is the number of suicides the player has done this game.

   * - $svname
     - Global
     - This is the server name set with *sv_name*.

   * - $team
     - Player
     - This is the team of the player (red/blue).

   * - $ticks
     - Global
     - This is the number of ticks since the beginning of the match.

   * - $tk
     - Player
     - This is the number of team kills the player has made this game.

   * - $valid
     - Player
     - This indicates whether or not a player is using a valid CD-key.

   * - $x
     - Player
     - This is the player’s X coordinate.

   * - $y
     - Player
     - This is the player’s Y coordinate.

   * - $z
     - Player
     - This is the player’s Z coordinate.

Custom Variables
~~~~~~~~~~~~~~~~

Variables can also be created and modified through scripting or events.
Being able to store arbitrary values can be useful for increasing functionality.

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - **Command Usage**
     - **Effect**

   * - var_add <name><type>
     - This command creates a new custom variable.
       Type can be:  0 = Global string  1 = Global integer  2 = Global float  3 = Player string  4 = Player Integer  5 = Player float  Player variables are
       stored per-player and are cleared when the player exits the server.

   * - var_conv <name>
     - This command converts between integers and float variables.

   * - var_del <name>
     - Delete a custom variable.

   * - var_list
     - List all custom variables.

   * - var_set <name><value_expr>[player number]
     - This command sets a variable.
       Integer and float expressions can be used here.
       If a player variable is being modified, specify a player number.