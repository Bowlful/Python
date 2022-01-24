import pygame
from random import *

# 레벨에 맞게 설정
def setup(level):
    #얼마동안 숫자를 보여줄지
    global display_time
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)


    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) # 많약에 20을 초과하면 20으로 처리

    # 실제 화면에 grid형태로 숫자를 랜덤으로 배치
    suffle_grid(number_count)

# 숫자 섞기
def suffle_grid(number_count):
    rows = 5
    colums = 9
    
    cell_size = 130 # 각 Grid cell 별 가로, 세로 크기
    button_size = 110 # Grid cell 내에 실제로 그려질 버튼크기
    screen_left_margin = 55 # 전체 스크린 왼쪽 여백
    screen_top_margin = 20 # 전체 스크린 윗족 여밴

    #[0, 0,0 , 0, 0, 0, 0, 0, 0]
    grid = [[0 for col in range(colums)] for row in range(rows)] # 5*9의 격자

    number = 1 # 시작 숫자를 1부터 number_count 까지. 만약 5라면 5까지 숫자를 랜덤으로 배치
    while number <= number_count:
        row_idx = randrange(0, rows) # 0 ~ 4중에서 랜덤
        col_idx = randrange(0, colums) # 0 ~ 8중에서 랜덤

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number #숫자 지정
            number += 1

            # 현재 gird cell 위치 기준으로 x, y위치 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색으로 동그라미를 그리는데 중심좌표는 start_button의 중심좌표를 따라가고, 반지름은 60, 선두께는 5

    msg = game_font.render(f"{curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)


def dispaly_game_screen(): #게임 화면 보여주기
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> sec
        if elapsed_time > display_time:
            hidden = True


    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            #버튼 사각형을 그리기
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # 실제 숫자 텍스트
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)

#pos에 해당하는 버튼확인
def check_buttons(pos):
    global start, start_ticks

    if start: #게임이 시작했으면
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks() # 타이머 시작(현재 시간을 저장)

def check_number_buttons(pos):
    global hidden, start, curr_level
    game_o = False
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                del number_buttons[0]
                if not hidden:
                    hidden = True # 숫자클릭
            else:
                msg = game_font.render(f"Your level is {curr_level}", True, WHITE)
                msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))

                screen.fill(BLACK)
                screen.blit(msg, msg_rect)
                pygame.display.update()
                pygame.time.delay(1500)
                game_o = True
                game_over()
                break
                
    # 모든 숫자를 다 맞혔다면? 레벨을 높여서 진행
    if game_o == False:
        if len(number_buttons) == 0:
            start = False
            hidden = False
            curr_level += 1
            setup(curr_level)

#게임 종료 처리
def game_over():
    global start, hidden, curr_level, number_buttons
    start = False
    hidden = False
    curr_level = 1
    number_buttons = []
    setup(curr_level)
    
    

    


#초기화
pygame.init()
screen_width = 1280 #가로 크기
screen_height = 720 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) #폰트

#시작버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

#색깔
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
number_buttons = [] # 플레이어가 눌러야 하는 버튼
curr_level = 1
display_time = None # 숫자를 보여주는 시간
start_ticks = None #시간 계산(현재 시간정보를 저장)

#게임 시작 여부
start = False

# 숫자 숨김 여부 (사용자가 1을 클릭했거나, 보여주는 시간을 초과했을때)
hidden = False

setup(curr_level)

#게임 루프
running = True #게임이 실행중인가?
while running:
    Click_pos = None

    #이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type ==pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False # 게임이 더이상 실행중이 아님
        elif event.type == pygame.MOUSEBUTTONUP:
            Click_pos = pygame.mouse.get_pos()

    # 화면전체를 검은색으로 
    screen.fill(BLACK)

    if start:
        dispaly_game_screen() #게임 화면을 표시
    else:
        display_start_screen() #시작 화면 표시

    # 사용자가 클릭한 좌표값이 있다면(어딘가 클릭을 했다면)
    if Click_pos:
        check_buttons(Click_pos)

    #화면 업데이트
    pygame.display.update()

#게임 종료
pygame.quit()