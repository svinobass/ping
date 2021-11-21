from pygame import *

FPS = 144

window = display.set_mode((1280, 720))
display.set_caption(".")
background = transform.scale(image.load("d.png"), (1280, 720))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, playerx_size, playery_size, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (playerx_size, playery_size))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
    

player1 = Player("pong.png", 30, 200, 50, 250, 15)
player2 = Player("pong.png", 30, 200, 1200, 250, 15)

game = True
while game:
    clock = time.Clock()
    clock.tick(FPS)

    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    player.fire()
                    num_fire = num_fire + 1
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True

    window.blit(background, (0, 0))
   
    player1.update1()
    player2.update2()

    player1.reset()
    player2.reset()

    display.update()
