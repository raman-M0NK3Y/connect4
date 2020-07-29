import pygame
import sys
import math

ROWS = 6
COLUMNS = 7
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLOCK_SIZE = 100
GRAY =  (128,128,128)
BLUE = (0,0,255)
BLACK = (0,0,0)
RADIUS = int(BLOCK_SIZE/2 -5)

pygame.init() 

def create_board():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0] 
    ] #6 rows, 7 cols of zeros
    return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece


def check_valid_location(board, col):
	return board[5][col] == 0

def get_next_open_row(board, col):
	for r in range(ROWS):
		if board[r][col] == 0:
			return r



def check_win(board, piece):
	#have to check horizontal, vertical, and diagonals
	#horzontal check win
	for r in range(ROWS):
		for c in range(COLUMNS - 3):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	#vertical check win
	for r in range(ROWS - 3):
		for c in range(COLUMNS):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	#diagonal check win positive
	for r in range(ROWS -3):
		for c in range(COLUMNS - 3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	#diagonal check win negative
	for r in range(3, ROWS):
		for c in range(COLUMNS - 3):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True
		

def print_board(board):
	for row in reversed(range(ROWS)):
		print(board[row])
		#return (board[row]) ###

#pygame graphics
def draw_board(board):
	board = board[::-1]
	for r in range(ROWS):
		for c in range(COLUMNS):
			pygame.draw.rect(screen, BLUE, (c * BLOCK_SIZE, r * BLOCK_SIZE + BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
			if board[r][c] == 0:
				pygame.draw.circle(screen, GRAY, (int(c * BLOCK_SIZE + BLOCK_SIZE / 2), int(r * BLOCK_SIZE + BLOCK_SIZE + BLOCK_SIZE / 2)), RADIUS)
			elif board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c * BLOCK_SIZE + BLOCK_SIZE / 2), int(r * BLOCK_SIZE + BLOCK_SIZE + BLOCK_SIZE / 2)), RADIUS)
			else:
				pygame.draw.circle(screen, YELLOW, (int(c * BLOCK_SIZE + BLOCK_SIZE / 2), int(r * BLOCK_SIZE + BLOCK_SIZE + BLOCK_SIZE / 2)), RADIUS)


        	
        	
	
	
	pygame.display.update()



	

board = create_board()
print_board(board)

#turn = 0



width = COLUMNS * BLOCK_SIZE
height = (ROWS + 1) * BLOCK_SIZE

#

screen = pygame.display.set_mode((width, height))
draw_board(board) ########
pygame.display.update()

font = pygame.font.SysFont("comicsans", 60) ####
run = True
turn = 0
count = 0 #####################

def animate_move(board, row, col, piece):
 	xposition = int(col*BLOCK_SIZE + BLOCK_SIZE/2)
 	yposition = int(BLOCK_SIZE/2)
 	COLOR = RED
 	if piece == 2:
  		COLOR = YELLOW
 	yspeed = 1
 	while yposition < (height-row*BLOCK_SIZE-BLOCK_SIZE/2):
  		yspeed += 2.3
  		yposition += yspeed
  		pygame.draw.rect(screen, GRAY, (0,0, width, BLOCK_SIZE))
  		draw_board(board)
  		pygame.draw.circle(screen, COLOR, (xposition, int(yposition)), RADIUS)
  		pygame.display.update()

 	return True

def display_text(screen, text, color):
	#font = pygame.font.SysFont("comicsans", size)
	label = font.render(text, 1, color)
	screen.blit(label, (180,50))
	#hasRun = True
#run = True

def check_draw(board, piece):
	global run, count
	# for c in range(COLUMN_COUNT):
	# 	if (board[ROW_COUNT-1][c] == 0 and winning_move(board, piece)) :
	# 		return False
			
			#pass#and winning_move(board, piece))
			#if not winning_move(board, piece):
	if not check_win(board, piece) and count == 42:
		display_text(screen, "It's A Draw", (255,255,255))
		run = False

def event_handling(board, col, piece, screen,text, color):
	#if turn == 1:
		#piece = 2
		#text = 'Player 2 wins!!'
		#color = YELLOW
	#posx = event.pos[0]
	global turn, run, count
	#while run:

	if check_valid_location(board, col):
		row = get_next_open_row(board, col)
		animate_move(board, row, col, piece)
		drop_piece(board, row, col, piece)
		count += 1##########################

		if check_win(board, piece):
							
			#screen.blit(label, (180,50))
			display_text(screen, text, color)

							
			run = False
		else:
			check_draw(board, piece)

	else:
		print("Invalid Move")
		turn -= 1
		count -=1 ##############

def main(screen):
	# turn = 0
	# run = True
	global turn, run
	board = create_board()
	print_board(board)
	draw_board(board)

	while run:
		pygame.init()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEMOTION:####
				pygame.draw.rect(screen, GRAY, (0,0, width, BLOCK_SIZE))
				posx = event.pos[0]
				if turn == 0:
					pygame.draw.circle(screen, RED, (posx, int(BLOCK_SIZE/2)), RADIUS)
				else: 
					pygame.draw.circle(screen, YELLOW, (posx, int(BLOCK_SIZE/2)), RADIUS)
				pygame.display.update()####

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(screen, GRAY, (0,0, width, BLOCK_SIZE))
			
				# Ask for Player 1 Input
				if turn == 0:
					posx = event.pos[0]
					col = int(math.floor(posx/100))
					event_handling(board, col, 1, screen, "Player 1 wins!!", RED)

				


				# # Ask for Player 2 Input
				else:				
					posx = event.pos[0]
					col = int(math.floor(posx/100))
					event_handling(board, col, 2, screen, "Player 2 wins!!", YELLOW)

					

					

				print_board(board)
				draw_board(board)

				turn = (turn + 1) % 2

				#if run == False: 
					#play_again()
					#label = font.render("Press Any Key To Play", 1, (255,255,255))
					#screen.blit(label, (80,10))
					#pygame.display.update()
					#for event in pygame.event.get():
						#if event.type == pygame.QUIT:
							#pygame.display.quit()
						#if event.type == pygame.KEYDOWN:
							#main(screen) ----
#main(screen)

#def play_again():
	#pygame.draw.rect(screen, GRAY, (0,0, width, SQUARESIZE))
	#label = font.render("Press Any Key To Play", 1, (255,255,255))
	#screen.blit(label, (80,10))
	#for event in pygame.event.get():
		#if event.type == pygame.QUIT:
			#pygame.display.quit()
		#if event.type == pygame.KEYDOWN:
			#main(screen)
			

				
					
def main_menu(screen):
	go = True
	global run, turn, count 
	while go:

		#pygame.draw.rect(screen, GRAY, (0,0, width, SQUARESIZE))
		#screen.fill(BLACK)
		label = font.render("Press Any Key To Play", 1, (255,255,255))
		#screen.lock()
		screen.blit(label, (100,10)) ####
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				go = False
			if event.type == pygame.KEYDOWN:
				turn = 0
				count = 0
				run = True
				main(screen)
	pygame.display.quit()

#screen = pygame.display.set_mode((width,height))
#screen.lock()
#draw_board(board)
#pygame.display.update()
main_menu(screen)#######






				