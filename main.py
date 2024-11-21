import arcade
import random

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Example"


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

        self.button_width = 150
        self.button_height = 40
        self.button_x = SCREEN_WIDTH // 2
        self.button_y = SCREEN_HEIGHT // 2 - 50
        self.button_color = arcade.color.GRAY

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        img = ":resources:images/animated_characters/male_person/malePerson_idle.png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for _ in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/items/coinGold.png",
                                 SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)

        if COIN_COUNT == self.score:
            arcade.draw_text(text="You win..",
                             start_x=SCREEN_WIDTH // 2 - 50,
                             start_y=SCREEN_HEIGHT // 2,
                             color=arcade.color.BLUE,
                             font_size=20,
                             anchor_x="center"
                             )

            arcade.draw_rectangle_filled(self.button_x, self.button_y,
                                         self.button_width, self.button_height,
                                         self.button_color)
            arcade.draw_text("Restart", self.button_x, self.button_y,
                             arcade.color.WHITE, font_size=14, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if (self.button_x - self.button_width / 2 < x < self.button_x + self.button_width / 2 and
                self.button_y - self.button_height / 2 < y < self.button_y + self.button_height / 2):

            self.setup()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
