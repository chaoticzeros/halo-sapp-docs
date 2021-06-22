.. _Lua Scripting:

Lua Scripting
=============

Lua scripting is the most advanced method to customize your server available in SAPP.
For your convenience, the relevant commands are in both the *Configuration Commands* section and right here.
Lua scripts are placed in the lua folder.

.. note::
    Current Lua API version: 1.12.0.0

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Command Usage
     - Effect

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



.. caution::
    This section is not a Lua scripting tutorial.
    If you want to learn how to script in Lua, look up an actual Lua scripting tutorial.
    If you need inspiration for a script or otherwise some sort of an example script, or you need help on a script you are currently making or plan to
    make, check out some of the existing scripts that have been released on the SAPP site’s forum or on the Open Carnage website.

A skeleton Lua script with everything required looks like this:


.. code-block:: lua

   api_version = "1.12.0.0"

   function OnScriptLoad()

   -- Put initialization code here.

   end

   function OnScriptUnload()

   -- Put cleanup code here.

   end

   function OnError(Message)

   -- This function is not required, but if you want to log errors, use this.

   end


One important detail to take into consideration when you write your scripts is that while the Lua script is evaluated before it’s loaded, the SAPP API
functions do not become available until *OnScriptLoad()* is called, which is when the script is loaded with *lua_load*.
If you need to initialize any global variables with SAPP API functions upon loading the script, you will need to do it in OnScriptLoad() or any
function called by this function.


.. toctree::
    
    game
    memory
    event
    global