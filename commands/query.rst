Query Packet Manipulation
-------------------------

SAPP allows you to add additional fields to the query packet received through Halo’s query’s system.

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Command Usage
     - Effect

   * - query_add <key><value>
     - Add an entry to the query string or overwrites an existing query value.

   * - query_del <index orname>
     - Remove an entry from the query string.

   * - query_list
     - List custom query entries.


To request a query packet, simply send “\query” to the server’s UDP port through a UDP socket.
Each entry is separated with backslashes with the first entry and every other entry after that being a key and the second entry with every other entry
after that being a value to its respective key.
These packets are often used with game tracking services and automatically-generated status images.