import pygame

# Define hex numbers used in seven segment display
nums = [0x7E, 0x30, 0x6D, 0x79, 0x33, 0x5B, 0x5F, 0x70, 0x7F, 0x7B]

# Depending on the number, display in ssd
def ssdDisp(number, shift):
	if ( (number >> shift) & 1 == 1):
		return (255,0,0)
	else:
		return (0,0,0)

# Draw the whole digit
def drawDigit(digit, rel_pos):
	pygame.draw.rect(win, ssdDisp(nums[digit],6), (rel_pos, 50, width,height))
	# B
	pygame.draw.rect(win, ssdDisp(nums[digit],5), (rel_pos+50, 60, height,width))
	# C
	pygame.draw.rect(win, ssdDisp(nums[digit],4), (rel_pos+50, 120, height,width))
	# D
	pygame.draw.rect(win, ssdDisp(nums[digit],3), (rel_pos, 170, width,height))
	# E
	pygame.draw.rect(win, ssdDisp(nums[digit],2), (rel_pos-10, 120, height,width))
	# F
	pygame.draw.rect(win, ssdDisp(nums[digit],1), (rel_pos-10, 60, height,width))
	# G
	pygame.draw.rect(win, ssdDisp(nums[digit],0), (rel_pos, 110, width, height))

### Actual program
print('Enter the first number:')
first = int(input())
print('Enter the second number:')
second = int(input())

# Convert to ssd
first2 = first % 10
first1 = int(first/10)
second2 = second % 10
second1 = int(second/10)

# Add and convert to ssd
summ = first + second
if (summ > 100):
	summ1 = 1
	summ3 = (summ - 100) % 10
	summ2 = int((summ-100)/10)
else:
	summ1 = 0
	summ3 = summ % 10
	summ2 = int(summ/10)

# Initialize pygame
pygame.init()

# Create window
win = pygame.display.set_mode((800,250))
pygame.display.set_caption('Seven Segment Display')



# Create running loop
width = 46
height = 9
run = True
while run:
	pygame.time.delay(300)

	# Digit 1
	drawDigit(first1,50)
	# Digit 2
	drawDigit(first2,129)
	
	# Plus sign
	pygame.draw.rect(win, (255,0,0), (199,110,width,height))
	pygame.draw.rect(win, (255,0,0), (219,90,height,width))

	# Digit 3
	drawDigit(second1,269)
	# Digit 4
	drawDigit(second2,349)

	# Equals sign
	pygame.draw.rect(win, (255,0,0), (419,100,width,height))
	pygame.draw.rect(win, (255,0,0), (419,120,width,height))

	# Digit 5
	drawDigit(summ1,489)
	# Digit 6
	drawDigit(summ2,564)
	# Digit 7
	drawDigit(summ3,644)

	# # Display next number
	pygame.display.update()

	# If user presses X, quit the loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


pygame.quit()