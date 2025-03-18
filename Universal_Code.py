import simplegui
import random

# Constants
WIDTH = 500
HEIGHT = 500
PLAYER_SPEED = 5
FRAME_COUNT = 6
FRAME_DELAY = 5
SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128
DISPLAY_SIZE = (100, 100)

# Loading backgrounds and sounds
WELCOME_SCREEN = simplegui.load_image("https://i.imgur.com/Zhl2jMw.jpeg")
START_BUTTON = simplegui.load_image("https://i.imgur.com/MqgJtv8.png")
BACKGROUND = simplegui.load_image("https://i.imgur.com/DudAEjc.png")
BKG_2 = simplegui.load_image("https://i.imgur.com/O671jzf.jpeg")
BACKGROUND_MUSIC = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")

# Loading sprites and animations (player and enemy)
IDLE_IMAGE = simplegui.load_image("https://i.imgur.com/Xq9mtbz.png")
RUN_IMAGE = simplegui.load_image("https://i.imgur.com/NAhLOeo.png")
ENEMY_IDLE_IMAGE = simplegui.load_image("https://i.imgur.com/atp0eco.png")
ENEMY_RUN_IMAGE = simplegui.load_image("https://i.imgur.com/QomI2XQ.png")
IDLE_FLIPPED = simplegui.load_image("https://i.imgur.com/LMXaTlK.png")
RUN_FLIPPED = simplegui.load_image("https://i.imgur.com/J8DS6FF.png")
ENEMY_IDLE_FLIPPED = simplegui.load_image("https://i.imgur.com/pxSuood.png")
ENEMY_RUN_FLIPPED = simplegui.load_image("https://i.imgur.com/n8hPFhE.png")

# Getter methods for backgrounds
BACKGROUND_WIDTH = BACKGROUND.get_width()
BACKGROUND_HEIGHT = BACKGROUND.get_height()
BKG_2_WIDTH = BKG_2.get_width() 
BKG_2_HEIGHT = BKG_2.get_height()

class Welcome:
    
    def draw(canvas):
        img_width = WELCOME_SCREEN.get_width()
        img_height = WELCOME_SCREEN.get_height()
        canvas.draw_image(WELCOME_SCREEN, (img_width // 2, img_height // 2), 
                              (img_width, img_height), 
                              (WIDTH/ 2, HEIGHT /2), (WIDTH, HEIGHT))

        button_width = START_BUTTON.get_width()
        button_height = START_BUTTON.get_height()
        
        canvas.draw_image(START_BUTTON, (button_width // 2, button_height // 2), 
                              (button_width, button_height), 
                              (WIDTH/ 2, HEIGHT /1.25), (80, 40))
        
        
    def welcome_click(pos):
        
        
        if ((WIDTH/2 - 40 <= pos[0] <= WIDTH/2 + 40) and (HEIGHT/1.25 - 20 <= pos[1] <= HEIGHT/1.25 + 20)):
            frame.set_draw_handler(Update.draw)
            frame.set_keydown_handler(Keys.keydown)
            frame.set_keyup_handler(Keys.keyup)
            frame.set_mouseclick_handler(Update.click)

    
    
    
    
class Player:
    def __init__(self, x, y, speed, health, name, AP, DM):
        self.pos = [x, y]
        self.speed = speed
        self.is_moving = False
        self.facing_right = True
        self.frame_index = 0
        self.frame_timer = 0
        self.keys = {"left": False, "right": False, "up": False, "down": False}
        self.health = health
        self.name = name
        self.AP = AP
        self.DM = DM
   
    def move(self):
        """Update player position based on key presses."""
        
        collStat = Backgrounds.check_collision(self.pos)
        
        if self.keys["left"] and not('left' in collStat):
            self.pos[0] = self.pos[0] - self.speed
            self.facing_right = False
        if self.keys["right"] and not('right' in collStat):
            self.pos[0] = self.pos[0] + self.speed
            self.facing_right = True
        if self.keys["up"] and not('up' in collStat):
            self.pos[1] = self.pos[1] - self.speed
        if self.keys["down"] and not('down' in collStat):
            self.pos[1] = self.pos[1] + self.speed
        
        self.is_moving = any(self.keys.values())

    def update_animation(self):
        """Update frame index for animation."""
        self.frame_timer += 1
        if self.frame_timer >= FRAME_DELAY:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % FRAME_COUNT

    def draw(self, canvas, camera_x, camera_y):
        """Draw player sprite."""
        sprite_image = RUN_IMAGE if self.is_moving else IDLE_IMAGE
        if not self.facing_right:
            sprite_image = RUN_FLIPPED if self.is_moving else IDLE_FLIPPED
        
        frame_x = (self.frame_index * SPRITE_WIDTH) + (SPRITE_WIDTH / 2)
       
        canvas.draw_image(sprite_image, 
                          (frame_x, SPRITE_HEIGHT / 2), 
                          (SPRITE_WIDTH, SPRITE_HEIGHT), 
                          (WIDTH // 2, HEIGHT // 2), 
                          DISPLAY_SIZE)
    def get_p(self):
        return self.pos
    
class Enemy:
    def __init__(self, x, y, speed, health, name, AP, DM, player, xVar, yVar):
        self.player_pos = player.get_p()
        self.pos = [x+ xVar, y+ yVar]      
        self.movement = [0 + xVar,0 + yVar]
        self.is_moving = False
        self.facing_right = True
        self.speed = speed
        self.frame_index = 0
        self.frame_timer = 0
        self.keys = {"left": False, "right": False, "up": False, "down": False}
        self.health = health
        self.name = name
        self.AP = AP
        self.DM = DM
        
    def enemy_move(self, player):
        self.player_pos = player.get_p()
        distance = ((self.player_pos[0] - self.pos[0])**2 + (self.player_pos[1] - self.pos[1])**2)**0.5
        self.is_moving = True
        collStat = Backgrounds.check_collision(self.pos)
        
        if distance > 200:
            self.is_moving = False
            
        if (self.player_pos[0] < self.pos[0]) and distance < 200 and not('left' in collStat):
            self.movement[0] -= self.speed
            self.pos[0] -= self.speed
            self.facing_right = False
           
            
        if (self.player_pos[0] > self.pos[0]) and distance < 200 and not('right' in collStat):
            self.movement[0] += self.speed
            self.pos[0] += self.speed
            self.facing_right = True
            
        if (self.player_pos[1] < self.pos[1]) and distance < 200 and not('up' in collStat):
            self.movement[1] -= self.speed
            self.pos[1] -= self.speed
        
        if (self.player_pos[1] > self.pos[1]) and distance < 200 and not('down' in collStat):
            self.movement[1] += self.speed
            self.pos[1] += self.speed

    def update_animation(self):
        """Update frame index for animation."""
        self.frame_timer += 1
        if self.frame_timer >= FRAME_DELAY:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % FRAME_COUNT

    def draw(self, canvas, camera_x, camera_y):
        """Draw player sprite."""
        sprite_image = ENEMY_RUN_IMAGE if self.is_moving else ENEMY_IDLE_IMAGE
        if not self.facing_right:
            sprite_image = ENEMY_RUN_FLIPPED if self.is_moving else ENEMY_IDLE_FLIPPED
        
        self.enemy_move(player)
        frame_x = (self.frame_index * SPRITE_WIDTH) + (SPRITE_WIDTH / 2)

        canvas.draw_image(sprite_image, 
                          (frame_x, SPRITE_HEIGHT / 2), 
                          (SPRITE_WIDTH, SPRITE_HEIGHT), 
                          (WIDTH / 2 - (camera_x - (BACKGROUND_WIDTH - WIDTH) / 2) + self.movement[0],  
                            HEIGHT / 2 - (camera_y - (BACKGROUND_HEIGHT - HEIGHT) / 2) + self.movement[1]), 
                          DISPLAY_SIZE)
        
verticalGrid = []
horizontalGrid = []    
    
class Backgrounds:    
    def create_grid():
        for x in range(14):
            for y in range(9):
                p1 = (x * BACKGROUND_WIDTH/13, y * BACKGROUND_HEIGHT/9)
                p2 = (x * BACKGROUND_WIDTH/13, (y + 1) * BACKGROUND_HEIGHT/9)
                verticalGrid.append((p1,p2, 0))

        for x in range(10):
            for y in range(13):
                p1 = (0 + y * (BACKGROUND_WIDTH/13), x * BACKGROUND_HEIGHT/9)
                p2 = (0 + ((y + 1) * BACKGROUND_WIDTH/13), x * BACKGROUND_HEIGHT/9)            
                horizontalGrid.append((p1,p2, 0))

    def new_wall(side, constant, beginning, end):
        if side == 'Vertical':
            for x in range(len(verticalGrid)):
                if ((verticalGrid[x][0][0] == constant) and (beginning <= verticalGrid[x][0][1] <= end)):
                    verticalGrid[x] = (verticalGrid[x][0], verticalGrid[x][1], side)                

        elif side == 'Horizontal':
            for x in range(len(horizontalGrid)):
                if ((constant - 1 < horizontalGrid[x][0][1] < constant + 1) and (beginning <= horizontalGrid[x][0][0] <= end)):
                    horizontalGrid[x] = (horizontalGrid[x][0], horizontalGrid[x][1], side)

        else:
            print("Incorrect format for side:", side, " constant:", constant, " beginning:", beginning, " end:", end)

    def create_walls():
        Backgrounds.new_wall('Vertical', 75, 216, 362)
        Backgrounds.new_wall('Vertical', 375, 215, 350)
        Backgrounds.new_wall('Horizontal', 216, 75, 300) 

    def check_collision(pos):
        touchingWalls = []

        # Check vertical walls
        for wall in verticalGrid:
            if wall[2] == 'Vertical':  # Check if the wall is impassable
                wall_x = wall[0][0]  # x-coordinate of the vertical wall
                wall_y1 = wall[0][1]  # y-coordinate of the top start point
                wall_y2 = wall[1][1]  # y-coordinate of the bottom end point

                # Check if the player's new position overlaps with the wall
                if (wall_x < pos[0] < wall_x + 15 and
                    wall_y1 - 45 < pos[1] < wall_y2):               

                    touchingWalls.append('left') # Collision detected

                if (wall_x - 15 < pos[0] < wall_x and
                    wall_y1 - 45 < pos[1] < wall_y2):               
                    touchingWalls.append('right')

        for wall in horizontalGrid:
            if wall[2] == 'Horizontal':  # Check if the wall is impassable
                wall_y = wall[0][1]  # y-coordinate of the horizontal wall
                wall_x1 = wall[0][0]  # x-coordinate of the left start point
                wall_x2 = wall[1][0]  # x-coordinate of the right end point

                # Check if the player's new position overlaps with the wall
                if (wall_y  < pos[1] + 40 < wall_y + 10 and
                    wall_x1 - 10 < pos[0] < wall_x2 + 10):
                    touchingWalls.append('up')  # Collision detected

                if (wall_y - 10 < pos[1] +40 < wall_y and
                    wall_x1 - 10 < pos[0] < wall_x2 + 10):
                    touchingWalls.append('down')  # Collision detected

        return touchingWalls
    
class Keys:
    def keydown(key):
        """Handle key press events."""
        if key == simplegui.KEY_MAP["left"]:
            player.keys["left"] = True
        elif key == simplegui.KEY_MAP["right"]:
            player.keys["right"] = True
        elif key == simplegui.KEY_MAP["up"]:
            player.keys["up"] = True
        elif key == simplegui.KEY_MAP["down"]:
            player.keys["down"] = True

    def keyup(key):
        """Handle key release events."""
        if key == simplegui.KEY_MAP["left"]:
            player.keys["left"] = False
        elif key == simplegui.KEY_MAP["right"]:
            player.keys["right"] = False
        elif key == simplegui.KEY_MAP["up"]:
            player.keys["up"] = False
        elif key == simplegui.KEY_MAP["down"]:
            player.keys["down"] = False

class Update:       

    def draw(canvas):
        """Draw game scene."""
        
        if not WELCOME_SCREEN:
            draw_welcome_screen(canvas)
            
        else:
            Update.update()

            # Calculate camera position
            camera_x = player.pos[0] - WIDTH // 2
            camera_y = player.pos[1] - HEIGHT // 2  

            # Draw background
            Update.draw_image(canvas, BKG_2, BKG_2_WIDTH, BKG_2_HEIGHT, camera_x, camera_y, scale=3)

            # Draw main map
            Update.draw_image(canvas, BACKGROUND, BACKGROUND_WIDTH, BACKGROUND_HEIGHT, camera_x, camera_y, scale=1)

            # Draw player
            player.draw(canvas, camera_x, camera_y)

            # Draw enemies
            for enemy in enemies:
                enemy.draw(canvas, camera_x, camera_y)
            
    def update():
        """Update player movement and animation."""
        player.move()
        player.update_animation()
        for enemy in enemies:    
            enemy.update_animation()
            
    def draw_image(canvas, image, img_width, img_height, camera_x, camera_y, scale=1):
        """Draw an image with the given parameters."""
        if image.get_width() <= 0 or image.get_height() <= 0:
            canvas.draw_text("Loading Image...", (WIDTH // 2 - 60, HEIGHT // 2), 20, "White")
            return
        
        canvas.draw_image(image,
            (img_width / 2, img_height / 2),  # Image center
            (img_width, img_height),  # Original size
            (
                WIDTH / 2 - (camera_x - (img_width - WIDTH) / 2),
                HEIGHT / 2 - (camera_y - (img_height - HEIGHT) / 2)
            ),
            (img_width * scale, img_height * scale)  # Scale image
        )
        
    def click(canvas):
        this = 0
        
        
        
def initialize_game():
    global player, enemies
    
    # Initialize player
    player = Player(WIDTH // 2, HEIGHT // 2, PLAYER_SPEED, 100, "Player 1", 15, 1)
    camera_x = player.pos[0] - WIDTH // 2
    camera_y = player.pos[1] - HEIGHT // 2 

    # Initialize enemies
    enemy_start = [WIDTH / 2 - (camera_x - (BACKGROUND_WIDTH - WIDTH) / 2),
                   HEIGHT / 2 - (camera_y - (BACKGROUND_HEIGHT - HEIGHT) / 2)]
    enemies = []
    amount_of_enemies = 10

    # Spawns enemies randomly around the map
    for i in range(amount_of_enemies):
        x_variation = random.randint(-500, 500)
        y_variation = random.randint(-300, 500)
        enemy = Enemy(enemy_start[0], enemy_start[1], PLAYER_SPEED - 2, 100, "Player 1", 15, 1, player, x_variation, y_variation)
        enemies.append(enemy)

    # Run all initial set-ups
    Backgrounds.create_grid()
    Backgrounds.create_walls()
    
initialize_game()

# Create the game frame
frame = simplegui.create_frame("Animated Player", WIDTH, HEIGHT)
frame.set_draw_handler(Welcome.draw)
frame.set_mouseclick_handler(Welcome.welcome_click)
# Start background music
BACKGROUND_MUSIC.play()

# Start the game
frame.start()