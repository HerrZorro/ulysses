'''
Created on May 26, 2014

A Tile is a "piece of the board" and contains all the information for that part
of the game (movement, interaction, etc.) 
'''
import string
from enum import Enum, unique

    
# Commands as they may show up from the user input
_go = ["go", "walk", "run", "jog"]
_check = ["check", "look", "inspect", "touch"]
_alter = ["open", "lift", "move", "push", "pull"]


# Directions
_north = ["N", "n", "NORTH", "north", "North"]
_east = ["E", "e", "EAST", "east", "East"]
_south = ["S", "s", "SOUTH", "south", "South"]
_west = ["W", "w", "WEST", "west", "West"]


@unique
class Command(Enum):
    NONE = 1  # ERROR
    GO = 2  # Move the player
    CHECK = 3  # Inspect, look at, etc. an object
    ALTER = 4  # Open, move, lift, etc. an object
    

class CommandParser(object):
    '''
    Parses input for a starting command.  This converts all text to lower case.
    '''
    def __init__(self,
                 userInput: string):
        '''
        @param userInput: string
        '''
        split = userInput.lower().split(' ', 1)
        first = split[0]
        self.remainder = split[1]
        if first in _go:
            self.command = Command.GO
        elif first in _check:
            self.command = Command.CHECK
        elif first in _alter:
            self.command = Command.ALTER
        else:
            self.command = Command.NONE


class TileNeighbors(object):
    def __init__(self,
                 north = None,
                 east = None,
                 south = None,
                 west = None):
        '''
        @param north: Tile
        @param east: Tile
        @param south: Tile
        @param west: Tile
        '''
        self.north = north
        self.east = east
        self.south = south
        self.west = west


class Tile(object):
    '''
    Tile objects are any space on a map.  They display information about where
    the player currently is, where else the player may travel, and support
    handling specific commands.
    
    Sub-classes are responsible for handling any specifics related to the
    acceptable commands (i.e. "look at book" - "book" needs to be handled). The
    exception to this is the GO Command, which has all directions handled in
    this base class.
    
    @type neighbors: TileNeighbors
    '''
    neighbors = TileNeighbors
    
    def __init__(self,
                 neighbors: TileNeighbors = TileNeighbors()):
        '''
        @param neighbors: TileNeighbors
        '''
        self.neighbors = neighbors
        
    def description(self):
        directions = "\n\nYou may go "
        options = []
        if self.neighbors.north:
            options.append("north")
        if self.neighbors.east:
            options.append("east")
        if self.neighbors.south:
            options.append("south")
        if self.neighbors.west:
            options.append("west")
        directions = directions + (", ".join(options) if options else "nowhere")
        return self._description() + directions
    
    def parseAndHandleCommand(self,
                              userInput: string):
        '''
        @param userInput: string
        '''
        parser = CommandParser(userInput)
        return self.__handleCommand(parser.command, parser.remainder)
    
    def __handleCommand(self,
                        command: Command = Command.NONE,
                        content: string = ""):
        '''
        @param command: Command
        @param content: string
        '''
        if command == Command.GO:
            return self._handleGo(content)
        elif command == Command.CHECK:
            return self._handleCheck(content)
        elif command == Command.ALTER:
            return self._handleAlter(content)
        else:
            return "That is inconsequential"
            
    def _description(self):
        '''
        Subclasses should override this
        @rtype: string
        '''
        return "You appear to be in a void... The master creator has made a terrible mistake..."
    
    def _handleCheck(self,
                     content: string):
        '''
        Subclasses should override this
        @rtype: string
        '''
        return "There is nothing interesting about it"
    
    def _handleAlter(self,
                    content: string):
        '''
        Subclasses should override this
        @rtype: string
        '''
        return "It cannot be moved"
    
    def _handleGo(self,
                  content: string):
        '''
        No need to override this
        @type content: string
        @rtype: Tile
        '''
        direction = content.split(' ')[0]
        neighborTile = NoneTile(self)
        if direction in _north and self.neighbors.north:
            neighborTile = self.neighbors.north
        elif direction in _east and self.neighbors.east:
            neighborTile = self.neighbors.east
        elif direction in _south and self.neighbors.south:
            neighborTile = self.neighbors.south
        elif direction in _west and self.neighbors.west:
            neighborTile = self.neighbors.west
        return neighborTile
    

class NoneTile(Tile):
    '''
    This is the None (null) implementation, mainly to be used when moving.  If
    this Tile occurs, it is a result of improper movement and any direction will
    lead back to the previous tile.
    '''
    
    def __init__(self,
                 previous: Tile):
        '''
        @param previous: Tile
        '''
        neighbors = TileNeighbors(north = previous,
                                  east = previous,
                                  south = previous,
                                  west = previous)
        Tile.__init__(self,
                      neighbors = neighbors)
        
    def description(self):
        return self._description()
    
    def _description(self):
        return "There is nothing this way"


class TileMap(object):
    '''
    The TileMap is the collection of all tiles in their appropriate layout.
    
    @param current: Tile
    '''
    current = Tile(TileNeighbors())
    
    def __init__(self):
        pass
    
    def handleCommand(self,
                      userInput: string):
        '''
        This handles dealing with updating the current position while returning
        the appropriate information for the user.
        @param userInput: string
        '''
        result = self.current.parseAndHandleCommand(userInput)
        text = ""
        if isinstance(result, NoneTile):
            # User tried to move to a bad place
            text = result.description() + "\n\n"
        elif isinstance(result, Tile):
            # User has moved
            self.current = result
        else:
            text = result + "\n\n"
        return text + self.current.description()
        