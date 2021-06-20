Naughty Commands
----------------

These commands can be used to directly modify various attributes of players, which may be useful for events, custom commands, and Lua scripts.
These commands cannot be used when *scrim_mode* is enabled, and all of them require the player to have level 4 admin access in order to use them.

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - **Command Usage**
     - **Effect**

   * - ammo <player_expr>[int_expr] [weapon]
     - Change a player’s weapon’s unloaded ammo.
       *Weapon* is the weapon with:  

       - 0 or unspecified = Current weapon  
       - 1 = Primary weapon  
       - 2 = Secondary weapon  
       - 3 = Tertiary weapon  
       - 4 = Quaternary weapon
       - 5 = All weapons

   * - area_add_cuboid<name> <a_x> <a_y><a_z> <b_x> <b_y><b_z>
     - Add a custom rectangular area.

   * - area_add_sphere<name> <x> <y> <z><r>
     - Add a custom spherical area.

   * - area_del <name>
     - Remove an area.

   * - area_list
     - List all areas for the loaded map.

   * - area_listall
     - List all areas for all maps.

   * - assists<player_expr>[int_expr]
     - Change a player’s assist count.

   * - battery<player_expr>[decimal_expr][weapon]
     - Change a player’s weapon’s battery, with the value.
       *Weapon* is the same as at the *ammo* command.

   * - boost <player_expr>
     - Moves a player to the location the player is looking at.

   * - camo <player_expr>[time]
     - Apply a camo to a player for an amount of ticks.
       This will have no effect if the player already has a camo.

   * - color <player_expr>[index]
     - Change a player’s FFA color.

   * - coord <player_expr>
     - Return the player’s coordinates.

   * - deaths<player_expr>[amount]
     - Change a player’s death count.

   * - disable_all_objects<team> <disable>
     - Disable all objects for a team, preventing all players on a team from using any objects.

   * - disable_all_vehicles<team> <disable>
     - Disable all vehicles for a team, preventing all players on a team from using any vehicles.

   * - disable_object<tag_path> [team]
     - Disable an object, optionally disabling for a specific team.
       Use tools like HMT or Eschaton to retrieve tag paths.

   * - disabled_objects
     - List all disabled objects.

   * - enable_object<index or tag_path>
     - Enable an object based on ID retrieved from disabled_objects, or based on a tag path.
       Use tools like HMT or Eschaton to retrieve tag paths.

   * - gamespeed [speed]
     - Change the ticks-per-second of the game.
       A tick normally lasts 1/30 of a second, but this command can change this to make the server faster or slower.
       
       **This setting requires that clients have HAC2 or Anticheat installed to sync automatically.**  
       **Values greater than 35 may result in networking issues for clients where the value has synced.**  
       **Values lower than 30 will result in unsynced clients visibly warping according to synced clients,
       effectively making all unsynced clients run at 30 ticks per second while everyone else runs at the slower speed of the server.**  
       
       *Default: 30.0*

   * - god <player_expr>
     - Enable invulnerability for a player.
       Use *ungod* to remove.

   * - gravity <float>
     - Set the server gravity in world units/tick\ :sup:`2`.
       By default, this is 0.003656.

       **This setting requires clients have Anticheat to sync automatically.**

   * - hp <player_expr>[decimal_expr]
     - Get or set the health for a player.

   * - kill <player_expr>
     - Kill the player.

   * - kills <player_expr>[int_expr]
     - Get or set the kills for a player.

   * - lag <player_expr>
     - Prevent the player from moving, resulting in them appearing to lag and warp back to a single spot.
       Use the *unlag* command to remove this effect from a player.

   * - loc_add<location_name>
     - Add a location to the location of the player.

   * - loc_add<location_name> <x><y> <z>
     - Add a location to an X/Y/Z coordinate.

   * - loc_del<location_name>
     - Delete a location.

   * - loc_list
     - List locations for the currently loaded map.

   * - loc_listall
     - List all locations for all maps.

   * - m <player_expr> <x><y> <z>
     - Teleport the player to a location relative to that player.

   * - mag <player_expr>[int_expr] [weapon]
     - Get or edit the ammo loaded in the player’s weapon.
       *Weapon* is the same as at the *ammo* command.

   * - nades <player_expr>[int_expr] [type]
     - Get or edit the amount of grenades that the player is holding.
       *Type* is the grenade type, with 1 being primary and 2 being secondary.
       If no grenade is specified, then both types of grenades are affected.

       **Although a player may have up to 127 grenades, grenade counts greater than 7 will not sync properly with clients.
       This may prevent the grenade counter from being displayed properly.
       Avoid using more than 7 grenades.**

   * - s <player_expr>[decimal_expr]
     - Get or edit the speed of the player.

   * - score <player_expr>[int_expr]
     - Get or edit the player’s score.

   * - sh <player_expr>[decimal_expr]
     - Get or edit the player’s shield.

   * - spawn <type><tag_path>[player_number][rotation]
     - Spawn an object at a player’s location.
       *Type* is the tag class.
       Use tools like HMT or Eschaton to retrieve tag paths.
       *Rotation* is in radians.

   * - spawn <type><tag_path>[location_name][rotation]
     - Spawn an object at a location.
       *Type* is the tag class.
       Use tools like HMT or Eschaton to retrieve tag paths.
       *Rotation* is in radians.

   * - spawn <type><tag_path> [<x> <y><z>] [rotation]
     - Spawn an object at an X/Y/Z coordinate, optionally providing rotation in radians.
       *Type* is the tag class.
       Use tools like HMT or Eschaton to retrieve tag paths.
       *Rotation* is in radians.

   * - st <player_expr>[red/blue]
     - Change the team of the player.
       Providing a team name will only change the player if they are on the team opposite to the provided team name.

   * - t <player_expr><location_name>
     - Teleport the player to a location.

   * - t <player_expr> <x><y> <z>
     - Teleport the player to an X/Y/Z coordinate.

   * - team_score[red/blue/both][int_expr]
     - Get or edit the score of a team or all teams.

   * - tp <player_expr><player_number>
     - Move the player to another player.

   * - ungod <player_expr>
     - Remove god mode from a player, if it’s enabled.

   * - unlag <player_expr>
     - Disable *lag* on a player.

   * - vdel <player_expr>
     - Delete all vehicle(s) that were assigned to the targeted player with the *spawn* command.

   * - vdel_all
     - Delete all vehicles that have been spawned with SAPP.

   * - venter<player_expr>[seat]
     - Force the player to enter the previously spawned vehicle.
       A player can be in multiple vehicles/seats.
       *Seat* is the index of the seat, with 1 usually being the driver’s seat.

   * - vexit <player_expr>
     - Force the player to exit all vehicles.

   * - wadd <player_expr>
     - Add the previously spawned weapon to the player’s inventory.

   * - wdel <player_expr><weapon>
     - Remove a weapon from the player’s inventory and delete it.
       *Weapon* is the weapon with:  
       
       - 0 = Current weapon  
       - 1 = Primary weapon  
       - 2 = Secondary weapon  
       - 3 = Tertiary weapon  
       - 4 = Quaternary weapon  
       - 5 or unspecified = All weapons

   * - wdrop <player_expr>
     - Drop the player’s currently held weapon.