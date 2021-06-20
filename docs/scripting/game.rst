Game Functions
--------------

These functions are used for manipulating the Halo game as well as accessing various functions of SAPP.

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Function
     - Description

   * - add_var
     - This function creates a new custom event variable.
       Type can be:  0 = Global string  1 = Global integer  2 = Global float  3 = Player string  4 = Player integer  5 = Player float  **Takes:** string
       VariableName, number Type

   * - assign_weapon
     - This function assigned a weapon to a player.
       This function will fail if the player cannot accept the weapon.
       A player can have at most four weapons.
       **Takes:** number ObjectID, number PlayerIndex  **Returns:** boolean Success

   * - camo
     - This function applies active camouflage to a player for a specified number of ticks.
       If a player already has camo applied, then this function will not do anything.
       Note that there are 30 ticks in a second.
       **Takes:** number PlayerIndex, number Duration

   * - cprint
     - This function outputs a message to the console.
       **Takes:** string Message.
       optional number Color

   * - del_var
     - This function deletes a custom event variable.
       **Takes:** string VariableName

   * - destroy_object
     - This function deletes an object.
       Deleting critical items such as flags, oddballs, and vehicles not spawned by SAPP may crash the server or result in undefined behavior.
       **Takes:** number ObjectID

   * - drop_weapon
     - This function removes an object from the player’s hand and throws it onto the ground.
       **Takes:** number PlayerIndex

   * - enter_vehicle
     - This function forces a player to enter a vehicle.
       Players may be in multiple vehicles or seats at once.
       **Takes:** number VehicleID, number PlayerIndex, string Seat  **Returns:** boolean Success

   * - execute_command
     - This function executes a command, optionally on a player’s behalf.
       Setting Echo to true will raise EVENT_ECHO if there is any output from the command executed.
       **Takes:** string Command, optional number PlayerIndex, optional boolean Echo

   * - execute_command_sequence
     - This function executes a sequence of commands separated with semicolons, optionally on a player’s behalf.
       Setting Echo to true will raise EVENT_ECHO if there is any output from any of the commands that were executed.
       **Takes:** string CommandSequence, optional number PlayerIndex, optional boolean Echo

   * - exit_vehicle
     - This function forces the player to exit a vehicle.
       **Takes:** number PlayerIndex

   * - get_dynamic_player
     - This function retrieves the memory address of a player.
       This function will return *0* if the player is not currently alive.
       **Takes:** number PlayerIndex  **Returns:** number PlayerObjectAddress

   * - get_object_memory
     - This function retrieves the memory address of an object from its object ID.
       This function will return *0* if the object ID is invalid or the object no longer exists.
       **Takes:** number ObjectID  **Returns:** number ObjectAddress

   * - get_player
     - This function retrieves the static memory address of the player table entry.
       **Takes:** number PlayerIndex  **Returns:** number PlayerTableAddress

   * - get_var
     - This function retrieves an event variable or custom event variable.
       See *Event Variables* and *Custom Variables* for more information on these variables.
       PlayerIndex does not need to be valid if you are going to retrieve a global variable.
       **Takes:** number PlayerIndex, string Variable

   * - intersect
     - This function performs a collision check from a given point and a vector.
       The object with the *ObjectID* will be ignored during the collision check.
       It returns the coordinates of the intersection and an ObjectID of the object that was hit, or 0xFFFFFFFF if nothing was hit.
       **Takes:** number PointX, number PointY, number PointZ, number VectorX, number VectorY, number VectorZ, optional number ObjectID  **Returns:** boolean
       Success, number CollisionX, number CollisionY, number collisionZ, number CollisionObjectID

   * - kill
     - This function kills a player, adding one death and applying any necessary respawn time.
       **Takes:** number PlayerIndex

   * - lookup_tag
     - This function returns the memory address of a tag in the map using the tag’s class and path.
       **Use the alternative tag ID version of the lookup_tag function if you anticipate a protected map or a map where the tag path can for any reason
       vary.**  **If you want to look for tag paths/classes in a map file, use a modding tool such as HMT or Eschaton.**  **Takes:** string TagClass, string
       TagPath  **Returns:** number TagAddress

   * - lookup_tag
     - This function returns the memory address of a tag in the map using the tag’s ID.
       This is useful if you have an exact tag ID or you anticipate a protected map.
       **Tag IDs vary from map to map.
       You will need a way to find them, such as from HMT or reading Halo’s memory.
       Use the alternative tag class/path version of this function if you want to specify a class and path.**  **Tag paths and classes on unprotected stock
       maps generally remain the same.
       Use the alternative tag class/path version of the lookup_tag function if you do not anticipate the tag path varying.**  **Takes:** number TagID
       **Returns:** number TagAddress

   * - player_alive
     - This function returns *true* if the player is alive.
       **Takes:** number PlayerIndex  **Returns:** boolean PlayerAlive

   * - player_present
     - This function returns *true* if the player is present.
       **Takes:** number PlayerIndex  **Returns:** boolean PlayerPresent

   * - powerup_interact
     - This function assigns a powerup to a player.
       This may fail if the player powerup cannot affect the player.
       **Takes:** number ObjectID, number PlayerIndex  **Returns:** boolean Success

   * - rand
     - This function returns a random number.
       The minimum number is inclusive, and the maximum number is exclusive.
       If you don’t specify either value, then *minimum* is *0* and *maximum* (exclusive) is *2\ 31 (2147483648)*.
       **Takes:** optional number Minimum, optional number Maximum  **Returns:** number RandomNumber

   * - register_callback
     - This function registers an event callback.
       If the callback is already set, then it will be overwritten.
       See the *Event Callbacks* section below.
       Use the *cb* global table for a list of all of the callback numbers.
       **Example usage:** *register_callback(cb['EVENT_GAME_START'], "OnGameStart")*  **Takes:** number Callback, string CallbackFunctionName

   * - rprint
     - This function sends a message to a player’s console.
       **Takes:** number PlayerIndex, string Message

   * - say
     - This function sends the chat message to a specific player.
       **Takes:** number PlayerIndex, string Message

   * - say_all
     - This function sends the chat message to all players that are on the server.
       **Takes:** string Message

   * - set_var
     - This function sets an event variable to a value, returning false if the variable doesn’t exist.
       Variables placed in *Value* will also be substituted for their value, optionally using a player variable if *CopiedPlayerIndex* is also specified.
       **Takes:** number PlayerIndex, string VariableName, string Value, optional number CopiedPlayerIndex  **Returns:** boolean Success

   * - sig_scan
     - This function scans Halo’s executable code for the given byte signature.
       A byte signature is a string of bytes, and unknown bytes are ?? (e.g. "83EC??568BF0A0????????84C00F84").
       This function returns *0* if the signature wasn’t found.
       **Takes:** string Signature  **Returns:** number Address

   * - spawn_object
     - This function spawns an object at the specified coordinates.
       If TagID is specified, then TagType and TagPath are ignored.
       **Takes:** string TagType, string TagPath, optional number X, optional number Y, optional number Z, optional number Rotation, optional number TagID
       **Returns:** number ObjectID

   * - spawn_object_location
     - This function spawns an object at the specified location.
       If TagID is specified, then TagType and TagPath are ignored.
       **Takes:** string TagType, string TagPath, string Location, optional number Rotation, optional number TagID  **Returns:** number ObjectID

   * - spawn_projectile
     - This function spawns a projectile at the specified location, optionally with the specified rotation.
       **Takes:** number TagID, number ParentID, number LocX, number LocY, number LocZ, optional number RotX, optional number RotY, optional number RotZ
       **Returns:** number ObjectID

   * - sync_ammo
     - This function syncs loaded and unloaded ammo of a weapon.
       **Takes:** number ObjectID

   * - timer
     - This function creates a timer and executes a function after a delay.
       If the timer returns *true*, then the timer repeats.
       **Takes:** number Milliseconds, string FunctionName, optional string Arguments...

   * - to_player_index
     - This function converts a player table index (internally used by Halo [0-15]) to a player index (used by commands and Lua functions [1-16]).
       **Takes:** number PlayerTableIndex  **Returns:** number PlayerIndex

   * - to_real_index
     - This function converts a player index (used by commands and Lua functions [1-16]) to a player table index (internally used by Halo [0-15]).
       **Takes:** number PlayerIndex  **Returns:** number PlayerTableIndex

   * - unregister_callback
     - This function unregisters an event registered with the *register_callback* function (see *Event Callbacks* section).
       **Example usage:** *unregister_callback(cb['EVENT_GAME_START'])*  **Takes:** number Callback