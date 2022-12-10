import pyray
from game.shared.color import Color
from game.shared.point import Point


RED = Color(255, 0, 0)
BLACK = Color(0, 0, 0)

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._points = 0
        self._is_game_over = False
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
            self._handle_game_over(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

        #Fires Missile
        if pyray.is_key_down(pyray.KEY_SPACE) and self._is_game_over == False:
            missiles = cast.get_actors("missiles")
            for missile in missiles:
                missile.set_position(player.get_position())
                missile.set_velocity(Point(0, -1))    

        '''#Fires Missile
        for missile in missiles:
            if pyray.is_key_down(pyray.KEY_SPACE) and self._is_game_over == False:
                missile.set_position(player.get_position())
                missile.set_velocity(Point(0, -1))'''    
                   

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with objects.
        
        Args:
            cast (Cast): The cast of actors.
        """

        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        objects = cast.get_actors("objects")
        missiles = cast.get_actors("missiles")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        #Allows missiles to move
        for missile in missiles:
            missile.move_next(max_x, max_y)    
        
        #Allows objects to move
        for object in objects:
            object.move_next(max_x, max_y)
            #Player getting hit by an object triggers a game over
            if player.get_position().equals(object.get_position()):
                self._is_game_over = True
                cast.remove_actor("objects", object)
            #Missile hits object. Object destroyed. +One point.
            elif missile.get_position().equals(object.get_position()):
                self._points += 1
                cast.remove_actor("objects", object)
                
        banner.set_text(f"Score: {self._points}")
        
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    #Game over triggered:
    def _handle_game_over(self, cast):
        if self._is_game_over:
            player = cast.get_first_actor("players")
            objects = cast.get_actors("objects")
            message = cast.get_first_actor("messages")

            message.set_text("Game Over!")
            #Player sprite disappears by turning black
            #Tried using the remove actor method but I keep getting an error when doing so.
            player.set_color(BLACK)
            
            for object in objects:
                object.set_color(RED)

            