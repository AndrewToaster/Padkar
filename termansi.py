import platform
from typing import Final, Any, Union


class Terminal:
    """Contains functions for making ANSI CSI escape values relating to the terminal window"""

    MOVE_HOME: Final[str] = "\x9bH"
    REPORT_POSITION: Final[str] = "\x9b6n"

    @staticmethod
    def move_up(amount: int = 1):
        """Creates an ANSI CSI value for moving the cursor up

        :param int amount: The amount to move the cursor (default 1)
        :returns: ANSI CSI value for moving the cursor by the specified amount
        :rtype str:
        :except ValueError: If amount is smaller than 1
        """
        if amount < 1:
            raise ValueError("Amount must be a positive integer")

        return f"\x9b{amount}A"

    @staticmethod
    def move_down(amount: int = 1):
        """Creates an ANSI CSI value for moving the cursor down

        :param int amount: The amount to move the cursor (default 1)
        :returns: ANSI CSI value for moving the cursor by the specified amount
        :rtype str:
        :except ValueError: If amount is smaller than 1
        """
        if amount < 1:
            raise ValueError("Amount must be a positive integer")

        return f"\x9b{amount}B"

    @staticmethod
    def move_forward(amount: int = 1):
        """Creates an ANSI CSI value for moving the cursor forward

        :param int amount: The amount to move the cursor (default 1)
        :returns: ANSI CSI value for moving the cursor by the specified amount
        :rtype str:
        :except ValueError: If amount is smaller than 1
        """
        if amount < 1:
            raise ValueError("Amount must be a positive integer")

        return f"\x9b{amount}C"

    @staticmethod
    def move_back(amount: int = 1):
        """Creates an ANSI CSI value for moving the cursor back

        :param int amount: The amount to move the cursor (default 1)
        :returns: ANSI CSI value for moving the cursor by the specified amount
        :rtype str:
        :except ValueError: If amount is smaller than 1
        """
        if amount < 1:
            raise ValueError("Amount must be a positive integer")

        return f"\x9b{amount}D"

    @staticmethod
    def move_nextline(amount: int = 1):
        """Creates an ANSI CSI value for moving the cursor to the next line

        :param int amount: The amount of lines to move the cursor (default 1)
        :returns: ANSI CSI value for moving the cursor to the next line
        :rtype str:
        :except ValueError: If amount is smaller than 1
        """
        if amount < 1:
            raise ValueError("Amount must be a positive integer")

        return f"\x9b{amount}E"

    # noinspection SpellCheckingInspection
    @staticmethod
    def move_prevline(amount: int = 1):
        """Creates an ANSI CSI value for moving the cursor to the previous line

        :param int amount: The amount of lines to move the cursor (default 1)
        :returns: ANSI CSI value for moving the cursor to the next line
        :rtype str:
        :except ValueError: If amount is smaller than 1
        """
        if amount < 1:
            raise ValueError("Amount must be a positive integer")

        return f"\x9b{amount}F"

    @staticmethod
    def move_column(col: int = 1):
        """Creates an ANSI CSI value for moving the cursor to a specified column

        :param int col: The column to move the cursor to (default 1)
        :returns: ANSI CSI value for moving the cursor to the specified column
        :rtype str:
        :except ValueError: If col is smaller than 1
        """
        if col < 1:
            raise ValueError("Line must be a positive integer")

        return f"\x9b{col}G"

    @staticmethod
    def move_row(row: int = 1):
        """Creates an ANSI CSI value for moving the cursor to a specified row

        :param int row: The row to move the cursor to (default 1)
        :returns: ANSI CSI value for moving the cursor to the specified column
        :rtype str:
        :except ValueError: If row is smaller than 1
        """
        if row < 1:
            raise ValueError("Line must be a positive integer")

        return f"\x9b{row}d"

    @staticmethod
    def move_position(col: int = 1, row: int = 1):
        """Creates an ANSI CSI value for moving the cursor to a specified row and column

        :param int col: The column to move the cursor to (default 1)
        :param int row: The row to move the cursor to (default 1)
        :returns: ANSI CSI value for moving the cursor to the specified position
        :rtype str:
        :except ValueError: If col or row is smaller than 1
        """
        if col < 1:
            raise ValueError("Line must be a positive integer")
        if row < 1:
            raise ValueError("Line must be a positive integer")

        return f"\x9b{row};{col}H"

    @staticmethod
    def erase_to_end():
        """Creates an ANSI CSI value for erasing from the cursor until end of screen

        :returns: ANSI CSI value for moving the cursor to the specified position
        :rtype str:
        """
        return "\x9b0J"

    @staticmethod
    def erase_to_begin():
        """Creates an ANSI CSI value for erasing from the cursor until end of screen

        :returns: ANSI CSI value for erasing from the cursor until end of screen
        :rtype str:
        """
        return "\x9b1J"

    @staticmethod
    def erase_screen():
        """Creates an ANSI CSI value for erasing the entire screen

        :returns: ANSI CSI value for erasing the entire screen
        :rtype str:
        """
        return "\x9b2J"

    @staticmethod
    def erase_all():
        """Creates an ANSI CSI value for erasing the entire window

        ----

        May not work on all terminals

        :returns: ANSI CSI value for erasing the entire window
        :rtype str:
        """
        return "\x9b3J"

    @staticmethod
    def erase_row_to_end():
        """Creates an ANSI CSI value for erasing from the cursor to end of line

        ----

        Does not modify the position of the cursor

        :returns: ANSI CSI value for erasing from the cursor to end of line
        :rtype str:
        """
        return "\x9b0K"

    @staticmethod
    def erase_row_from_begin():
        """Creates an ANSI CSI value for erasing from the cursor to end of line

        ----

        Does not modify the position of the cursor

        :returns: ANSI CSI value for erasing from the cursor to end of line
        :rtype str:
        """
        return "\x9b1K"

    @staticmethod
    def erase_row():
        """Creates an ANSI CSI value for erasing the entire line

        ----

        Does not modify the position of the cursor

        :returns: ANSI CSI value for erasing the entire line
        :rtype str:
        """
        return "\x9b2K"

    @staticmethod
    def scroll_up(amount: int = 1):
        """Creates an ANSI CSI value for scrolling the window up

        :param int amount: The amount of lines to scroll the window (default 1)
        :returns: ANSI CSI value for scrolling the window up by the specified value
        :rtype str:
        :except ValueError: If amount is smaller than 1
        """
        if amount < 1:
            raise ValueError("Amount must be a positive integer")

        return f"\x9b{amount}S"

    @staticmethod
    def scroll_down(amount: int = 1):
        """Creates an ANSI CSI value for scrolling the window down

        :param int amount: The amount of lines to scroll the window (default 1)
        :returns: ANSI CSI value for scrolling the window down by the specified value
        :rtype str:
        :except ValueError: If amount is smaller than 1
        """
        if amount < 1:
            raise ValueError("Amount must be a positive integer")

        return f"\x9b{amount}T"


class GraphicMode:
    """Contains ANSI values for selecting graphic modes (SGR)

    Most these codes can be found at
    `Here (Wikipedia) <https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters>`_
    or
    `Here (Github Gist) <https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#colors--graphics-mode>`_

    ----

    Values beginning with **R_** are used to reset/disable the graphic mode
    """

    RESET: Final[str] = "\x9b0m"
    BOLD: Final[str] = "\x9b1m"
    R_BOLD: Final[str] = "\x9b22m"
    DIM: Final[str] = "\x9b2m"
    R_DIM: Final[str] = "\x9b22m"
    ITALIC: Final[str] = "\x9b3m"
    R_ITALIC: Final[str] = "\x9b23m"
    UNDERLINE: Final[str] = "\x9b4m"
    R_UNDERLINE: Final[str] = "\x9b24m"
    BLINK: Final[str] = "\x9b5m"
    NO_BLINK: Final[str] = "\x9b25m"
    REVERSE: Final[str] = "\x9b7m"
    R_REVERSE: Final[str] = "\x9b27m"
    HIDDEN: Final[str] = "\x9b8m"
    R_HIDDEN: Final[str] = "\x9b28m"
    STRIKETHROUGH: Final[str] = "\x9b9m"
    R_STRIKETHROUGH: Final[str] = "\x9b29m"
    RESET_FG: Final[str] = "\x9b39m"
    RESET_BG: Final[str] = "\x9b49m"
    RESET_COLOR: Final[str] = f"\x9b39;49m"


class Color256:
    """Contains methods for generating ANSI escape values for 8bit colors"""
    @staticmethod
    def fg(index: int):
        """Create a foreground color escape code for the specified RGB combination

        :param int index: Index of the color in the palette
        :returns: ANSI escape code for the specified 8bit color
        :rtype: str
        :except ValueError: If index falls outside the range of 0-255
        """
        if index > 255 or index < 0:
            raise ValueError("Index must be inside the range 0-255")
        return f"\x9b38;5;{index}m"

    @staticmethod
    def bg(index: int):
        """Create a background color escape code for the specified RGB combination

        :param int index: Index of the color in the palette
        :returns: ANSI escape code for the specified 8bit color
        :rtype: str
        :except ValueError: If index falls outside the range of 0-255
        """
        if index > 255 or index < 0:
            raise ValueError("Index must be inside the range 0-255")
        return f"\x9b48;5;{index}m"


class ColorRGB:
    """Contains methods for generating RGB ANSI escape values"""
    @staticmethod
    def assert_valid_color(red: int, green: int, blue: int):
        """Asserts if all components of a rgb combination fall within the range 0-255

        :param int red: RED component of the rgb combination
        :param int green: GREEN component of the rgb combination
        :param int blue: BLUE component of the rgb combination
        :returns: Nothing
        :except ValueError: If any of the values fall outside the range
        """
        if red > 255 or red < 0:
            ValueError("RED must be inside the range 0-255")
        if green > 255 or red < 0:
            ValueError("GREEN must be inside the range 0-255")
        if blue > 255 or red < 0:
            ValueError("BLUE must be inside the range 0-255")

    @staticmethod
    def fg(red: int, green: int, blue: int):
        """Create a foreground color escape code for the specified RGB combination

        :param int red: RED component of the rgb combination
        :param int green: GREEN component of the rgb combination
        :param int blue: BLUE component of the rgb combination
        :returns: ANSI escape code for the specified rgb combination
        :rtype: str
        :except ValueError: If any of the values fall outside the range of 0-255
        """
        ColorRGB.assert_valid_color(red, green, blue)
        return f"\x9b38;2;{red};{green};{blue}m"

    @staticmethod
    def bg(red: int, green: int, blue: int):
        """Create a background color escape code for the specified RGB combination

        :param int red: RED component of the rgb combination
        :param int green: GREEN component of the rgb combination
        :param int blue: BLUE component of the rgb combination
        :returns: ANSI escape code for the specified rgb combination
        :rtype: str
        :except ValueError: If any of the values fall outside the range of 0-255
        """
        ColorRGB.assert_valid_color(red, green, blue)
        return f"\x9b48;2;{red};{green};{blue}m"


class Color16FG:
    """Contains string constants for foreground colors in the 4bit range"""
    BLACK: Final[str] = "\x9b30m"
    RED: Final[str] = "\x9b31m"
    GREEN: Final[str] = "\x9b32m"
    YELLOW: Final[str] = "\x9b33m"
    BLUE: Final[str] = "\x9b34m"
    MAGENTA: Final[str] = "\x9b35m"
    CYAN: Final[str] = "\x9b36m"
    WHITE: Final[str] = "\x9b37m"
    BRIGHT_BLACK: Final[str] = "\x9b90m"
    BRIGHT_RED: Final[str] = "\x9b91m"
    BRIGHT_GREEN: Final[str] = "\x9b92m"
    BRIGHT_YELLOW: Final[str] = "\x9b93m"
    BRIGHT_BLUE: Final[str] = "\x9b94m"
    BRIGHT_MAGENTA: Final[str] = "\x9b95m"
    BRIGHT_CYAN: Final[str] = "\x9b96m"
    BRIGHT_WHITE: Final[str] = "\x9b97m"


class Color16BG:
    """Contains string constants for background colors in the 4bit range"""
    BLACK: Final[str] = "\x9b40m"
    RED: Final[str] = "\x9b41m"
    GREEN: Final[str] = "\x9b42m"
    YELLOW: Final[str] = "\x9b43m"
    BLUE: Final[str] = "\x9b44m"
    MAGENTA: Final[str] = "\x9b45m"
    CYAN: Final[str] = "\x9b46m"
    WHITE: Final[str] = "\x9b47m"
    BRIGHT_BLACK: Final[str] = "\x9b100m"
    BRIGHT_RED: Final[str] = "\x9b101m"
    BRIGHT_GREEN: Final[str] = "\x9b102m"
    BRIGHT_YELLOW: Final[str] = "\x9b103m"
    BRIGHT_BLUE: Final[str] = "\x9b104m"
    BRIGHT_MAGENTA: Final[str] = "\x9b105m"
    BRIGHT_CYAN: Final[str] = "\x9b106m"
    BRIGHT_WHITE: Final[str] = "\x9b107m"


class Utils:
    @staticmethod
    def vt_seq_win(enable: bool = True):
        from ctypes import byref, windll
        from ctypes.wintypes import DWORD
        kernel = windll.kernel32
        handle = kernel.GetStdHandle(-11)
        mode = DWORD(-1)

        if kernel.GetConsoleMode(handle, byref(mode)) == 0:
            raise WindowsError("GetConsoleMode returned 0")
        if mode.value == 0xFFFFFFFF:
            raise WindowsError("Invalid mode value received")

        if enable:
            kernel.SetConsoleMode(handle, mode.value | 0b111)
        else:
            kernel.SetConsoleMode(handle, mode.value & ~0b111)

    @staticmethod
    def get_cursor_position():
        """Reports the position of the cursor

        Coordinates are represented as row-major tuples of integers

        :returns: Coordinates of the cursors position
        """
        fwrite(Terminal.REPORT_POSITION)
        data = bytes()
        for _ in range(6):
            data += Utils.getch()
        return int(chr(data[2])), int(chr(data[4]))

    @staticmethod
    def getch() -> bytes:
        ...

    @staticmethod
    def is_key_avail() -> bool:
        ...


def fwrite(*values: Any, file: Union[Any, None] = None):
    """Proxy function for print, appends CSI (0x9b) to every value and prints them.
    Should be used for print ANSI escape sequences

    :param Any values: Tuple of all CSI values to be outputted into the terminal
    :param Any|None file: The output file to write to (default STDOUT)
    """
    print(*values, sep="", end="", file=file, flush=True)


def combine_modes(*modes: str) -> str:
    """Returns an SGM (SGR) string using the specified modes

    :param str modes: Collection of all modes to be formatted
    :returns: SGR escape value
    :rtype: str
    """
    return "\x9b" + ';'.join(map(lambda x: x[1:-1], modes)) + "m"


# Implement platform specific functions
if platform.system() == "Windows":
    import msvcrt
    Utils.getch = msvcrt.getch
    Utils.is_key_avail = msvcrt.kbhit
else:
    import tty
    import termios
    import sys
    import select

    def _linux_getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def _linux_is_key_avail():
        dr, dw, de = select.select([sys.stdin], [], [], 0)
        return dr != []

    Utils.getch = _linux_getch
    Utils.is_key_avail = _linux_is_key_avail
