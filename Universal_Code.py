import simplegui
import random
import math

# Constants
WIDTH = 500
HEIGHT = 500
PLAYER_SPEED = 5
FRAME_COUNT = 6
NPC_FRAME_COUNT = 5
ATTACK_FRAME_COUNT = 5
RANGED_ENEMY_ATTACK_FRAME_COUNT = 8
PLAYER_HURT_FRAME_COUNT = 3
DEAD_FRAME_COUNT = 4
FRAME_DELAY = 5
SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128
DISPLAY_SIZE = (100, 100)
DEATH_SCREEN = False
LIVES = 3
SCORE = 0
HIGH_SCORE = 0
WAVE = 0

# Loading backgrounds and sounds
WELCOME_SCREEN = simplegui.load_image("https://i.imgur.com/Zhl2jMw.jpeg")
START_BUTTON = simplegui.load_image("https://i.imgur.com/MqgJtv8.png")
WASTED = simplegui.load_image("https://i.imgur.com/pFupxi8.png")
SPEECH = simplegui.load_image("https://i.imgur.com/RHrJ2RA.png")
BACKGROUND = simplegui.load_image("https://i.imgur.com/oHrKyJ2.png")
BKG_2 = simplegui.load_image("https://i.imgur.com/O671jzf.jpeg")
BACKGROUND_MUSIC = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
EXPLOSION_EFFECT = simplegui.load_sound("https://dl.dropboxusercontent.com/scl/fi/n8lrksp0as7maf5v7xg0k/explosion-312361.mp3?rlkey=l3yago6kmsh2utwey48lkdo0h&st=d2bdyxza")
POTION_DRINKING_EFFECT = simplegui.load_sound("https://dl.dropboxusercontent.com/scl/fi/n76nsgjxmyyr7jkjzrufi/085594_potion-35983.mp3?rlkey=l8glwgs6nwye5av1og8bbntv9&st=sfcxevjp")
PLAYER_ATTACKEFFECT = simplegui.load_sound("https://dl.dropboxusercontent.com/scl/fi/5jtk6obferdvbsi9tck6x/audiomass-output.mp3?rlkey=9s6kqrb3zlvjy03f5unvioega&st=veueqnuo")

# Loading sprites and animations (player and enemy)
NPC_IMAGE = simplegui.load_image("https://i.imgur.com/wU60Hb7.png")
IDLE_IMAGE = simplegui.load_image("https://i.imgur.com/Xq9mtbz.png")
RUN_IMAGE = simplegui.load_image("https://i.imgur.com/NAhLOeo.png")
HURT_IMAGE = simplegui.load_image("https://i.imgur.com/01pyiDj.png")
ATTACK_IMAGE = simplegui.load_image("https://i.imgur.com/HbqNc4s.png")
ENEMY_IDLE_IMAGE = simplegui.load_image("https://i.imgur.com/atp0eco.png")
ENEMY_RUN_IMAGE = simplegui.load_image("https://i.imgur.com/QomI2XQ.png")
ENEMY_ATTACK_IMAGE = simplegui.load_image("https://i.imgur.com/eJ7dTBA.png")
ENEMY_DEATH_IMAGE = simplegui.load_image("https://i.imgur.com/mPEEU4v.png")
FIREBALL_WRIGHT = simplegui.load_image("https://i.imgur.com/gPDsxrc.png")
FIREBALL_HIT = simplegui.load_image("https://i.imgur.com/dtYaPGM.png")
RANGED_ENEMY_IDLE = simplegui.load_image("https://i.imgur.com/zHnkE5g.png")
RANGED_ENEMY_ATTACK = simplegui.load_image("https://i.imgur.com/EXx8oHf.png")
RANGED_ENEMY_DEATH = simplegui.load_image("https://i.imgur.com/YPXSoVx.png")
HEALING_POTION = simplegui.load_image("https://i.imgur.com/p1ECdyv.png")
# Loading animations
IDLE_FLIPPED = simplegui.load_image("https://i.imgur.com/LMXaTlK.png")
RUN_FLIPPED = simplegui.load_image("https://i.imgur.com/J8DS6FF.png")
HURT_FLIPPED = simplegui.load_image("https://i.imgur.com/BPkrMM8.png")
ATTACK_FLIPPED = simplegui.load_image("https://i.imgur.com/FRh1JQu.png")
ENEMY_IDLE_FLIPPED = simplegui.load_image("https://i.imgur.com/pxSuood.png")
ENEMY_RUN_FLIPPED = simplegui.load_image("https://i.imgur.com/n8hPFhE.png")
ENEMY_ATTACK_FLIPPED = simplegui.load_image("https://i.imgur.com/KTSabih.png")
ENEMY_DEATH_FLIPPED = simplegui.load_image("https://i.imgur.com/fdffUJr.png")
RANGED_ENEMY_IDLE_FLIPPED = simplegui.load_image("https://i.imgur.com/9INlzYg.png")
RANGED_ENEMY_ATTACK_FLIPPED = simplegui.load_image("https://i.imgur.com/IaIFMfZ.png")
RANGED_ENEMY_DEATH_FLIPPED = simplegui.load_image("https://i.imgur.com/OmMnhkA.png")


BACKGROUND_WIDTH = BACKGROUND.get_width()
BACKGROUND_HEIGHT = BACKGROUND.get_height()
BKG_2_WIDTH = BKG_2.get_width() 
BKG_2_HEIGHT = BKG_2.get_height()
LIVES_IMAGE = simplegui.load_image("https://i.imgur.com/Mw3kXLa.png")

class Welcome:
    
    def draw(canvas):
        global HIGH_SCORE
        Welcome.draw_image(canvas, WELCOME_SCREEN, WIDTH, HEIGHT, 2)
        canvas.draw_text(f"High Score: {HIGH_SCORE}", (10, 20), 20, "White")
        canvas.draw_text("CONTROLS", (10, 100), 20, "White")
        canvas.draw_text("W - UP", (10, 120), 20, "White")
        canvas.draw_text("A - LEFT", (10, 140), 20, "White")
        canvas.draw_text("S - DOWN", (10, 160), 20, "White")
        canvas.draw_text("D - RIGHT", (10, 180), 20, "White")
        canvas.draw_text("J - ATTACK", (10, 200), 20, "White")
        Welcome.draw_image(canvas, START_BUTTON, 80, 40, 1.25)
        
        if DEATH_SCREEN:
            Welcome.draw_image(canvas, WASTED, 250, 100, 2)
            canvas.draw_text(f"Score last game: {SCORE}", (10, 40), 20, "White")
        
    def welcome_click(pos):
        if ((WIDTH/2 - 40 <= pos[0] <= WIDTH/2 + 40) and (HEIGHT/1.25 - 20 <= pos[1] <= HEIGHT/1.25 + 20)):
            frame.set_draw_handler(Update.draw)
            frame.set_keydown_handler(Keys.keydown)
            frame.set_keyup_handler(Keys.keyup)
            frame.set_mouseclick_handler(Update.click)
            initialize_game()
            
            
    def draw_image(canvas, image, size_x, size_y, hight_mod):

        image_width = image.get_width()
        image_height = image.get_height()

        if image_width <= 0 or image_height <= 0:
            canvas.draw_text("Loading Image...", (WIDTH // 2 - 60, HEIGHT // 2), 20, "White")
            return
        
        canvas.draw_image(image, (image_width // 2, image_height // 2), 
                              (image_width, image_height), 
                              (WIDTH/ 2, HEIGHT /hight_mod), (size_x, size_y))


class NPC:
    def __init__(self, pos):	
        self.pos = pos
        self.frame_timer = 0
        self.frame_index = 0
        self.display_message = False
        self.messages = [
            "HELP ME!",
            "Hello sir! Please may you clean my garden!",
            "There's tons of skeletons! I hate skeletons!!",
            "For every one you 'clean-up' I'll pay you 10 gold!",
            "I think theres some on the otherside of the garden!",
            "Have a go at 'cleaning them up'",
            "I will provide healing potions if it helps",
            "Here you go the first one",
            "Come back for another one after each group"
        ]
        self.message_index = 0
        self.frame_counter = 0
        self.frame_delay = 180
        self.healing_given = False
        
        
                 
    def update_animation(self):
        self.frame_timer += 1
        if self.frame_timer >= 10:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % NPC_FRAME_COUNT
            
            
            
            
    def draw(self, canvas, camera_x, camera_y):
        sprite_image = NPC_IMAGE
        frame_x = (self.frame_index * SPRITE_WIDTH) + (SPRITE_WIDTH / 2)
        adjusted_x = self.pos[0] - camera_x 
        adjusted_y = self.pos[1] - camera_y
        
        canvas.draw_image(sprite_image, 
                          (frame_x, SPRITE_HEIGHT / 2), 
                          (SPRITE_WIDTH, SPRITE_HEIGHT), 
                          (adjusted_x,  
                           adjusted_y), 
                          DISPLAY_SIZE)
        
        distance = ((self.pos[0] - player.pos[0]) ** 2 + (self.pos[1] - player.pos[1]) ** 2) ** 0.5

        if distance < 100:
            self.display_message = True
        else:
            self.display_message = False
            self.message_index = 0  # Reset message when player moves away
            self.frame_counter = 0  # Reset frame count 
            
        if self.display_message:
            text_x = adjusted_x - 30
            text_y = adjusted_y - 20

            # Draw the current message
            canvas.draw_text(self.messages[self.message_index], (text_x, text_y), 14, "White")

            # Increase frame counter
            self.frame_counter += 1

            # Change message when delay is reached
            if self.frame_counter >= self.frame_delay:
                self.frame_counter = 0  # Reset counter
                if self.message_index < len(self.messages) - 1:
                    self.message_index += 1
                    if self.message_index == 7 and self.healing_given == False:
                        healing_potion.activate()
                        self.healing_given = True;
                        
            
class Player:
    def __init__(self, x, y, speed, health, name, AP, DM):
        self.pos = [x, y]
        self.OGspeed = speed
        self.is_moving = False
        self.facing_right = True
        self.frame_index = 0
        self.frame_timer = 0
        self.keys = {"a": False, "d": False, "w": False, "s": False, "j": False}
        self.health = health
        self.max_health = health
        self.hurt = False
        self.attack = False
        self.name = name
        self.AP = AP
        self.DM = DM
        self.attack_cooldown = 0
       
   
    def move(self):
        """Update player position based on key presses."""
        
        
        collStat = Backgrounds.check_collision(self.pos, self.hitbox(), 'player')
        speed_x = 0
        speed_y = 0
        self.is_moving = False
        
        
        if self.keys["a"] and not('left' in collStat):
            speed_x = 0 - self.OGspeed
            self.facing_right = False
            self.is_moving = True
            
        elif self.keys["d"] and not("right" in collStat):
            speed_x = 0 + self.OGspeed
            self.facing_right = True
            self.is_moving = True
            
        if self.keys["w"] and not("up" in collStat):
            speed_y = 0 - self.OGspeed
            self.is_moving = True
            
        elif self.keys["s"] and not("down" in collStat):
            speed_y = 0 + self.OGspeed
            self.is_moving = True
        
        elif self.keys["j"] and self.attack_cooldown == 0:
            self.attack_cooldown = 35
            self.attack_move()
        
        if (self.keys["a"] or self.keys["d"]) and (self.keys["w"] or self.keys["s"]):
            speed_x *= 1 / (2**0.5)
            speed_y *= 1 / (2**0.5)
            
        
        
        self.pos[0] += speed_x
        self.pos[1] += speed_y
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def update_animation(self):
        """Update frame index for animation."""
        if self.hurt == True:
            self.frame_timer += 1
            if self.frame_timer >= FRAME_DELAY:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % PLAYER_HURT_FRAME_COUNT
                
                if self.frame_index == 0:
                    self.hurt = False
        elif self.attack == True:
            self.frame_timer += 1
            if self.frame_timer >= FRAME_DELAY:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % ATTACK_FRAME_COUNT
                
                if self.frame_index == 0:
                    #attack_move(self)
                    self.attack = False
        
        else:
            self.frame_timer += 1
            if self.frame_timer >= FRAME_DELAY:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % FRAME_COUNT

            
    def take_damage(self, damage):
            global LIVES
            self.hurt = True
            self.health -= damage
            self.health = max(self.health, 0)
            if self.health <= 0:
                LIVES -= 1
                self.pos = [743,254]
                self.health = 100
                if LIVES <= 0:
                    game_reset()
                
        
    def attack_move(self):
        PLAYER_ATTACKEFFECT.set_volume(0.2)
        PLAYER_ATTACKEFFECT.play()
        print (self.pos)
        self.attack = True
        self.frame_index = 0
        attack_range = 50  # Define the attack range       
        
        for enemy in enemies:
                
            distance = ((self.pos[0] - enemy.pos[0]) ** 2 + (self.pos[1] - enemy.pos[1]) ** 2) ** 0.5

            # Check if the distance is within the attack range
            if distance <= attack_range:
                # If there's a hit, apply damage to the enemy
                enemy.take_damage(self.AP) 
                #print(f"Hit {enemy.name} for {self.AP} damage!")  # Debugging line
                break  
                
        for ranged_enemy in ranged_enemies:
            distance = ((self.pos[0] - ranged_enemy.pos[0]) ** 2 + (self.pos[1] - ranged_enemy.pos[1]) ** 2) ** 0.5

            # Check if the distance is within the attack range
            if distance <= attack_range:
                # If there's a hit, apply damage to the enemy
                ranged_enemy.take_damage(self.AP) 
                #print(f"Hit {enemy.name} for {self.AP} damage!")  # Debugging line
                break 
    
    
    def hitbox(self):
        self.Hitbox=[]
        position = self.pos
        self.Hitbox=[]
        self.Hitbox.append((((position[0] - 15), (position[1] - 5)),((position[0] - 15), (position[1] + 50))))
        self.Hitbox.append((((position[0] + 15), (position[1] - 5)),((position[0] + 15), (position[1] + 50))))
        self.Hitbox.append((self.Hitbox[0][0], self.Hitbox[1][0]))
        self.Hitbox.append((self.Hitbox[0][1], self.Hitbox[1][1]))
        rect = [self.Hitbox[0][0][0], self.Hitbox[2][0][1], self.Hitbox[1][0][0], self.Hitbox[3][0][1]]

        return rect
    
    def draw(self, canvas, camera_x, camera_y):
        #print(self.hurt)
        if self.hurt and self.facing_right:
            sprite_image = HURT_IMAGE
        elif self.hurt and not self.facing_right:
            sprite_image = HURT_FLIPPED
        elif self.attack and self.facing_right:
            sprite_image = ATTACK_IMAGE
        elif self.attack and not self.facing_right:
            sprite_image = ATTACK_FLIPPED
        else:
            sprite_image = RUN_IMAGE if self.is_moving else IDLE_IMAGE
            if not self.facing_right:
                sprite_image = RUN_FLIPPED if self.is_moving else IDLE_FLIPPED
        
        frame_x = (self.frame_index * SPRITE_WIDTH) + (SPRITE_WIDTH / 2)
        screen_x = WIDTH // 2
        screen_y = HEIGHT // 2
        canvas.draw_image(sprite_image, 
                          (frame_x, SPRITE_HEIGHT / 2), 
                          (SPRITE_WIDTH, SPRITE_HEIGHT), 
                          (WIDTH // 2, HEIGHT // 2), 
                          DISPLAY_SIZE)
        hitbox = self.hitbox()
        canvas.draw_line((hitbox[0] - camera_x, hitbox[1] - camera_y), (hitbox[2] - camera_x, hitbox[1] - camera_y), 2, 'Red')  # Top edge
        canvas.draw_line((hitbox[0] - camera_x, hitbox[3] - camera_y), (hitbox[2] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Left edge
        canvas.draw_line((hitbox[0] - camera_x, hitbox[1] - camera_y), (hitbox[0] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Right edge
        canvas.draw_line((hitbox[2] - camera_x, hitbox[1] - camera_y), (hitbox[2] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Bottom edge
        
        
        # Draw Health Bar
        bar_width = 50
        bar_height = 5
        bar_x = screen_x - bar_width // 2
        bar_y = screen_y - 40  # Above player
        
        # Health bar background
        canvas.draw_polygon([(bar_x, bar_y),
                             (bar_x + bar_width, bar_y),
                             (bar_x + bar_width, bar_y + bar_height),
                             (bar_x, bar_y + bar_height)], 
                            1, "black", "red")

        # Draw current health
        health_ratio = max(self.health / self.max_health, 0)  
        if health_ratio > 0:  
            canvas.draw_polygon([(bar_x, bar_y),
                                 (bar_x + bar_width * health_ratio, bar_y),
                                 (bar_x + bar_width * health_ratio, bar_y + bar_height),
                                 (bar_x, bar_y + bar_height)], 
                                1, "black", "green")
            
    def healing(self, healing):
        self.health += healing
        if self.health > self.max_health:
            self.health = self.max_health
        
        
    def get_p(self):
        return self.pos
    
    
class HealingPotion:
    def __init__(self, x , y):
        self.pos = [x, y] 
        self.healing = 50
        self.image_width = HEALING_POTION.get_width()
        self.image_height = HEALING_POTION.get_height()
        self.active = False
    
    def update(self):
        if self.active == True:
            distance = ((player.pos[0] - self.pos[0])**2 + (player.pos[1] - self.pos[1])**2)**0.5  

            if distance <= 50:
                player.healing(self.healing)
                POTION_DRINKING_EFFECT.play()
                self.active = False
        
    def draw(self, canvas, camera_x, camera_y):
        if self.active == True:
            canvas.draw_image(
                HEALING_POTION,
                (self.image_width / 2, self.image_height / 2), 
                (self.image_width, self.image_height), 
                (self.pos[0] - camera_x, self.pos[1] - camera_y),  
                (40, 40))
            
    def activate(self):
        self.active = True
    
class Enemy:
    def __init__(self, x, y, speed, health, name, AP, DM, player, xVar, yVar):
        self.adjusted_x = 0
        self.adjusted_y = 0        
        self.player_pos = player.get_p()
        self.player = player
        self.pos = [x + xVar, y + yVar]      
        self.movement = [0 + xVar, 0 + yVar]
        self.state = 'idle'
        self.facing_right = True
        self.OGspeed = speed
        self.frame_index = 0
        self.frame_timer = 0
        self.health = health
        self.max_enemy_health = health
        self.name = name
        self.AP = AP
        self.DM = DM
        self.attack = False
        self.attack_cooldown = 0  # Cooldown timer
        self.attack_delay = 180  # Frames before enemy can attack again
        self.counter_a = 3
        self.counter_b = 5
        self.notMoving = True
        self.escapeTime = 501
    
    def check_hit(self, player):
        
        enemy_rect = self.hitbox()
        player_rect = self.player.hitbox()
        
        if ((enemy_rect[2] > player_rect[0] and enemy_rect[0] < player_rect[0] and enemy_rect[3] > player_rect[1] and enemy_rect[1] < player_rect[3]) or \                                                         
            (enemy_rect[0]  <= player_rect[2] and enemy_rect[2] > player_rect[2] and 
            enemy_rect[3] > player_rect[1] and enemy_rect[1] < player_rect[3])):
              
              
            damage = self.AP * self.player.DM
            self.player.take_damage(damage)
            self.state = 'idle'
            self.frame_index = 0
            
    def take_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.state = "dead"
            self.frame_index = 0
        else:
            pass
            

    def enemy_move(self, player):
        """Handles enemy movement and attack decisions."""
        #setting player position, distance from player and any collisions
        if self.state != "dead":
            
            self.player_pos = player.get_p()        
            distance = ((self.player_pos[0] - self.pos[0])**2 + (self.player_pos[1] - self.pos[1])**2)**0.5        
            if (self.movement == [0,0] and distance > 50):
                notMoving = True

            else:
                notMoving = False

            speed = self.OGspeed             
            collStat = Backgrounds.check_collision(self.pos, self.hitbox(), 'enemy')        

            if len(collStat) > 3:
                escapeTime = 0

            self.movement = [0,0]


            if distance > 200 and self.escapeTime > 180:
                self.state = 'idle'
                self.frame_index = 0


            # Attack only if cooldown has expired
            elif distance < 50 and self.state != 'attack' and self.attack_cooldown == 0 and self.escapeTime > 500:
                self.attack = True
                self.state = 'attack'
                self.attack_cooldown = self.attack_delay
                self.frame_index = 0




            #if not attacking and in distance of player, move towards players position
            elif (self.state != 'attack') and self.escapeTime > 500:
                self.state = 'moving'
                


                #normalise speed when going diagonal left
                if ((self.player_pos[0] - self.pos[0] < -10) and \
                    not('left' in collStat)):

                    if self.player_pos[1] - self.pos[1] < -10 and not('up' in collStat):
                        speed = (2 * speed) **0.5
                        self.movement[1] -= speed

                    elif self.player_pos[1] - self.pos[1] > 10 and not('down' in collStat):
                        speed = (2 * speed) **0.5                    
                        self.movement[1] += speed

                    self.movement[0] -= speed
                    self.facing_right = False            


                #normalise speeds when going diagonal right
                elif (self.player_pos[0] - self.pos[0] > 10) and \
                    not('right' in collStat):

                    if self.player_pos[1] - self.pos[1] < -10 and not('up' in collStat):
                        speed = (2 * speed) **0.5
                        self.movement[1] -= speed


                    elif self.player_pos[1] - self.pos[1] > 10 and not('down' in collStat):
                        speed = (2 * speed) **0.5
                        self.movement[1] += speed                

                    self.movement[0] += speed                
                    self.facing_right = True


                elif (self.player_pos[1] - self.pos[1] < -10) and not('up' in collStat):
                    self.movement[1] -= speed


                elif (self.player_pos[1] - self.pos[1] > 10) and not('down' in collStat):
                    self.movement[1] += speed


            elif (len(collStat) == 3 or notMoving) or self.escapeTime <= 500 and self.state != "attack":
                self.escapeTime += 1
                if not('left' in collStat):
                    #escapeDir = "left"
                    self.movement[0] -= speed 
                elif not('right' in collStat):
                    #escapeDir = "right"
                    self.movement[0] += speed
                elif not('up' in collStat):
                    #escapeDir = "up"
                    self.movement[1] -= speed	
                elif not('down' in collStat):
                    #escapeDir = "down"
                    self.movement[1] += speed

            #elif (len(collStat)) == 2) or self.escapeTime <= 500:
                #if ('left' in collStat and ('right' in collStat or 'up' in collStat):


            elif self.state != 'attack' or self.state == 'moving':                
                self.counter_a -= 1
                if self.counter_a < 30:
                    self.state = 'idle'
                    self.frame_index = 0
                    self.counter_a = 100


            self.pos = [self.pos[0] + self.movement[0], self.pos[1] + self.movement[1]]                

            # Reduce cooldown
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

    
    def hitbox(self):
        #box[0] is left, 1 is right, 2 is top, 3 is bottom
        self.Hitbox=[]
        position = [self.pos[0], self.pos[1]]
        self.Hitbox.append((((position[0] - 15), (position[1] - 5)),((position[0] - 15), (position[1] + 50))))
        self.Hitbox.append((((position[0] + 15), (position[1] - 5)),((position[0] + 15), (position[1] + 50))))
        self.Hitbox.append((self.Hitbox[0][0], self.Hitbox[1][0]))
        self.Hitbox.append((self.Hitbox[0][1], self.Hitbox[1][1]))
        rect = [self.Hitbox[0][0][0], self.Hitbox[2][0][1], self.Hitbox[1][0][0], self.Hitbox[3][0][1]]

        return rect
    
    
    def update_animation(self, player): 
        distance = ((self.player_pos[0] - self.pos[0])**2 + (self.player_pos[1] - self.pos[1])**2)**0.5    
        if self.state == "dead":
            self.frame_timer += 1
            if self.frame_timer >= 10:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % DEAD_FRAME_COUNT
                print(self.frame_index)
                if self.frame_index == 0: 
                    
                    clear_dead(self.pos)
        
        if self.state == 'attack':
            self.frame_timer += 1
            if self.frame_timer >= 10:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % ATTACK_FRAME_COUNT

                if self.frame_index == 0:                        
                        self.check_hit(self.AP * player.DM)						                            
                        self.state = 'idle'
                        self.frame_index = 0

        else:
            self.frame_timer += 1
            if self.frame_timer >= 10:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % FRAME_COUNT


    def draw(self, canvas, camera_x, camera_y):
        """Draw enemy sprite."""
        if self.state == "dead" and self.facing_right:
            sprite_image = ENEMY_DEATH_IMAGE
            
        elif self.state == "dead" and not self.facing_right:
            sprite_image = ENEMY_DEATH_FLIPPED
            
        elif self.state == 'attack' and self.facing_right:
            sprite_image = ENEMY_ATTACK_IMAGE
            
        elif self.state == 'attack' and not self.facing_right:
            sprite_image = ENEMY_ATTACK_FLIPPED
            
        else:
            sprite_image = ENEMY_RUN_IMAGE if self.state == 'moving' else ENEMY_IDLE_IMAGE
            if not self.facing_right:
                sprite_image = ENEMY_RUN_FLIPPED if self.state == 'moving' else ENEMY_IDLE_FLIPPED

        
        if self.state == "dead":
            print(self.frame_index)
        
        self.enemy_move(self.player)
        hitbox = self.hitbox()
        
        
        hitbox = self.hitbox()
        canvas.draw_line((hitbox[0] - camera_x, hitbox[1] - camera_y), (hitbox[2] - camera_x, hitbox[1] - camera_y), 2, 'Red')  # Top edge
        canvas.draw_line((hitbox[0] - camera_x, hitbox[3] - camera_y), (hitbox[2] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Left edge
        canvas.draw_line((hitbox[0] - camera_x, hitbox[1] - camera_y), (hitbox[0] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Right edge
        canvas.draw_line((hitbox[2] - camera_x, hitbox[1] - camera_y), (hitbox[2] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Bottom edge
        
        
        
        #canvas.draw_line((hitbox[0], hitbox[1]), (hitbox[2], hitbox[1]), 2, 'Red')  # Top edge
        #canvas.draw_line((hitbox[0], hitbox[3]), (hitbox[2], hitbox[3]), 2, 'Red')  # Left edge
        #canvas.draw_line((hitbox[0], hitbox[1]), (hitbox[0], hitbox[3]), 2, 'Red')  # Right edge
        #canvas.draw_line((hitbox[2], hitbox[1]), (hitbox[2], hitbox[3]), 2, 'Red')  # Bottom edge
        
        
        frame_x = (self.frame_index * SPRITE_WIDTH) + (SPRITE_WIDTH / 2)
        
        
        self.adjusted_x = self.pos[0] - camera_x 
        self.adjusted_y = self.pos[1] - camera_y
        
        canvas.draw_image(sprite_image, 
                          (frame_x, SPRITE_HEIGHT / 2), 
                          (SPRITE_WIDTH, SPRITE_HEIGHT), 
                          (self.adjusted_x,  
                           self.adjusted_y), 
                          DISPLAY_SIZE)
        
    def get_p(self):
        return self.pos
       
        
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other):
        self.x += other.x
        self.y += other.y
    
    def negate_x(self):
        self.x = -self.x
    
    def negate_y(self):
        self.y = -self.y
        
        
class bouncingObject:
    def __init__(self, pos, vel, radius, bounce_limit):
        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector(vel[0], vel[1])
        self.radius = radius
        self.bounce_limit = bounce_limit
        self.bounces = 0
        self.sprite_width = 154
        self.sprite_height = 154
        self.num_frames = 5
        self.current_frame = 0
        self.animation_speed = 5
        self.frame_counter = 0
        self.scale = 0.5
        self.Hitbox = self.hitbox()
        self.player = player
        self.scale_fireball = 1
        self.exploding = False
        self.row_explosion = 0
        self.col_explosion = 0
    
    def coll_check(self):
        
        collStat = Backgrounds.check_collision([self.pos.x,self.pos.y], self.hitbox(), "projectile")
        if 'left' in collStat or 'right' in collStat:
            self.vel.negate_x()
            self.bounces += 1
            
        if 'up' in collStat or 'down' in collStat:
            self.vel.negate_y()
            self.bounces += 1
        if self.bounces > self.bounce_limit:
            self.projectile_hit()
            
    def projectile_hit(self):
            bouncing_objects.remove(self)
            self.sprite_width = 103
            self.sprite_height = 106
            self.exploding = True
            exploding_objects.append(self)
            EXPLOSION_EFFECT.play()
            
    
    def hitbox(self):
   
        left = self.pos.x - self.radius - 5
        right = self.pos.x + self.radius + 5
        top = self.pos.y - self.radius - 5
        bottom = self.pos.y + self.radius + 5
        
        return [left, top, right, bottom]
    
    def check_hit(self):
        
        enemy_rect = self.hitbox()
        player_rect = self.player.hitbox()
        
        if ((enemy_rect[2] > player_rect[0] and enemy_rect[0] < player_rect[0] and enemy_rect[3] > player_rect[1] and enemy_rect[1] < player_rect[3]) or \                                                         
            (enemy_rect[0]  <= player_rect[2] and enemy_rect[2] > player_rect[2] and 
            enemy_rect[3] > player_rect[1] and enemy_rect[1] < player_rect[3])):
              
            self.projectile_hit()
            player.take_damage(15)
            
            
            
    def update(self):
        
        if self.exploding == False:
            self.coll_check()
            self.pos.add(self.vel)
            self.check_hit()
            

            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed:
                self.current_frame = (self.current_frame + 1) % self.num_frames
                self.frame_counter = 0
                
        if self.exploding is True:
            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed:
                self.col_explosion +=1
                if self.col_explosion >= 7:
                    self.col_explosion = 0
                    self.row_explosion += 1
                if self.row_explosion >= 3:
                    exploding_objects.remove(self)
                self.frame_counter = 0
    
            
    def drawSprite(self, canvas, camera_x, camera_y):
        """Draws the fireball using the sprite sheet."""
        
        hitbox = self.hitbox()
        canvas.draw_line((hitbox[0] - camera_x, hitbox[1] - camera_y), (hitbox[2] - camera_x, hitbox[1] - camera_y), 2, 'Red')  # Top edge
        canvas.draw_line((hitbox[0] - camera_x, hitbox[3] - camera_y), (hitbox[2] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Left edge
        canvas.draw_line((hitbox[0] - camera_x, hitbox[1] - camera_y), (hitbox[0] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Right edge
        canvas.draw_line((hitbox[2] - camera_x, hitbox[1] - camera_y), (hitbox[2] - camera_x, hitbox[3] - camera_y), 2, 'Red')  # Bottom edge
        
        frame_x = self.current_frame * self.sprite_width
        
        scaled_width = self.sprite_width * self.scale
        scaled_height = self.sprite_height * self.scale
        
        angle = math.atan2(self.vel.y, self.vel.x)
        
        canvas.draw_image(
            FIREBALL_WRIGHT,
            (frame_x + self.sprite_width // 2, self.sprite_height // 2), 
            (self.sprite_width, self.sprite_height), 
            (self.pos.x - camera_x, self.pos.y - camera_y),  
            (scaled_width, scaled_height),
            angle)
        
    def drawExplosion(self, canvas, camera_x, camera_y):
        

        frame_x = self.col_explosion * self.sprite_width
        frame_y = self.row_explosion * self.sprite_height
        
        scaled_width = self.sprite_width * self.scale_fireball
        scaled_height = self.sprite_height * self.scale_fireball
        
        
        
        canvas.draw_image(
            FIREBALL_HIT,
            (frame_x + self.sprite_width // 2, frame_y + self.sprite_height // 2), 
            (self.sprite_width, self.sprite_height), 
            (self.pos.x - camera_x, self.pos.y - camera_y),  
            (scaled_width, scaled_height))
        
               
class RangedEnemy:
    def __init__(self, x, y, speed, health, name, AP, DM, player, xVar, yVar):
        self.adjusted_x = 0
        self.adjusted_y = 0        
        self.player_pos = player.get_p()
        self.player = player
        self.pos = [x + xVar, y + yVar]      
        self.movement = [0 + xVar, 0 + yVar]
        self.state = 'idle'
        self.facing_right = True
        self.OGspeed = speed
        self.frame_index = 0
        self.frame_timer = 0
        self.health = health
        self.max_enemy_health = health
        self.name = name
        self.AP = AP
        self.DM = DM
        self.attack = False
        self.attack_cooldown = 0  # Cooldown timer
        self.attack_delay = 180  # Frames before enemy can attack again
        self.counter_a = 3
        self.counter_b = 5
        self.notMoving = True
        self.escapeTime = 501

    def take_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.state = "dead"
            self.frame_index = 0
        else:
            pass
            
    def range_check(self, player):  
        
        distance = ((player.pos[0] - self.pos[0])**2 + (player.pos[1] - self.pos[1])**2)**0.5    
        direction = [player.pos[0] - self.pos[0], player.pos[1] - self.pos[1]]
        tempDir = self.facing_right
        if self.player_pos[0] <= self.pos[0] + 15:
            self.facing_right = False
        elif self.player_pos[0] >= self.pos[0] - 15:
            self.facing_right = True
        
        if self.facing_right != tempDir and self.facing_right == False:
            self.pos[0] -= 15
        elif self.facing_right != tempDir and self.facing_right == True:
            self.pos[0] += 15
        magnitude = (direction[0]**2 + direction[1]**2) ** 0.5
        if magnitude != 0:  # Avoid division by zero
            direction[0] = (direction[0] / magnitude) * 2.5
            direction[1] = (direction[1] / magnitude) * 2.5    
       
        if (distance < 200 and self.attack_cooldown <= 0):
            fireball = bouncingObject((self.pos[0],self.pos[1]), direction, 10, 5)
            bouncing_objects.append(fireball)
            self.state = "attack"
            self.attack_cooldown = 270
            
        self.attack_cooldown -= 1
       
    def update_animation(self, player): 
        distance = ((self.player_pos[0] - self.pos[0])**2 + (self.player_pos[1] - self.pos[1])**2)**0.5    
        if self.state == "dead":
            self.frame_timer += 1
            if self.frame_timer >= 10:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % DEAD_FRAME_COUNT
                print(self.frame_index)
                if self.frame_index == 0: 
                    
                    clear_dead(self.pos)
        
        if self.state == 'attack':
            self.frame_timer += 1
            if self.frame_timer >= 10:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % RANGED_ENEMY_ATTACK_FRAME_COUNT

                if self.frame_index == 0:                        
                                                                    
                        self.state = 'idle'
                        self.frame_index = 0

        else:
            self.frame_timer += 1
            if self.frame_timer >= 10:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % FRAME_COUNT

                
    def draw(self, canvas, camera_x, camera_y):
        self.range_check(player)
        if self.state == "idle" and self.facing_right == True:
            sprite_image = RANGED_ENEMY_IDLE
        
        elif self.state == "idle" and self.facing_right == False:
            sprite_image = RANGED_ENEMY_IDLE_FLIPPED
            
        elif self.state == 'attack' and self.facing_right:
            sprite_image = RANGED_ENEMY_ATTACK
            
        elif self.state == 'attack' and not self.facing_right:
            sprite_image = RANGED_ENEMY_ATTACK_FLIPPED
            
        elif self.state == 'dead' and self.facing_right:
            sprite_image = RANGED_ENEMY_DEATH
            
        elif self.state == 'dead' and not self.facing_right:
            sprite_image = RANGED_ENEMY_DEATH_FLIPPED
        else:
            if self.facing_right == True:
                sprite_image = RANGED_ENEMY_IDLE
            else:
                sprite_image = RANGED_ENEMY_IDLE_FLIPPED
                
        frame_x = (self.frame_index * SPRITE_WIDTH) + (SPRITE_WIDTH / 2)
        
        self.adjusted_x = self.pos[0] - camera_x 
        self.adjusted_y = self.pos[1] - camera_y
        
        canvas.draw_image(sprite_image, 
                          (frame_x, SPRITE_HEIGHT / 2), 
                          (SPRITE_WIDTH, SPRITE_HEIGHT), 
                          (self.adjusted_x,  
                           self.adjusted_y), 
                          DISPLAY_SIZE)
        
        
        
        
        
verticalGrid = []
horizontalGrid = []    
    
class Backgrounds:    
    def create_grid():
        for x in range(19):
            for y in range(22):
                p1 = (x * BACKGROUND_WIDTH/19, y * BACKGROUND_HEIGHT/22)
                p2 = (x * BACKGROUND_WIDTH/19, (y + 1) * BACKGROUND_HEIGHT/22)
                verticalGrid.append((p1,p2, 0))

        for x in range(23):
            for y in range(20):
                p1 = (0 + y * (BACKGROUND_WIDTH/19), x * BACKGROUND_HEIGHT/22)
                p2 = (0 + ((y + 1) * BACKGROUND_WIDTH/19), x * BACKGROUND_HEIGHT/22)            
                horizontalGrid.append((p1,p2, 0))

        for x in verticalGrid:
            print(x)
        
        for x in range(10):
            print()
        
        for x in horizontalGrid:
            print(x)
    
    
    
    def new_wall(side, constant, beginning, end):
        if side == 'Vertical':
            for x in range(len(verticalGrid)):
                if ((constant - 5 <= verticalGrid[x][0][0] <= constant + 5) and (beginning-5 <= verticalGrid[x][0][1] <= end +5)):
                    verticalGrid[x] = (verticalGrid[x][0], verticalGrid[x][1], side)                
                    print(verticalGrid[x], "SUCCESS")
                    
        elif side == 'Horizontal':
            for x in range(len(horizontalGrid)):
                if ((constant - 1 < horizontalGrid[x][0][1] < constant + 1) and (beginning <= horizontalGrid[x][0][0] <= end)):
                    horizontalGrid[x] = (horizontalGrid[x][0], horizontalGrid[x][1], side)
                    print(horizontalGrid[x], "SUCCESS")
        else:
            print("Incorrect format for side:", side, " constant:", constant, " beginning:", beginning, " end:", end)

    def create_walls():
        print("TRY")
        Backgrounds.new_wall('Vertical', 202, 480, 610)
        Backgrounds.new_wall('Horizontal', 654, 202, 404)
        Backgrounds.new_wall('Vertical', 404, 654, 785)
        Backgrounds.new_wall('Horizontal', 785, 404, 875)
        
        Backgrounds.new_wall('Vertical', 875, 785, 872)
        Backgrounds.new_wall('Horizontal', 872, 875, 1010)
        Backgrounds.new_wall('Vertical', 1010, 785, 872)
        Backgrounds.new_wall('Horizontal', 785, 1010, 1077)
        
        Backgrounds.new_wall('Vertical', 1077, 741, 785)
        Backgrounds.new_wall('Horizontal', 741, 1077, 1212)
        Backgrounds.new_wall('Vertical', 1212, 654, 741)
        Backgrounds.new_wall('Horizontal', 654, 943, 1212)
        
        Backgrounds.new_wall('Vertical', 943, 567, 610)
        Backgrounds.new_wall('Horizontal', 567, 808, 943)
        Backgrounds.new_wall('Vertical', 808, 392, 523)
        Backgrounds.new_wall('Horizontal', 392, 808, 943)
        
        Backgrounds.new_wall('Vertical', 943, 261, 349)
        Backgrounds.new_wall('Horizontal', 261, 875, 943)
        Backgrounds.new_wall('Vertical', 875, 218, 218)
        Backgrounds.new_wall('Horizontal', 218, 606, 875)
        
        Backgrounds.new_wall('Vertical', 606, 218, 218)
        Backgrounds.new_wall('Horizontal', 261, 538, 606)
        Backgrounds.new_wall('Vertical', 538, 261, 349)
        Backgrounds.new_wall('Horizontal', 392, 538, 673)
        
        Backgrounds.new_wall('Vertical', 673, 392, 523)
        Backgrounds.new_wall('Horizontal', 567, 538, 673)
        Backgrounds.new_wall('Vertical', 538, 480, 523)
        Backgrounds.new_wall('Horizontal', 480, 202, 538)
        
    def check_collision(pos, hitbox, character):
        collisionDir = []
        prime_rect = hitbox # setting and getting hitboxes
        player_rect = player.hitbox()
        
        var = [10,10] if character == "projectile" else [15, 45]
        
        
        
        # Check vertical walls
        # Check vertical walls
        for wall in verticalGrid:
            if wall[2] == 'Vertical':  # Check if the wall is impassable
                wall_x = wall[0][0]  # x-coordinate of the vertical wall
                wall_y1 = wall[0][1]  # y-coordinate of the top start point
                wall_y2 = wall[1][1]  # y-coordinate of the bottom end point

                # Check if the player's new position overlaps with the wall
                if (wall_x < pos[0] < wall_x + var[0] and
                    wall_y1 - var[1] < pos[1] < wall_y2) and not('left' in collisionDir):                               
                    collisionDir.append('left') # Collision detected

                if (wall_x - var[0] < pos[0] < wall_x and
                    wall_y1 - var[1] < pos[1] < wall_y2) and not('right' in collisionDir):               
                    collisionDir.append('right')



        for wall in horizontalGrid:
            if wall[2] == 'Horizontal':  # Check if the wall is impassable
                wall_y = wall[0][1]  # y-coordinate of the horizontal wall
                wall_x1 = wall[0][0]  # x-coordinate of the left start point
                wall_x2 = wall[1][0]  # x-coordinate of the right end point

                    # Check if the player's new position overlaps with the wall
                if (wall_y <= pos[1] + 10 <= wall_y + var[0] and                
                    wall_x1 - 10 <= pos[0] <= wall_x2 + 10) and not('up' in collisionDir):
                    collisionDir.append('up')  # Collision detected



                if (wall_y - var[0] < pos[1] + var[1] - 5 < wall_y and 
                    wall_x1  - 10< pos[0] < wall_x2+10) and not('down' in collisionDir):
                    collisionDir.append('down')  # Collision detected

        if character == 'enemy':
            for enemy in enemies:
                if hitbox == enemy.hitbox():
                    
                    prime_rect = enemy.hitbox()
                    
            for enemy in enemies:
                if hitbox != enemy.hitbox(): 
                    enemy_rect = enemy.hitbox()
                    #Checks collision of prime on right side of enemies and player
                    if ((prime_rect[2] >= enemy_rect[0] and prime_rect[0] < enemy_rect[0] and \
                       prime_rect[3] > enemy_rect[1]  and prime_rect[1] < enemy_rect[3]) or \
                       (prime_rect[2] >= player_rect[0] and prime_rect[0] < player_rect[0] and \
                       prime_rect[3] > player_rect[1]  and prime_rect[1] < player_rect[3])) and not('right' in collisionDir):
                        collisionDir.append('right')  

                    # Check for collision on the left side of the prime and the right side of the enemy
                    if ((prime_rect[0]  <= enemy_rect[2] and prime_rect[2] > enemy_rect[2] and \
                       prime_rect[3] > enemy_rect[1] and prime_rect[1] < enemy_rect[3]) or \
                       (prime_rect[0]  <= player_rect[2] and prime_rect[2] > player_rect[2] and \
                       prime_rect[3] > player_rect[1] and prime_rect[1] < player_rect[3])) and not('left' in collisionDir):
                        collisionDir.append('left')

                    # Check for collision on the bottom side of the prime and the top side of the enemy
                    if ((prime_rect[3] >= enemy_rect[1] and prime_rect[1] < enemy_rect[1] and \
                       prime_rect[2] > enemy_rect[0] and prime_rect[0]  < enemy_rect[2]) or \
                       (prime_rect[3] >= player_rect[1] and prime_rect[1] < player_rect[1] and \
                       prime_rect[2] > player_rect[0] and prime_rect[0]  < player_rect[2])) and not('down' in collisionDir):
                        collisionDir.append('down')

                    # Check for collision on the top side of the prime and the bottom side of the enemy
                    if ((prime_rect[1] <= enemy_rect[3] and prime_rect[3] > enemy_rect[3] and \
                       prime_rect[2] > enemy_rect[0] and prime_rect[0]  < enemy_rect[2]) or \
                       (prime_rect[1] <= player_rect[3] and prime_rect[3] > player_rect[3] and \
                       prime_rect[2] > player_rect[0] and prime_rect[0]  < player_rect[2])) and not('up' in collisionDir):
                        collisionDir.append('up')  




        return collisionDir
    
class Keys:
    def keydown(key):
        """Handle key press events."""
        if key == simplegui.KEY_MAP["a"]:
            player.keys["a"] = True
        elif key == simplegui.KEY_MAP["d"]:
            player.keys["d"] = True
        elif key == simplegui.KEY_MAP["w"]:
            player.keys["w"] = True
        elif key == simplegui.KEY_MAP["s"]:
            player.keys["s"] = True
        elif key == simplegui.KEY_MAP["j"]:
            player.keys["j"] = True

    def keyup(key):
        """Handle key release events."""
        if key == simplegui.KEY_MAP["a"]:
            player.keys["a"] = False
        elif key == simplegui.KEY_MAP["d"]:
            player.keys["d"] = False
        elif key == simplegui.KEY_MAP["w"]:
            player.keys["w"] = False
        elif key == simplegui.KEY_MAP["s"]:
            player.keys["s"] = False
        elif key == simplegui.KEY_MAP["j"]:
            player.keys["j"] = False

class Update:  
    def update():
        global SCORE
        """Update player movement and animation."""
        player.move()
        player.update_animation()
        for NPC in NPCs:
            NPC.update_animation()
        for enemy in enemies:    
            enemy.update_animation(player)
            if enemy.state == "dead" and enemy.frame_index == 0:
                enemies.remove(enemy)
                SCORE += 10
        for ranged_enemy in ranged_enemies:    
            ranged_enemy.update_animation(player)
            if ranged_enemy.state == "dead" and ranged_enemy.frame_index == 0:
                ranged_enemies.remove(ranged_enemy)
                SCORE += 50
        for projectile in bouncing_objects:
            projectile.update()
            
        for exmplosion in exploding_objects:
            exmplosion.update()
        #print (enemies)
        if enemies == []:
            new_wave()
            
        healing_potion.update()
                
                
            
    def draw(canvas):
        """Draw game scene."""
        Update.update()

        # Calculate camera position
        camera_x = player.pos[0] - WIDTH // 2
        camera_y = player.pos[1] - HEIGHT // 2  

        fixed_x = max(0, min(camera_x, BKG_2_WIDTH - WIDTH))
        fixed_y = max(0, min(camera_y, BKG_2_HEIGHT - HEIGHT))

        # Draw background
        Update.draw_image(canvas, BKG_2, fixed_x, fixed_y, scale=3)

        # Draw main map
        Update.draw_image(canvas, BACKGROUND, camera_x, camera_y, scale=1)

        # Draw player
        player.draw(canvas, camera_x, camera_y)
        
        # Draw enemies
        for enemy in enemies:
            enemy.draw(canvas, camera_x, camera_y)
        
        for NPC in NPCs:
            NPC.draw(canvas, camera_x, camera_y)
        
        for ranged_enemy in ranged_enemies:
            ranged_enemy.draw(canvas, camera_x, camera_y)
        
        for fireball in bouncing_objects:
            fireball.drawSprite(canvas, camera_x, camera_y)
            
        for explosion in exploding_objects:
            explosion.drawExplosion(canvas, camera_x, camera_y)
            
        healing_potion.draw(canvas, camera_x, camera_y)
            
    
    
    def draw_image(canvas, image, camera_x, camera_y, scale=1):
        """Draw an image with the given parameters."""

        img_width = image.get_width()
        img_height = image.get_height()
        
        if img_width <= 0 or img_height <= 0:
            canvas.draw_text("Loading Image...", (WIDTH // 2 - 60, HEIGHT // 2), 20, "White")
            return
        
        canvas.draw_image(image,
            (img_width / 2, img_height / 2),  # Image center
            (img_width, img_height),  # Original size
            (WIDTH / 2 - (camera_x - (img_width - WIDTH) / 2),
             HEIGHT / 2 - (camera_y - (img_height - HEIGHT) / 2)),
            (img_width * scale, img_height * scale)  # Scale image
        )
        
        
        canvas.draw_text(f"Lives: {LIVES}", (10, 20), 20, "White")
        canvas.draw_text(f"Score: {SCORE}", (220, 40), 20, "White")
        canvas.draw_text(f"Wave: {WAVE}", (220, 20), 20, "White")

        # Check if assets are still loading
        if BACKGROUND.get_width() <= 0 or BACKGROUND.get_height() <= 0:
            canvas.draw_text("Loading Background...", (WIDTH // 2 - 60, HEIGHT // 2), 20, "White")
            return

        if (IDLE_IMAGE.get_width() <= 0 or RUN_IMAGE.get_width() <= 0 or 
            IDLE_FLIPPED.get_width() <= 0 or RUN_FLIPPED.get_width() <= 0):
            canvas.draw_text("Loading...", (WIDTH // 2 - 40, HEIGHT // 2), 20, "White")
            return

    def click(canvas):
        this = 0

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

def new_wave():
    #print("new wave")
    global player, enemies, WAVE
    WAVE += 1
    camera_x = player.pos[0] - WIDTH // 2
    camera_y = player.pos[1] - HEIGHT // 2 
    enemy_start = [WIDTH / 2 - (camera_x - (BACKGROUND_WIDTH - WIDTH) / 2),
                   HEIGHT / 2 - (camera_y - (BACKGROUND_HEIGHT - HEIGHT) / 2)]
    enemies = []
    amount_of_enemies = 3 * WAVE

    # Spawns enemies randomly around the map
    for i in range(amount_of_enemies):
        x_variation = random.randint(100, 300) #CHANGE FOR WHERE YOU WANT ENEMIES TO SPAWN
        y_variation = random.randint(0, 100)
        enemy = Enemy(enemy_start[0], enemy_start[1], PLAYER_SPEED - 2, 100, "Player 1", 15, 1, player, x_variation, y_variation)
        enemies.append(enemy)
    healing_potion.activate()
        
def initialize_game():
    global player, enemies, ranged_enemies, bouncing_objects, exploding_objects, NPCs, WAVE, SCORE, healing_potion
    SCORE = 0
    WAVE = 0
    # Initialize player
    NPCs = []
    NPCs.append(NPC([865,745]))
    player = Player(743, 254, PLAYER_SPEED, 100, "Player 1", 15, 1)
    camera_x = player.pos[0] - WIDTH // 2
    camera_y = player.pos[1] - HEIGHT // 2 

    # Initialize enemies
    enemy_start = [WIDTH / 2 - (camera_x - (BACKGROUND_WIDTH - WIDTH) / 2),
                   HEIGHT / 2 - (camera_y - (BACKGROUND_HEIGHT - HEIGHT) / 2)]
    enemies = []
    amount_of_enemies = 3
    
    ranged_enemies = []
    amount_of_ranged = 1
    
    bouncing_objects = []
    exploding_objects = []
    healing_potion = HealingPotion(905, 775)
    
    
    for i in range(amount_of_ranged):
        x_variation = random.randint(100, 300)
        y_variation = random.randint(0, 100)
        enemy = RangedEnemy(enemy_start[0], enemy_start[1], PLAYER_SPEED - 2, 100, "Player 1", 15, 1, player, x_variation, y_variation)
        ranged_enemies.append(enemy)
        
    # Spawns enemies randomly around the map
    for i in range(amount_of_enemies):
        x_variation = random.randint(100, 300)
        y_variation = random.randint(0, 100)
        enemy = Enemy(enemy_start[0], enemy_start[1], PLAYER_SPEED - 2, 100, "Player 1", 15, 1, player, x_variation, y_variation)
        enemies.append(enemy)

    # Run all initial set-ups
    Backgrounds.create_grid()
    Backgrounds.create_walls()
    
def clear_dead(pos):
    #for prime in enemies:
        #if pos == prime.get_p():
            #enemies.remove(prime)
    print("dead clear")
    
def game_reset():
    global DEATH_SCREEN
    global LIVES
    global SCORE
    global HIGH_SCORE
    frame.set_draw_handler(Welcome.draw)
    frame.set_mouseclick_handler(Welcome.welcome_click)
    DEATH_SCREEN = True
    LIVES = 3
    if SCORE >= HIGH_SCORE:	
        HIGH_SCORE = SCORE
    
    enemies.clear()
    

# Create the game frame
frame = simplegui.create_frame("Animated Player", WIDTH, HEIGHT)
frame.set_draw_handler(Welcome.draw)
frame.set_mouseclick_handler(Welcome.welcome_click)
frame.add_button("Test restart", game_reset, 150)

# Start background music
BACKGROUND_MUSIC.set_volume(0.25)
BACKGROUND_MUSIC.play()

# Start the game
frame.start()
