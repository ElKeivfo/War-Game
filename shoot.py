import pygame,sys
import random
import time
from pygame import mixer



    

def game(highest_score):
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    pygame.display.set_caption("Shoot Before You Are Shot")
    icon = pygame.image.load('aim.jpg')
    pygame.display.set_icon(icon)
    background = pygame.image.load('sky.jpg')

    mixer.music.load('warmusic.mp3')
    mixer.music.play(-1)

    target = pygame.image.load('aim2.jpg')
    targetX=144
    targetY=0

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    textX = 10
    textY = 10
    time_textX = 256
    time_textY = 0

    e1 = pygame.image.load('e1.png')
    e2 = pygame.image.load('e2 (3).png')
    e3 = pygame.image.load('e4 (2).png')
    e4 = pygame.image.load('e4 (3).png')
    e5 = pygame.image.load('e4 (4).png')

    def show_score(x,y):
        score = font.render('SCORE: '+str(score_value),True,(0,0,0))
        screen.blit(score, (x,y))

    def show_time(x,y):
        mins = round(time.time()-start_time) // 60
        sec = round(time.time()-start_time) % 60
      
        timer = font.render("{0}:{1}".format(str(mins),str(sec)),True,(0,0,0))
        screen.blit(timer, (x,y))


    def set_enemy():
        enemy_sizes = [35,75,150,250]
        e1 = pygame.image.load('e1.png')
        e2 = pygame.image.load('e2 (3).png')
        e3 = pygame.image.load('e4 (2).png')
        e4 = pygame.image.load('e4 (3).png')
        e5 = pygame.image.load('e4 (4).png')
        enemies = [e1,e2,e3,e4,e5]
        enemyX=random.randrange(0,800)
        enemyY=random.randrange(0,500)
        enemy_size = random.choice(enemy_sizes)
        e = random.choice(enemies)
        if e == e1 or e == e2:
            m = 'r'
        else:
            m = 'l'
        if enemyX <= 0-256:
            enemyX = 0-256
        if enemyX >= 800-256:
            enemyX = 800-256
        if enemyY <= 0-256:
            enemyY = 0-256
        if enemyY >= 500-256:
            enemyY = 500-256
        return enemyX,enemyY,enemy_size,e,m

    enemyX,enemyY,enemy_size,e,m = set_enemy()

    def target_aquired(x,y):
        
        screen.blit(target,(x,y))

    def enemy(x,y,enemy_size,e):
        
        new_e = pygame.transform.scale(e, (enemy_size, enemy_size))
        screen.blit(new_e, (x,y))










    running  = True
    start_time=time.time()
    while running:

        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        
        if m == 'r':
            enemyX -= 0.3
        else:
            enemyX += 0.3

        if enemyX <= 0 or enemyX >= 800:
            enemyX,enemyY,enemy_size,e,m = set_enemy()
            enemy(enemyX,enemyY,enemy_size,e)
        
        
        
        
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

       

            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                targetX -= 0.5
            if event.key == pygame.K_RIGHT:
                targetX += 0.5
            if event.key == pygame.K_UP:
                targetY -= 0.5
            if event.key == pygame.K_DOWN:
                targetY += 0.5
            if event.key == pygame.K_RETURN:
                gun = mixer.Sound('gun.mp3')
                gun.play()
            if event.key == pygame.K_RETURN and (enemyX > targetX + (250-enemy_size) and enemyX+(enemy_size)  < targetX+512 - (256-enemy_size)) and (enemyY > targetY + (250-enemy_size) and enemyY+(enemy_size)< targetY+512 - (256-enemy_size)):

                score_value += 1
                gun = mixer.Sound('gun.mp3')
                gun.play()
                
                
                enemyX,enemyY,enemy_size,e,m = set_enemy()
                enemy(enemyX,enemyY,enemy_size,e)

                
                    
                
                

        if targetX <= 0-256:
            targetX = 0-256
        if targetX >= 800-256:
            targetX = 800-256
        if targetY <= 0-256:
            targetY = 0-256
        if targetY >= 500-256:
            targetY = 500-256



        

        show_time(time_textX,time_textY)
        show_score(textX,textY)
        enemy(enemyX,enemyY,enemy_size,e)
        target_aquired(targetX,targetY)

        if round(time.time()-start_time) == 90:
            end_game(score_value,highest_score)

            
        
        pygame.display.update()




def end_game(score_value,highest_score):
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    pygame.display.set_caption("Shoot Before You Are Shot")
    icon = pygame.image.load('aim.jpg')
    pygame.display.set_icon(icon)
    pic2 = pygame.image.load('a2.png')
    start = pygame.image.load('pg.png').convert_alpha()
    exiting = pygame.image.load('ex.png').convert_alpha()
    font = pygame.font.Font('freesansbold.ttf',32)
    if score_value > highest_score:
        highest_score = score_value
    score = font.render('SCORE: '+str(score_value),True,(0,0,0))
    disp_highest_score = font.render('HIGHEST SCORE: '+str(highest_score),True,(0,0,0))
    
    
        

    class Button():
        def __init__(self, x, y, image, scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):

            
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
            screen.blit(self.image, (self.rect.x, self.rect.y))

            return self.clicked
            
    start_button = Button(200,200,start,0.8)
    exit_button = Button(500,200,exiting,0.8)

    
    running = True
    while running:

        
    
        screen.fill((144, 172,144))

        screen.blit(pic2, (20,170))

        screen.blit(score, (10,10))
        screen.blit(disp_highest_score, (10,50))
        
        if start_button.draw():
            
            game(highest_score)
        if exit_button.draw():
            
            pygame.quit()
            sys.exit()
            

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

        
        pygame.display.update()
    pygame.quit()







def main(highest_score):
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    pygame.display.set_caption("Shoot Before You Are Shot")
    icon = pygame.image.load('aim.jpg')
    pic = pygame.image.load('a1.png')
    pygame.display.set_icon(icon)
    start = pygame.image.load('st.png').convert_alpha()
    exiting = pygame.image.load('ex.png').convert_alpha()

    class Button():
        def __init__(self, x, y, image, scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):

            
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
            screen.blit(self.image, (self.rect.x, self.rect.y))

            return self.clicked
            
    start_button = Button(200,200,start,0.8)
    exit_button = Button(500,200,exiting,0.8)

    
    running = True
    while running:
        screen.fill((144, 172,144))

        screen.blit(pic, (10,0))

        
        if start_button.draw():
            
            game(highest_score)
        if exit_button.draw():
            
            pygame.quit()
            sys.exit()
            

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

        
        pygame.display.update()
    pygame.quit()
    
highest_score = 0
main(highest_score)            
