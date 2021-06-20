Memory Functions
----------------

These functions are used for directly reading/writing to Halo’s memory.
Functions here are not displayed in alphabetical order for logical reasons.

.. list-table::
   :widths: 15 30
   :header-rows: 1


   * - Function
     - Description

   * - safe_read
     - Enabling safe reading prevents segmentation fault when reading invalid addresses at a performance penalty.
       Read functions will also return nil upon failure.

       **Don’t use this unless necessary (which is never).
       If you think that this is the only way you can do something, then you are probably doing something wrong.**  **Takes:** boolean Enabled

   * - safe_write
     - Enabling safe writing prevents segmentation fault when writing to invalid addresses at a performance penalty.
       Write functions will also return false upon failure or true upon success.
       Read-only memory such as Halo’s instructions can also be written to when this is enabled, allowing one to modify Halo’s code.

       **The game may still crash or result in undefined behavior if you write invalid instructions to Halo’s memory (e.g. your name is Devieth).
       Make sure you undo your changes to Halo’s instructions when your script is unloaded.**  
       
       **Takes:** boolean Enabled

   * - read_bit
     - This function reads a bit from a byte at an address.
       Bits are the most basic unit of binary, and thus the possible values for bits are 0 or 1.

       **Takes:** number Address, number Bit  
       
       **Returns**\ *:* number Value

   * - write_bit
     - This function writes a bit to a byte at an address.
       Bits are the most basic unit of binary, and thus the possible values for bits are 0 or 1.
       
       **Takes:** number Address, number Bit, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_byte
     - This function reads an unsigned 8-bit byte at an address.
       Possible values range from 0 to 255.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number Value

   * - write_byte
     - This function writes to an unsigned 8-bit byte at an address.
       Possible values range from 0 to 255, and values outside of this range may overflow.
       
       **Takes:** number Address, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_char
     - This function reads a signed 8-bit byte at an address.
       Possible values range from -128 to 127, and values outside of this range may overflow.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number Value

   * - write_char
     - This function writes to a signed 8-bit byte at an address.
       Possible values range from -128 to 127, and values outside of this range may overflow.
       
       **Takes:** number Address, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_word
     - This function reads an unsigned 16-bit integer at an address.
       Possible values range from 0 to 65535, and values outside of this range may overflow.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number Value

   * - write_word
     - This function writes to an unsigned 16-bit integer at an address.
       Possible values range from 0 to 65535, and values outside of this range may overflow.
       
       **Takes:** number Address, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_short
     - This function reads a signed 16-bit integer at an address.
       Possible values range from -32768 to 32767, and values outside of this range may overflow.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number Value

   * - write_short
     - This function writes to a signed 16-bit integer at an address.
       Possible values range from -32768 to 32767, and values outside of this range may overflow.
       
       **Takes:** number Address, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_dword
     - This function reads an unsigned 32-bit integer at an address.
       Possible values range from 0 to 4294967295, and values outside of this range may overflow.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number Value

   * - write_dword
     - This function writes to an unsigned 32-bit integer at an address.
       Possible values range from 0 to 4294967295, and values outside of this range may overflow.
       
       **Takes:** number Address, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_int
     - This function reads a signed 32-bit integer at an address.
       Possible values range from -2147483648 to 2147483647, and values outside of this range may overflow.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number Value

   * - write_int
     - This function writes to a signed 32-bit integer at an address.
       Possible values range from -2147483648 to 2147483647, and values outside of this range may overflow.
       
       **Takes:** number Address, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_float
     - This function reads a 32-bit floating point number at an address.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number Value

   * - write_float
     - This function writes to a 32-bit floating point number at an address.
       
       **Takes:** number Address, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_double
     - This function reads a 64-bit double-precision floating point number at an address.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number Value

   * - write_double
     - This function writes to a 64-bit double-precision floating point number at an address.
       
       **Takes:** number Address, number Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*

   * - read_vector3d
     - This function reads three 32-bit floating point numbers at an address.
       
       **Takes:** number Address  
       
       **Returns**\ *:* number ValueX, number ValueY, number ValueZ

   * - write_vector3d
     - This function writes to three 32-bit floating point numbers at an address.
       
       **Takes:** number Address, number ValueX, number ValueY, number ValueZ  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is
       enabled)*

   * - read_string
     - This function reads an 8-bit null-terminated string at an address.
       
       **Takes:** number Address  
       
       **Returns**\ *:* string Value

   * - write_string
     - This function writes an 8-bit null-terminated string at an address.
       
       **Takes:** number Address, string Value  
       
       **Returns:** boolean Success *(segfaults on failure unless safe_write is enabled)*