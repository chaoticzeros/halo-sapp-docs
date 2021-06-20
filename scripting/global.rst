Global Variables
----------------

These are global variables provided by the SAPP API rather than functions.

.. list-table::
   :widths: 10 10 20
   :header-rows: 1


   * - Variable
     - Type
     - Description

   * - cb
     - table [string]
     - This is a table of callbacks.
       Refer to the Scripting Events section for each possible callback.

   * - halo_type
     - string
     - This is the version of Halo being used.
       “CE” is Halo Custom Edition and “PC” is the retail version of Halo.

   * - lua_api_version
     - string
     - This is the Lua API version being used on the server.

   * - pid
     - number
     - This is the process ID of the server.

   * - sapp_version
     - string
     - This is the SAPP version being used on the server.