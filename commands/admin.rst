Admin Management
----------------

These commands are used for managing your server administrators.
With SAPP admins, you can allow your server administrators to use certain commands based on a tiered system of levels, and higher level admins can use
more commands.
In SAPP, there are two flavors of admins: CD-key based admins as well as admins based on profile name and password.

The use of these commands is completely optional if you want to exclusively use the vanilla rcon-password system without setting up any SAPP admins on
your server.
SAPP enables brute force protection to rcon, and temporarily sets the level of the player to 4 upon success.

CD-Key based Admin Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These admins are automatically authenticated upon joining the server based on CD-key hash and, optionally, their IP.
If your admin shares CD keys, then using an IP is recommended.

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **Command Usage**
     - **Effect**
     - **L eve l**

   * - adminadd <playerexpr> <level>[allowed IPranges…]
     - Add a CD-Key based admin.
       You can also provide any number of IP ranges which uses CIDR addressing.
       If you want to allow admins to use this command, you will need to configure the adminadd_samelevel command.
     - 0

   * - adminlevel <index><level>
     - Set a new level for a CD-Key based admin.
     - 0

   * - admindel <index>
     - Remove a CD-Key based admin.
       If you want to allow admins to use this command, you will need to configure the adminadel_samelevel command.
     - 0

   * - admins
     - Display a list of CD-Key based admins.
     - 4


Name and Password based Admin Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These admins must use the login command to be authenticated and must have the correct profile name and provide the correct password.
This system can be more secure than automatically authenticating the user, especially if a user uses the same PC as someone else.

Note that if someone steals your name, while they may not be able to log into your admin account, you will not be able to log into your own admin
account.
If you want protection against this, you will want a backup method of logging in.
Alternatively, you can create a script that kicks users with certain names who have not logged in after a period of time.

Name-based admins can also use remote console if it’s enabled on the server.

.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - **Command Usage**
     - **Effect**
     - **L eve l**

   * - admin_add <playerexpr> <password><level>
     - Add a name and password based admin.
     - 4

   * - admin_add_manually<name> <password><level>
     - Add a name and password based admin that is not present on the server.
     - 4

   * - admin_change_pw<index> <password>
     - Change a name and password based admin’s password.
     - 4

   * - admin_change_level<index> <level>
     - Change a name and password based admin’s level.
     - 4

   * - admin_del <index>
     - Delete a name and password based admin.
     - 4

   * - admin_list
     - List name and password based admins.
     - 4

   * - change_password<old password> <newpassword>
     - Change the password of the currently logged in name and password based admin.
     - 0

   * - login <password>
     - Log into a name and password based admin account.
       This command’s level and name cannot be modified with setcmd.
     - -1
