Remote Console
==============

The remote console API allows you to remotely manage your servers without needing to use the server’s main console.
For your convenience, the remote console commands are listed twice: once in the Configuration Commands section and once here, in the Remote Console
section.

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - **Command Usage**
     - **Effect**

   * - remote_console[enabled]
     - Enabling this will enable the remote console.
       *Default: false*

   * - remote_console_list
     - List all connected players currently connected through the remote console.

   * - remote_console_port[port]
     - Set the TCP port of the remote console.
       Using this command will require restarting the remote console to take effect.
       *Default: Port for the Halo server*


The remote console uses the name and password based admin system where the password is MD5-hashed *(yes, I bugged him and he still stuck with MD5 for
backward compatibility)*.
Command permissions work as expected: level 2 admins can neither execute level 3 nor level 4 commands using the remote console.

**The rest of this section is a little bit more technical and is designed to help you create a remote console client.
If you just want to use remote console, there are pre-existing clients out there on sites like Open Carnage** (http://opencarnage.net).

**The SAPP site also has a web client:** http://halo.isimaginary.com/remote_console/

The remote console uses TCP, and every request is a JSON structure terminated with a single line feed character (\\n) and parsed upon receipt.

To do anything, the client has to log in, first.

Opcodes
-------

.. list-table::
   :widths: 5 15 10 20
   :header-rows: 1


   * - Opcode
     - Name
     -  Type
     - Fields

   * - 1
     - Login
     - Client
     - opcode: integer

       username: string

       password: string (md5 hashed)

   * - 1
     - Login (response)
     - Server
     - opcode: integer

       level: integer (-1 if unsuccessful)

   * - 2
     - Query
     - Client
     - opcode: integer

   * - 2
     - Query (response)
     - Server
     - opcode: integer

       anticheat: boolean

       blue_score: integer

       gametype: string

       map: string

       maxplayers: integer

       mode: string

       no-lead: boolean

       **players: table (not present if the server is empty)**

          -  assists: integer

          - betrays: integer

          - color: {red: integer, green: integer, blue: integer}

          - deaths: integer

          - index: integer

          - kills: integer

          - name: string

          - score: integer

          - suicides: integer

          - team: string

       red_score: integer

       running: boolean (equals false)

       sapp_version: string

       version: string

   * - 2
     - Query (response - idle server)
     - Server
     - opcode: integer

       anticheat: boolean

       no-lead: boolean

       running: boolean (equals false)

       sapp_version: string

       version: string

   * - 3
     - Query stats
     - Client
     - opcode: integer

   * - 3
     - Query stats (response)
     - Server
     - opcode: integer

       blue_score: integer

       players: table *(same as Query)*

       red_score: integer

   * - 3
     - Query stats (response - empty)
     - Server
     - opcode: integer

   * - 4
     - Query position
     - Client
     - opcode: integer

   * - 4
     - Query position (response)
     - Server
     - opcode: integer

       **players: table (not present if server is empty)**

          - index: integer

          - x: float

          - y: float

          - z: float

   * - 5
     - Console input
     - Client
     - opcode: integer

       command: string

   * - 5
     - Console input (response)
     - Server
     - opcode: integer

       ret: integer (-1 no permission, 0 failed, 1 success)

   * - 6
     - Console output
     - Server
     - opcode: integer

       text: string

   * - 7
     - Chat
     - Server
     - opcode: integer

       message: string

       type: integer (0 global, 1 team, 2 vehicle)

   * - 8
     - Player joined
     - Server
     - opcode: integer

       *The rest is the same as a player object in Query*

   * - 9
     - Player left
     - Server
     - opcode: integer

       index: integer

   * - 10
     - Team change
     - Server
     - opcode: integer

       integer: index

       team: integer (0 red, 1 blue)

   * - 11
     - New game
     - Server
     - opcode: integer

       gametype: string

       map: string

       mode: string

       teams: boolean

   * - 12
     - System status
     - Server
     - opcode: integer

       cpu_load: integer

       memory_load: integer

       my_cpu_load: integer


Note: **Bold** fields indicate variables that may not always be present.