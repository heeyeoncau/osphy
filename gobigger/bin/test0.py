import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

# 게임 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Pygame 화면 초기화
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Game')

# 일시정지 상태 플래그
paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # ESC 키를 누르면 일시정지 상태를 토글
                paused = not paused

    if not paused:
        # 게임 로직 수행
        screen.fill((255, 255, 255))  # 예시로 흰 배경을 그림
        pygame.display.flip()
        clock.tick(60)  # FPS를 60으로 유지

    else:
        # 일시정지 화면을 그림
        font = pygame.font.Font(None, 36)
        text = font.render('Paused', True, (255, 0, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()

        # 일시정지 상태에서는 FPS를 낮춰 화면이 갱신되지 않도록 함
        clock.tick(5)
