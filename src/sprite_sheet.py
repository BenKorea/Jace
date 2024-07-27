import pygame
import sys

class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert()
    
    def get_image(self, x, y, width, height):
        # 스프라이트 시트에서 이미지를 잘라내기
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))  # 배경이 검정색일 경우 투명 처리
        return image

# 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Sheet Example")

# 색상 정의
BLACK = (0, 0, 0)

# 스프라이트 시트 로드
sprite_sheet = SpriteSheet('spritesheet.png')

# 스프라이트 이미지 추출
player_image = sprite_sheet.get_image(0, 0, 32, 48)

# 메인 루프
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 그리기
    screen.fill(BLACK)
    screen.blit(player_image, (100, 100))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 설정
    clock.tick(60)

# 종료
pygame.quit()
sys.exit()
