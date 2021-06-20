Event Callbacks
---------------

Your functions are not required to take all of the variables or any of them, but if they do, they have to be in the same order.
Some of these events work identically to events in the event system.


.. caution::
  Look carefully at the variable types taken in some of these functions.
  Although some variables will always be numerical, sometimes they’re still provided as strings, mainly event callbacks based on the SAPP event system.
  Use tonumber() if you want to coerce a string value into a number.

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Callback (cbtable)
     - Description

   * - EVENT_ALIVE
     - This event is called every second a player is alive.
       This is the Lua equivalent of the *event_alive* event.
       **Takes:** number PlayerIndex

   * - EVENT_AREA_ENTER
     - This event is called when a player enters an area.
       This is the Lua equivalent of the *event_aenter* event.
       **Takes:** number PlayerIndex, string Area

   * - EVENT_AREA_EXIT
     - This event is called when a player exits an area.
       This is the Lua equivalent of the *event_aexit* event.
       **Takes:** number PlayerIndex, string Area

   * - EVENT_ASSIST
     - This event is called when a player gets an assist.
       This is the Lua equivalent of the *event_assist* event.
       **Takes:** number PlayerIndex

   * - EVENT_BETRAY
     - This event is called when a player team kills.
       This is the Lua equivalent of the *event_tk* event.
       **Takes:** number PlayerIndex, string VictimIndex

   * - EVENT_CAMP
     - This event is called when a camping player kills another player while the *anticamp* command is enabled.
       This is the Lua equivalent of the *event_camp* event.
       **Takes:** number PlayerIndex

   * - EVENT_CHAT
     - This event is called when a player has sent a message.
       Returning *false* will block the message.
       Possible values for Type:  0 = global chat  1 = team chat  2 = vehicle chat  **Takes:** number PlayerIndex, string Message, number Type  **Returns:**
       optional boolean Allow

   * - EVENT_COMMAND
     - This event is called when a player attempts to use a command (valid or not) through rcon or messages or when the console has issued a command
       (remotely or not).
       Returning *false* will block the command.
       Note that some Player Commands cannot be blocked.
       Possible values for Environment:  0 = sent through the console (RconPassword is nil)  1 = sent through rcon  2 = sent through chat (RconPassword is
       nil)  **Takes:** number PlayerIndex, string Command, number Environment, string RconPassword  **Returns:** optional boolean Allow

   * - EVENT_CUSTOM
     - This event is called when the *cevent* command is executed.
       This is the Lua equivalent of the *event_custom* event.
       **Takes:** number PlayerIndex, string EventName

   * - EVENT_DAMAGE_APPLICATION
     - This event is called when damage is applied to a player.
       Returning *false* will block the damage.
       Returning *true* will allow the damage and, with a second value, to change how much damage.
       **Takes:** number PlayerIndex, number Causer, number DamageTagID, number Damage, string CollisionMaterial, number Backtap  **Returns:** optional
       boolean Allow, optional number NewDamage

   * - EVENT_DIE
     - This event is called when a player dies.
       The causer can be either a player index, -1 if the player died to unknown causes, or 0 if the player was killed by a vehicle or AI.
       This is the Lua equivalent of the *event_die* event.
       **Takes:** number PlayerIndex, string Causer

   * - EVENT_ECHO
     - This event is called when *true* is passed to the Echo argument of either the *execute_command()* or the *execute_command_sequence()* functions.
       **Takes:** number PlayerIndex, string Message

   * - EVENT_GAME_END
     - This event is called when the game ends, but before the postgame carnage report is displayed.
       This is the Lua equivalent of the *event_end* event.

   * - EVENT_GAME_START
     - This event is called when the game begins.
       This is the Lua equivalent of the *event_start* event.

   * - EVENT_JOIN
     - This event is called when a player has finished joining the server.
       This event is called after *event_prejoin*, and values in the get_player() struct is valid at this point.
       This is the Lua equivalent of the *event_join* event.
       **Takes:** number PlayerIndex

   * - EVENT_KILL
     - This event is called when a player kills another player.
       This is the Lua equivalent of the *event_kill* event.
       **Takes:** number PlayerIndex, string VictimIndex

   * - EVENT_LEAVE
     - This event is called when a player disconnects from the server.
       This is the Lua equivalent of the *event_leave* event.
       **Takes:** number PlayerIndex

   * - EVENT_LOGIN
     - This event is called when a username and password based admin logs in.
       For more information on login, see the *Name and Password based Admin Management* section.
       This is the Lua equivalent of the *event_login* event.
       **Takes:** number PlayerIndex

   * - EVENT_MAP_RESET
     - This event is called when the *sv_map_reset* command has been executed.
       This is the Lua equivalent of the *event_reset* event.

   * - EVENT_OBJECT_SPAWN
     - This event is called when the server is attempting to spawn an object.
       *ParentObjectID* is 0xFFFFFFFF if the object is not owned by another object.
       *SappSpawning* is 1 if the object spawning was issued from SAPP, 0 if it was from Halo.
       Returning *false* will block the spawn, and returning *true* will allow the spawn, with a second value to change the tag ID that the object will be.
       **Takes:** number PlayerIndex, number TagID, number ParentObjectID, number NewObjectID, number SappSpawning  **Returns:** optional boolean Allow,
       optional number ReplacementTagID

   * - EVENT_PREJOIN
     - This event is called when a player joins, but players have not been notified yet.
       Values from *get_player()* are not valid yet.
       Kicking the player with *sv_kick* or *sv_ban* will prevent the player from successfully joining, and no join or exit notification will be visible to
       players in the game.
       This is the Lua equivalent of the *event_prejoin* event.
       **Takes:** number PlayerIndex

   * - EVENT_PRESPAWN
     - This event is called when a player has spawned, but players have not been notified yet.
       This can be useful for moving or rotating players before they spawn or changing armor color.
       This is the Lua equivalent of the *event_prespawn* event.
       **Takes:** number PlayerIndex

   * - EVENT_SCORE
     - This event is called when a player has scored a point.
       This is the Lua equivalent of the *event_score* event.
       **Takes:** number PlayerIndex

   * - EVENT_SNAP
     - This event is called when a player has snapped while aimbot banning has been enabled.
       This is the Lua equivalent of the *event_snap* event.
       **Takes:** number PlayerIndex, string SnapScore

   * - EVENT_SPAWN
     - This event is called when a player has finished spawning.
       Things like armor color can no longer be changed, and changing the player’s position will not appear instantly to the player.
       This is the Lua equivalent of the *event_spawn* event.
       **Takes:** number PlayerIndex

   * - EVENT_STICK
     - This event is called when a player has been stuck by an object such as a plasma grenade.
       *Object* is the object, *VictimObject* is the object that was stuck, and *Where* is the index of the body part that stuck.
       **Takes:** number PlayerIndex, number VictimIndex, number Object, number VictimObject, number Where

   * - EVENT_SUICIDE
     - This event is called when a player has committed suicide.
       This is the Lua equivalent of the *event_suicide* event.
       **Takes:** number PlayerIndex

   * - EVENT_TEAM_SWITCH
     - This event is called when a player has changed teams.
       This is the Lua equivalent of the *event_teamswitch* event.
       **Takes:** number PlayerIndex

   * - EVENT_TICK
     - This event is called every tick.
       One tick lasts 1/30 of a second.
       This is the Lua equivalent of the *event_tick* event.

   * - EVENT_VEHICLE_ENTER
     - This event is called when a player has entered a vehicle.
       This is the Lua equivalent of the *event_venter* event.
       **Takes:** number PlayerIndex

   * - EVENT_VEHICLE_EXIT
     - This event is called when a player has exited a vehicle.
       This is the Lua equivalent of the *event_venter* event.
       **Takes:** number PlayerIndex

   * - EVENT_WARP
     - This event is called when a player has warped more times than specified by the *antiwarp* command, if it’s enabled.
       This is the Lua equivalent of the *event_warp* event.
       **Takes:** number PlayerIndex

   * - EVENT_WEAPON_DROP
     - This event is called when a player has dropped a weapon.
       This is the Lua equivalent of the *event_wdrop*  **Takes:** number PlayerIndex, string WeaponSlot

   * - EVENT_WEAPON_PICKUP
     - This event is called when a player has picked up a weapon/grenade.
       WeaponType is “1” if a weapon or “2” if a grenade.
       If a grenade, then WeaponSlot is “1” if it’s a fragmentation grenade or “2” if a plasma grenade.
       This is the Lua equivalent of the *event_wpickup*  **Takes:** number PlayerIndex, string WeaponSlot, string WeaponType