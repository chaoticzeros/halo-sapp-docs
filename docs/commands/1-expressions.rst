Expressions
============

Player Expressions
------------------

Some commands have <player_expr> as an argument.
While you can use a player index here, you can also target multiple players, or players with a specific name.
Stock Halo commands do not support player expressions.

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Expression
     - Effect

   * - \*
     - This is a wildcard expression which matches any number of any characters.
       Using it by itself will match all players.

   * - me
     - This matches the player executing the command.

   * - rt
     - This matches all players on the red team.

   * - bt
     - This matches all players on the blue team.

   * - pl
     - This matches all non-admins.

   * - admin
     - This matches all admins.

   * - rand
     - This matches a random player.

   * - randred
     - This matches a random player on red team.

   * - randblue
     - This matches a random player on blue team.


Decimal and Integer Expressions
-------------------------------

In certain commands, some commands have <decimal_expr> and <int_expr>.
While you can simply set the value to whatever positive value you want (negative values require the : expression), using an expression can be useful
depending on what the goal is.

*<int_expr> is an integer value.
Some integers may have lower upper-bound limits due to the size of the integer.*

*<decimal_expr> is a float value and is a decimal, meaning 0.0 to 1.0.
One percent is equal to 0.01.*

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Expression
     - Effect

   * - :<number>
     - Set a value to an exact value.
       This is not required for positive values but is required for negative values.

   * - +<number>
     - Add a value to the current value.

   * - -<number>
     - Subtract a value from the current value.
       **If you are intending to set a value to a negative value, use the : expression.**

   * - \*<number>
     - Multiply the current value with a value.

   * - /<number>
     - Divide the current value with a value.

   * - %<number>
     - Set the remainder of the current value divided by the given value (modulo).