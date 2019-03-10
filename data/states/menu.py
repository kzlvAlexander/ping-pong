

import pygame as pg
from .. import tools
from .. import ball as ball_
import random

class Menu(tools.States):
    def __init__(self, screen_rect):
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        self.options = ['Play', 'Options', 'Quit']
        self.next_list = ['MODE', 'OPTIONS']
        self.title, self.title_rect = self.make_text('Ping Pong', (75,75,75), (self.screen_rect.centerx, 75), 150)
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 75
        self.menu_balls = []
        for i in range(15):
            random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            ball = ball_.Ball(self.screen_rect, 10,10, random_color, menu=True)
            ball.speed = random.randint(3,8)
            ball = self.menu_balls.append(ball)

    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        self.mouse_menu_click(event)

    def update(self, now, keys):
        for ball in self.menu_balls:
            ball.update(self.bogus_rect, self.bogus_rect)
        pg.mouse.set_visible(True)
        self.mouse_hover_sound()

    def render(self, screen):
        screen.fill(self.bg_color)
        for ball in self.menu_balls:
            ball.render(screen)
        screen.blit(self.title,self.title_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if opt[1].collidepoint(pg.mouse.get_pos()):
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
                
        
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/Megadeth.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
        
    def pre_render_options(self):
        font_deselect = pg.font.Font("resources/fonts/Megadeth.ttf",50)
        font_selected = pg.font.Font("resources/fonts/Megadeth.ttf",75)

        rendered_msg = {"des":[],"sel":[]}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, (255,255,255))
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, (255,0,0))
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend,d_rect))
            rendered_msg["sel"].append((s_rend,s_rect))
        self.rendered = rendered_msg
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
