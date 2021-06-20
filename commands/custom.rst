Custom Commands
---------------

Custom commands allow one to execute a series of commands in one go.
This can be used for either convenience or additional server functionality.
One advantage to doing this is that only the custom command’s level is checked.
Almost any commands executed through a custom command can be used regardless of the player’s level.
Using custom events and using the *cevent* command can also be used to add additional logic.
Like events, custom commands are non-volatile and are stored in commands.txt.

The format for a line in commands.txt:

.. code-block::

 
   command_name *#argument1 #argument2...* ‘command1;command2;etc...’ *level*

Arguments function like variables, but require a pound sign (#) instead of a dollar sign ($).
Arguments and levels are not required, and your command will default to requiring level 4 if you do not specify a level.

You can also have SAPP add and remove commands with these commands:

.. list-table::
   :widths: 50 50
   :header-rows: 0


   * - **Command Usage**
     - **Effect**

   * - cmd_add <command>[arguments]<command sequence>[level]
     - This creates a new custom command and places it at the end of commands.txt.

   * - cmd_del <command>
     - This removes a command from commands.txt.


As an example of custom commands, custom variables, and custom event, let’s say you want to add a basic economy system without using any Lua scripts.
First, you’d want to set up the money variable in your SAPP init.txt:

.. code-block::

 
   ``var_add money 4``

What you’re doing here is creating a custom variable, an integer on the player scope.
These are initially blank or 0, but can be set later through the use of the var_set command, which can be useful if you intend to use the value later.
Refer to the *Custom Variables* section if you want to know more about custom variables.

Now, give players a small amount of cash for when the player joins the game.
Place this in your events.txt file:

.. code-block::

 
   ``event_join ‘var_set money 100 $n’``

Why don’t you also award them some points for when they score, too.

.. code-block::

   event_score ‘var_set money +50 $n; say $n “+50 ($money)”’

Next, you’ll need to add some custom events for this, which will serve as checking if the player has enough money to max out grenades, which you’ll be
selling for 100 points.
Refer to the *Custom Events* section if this isn’t familiar.

.. code-block::

 
   event_custom $ename=buynades $money<100 ‘say $n “Insufficient funds ($money)”’

   event_custom $ename=buynades $money>=100 ‘var_set money -100 $n; nades $n 4; say $n “Nades maxed ($money)”’

Lastly, we can add a command to get this custom event to be used.
Put this in your commands.txt file:

.. code-block::

 
   buynades ‘cevent buynades $n’ -1

What this will do is it’ll run the custom event *buynades*.
If the player’s *$money* variable is less than 100 (the price to refill nades to 4), it’ll tell the player that the item cannot be afforded and remind
the player of the current balance.
Otherwise, it’ll deduct 100 from the player’s $money variable, then set the player’s nade count to four fragmentation and plasma grenades.
The -1 means that all players can use it.

Custom events, custom commands, and custom variables are as powerful as SAPP gets before Lua scripting.
