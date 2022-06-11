# 보석 클래스, 보석이미지 불러오기
from cProfile import run
from cgitb import small
import pygame
import os

# 보석 클래스


class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()  # 상속받았으니 초기화
        # sprite를 받아 쓰기 위해서는 두개의 맴버변수를 정의해주어야한다.
        self.image = image  # 이미지정보
        self.rect = image.get_rect(center=position)  # 캐릭터정보


def setup_gemstone():
    # 작은 금
    # 0번째 이미지를 해당 위치에 둔다.
    small_gold = Gemstone(gemstone_images[0], (200, 380))


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("gold miner")
clock = pygame.time.Clock()


current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")),
    pygame.image.load(os.path.join(current_path, "big_gold.png")),
    pygame.image.load(os.path.join(current_path, "stone.png")),
    pygame.image.load(os.path.join(current_path, "diamond.png"))]

# 파이게임이 제공해주는 sprite 클래스를 사용.
# 그룹을 사용하면 그룹에 모든 보석을 집어넣고 한번에 처리

# 보석 그룹 만들기
gemstone_group = pygame.sprite.Group()

setup_gemstone()  # 게임에 원하는만큼의 보석을 정의

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()
