import random
import os
import json
import sys
from os.path import exists
import pygame
from pygame.locals import *
workingDirectory = os.path.split(os.path.abspath(__file__))[0]
deedDirectory = os.path.join(workingDirectory, "deedimages")
certificateDirectory = os.path.join(workingDirectory, "StockCerts")
chanceDirectory = os.path.join(workingDirectory, "chancecards")
commChestDirectory = os.path.join(workingDirectory, "commchestcards")
travelVoucherDirectroy = os.path.join(workingDirectory, "travelcards")
rollThreeDirectory = os.path.join(workingDirectory, "rollthreecards")
stockCertDirectory = os.path.join(workingDirectory, "stockcertificates")
saveFileVersion = "0.0.2"

pygame.init()
if os.path.exists(os.path.join(workingDirectory, "MONOPOLY_INLINE.ttf")):
	fontPath = os.path.join(workingDirectory, "MONOPOLY_INLINE.ttf")
elif pygame.font.match_font("bahnschrift") != None:
	fontPath = pygame.font.match_font("bahnschrift")
font = pygame.font.Font(fontPath, 24)
fontBig = pygame.font.Font(fontPath, 48)
window = pygame.display.set_mode((0,0))
pygame.display.set_caption("Ultimate Monopoly")
pygame.event.set_blocked(MOUSEMOTION)


class globalVariablesClass:
	def __init__ (self):
		self.backgroundColor = (55,171,200)
		self.displaySize = pygame.display.get_desktop_sizes()[0]
		self.dispHeight = self.displaySize[1]
		self.activePlayerNumber = None
		self.recentBankruptcyFlag = False
		self.currentPlayer = None

globalVars = globalVariablesClass()

def gameboardSpaceLookup(coords):
	lookupTable = [[[0.940*dispHeight,0.940*dispHeight],[0.825*dispHeight,0.940*dispHeight],[0.767*dispHeight,0.940*dispHeight],[0.709*dispHeight,0.940*dispHeight],[0.651*dispHeight,0.940*dispHeight],[0.593*dispHeight,0.940*dispHeight],[0.535*dispHeight,0.940*dispHeight],[0.477*dispHeight,0.940*dispHeight],[0.419*dispHeight,0.940*dispHeight],[0.361*dispHeight,0.940*dispHeight],[0.303*dispHeight,0.940*dispHeight],[0.245*dispHeight,0.940*dispHeight],[0.187*dispHeight,0.940*dispHeight],[0.129*dispHeight,0.940*dispHeight],[0.010*dispHeight,0.940*dispHeight],[0.010*dispHeight,0.825*dispHeight],[0.010*dispHeight,0.767*dispHeight],[0.010*dispHeight,0.709*dispHeight],[0.010*dispHeight,0.651*dispHeight],[0.010*dispHeight,0.593*dispHeight],[0.010*dispHeight,0.535*dispHeight],[0.010*dispHeight,0.477*dispHeight],[0.010*dispHeight,0.419*dispHeight],[0.010*dispHeight,0.361*dispHeight],[0.010*dispHeight,0.303*dispHeight],[0.010*dispHeight,0.245*dispHeight],[0.010*dispHeight,0.187*dispHeight],[0.010*dispHeight,0.129*dispHeight],[0.010*dispHeight,0.010*dispHeight],[0.129*dispHeight,0.010*dispHeight],[0.187*dispHeight,0.010*dispHeight],[0.245*dispHeight,0.010*dispHeight],[0.303*dispHeight,0.010*dispHeight],[0.361*dispHeight,0.010*dispHeight],[0.419*dispHeight,0.010*dispHeight],[0.477*dispHeight,0.010*dispHeight],[0.535*dispHeight,0.010*dispHeight],[0.593*dispHeight,0.010*dispHeight],[0.651*dispHeight,0.010*dispHeight],[0.709*dispHeight,0.010*dispHeight],[0.767*dispHeight,0.010*dispHeight],[0.825*dispHeight,0.010*dispHeight],[0.940*dispHeight,0.010*dispHeight],[0.940*dispHeight,0.129*dispHeight],[0.940*dispHeight,0.187*dispHeight],[0.940*dispHeight,0.245*dispHeight],[0.940*dispHeight,0.303*dispHeight],[0.940*dispHeight,0.361*dispHeight],[0.940*dispHeight,0.419*dispHeight],[0.940*dispHeight,0.477*dispHeight],[0.940*dispHeight,0.535*dispHeight],[0.940*dispHeight,0.593*dispHeight],[0.940*dispHeight,0.651*dispHeight],[0.940*dispHeight,0.709*dispHeight],[0.940*dispHeight,0.767*dispHeight],[0.940*dispHeight,0.825*dispHeight],[0.940*dispHeight,0.940*dispHeight]],[[0.818*dispHeight,0.818*dispHeight],[0.703*dispHeight,0.818*dispHeight],[0.647*dispHeight,0.818*dispHeight],[0.590*dispHeight,0.818*dispHeight],[0.534*dispHeight,0.818*dispHeight],[0.476*dispHeight,0.818*dispHeight],[0.420*dispHeight,0.818*dispHeight],[0.363*dispHeight,0.818*dispHeight],[0.306*dispHeight,0.818*dispHeight],[0.250*dispHeight,0.818*dispHeight],[0.135*dispHeight,0.818*dispHeight],[0.135*dispHeight,0.703*dispHeight],[0.135*dispHeight,0.647*dispHeight],[0.135*dispHeight,0.590*dispHeight],[0.135*dispHeight,0.534*dispHeight],[0.135*dispHeight,0.476*dispHeight],[0.135*dispHeight,0.420*dispHeight],[0.135*dispHeight,0.363*dispHeight],[0.135*dispHeight,0.306*dispHeight],[0.135*dispHeight,0.250*dispHeight],[0.135*dispHeight,0.135*dispHeight],[0.250*dispHeight,0.135*dispHeight],[0.306*dispHeight,0.135*dispHeight],[0.363*dispHeight,0.135*dispHeight],[0.420*dispHeight,0.135*dispHeight],[0.476*dispHeight,0.135*dispHeight],[0.534*dispHeight,0.135*dispHeight],[0.590*dispHeight,0.135*dispHeight],[0.647*dispHeight,0.135*dispHeight],[0.703*dispHeight,0.135*dispHeight],[0.818*dispHeight,0.135*dispHeight],[0.818*dispHeight,0.250*dispHeight],[0.818*dispHeight,0.306*dispHeight],[0.818*dispHeight,0.363*dispHeight],[0.818*dispHeight,0.420*dispHeight],[0.818*dispHeight,0.476*dispHeight],[0.818*dispHeight,0.534*dispHeight],[0.818*dispHeight,0.590*dispHeight],[0.818*dispHeight,0.647*dispHeight],[0.818*dispHeight,0.703*dispHeight],[0.818*dispHeight,0.818*dispHeight]],[[0.696*dispHeight,0.696*dispHeight],[0.585*dispHeight,0.696*dispHeight],[0.532*dispHeight,0.696*dispHeight],[0.479*dispHeight,0.696*dispHeight],[0.420*dispHeight,0.696*dispHeight],[0.367*dispHeight,0.696*dispHeight],[0.252*dispHeight,0.696*dispHeight],[0.252*dispHeight,0.585*dispHeight],[0.252*dispHeight,0.532*dispHeight],[0.252*dispHeight,0.479*dispHeight],[0.252*dispHeight,0.420*dispHeight],[0.252*dispHeight,0.367*dispHeight],[0.252*dispHeight,0.252*dispHeight],[0.367*dispHeight,0.252*dispHeight],[0.420*dispHeight,0.252*dispHeight],[0.479*dispHeight,0.252*dispHeight],[0.532*dispHeight,0.252*dispHeight],[0.585*dispHeight,0.252*dispHeight],[0.696*dispHeight,0.252*dispHeight],[0.696*dispHeight,0.367*dispHeight],[0.696*dispHeight,0.420*dispHeight],[0.696*dispHeight,0.479*dispHeight],[0.696*dispHeight,0.532*dispHeight],[0.696*dispHeight,0.585*dispHeight],[0.696*dispHeight,0.696*dispHeight]]]
	return lookupTable[coords[0]][coords[1]]

class Token(pygame.sprite.Sprite):
	def __init__(self, tokenChoice):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(tokenChoice + ".png")
		self.image = pygame.transform.scale(self.image, (displaySize[1]*0.05,displaySize[1]*0.05))
		self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = (0,0)
		self.gbCoords = [0,0]
		
	def MoveDraw(self):
		self.rect.topleft = gameboardSpaceLookup(self.gbCoords)

class houseSpriteClass(pygame.sprite.Sprite):
	def __init__(self, name):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(name + ".png")
		#self.image = pygame.transform.scale(self.image, (20, 20))
		self.image.convert_alpha()
		
class Button:
	def __init__(self, top, left, width, height, btext=""):
		self.buttonRect = pygame.Rect(top, left, width, height)
		self.text = btext
	
	def __str__(self):
		return [self.text, self.buttonRect]
	def __repr__(self):
		return str([self.text, self.buttonRect])
	
	def draw(self):
		if self.text == "":
			pass
		else:
			pygame.draw.rect(window, (255,255,255), self.buttonRect)
			window.blit(font.render(self.text, True, (0,0,0)), (self.buttonRect.left + 5, self.buttonRect.top + 5))
			
class dButton:
	def __init__(self, top, left, width, height, btext=""):
		self.buttonRect = pygame.Rect(top, left, width, height)
		self.text = btext
		
	def __repr__(self):
		return str([self.text, self.buttonRect])
		
	def draw(self):
		if self.text == "":
			pass
		else:
			pygame.draw.rect(window, (255,255,255), self.buttonRect)
			window.blit(font.render(self.text, True, (0,0,0)), (self.buttonRect.left + 5, self.buttonRect.top + 5))

class dButtonSD:
	def __init__(self, top, left, width, height, btext, bdata):
		self.buttonRect = pygame.Rect(top, left, width, height)
		self.printText = btext
		self.data = bdata
		self.text = (self.printText, self.data)
		
	def __repr__(self):
		return str([self.text, self.buttonRect])
		
	def draw(self):
		if self.text == "":
			pass
		else:
			pygame.draw.rect(window, (255,255,255), self.buttonRect)
			window.blit(font.render(self.printText, True, (0,0,0)), (self.buttonRect.left + 5, self.buttonRect.top + 5))

class spriteButton:
	def __init__(self, top, left, bimage, btext=""):
		self.buttonImage = bimage
		self.buttonRect = self.buttonImage.get_rect()
		self.buttonRect.topleft = (top,left)
		self.text = btext
	
	def __repr__(self):
		return str([self.text, self.buttonRect, "Sprite"])
	
	def draw(self):
		if self.text == "":
			pass
		else:
			window.blit(self.buttonImage, self.buttonRect)

class GUIstring:
	def __init__ (self, sstring, screenCoords, Tcolor = (255,255,255)):
		self.string = sstring
		self.coords = screenCoords
		self.color = Tcolor
		
	def __repr__ (self):
		return(self.string)
		
	def draw (self):
		window.blit(font.render(self.string, True, self.color), self.coords)

class GUIstringDynamic(GUIstring):
	def __init__(self, prestringN, value, poststringN, screenCoords, Tcolor = (255,255,255)):
		self.prestring = prestringN
		self.poststring = poststringN
		self.string = self.prestring + str(value) + self.poststring
		super().__init__(self.string, screenCoords, Tcolor)
	
	def updateVal(self, value):
		self.string =  self.prestring + str(value) + self.poststring

class GUIComponent():
	def __init__(self, container, topLeft):
		self.container = container
		self.origin = topLeft
		self.activeButtons = []
		self.stringsToPrint = []
		self.isActive = False
	
	def drawGUI(self):
		for i in self.activeButtons:
			if not(i in self.container.activeButtons):
				self.container.activeButtons.extend(self.activeButtons)
		for i in self.stringsToPrint:
			if not(i in self.container.stringsToPrint):
				self.container.stringsToPrint.extend(self.stringsToPrint)
				
	def makeInactive(self):
		for i in self.activeButtons:
			if i in self.container.activeButtons:
				self.container.activeButtons.pop(self.container.activeButtons.index(i))
		for i in self.stringsToPrint:
			if i in self.container.stringsToPrint:
				self.container.stringsToPrint.pop(self.container.stringsToPrint.index(i))
		self.isActive = False

class GUIbaseClass:
	def __init__ (self):
		self.buttonsList = []
		self.activeButtons = []
		self.stringsToPrint = []
		self.GUIarea = None
		self.buttonQ = dButton(1720,990,200,80, btext = "Quit")
		self.buttonsList.append(self.buttonQ)
		self.activeButtons.append(self.buttonQ)
		self.quitDialog = True
		
	def mouseOverButton (self):
		for i in self.activeButtons:
			if i.buttonRect.collidepoint(pygame.mouse.get_pos()):
				return(i.text)
		return("")
	
	def drawGUI (self):
		window.fill(globalVars.backgroundColor, self.GUIarea)
		for i in self.activeButtons:
			i.draw()
		for i in self.stringsToPrint:
			i.draw()
		pygame.display.update()
			
	def buttonActive(self, aButton):
		if aButton in self.activeButtons:
			pass
		else:
			self.activeButtons.append(aButton)
			
	def buttonInactive(self, aButton):
		if aButton in self.activeButtons:
			self.activeButtons.pop(self.activeButtons.index(aButton))
	
	def allButtonsActive(self):
		for i in self.buttonsList:
			if i in self.activeButtons:
				pass
			else:
				self.activeButtons.append(i)
				
	def allButtonsInactive(self):
		self.activeButtons = [self.buttonQ]
	
	def getUserInput (self):
		inputLoop = True
		while inputLoop == True:
			for event in pygame.event.get():
				if event.type == QUIT:
					if self.quitDialog == True:
						quitGame()
					else:
						sys.exit()
				elif event.type == KEYUP:
					if event.key == K_ESCAPE:
						if self.quitDialog == True:
							quitGame()
						else:
							sys.exit()
				elif event.type == MOUSEBUTTONUP:
					#print(self.mouseOverButton())
					if self.mouseOverButton() == "Quit":
						if self.quitDialog == True:
							quitGame()
						else:
							sys.exit()
					elif not(self.mouseOverButton() == ""):
						return self.mouseOverButton()
	
class mainMenuGUIClass(GUIbaseClass):
	def __init__ (self):
		super().__init__()
		self.quitDialog = False
		self.buttonsList.extend([dButton(300, 500, 200, 100, btext = "Yes"), dButton(600, 500, 200, 100, btext = "No")])
		self.activeButtons = self.buttonsList
		self.stringsToPrint.append(GUIstring("Would you like to load from save?", (300,400)))

class newGamePlayerNumberGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.quitDialog = False
		self.newGamePlayerCount = 2
		self.buttonsList.extend([dButton(300, 500, 100, 100, "-"), dButton(600, 500, 100, 100, "+"), dButton(300, 700, 100, 100, "Confirm")])
		self.stringsToPrint.append(GUIstring("How many players?", (300,400)))
		self.playerNumString = GUIstringDynamic("", self.newGamePlayerCount, "", (400, 500))
		self.stringsToPrint.append(self.playerNumString)
		self.allButtonsActive()
		
	def getUserInput(self):
		response = super().getUserInput()
		if response == "-" and self.newGamePlayerCount > 2:
			self.newGamePlayerCount = self.newGamePlayerCount - 1
			self.playerNumString.updateVal(self.newGamePlayerCount)
			self.drawGUI
		elif response == "+" and self.newGamePlayerCount < len(newGameSelectTokenGUI.availableTokens):
			self.newGamePlayerCount = self.newGamePlayerCount + 1
			self.playerNumString.updateVal(self.newGamePlayerCount)
			self.drawGUI
		else:
			return response
		
class newGamePlayerNameGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.quitDialog = False
		self.inputString = GUIstring("", (300,500))
		self.PlayerString = GUIstringDynamic("What is player ", None, "'s name?", (300,400)) 
		self.stringsToPrint.append(self.inputString)
		self.stringsToPrint.append(self.PlayerString) 
			
	def drawGUI(self):
		self.PlayerString.updateVal(globalVars.activePlayerNumber + 1)
		super().drawGUI()
	
	def inputTextField(self):
		inputLoop = True
		while inputLoop == True:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_RETURN or event.key == K_KP_ENTER:
						if not(self.inputString.string == ""):
							inputLoop = False
					elif event.key == K_BACKSPACE:
						self.inputString.string = self.inputString.string[:-1]
					else:
						self.inputString.string = self.inputString.string + event.unicode
			self.drawGUI()
		return self.inputString.string
		
class newGameSelectTokenGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.quitDialog = False
		self.availableTokens = {"car": pygame.image.load("car.png"), "dog": pygame.image.load("dog.png"), "hat": pygame.image.load("hat.png"), "iron": pygame.image.load("iron.png"), "ship": pygame.image.load("ship.png"), "shoe": pygame.image.load("shoe.png"), "thimble": pygame.image.load("thimble.png"), "wheelbarrow": pygame.image.load("wheelbarrow.png")}
		#print(self.availableTokens)
		self.tokenList = []
		self.tokenButtons = {}
		self.takenTokenNames = []
		self.playerName = GUIstringDynamic("", "", ", which token would you like to use?", (300,400))
		self.stringsToPrint.append(self.playerName)
		for i in self.availableTokens:
			self.tokenList.append(i)
			self.availableTokens[i] = pygame.transform.scale(self.availableTokens[i], (globalVars.displaySize[1]*0.05,globalVars.displaySize[1]*0.05))
			self.availableTokens[i].convert_alpha()
			self.tokenButtons[i] = spriteButton(0, 0, self.availableTokens[i], i)
		for i in self.tokenButtons:
			self.buttonsList.append(self.tokenButtons[i])
		random.shuffle(self.tokenList)
		
	def updateName(self, pName):
		self.playerName.updateVal(pName)
		
	def drawGUI(self):
		posW = 300
		self.allButtonsActive()
		for i in self.tokenList:
			if self.tokenButtons[i].text in self.takenTokenNames:
				self.buttonInactive(self.tokenButtons[i])
			else:
				self.tokenButtons[i].buttonRect.topleft = (posW, 500)
				posW = posW + 100
		super().drawGUI()
		
class gameLoopGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.GUIarea = (1090,0,1000,1000)
		self.primaryActionButton = dButton(1090,900,200,80)
		self.secondaryActionButton = dButton(1300,900,200,80)
		self.tertiaryActionButton = dButton(1510,900,200,80)
		self.quaternaryActionButton = dButton(1720,900,200,80)
		self.tradeButton = dButton(1090,990,200,80, "Trade")
		self.improveButton = dButton(1300,990,200,35)
		self.unimproveButton = dButton(1300,1030,200,35)
		self.unmortgageButton = dButton(1510,990,200,35)
		self.mortgageButton = dButton(1510,1030,200,35)
		self.tokenDisplay = spriteButton(1090, 0, pygame.Surface((5,5)), ".")
		self.buttonsList.extend([self.primaryActionButton, self.secondaryActionButton, self.tertiaryActionButton, self.quaternaryActionButton, self.tradeButton, self.improveButton, self.unimproveButton, self.unmortgageButton, self.mortgageButton, self.tokenDisplay])
		self.activeButtons.append(self.tokenDisplay)
		self.activeButtons.append(self.tradeButton)
		self.stringStack = []
		self.propertyButtons = []
		self.topLineString = GUIstring("", (1150,20))
		self.playerMoneyString = GUIstringDynamic("You have ", 0, " dollars", (1090, 360))
		self.stringsToPrint.extend([self.topLineString, self.playerMoneyString])
	
	def allButtonsInactive(self):
		super().allButtonsInactive
		self.buttonActive(self.tokenDisplay)

	
	def drawGUI(self, token):
		if token.turnActive == True:
			if token.IsInJail == False:
				self.topLineString.string = "It is " + token.PlayerName + "'s turn. You are on " + Gameboard.listspace[token.BoardPosition[0]][token.BoardPosition[1]]
			elif token.IsInJail == True:
				self.topLineString.string = "It is " + token.PlayerName + "'s turn. You are in Jail. This is your " + token.turnsInJailString() + " turn in Jail."
		else:
			self.topLineString.string = "It is the end of " + token.PlayerName + "'s turn. You are on " + Gameboard.listspace[token.BoardPosition[0]][token.BoardPosition[1]]
		self.tokenDisplay.buttonImage = token.token.image
		self.playerMoneyString.updateVal(token.PlayerMoney)
		posW = 1090
		posH = 60
		for i in range(len(self.stringStack)):
			self.stringsToPrint.append(GUIstring(self.stringStack[i], (posW, posH)))
			if i < len(self.stringStack) - 1:
				if posW + font.size(self.stringStack[i])[0] + 10 + font.size(self.stringStack[i+1])[0] < globalVars.displaySize[0]:
					posW = posW + font.size(self.stringStack[i])[0] + 10
				else:
					posW = 1090
					posH = posH + 20
		posWa = 990
		posWb = 990
		posWc = 990
		posHa = 400
		posHb = 530
		posHc = 630
		posHR = 630
		posHCC = 630
		posHU = 630
		posWU = 1690
		lastCG = "none"
		posACO = 1090
		for i in range(len(token.heldChanceCards)):
			self.propertyButtons.append(spriteButton(posACO, 810, actionCards.chanceCards[token.heldChanceCards[i]][4].cardImageS, actionCards.chanceCards[token.heldChanceCards[i]][0]))
			posACO = posACO + 90
		for i in range(len(token.heldChestCards)):
			self.propertyButtons.append(spriteButton(posACO, 810, actionCards.chestCards[token.heldChestCards[i]][4].cardImageS, actionCards.chestCards[token.heldChestCards[i]][0]))
			posACO = posACO + 90
		for i in range(len(token.heldTravelVouchers)):
			self.propertyButtons.append(spriteButton(posACO, 810, actionCards.travelVoucherCards[token.heldTravelVouchers[i]][1].cardImageS, actionCards.travelVoucherCards[token.heldTravelVouchers[i]][0]))
			posACO = posACO + 90
		for i in range(len(token.heldRollThreeCards)):
			#print(actionCards.rollThreeImages, actionCards.rollThreeCards)
			#print(i, token.heldRollThreeCards, token.heldRollThreeCards[i])
			self.propertyButtons.append(spriteButton(posACO, 810, actionCards.rollThreeImages[token.heldRollThreeCards[i]].cardImageS, actionCards.rollThreeCards[token.heldRollThreeCards[i]]))
			posACO = posACO + 90
		for i in range(len(token.OwnedProps)):
			if Gameboard.propList[token.OwnedProps[i]][1] == "CG":
				if token.OwnedProps[i] < 40:
					if Gameboard.propList[token.OwnedProps[i]][5] == lastCG:
						posHa = posHa + 30
					else:
						posWa = posWa + 100
						posHa = 400
					if Gameboard.propList[token.OwnedProps[i]][4] == "unmortgaged":
						self.propertyButtons.append(spriteButton(posWa, posHa, Gameboard.propList[token.OwnedProps[i]][12][0].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
					else:
						self.propertyButtons.append(spriteButton(posWa, posHa, Gameboard.propList[token.OwnedProps[i]][12][1].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				elif token.OwnedProps[i] < 66:
					if Gameboard.propList[token.OwnedProps[i]][5] == lastCG:
						posHb = posHb + 30
					else:
						posWb = posWb + 100
						posHb = 530
					if Gameboard.propList[token.OwnedProps[i]][4] == "unmortgaged":
						self.propertyButtons.append(spriteButton(posWb, posHb, Gameboard.propList[token.OwnedProps[i]][12][0].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
					else:
						self.propertyButtons.append(spriteButton(posWb, posHb, Gameboard.propList[token.OwnedProps[i]][12][1].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				else:
					if Gameboard.propList[token.OwnedProps[i]][5] == lastCG:
						posHc = posHc + 30
					else:
						posWc = posWc + 100
						posHc = 630
					if Gameboard.propList[token.OwnedProps[i]][4] == "unmortgaged":
						self.propertyButtons.append(spriteButton(posWc, posHc, Gameboard.propList[token.OwnedProps[i]][12][0].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
					else:
						self.propertyButtons.append(spriteButton(posWc, posHc, Gameboard.propList[token.OwnedProps[i]][12][1].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				lastCG = Gameboard.propList[token.OwnedProps[i]][5]
		for i in range(len(token.OwnedProps)):
			if Gameboard.propList[token.OwnedProps[i]][1] == "Railroad":
				if Gameboard.propList[token.OwnedProps[i]][4] == "unmortgaged":
					self.propertyButtons.append(spriteButton(1490, posHR, Gameboard.propList[token.OwnedProps[i]][7][0].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				else:
					self.propertyButtons.append(spriteButton(1490, posHR, Gameboard.propList[token.OwnedProps[i]][7][1].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				posHR = posHR + 30
			elif Gameboard.propList[token.OwnedProps[i]][1] == "CabCo":
				if Gameboard.propList[token.OwnedProps[i]][4] == "unmortgaged":
					self.propertyButtons.append(spriteButton(1590, posHCC, Gameboard.propList[token.OwnedProps[i]][7][0].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				else:
					self.propertyButtons.append(spriteButton(1590, posHCC, Gameboard.propList[token.OwnedProps[i]][7][1].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				posHCC = posHCC + 30
			elif Gameboard.propList[token.OwnedProps[i]][1] == "Utility":
				if Gameboard.propList[token.OwnedProps[i]][4] == "unmortgaged":
					self.propertyButtons.append(spriteButton(posWU, posHU, Gameboard.propList[token.OwnedProps[i]][7][0].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				else:
					self.propertyButtons.append(spriteButton(posWU, posHU, Gameboard.propList[token.OwnedProps[i]][7][1].deedImageS, Gameboard.propList[token.OwnedProps[i]][0]))
				posHU = posHU + 30
				if posHU == 750:
					posHU = 630
					posWU = 1790
		self.buttonsList.extend(self.propertyButtons)
		for i in self.buttonsList:
			if i in self.propertyButtons:
				self.buttonActive(i)
		drawBackground()
		super().drawGUI()
		popIndex = []
		for i in self.stringsToPrint:
			if i.string in self.stringStack:
				popIndex.append(self.stringsToPrint.index(i))
		popIndex.reverse()
		for i in popIndex:
			self.stringsToPrint.pop(i)
		self.stringStack = []
		self.propertyButtons.reverse()
		for i in self.propertyButtons:
			self.buttonsList.pop(self.buttonsList.index(i))
			self.activeButtons.pop(self.activeButtons.index(i))
		self.propertyButtons = []
			
class improvePropsPickGroupGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.GUIarea = (1090,0,1000,1080)
		self.doneButton = dButton(1300,900,200,80, "Go Back")
		self.activeButtons.append(self.doneButton)
		self.activeButtons.append(gameLoopGUI.tokenDisplay)
		self.deedButtons = []
		self.stringsToPrint.append(GUIstring("Select a color group to improve.", (1090, 360)))
		self.topLineString = GUIstringDynamic("", "", ", which color group would you like to improve?", (1150,20))
		self.stringsToPrint.append(self.topLineString)
		
		
	def drawGUI(self, token):
		for i in self.deedButtons:
			if i in self.activeButtons:
				self.activeButtons.pop(self.activeButtons.index(i))
		self.topLineString.updateVal(token.PlayerName)
		self.deedButtons = []
		posH = 400
		posHT = 400
		posW = 1090
		buttonNum = 0
		for i in token.ownedColorGroups:
			hasMortgagedProps = False
			for j in token.ownedColorGroups[i][1]:
				if Gameboard.propList[j][4] == "mortgaged":
					hasMortgagedProps = True
			if token.ownedColorGroups[i][0] > 0 and hasMortgagedProps == False:
				offset = 0
				posH = posHT
				self.deedButtons.append(spriteButton(posW, posH, pygame.Surface((100, 114 + ((len(token.ownedColorGroups[i][1]) - 1) * 30))), i))
				for j in range(len(token.ownedColorGroups[i][1])):
					self.deedButtons[buttonNum].buttonImage.blit(Gameboard.propList[token.ownedColorGroups[i][1][j]][12][0].deedImageS, (0, offset))
					offset = offset + 30
					self.deedButtons[buttonNum].buttonRect.union_ip((posW,posH,100,114))
				posW = posW + 100
				if posW > 1790:
					posW = 1090
					posHT = posHT + 130
				buttonNum = buttonNum + 1
		self.activeButtons.extend(self.deedButtons)
		super().drawGUI()
				
class unimprovePropsPickGroupGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.GUIarea = (1090,0,1000,1080)
		self.doneButton = dButton(1300,900,200,80, "Go Back")
		self.activeButtons.append(self.doneButton)
		self.activeButtons.append(gameLoopGUI.tokenDisplay)
		self.deedButtons = []
		self.stringsToPrint.append(GUIstring("Select a color group to unimprove.", (1090, 360)))
		self.topLineString = GUIstringDynamic("", "", ", which color group would you like to unimprove?", (1150,20))
		self.stringsToPrint.append(self.topLineString)
		
		
	def drawGUI(self, token):
		for i in self.deedButtons:
			if i in self.activeButtons:
				self.activeButtons.pop(self.activeButtons.index(i))
		self.topLineString.updateVal(token.PlayerName)
		self.deedButtons = []
		posH = 400
		posHT = 400
		posW = 1090
		buttonNum = 0
		for i in token.ownedColorGroups:
			if token.ownedColorGroups[i][2] > 0:
				offset = 0
				posH = posHT
				self.deedButtons.append(spriteButton(posW, posH, pygame.Surface((100, 114 + ((len(token.ownedColorGroups[i][1]) - 1) * 30))), i))
				for j in range(len(token.ownedColorGroups[i][1])):
					self.deedButtons[buttonNum].buttonImage.blit(Gameboard.propList[token.ownedColorGroups[i][1][j]][12][0].deedImageS, (0, offset))
					offset = offset + 30
					self.deedButtons[buttonNum].buttonRect.union_ip((posW,posH,100,114))
				posW = posW + 100
				if posW > 1790:
					posW = 1090
					posHT = posHT + 130
				buttonNum = buttonNum + 1
		self.activeButtons.extend(self.deedButtons)
		super().drawGUI()
		
class improvePropsGUIClass(GUIbaseClass):
	def __init__ (self):
		super().__init__()
		self.GUIarea = (1090,0,1000,1080)
		self.doneButton = dButton(1300,900,200,80, "Done")
		self.activeButtons.append(self.doneButton)
		self.deedButtons = []
		self.activeButtons.append(gameLoopGUI.tokenDisplay)
		self.stringsToPrint.append(GUIstring("Select a property to improve.", (1090, 360)))
		self.improveCostString = GUIstringDynamic("Improvements cost ", 0, " dollars.", (1090, 340))
		self.stringsToPrint.append(self.improveCostString)
		self.playerMoneyStringa = GUIstringDynamic("You have $", 0, " dollars.", (1090, 320))
		self.stringsToPrint.append(self.playerMoneyStringa)
		self.topLineString = GUIstringDynamic("", "", ", select a property to improve. Select 'Done' when you are finished.", (1150,20))
		self.stringsToPrint.append(self.topLineString)
	
	def drawGUI(self, token, colorGroup):
		for i in self.deedButtons:
			if i in self.activeButtons:
				self.activeButtons.pop(self.activeButtons.index(i))
		self.topLineString.updateVal(token.PlayerName)
		self.deedButtons = []
		propsToImprove = token.ownedColorGroups[colorGroup][1]
		propsToImprove.sort()
		minimumImpLevel = 7
		self.improveCostString.updateVal(str(Gameboard.propList[propsToImprove[0]][10]))
		self.playerMoneyStringa.updateVal(str(token.PlayerMoney))
		for i in range(len(propsToImprove)):
			if Gameboard.propList[propsToImprove[i]][7] < minimumImpLevel:
				minimumImpLevel = Gameboard.propList[propsToImprove[i]][7]
		posW = 1090
		for i in range(len(propsToImprove)):
			if Gameboard.propList[propsToImprove[i]][7] <= minimumImpLevel:
				self.deedButtons.append(spriteButton(posW, 400, Gameboard.propList[propsToImprove[i]][12][0].deedImageS, propsToImprove[i]))
				posW = posW + 100
		self.activeButtons.extend(self.deedButtons)
		drawBackground()
		super().drawGUI()
		
class unimprovePropsGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.GUIarea = (1090,0,1000,1080)
		self.doneButton = dButton(1300,900,200,80, "Done")
		self.activeButtons.append(self.doneButton)
		self.deedButtons = []
		self.activeButtons.append(gameLoopGUI.tokenDisplay)
		self.stringsToPrint.append(GUIstring("Select a property to improve.", (1090, 360)))
		self.improveCostString = GUIstringDynamic("Improvements may be sold for ", 0, " dollars.", (1090, 340))
		self.stringsToPrint.append(self.improveCostString)
		self.playerMoneyStringa = GUIstringDynamic("You have $", 0, " dollars.", (1090, 320))
		self.stringsToPrint.append(self.playerMoneyStringa)
		self.topLineString = GUIstringDynamic("", "", ", select a property to improve. Select 'Done' when you are finished.", (1150,20))
		self.stringsToPrint.append(self.topLineString)
	
		
	def drawGUI(self, token, colorGroup):
		for i in self.deedButtons:
			if i in self.activeButtons:
				self.activeButtons.pop(self.activeButtons.index(i))
		self.deedButtons = []
		self.topLineString.updateVal(token.PlayerName)
		propsToImprove = token.ownedColorGroups[colorGroup][1]
		propsToImprove.sort()
		maximumImpLevel = 0
		self.improveCostString.updateVal(str(Gameboard.propList[propsToImprove[0]][10] // 2))
		self.playerMoneyStringa.updateVal(str(token.PlayerMoney))
		for i in range(len(propsToImprove)):
			if Gameboard.propList[propsToImprove[i]][7] > maximumImpLevel:
				maximumImpLevel = Gameboard.propList[propsToImprove[i]][7]
		posW = 1090
		for i in range(len(propsToImprove)):
			if Gameboard.propList[propsToImprove[i]][7] >= maximumImpLevel and Gameboard.propList[propsToImprove[i]][7] > 0:
				self.deedButtons.append(spriteButton(posW, 400, Gameboard.propList[propsToImprove[i]][12][0].deedImageS, propsToImprove[i]))
				posW = posW + 100
		self.activeButtons.extend(self.deedButtons)
		drawBackground()
		super().drawGUI()
			
class mortgagePropertiesGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.deedButtons = []
		self.doneButton = dButton(200, 600, 200, 80, "Go Back")
		self.buttonsList.append(self.doneButton)
		self.buttonActive(self.doneButton)
		self.tokenDisplay = spriteButton(200, 0, pygame.Surface((5,5)), ".")
		self.buttonActive(self.tokenDisplay)
		self.topLineString = GUIstringDynamic("", "", ", select a property to mortgage:", (200, 200))
		self.stringsToPrint.append(self.topLineString)
		
	def drawGUI(self, token):
		for i in self.deedButtons:
			if i in self.activeButtons:
				self.activeButtons.pop(self.activeButtons.index(i))
		self.deedButtons = []
		posHT = 400
		posH = 300
		posW = 200
		self.topLineString.updateVal(token.PlayerName)
		self.tokenDisplay.buttonImage = token.token.image 
		for i in token.OwnedProps:
			if Gameboard.propList[i][4] == "unmortgaged":
				if Gameboard.propList[i][1] == "CG":
					if token.ownedColorGroups[Gameboard.propList[i][5]][2] == 0:
						self.deedButtons.append(spriteButton(posW, posH, Gameboard.propList[i][12][0].deedImageS, i))
					else:
						posW = posW - 100
				else:
					self.deedButtons.append(spriteButton(posW, posH, Gameboard.propList[i][7][0].deedImageS, i))
				posW = posW + 100
				if posW > 1500:
					posW = 200
					posH = posH + 150
		self.activeButtons.extend(self.deedButtons)
		super().drawGUI()

class unmortgagePropertiesGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.deedButtons = []
		self.doneButton = dButton(200, 600, 200, 80, "Go Back")
		self.buttonsList.append(self.doneButton)
		self.buttonActive(self.doneButton)
		self.tokenDisplay = spriteButton(200, 0, pygame.Surface((5,5)), ".")
		self.buttonActive(self.tokenDisplay)
		self.topLineString = GUIstringDynamic("", "", ", select a property to unmortgage:", (200, 200))
		self.stringsToPrint.append(self.topLineString)
		
	def drawGUI(self, token):
		for i in self.deedButtons:
			if i in self.activeButtons:
				self.activeButtons.pop(self.activeButtons.index(i))
		self.deedButtons = []
		posHT = 400
		posH = 300
		posW = 200
		self.topLineString.updateVal(token.PlayerName)
		self.tokenDisplay.buttonImage = token.token.image 
		for i in token.OwnedProps:
			if Gameboard.propList[i][4] == "mortgaged":
				if Gameboard.propList[i][1] == "CG":
					self.deedButtons.append(spriteButton(posW, posH, Gameboard.propList[i][12][0].deedImageS, i))
				else:
					self.deedButtons.append(spriteButton(posW, posH, Gameboard.propList[i][7][0].deedImageS, i))
				posW = posW + 100
				if posW > 1500:
					posW = 200
					posH = posH + 150
		self.activeButtons.extend(self.deedButtons)
		super().drawGUI()

class readActionCardGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.dialogButtonA = dButton(300, 600, 200, 80, "Okay")
		self.dialogButtonB = dButton(600, 600, 200, 80, "")
		self.cardDisplay = spriteButton(300, 60, pygame.Surface((5,5)), ".")
		self.buttonsList.extend([self.dialogButtonA, self.cardDisplay])
		self.allButtonsActive()
		
		
	def drawGUI(self, pulledCard):
		print(pulledCard)
		self.cardDisplay.buttonImage = pulledCard[4].cardImage
		super().drawGUI()

class rollThreeGUIClass(GUIbaseClass):
	def __init__(self):
		super().__init__()
		self.dialogButtonA = dButton(300, 600, 200, 80, "Okay")
		self.cardDisplay = spriteButton(300, 60, pygame.Surface((5,5)), ".")
		self.buttonsList.extend([self.dialogButtonA, self.cardDisplay])
		self.allButtonsActive()
		
	def drawGUI(self, token, pulledCard):
		self.cardDisplay.buttonImage = actionCards.rollThreeImages[pulledCard].cardImage
		super().drawGUI()

class tradeAddMoneyClass(GUIComponent):
	def __init__ (self, container, topLeft, side):
		super().__init__(container, topLeft)
		self.side = side
		self.minusHundredButton = dButton(self.origin[0], self.origin[1] + 300, 80, 80, "-100")
		self.minusTenButton = dButton(self.origin[0] + 100, self.origin[1] + 300, 80, 80, "-10")
		self.minusOneButton = dButton(self.origin[0] + 200, self.origin[1] + 300, 80, 80, "-1")
		self.plusOneButton = dButton(self.origin[0] + 400, self.origin[1] + 300, 80, 80, "+1")
		self.plusTenButton = dButton(self.origin[0] + 500, self.origin[1] + 300, 80, 80, "+10")
		self.plusHundredButton = dButton(self.origin[0] + 600, self.origin[1] + 300, 80, 80, "+100")
		self.doneButton = dButton(self.origin[0] + 300, self.origin[1] + 400, 100, 80, "Finished")
		self.activeButtons.extend([self.minusHundredButton, self.minusTenButton, self.minusOneButton, self.plusOneButton, self.plusTenButton, self.plusHundredButton, self.doneButton])
		self.moneyString = GUIstringDynamic("", "0", "", (self.origin[0] + 300, self.origin[1] + 300))
		self.playerMoneyString = GUIstringDynamic("This player has $", "0", " dollars", (self.origin[0], self.origin[1] + 500))
		self.stringsToPrint.extend([self.moneyString, self.playerMoneyString])
	
	def drawGUI(self):
		self.moneyString.updateVal(self.side.proposedMoney)
		self.playerMoneyString.updateVal(self.side.player.PlayerMoney)
		super().drawGUI()
		
	def addMoneyFunc(self, response):
		if response == "-100":
			value = -100
		elif response == "-10":
			value = -10
		elif response == "-1":
			value = -1
		elif response == "+1":
			value = 1
		elif response == "+10":
			value = 10
		elif response == "+100":
			value = 100
		if self.side.proposedMoney + value >= 0 and self.side.proposedMoney + value <= self.side.player.PlayerMoney:
			self.side.proposedMoney = self.side.proposedMoney + value
	
class tradeIntAssetsClass(GUIComponent):
	def __init__(self, container, topLeft, side):
		super().__init__(container, topLeft)
		self.side = side
		self.moneyString = GUIstringDynamic("This player has $", "", " dollars, and the following assets.", (self.origin[0], self.origin[1] + 400))
		self.propMoneyString = GUIstringDynamic("This player will pay $", "0", " dollars, and trade the following assets.", (self.origin[0], self.origin[1])) 
		self.stringsToPrint.extend([self.moneyString, self.propMoneyString])
		self.addMoneyButton = dButtonSD(self.origin[0], self.origin[1] + 300, 200, 80, "Add/remove money", side)
		self.player = None
		self.deedButtons = []
		self.aCardButtons = []
		self.proposedMoney = 0
		self.proposedProps = []
		self.proposedChestCards = []
		self.proposedChanceCards = []
	
	def hasAssets(self):
		if self.proposedMoney > 0 or len(self.proposedProps) > 0 or len(self.proposedChanceCards) > 0 or len(self.proposedChestCards) > 0:
			return True
	
	def deedSpread (self, deedList, offsetVa, topOrBottom):
		layer = topOrBottom
		offsetH = 0
		offsetV = offsetVa
		for i in deedList:
			if Gameboard.propList[i][1] == "CG":
				if Gameboard.propList[i][4] == "unmortgaged":
					self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, Gameboard.propList[i][12][0].deedImageS, ["Prop", self.side, layer, i]))
				else:
					self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, Gameboard.propList[i][12][1].deedImageS, ["Prop", self.side, layer, i]))
				offsetV = offsetV + 30
				if offsetV >= offsetVa + 150:
					offsetV = offsetVa
					offsetH = offsetH + 100
		for i in deedList:
			if Gameboard.propList[i][1] == "CabCo":
				if Gameboard.propList[i][4] == "unmortgaged":
					self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, Gameboard.propList[i][7][0].deedImageS, ["Prop", self.side, layer, i]))
				else:
					self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, Gameboard.propList[i][7][1].deedImageS, ["Prop", self.side, layer, i]))
				offsetV = offsetV + 30
				if offsetV >= offsetVa + 150:
					offsetV = offsetVa
					offsetH = offsetH + 100
		for i in deedList:
			if Gameboard.propList[i][1] == "Railroad":
				if Gameboard.propList[i][4] == "unmortgaged":
					self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, Gameboard.propList[i][7][0].deedImageS, ["Prop", self.side, layer, i]))
				else:
					self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, Gameboard.propList[i][7][1].deedImageS, ["Prop", self.side, layer, i]))
				offsetV = offsetV + 30
				if offsetV >= offsetVa + 150:
					offsetV = offsetVa
					offsetH = offsetH + 100
		for i in deedList:
			if Gameboard.propList[i][1] == "Utility":
				if Gameboard.propList[i][4] == "unmortgaged":
					self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, Gameboard.propList[i][7][0].deedImageS, ["Prop", self.side, layer, i]))
				else:
					self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, Gameboard.propList[i][7][1].deedImageS, ["Prop", self.side, layer, i]))
				offsetV = offsetV + 30
				if offsetV >= offsetVa + 150:
					offsetV = offsetVa
					offsetH = offsetH + 100
		for i in self.activeButtons:
			for j in self.activeButtons:
				if j == i:
					pass
				else:
					if i.buttonRect.colliderect(j.buttonRect):
						if i.buttonRect.bottom > j.buttonRect.top:
							i.buttonRect.height = i.buttonRect.height - (i.buttonRect.bottom - j.buttonRect.top)
						elif j.buttonRect.bottom > i.buttonRect.top:
							j.buttonRect.height = j.buttonRect.height - (j.buttonRect.bottom - i.buttonRect.top)
							
		
	def cardSpread (self, chanceCardsList, chestCardsList, offsetV):
		offsetH = 0
		for i in chanceCardsList:
			self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, actionCards.chanceCards[i][4].cardImageS, "Card"))
			offsetH = offsetH + 30
		for i in chestCardsList:
			self.activeButtons.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, actionCards.chestCards[i][4].cardImageS, "Card"))
			offsetH = offsetH + 30
	
	def drawGUI(self):
		self.moneyString.updateVal(self.player.PlayerMoney)
		self.propMoneyString.updateVal(self.proposedMoney)
		for i in self.activeButtons:
			if i in self.container.activeButtons:
				self.container.activeButtons.pop(self.container.activeButtons.index(i))
		self.activeButtons = [self.addMoneyButton]
		self.deedSpread(self.player.OwnedProps, 450, "bottom")
		self.deedSpread(self.proposedProps, 30, "top")
		self.cardSpread(self.player.heldChanceCards, self.player.heldChestCards, 700)
		super().drawGUI()

class tradeSelectPartnerClass(GUIComponent):
	def __init__(self, container, topLeft):
		super().__init__(container, topLeft)
		self.playerTokenList = []
		self.stringsToPrint.append(GUIstring("Select a player to trade with:", (self.origin[0], self.origin[1])))
		
	def drawGUI(self):
		for i in self.playerTokenList:
			if i in self.container.activeButtons:
				self.container.activeButtons.pop(self.container.activeButtons.index(i))
		self.playerTokenList = []
		self.activeButtons = []
		offsetH = 0
		offsetV = 20
		for i in listPlayers:
			if not(i == self.container.activePlayer):
				self.playerTokenList.append(spriteButton(self.origin[0] + offsetH, self.origin[1] + offsetV, i.token.image, i.Playernumber))
				offsetH = offsetH + 100
		self.activeButtons.extend(self.playerTokenList)
		super().drawGUI()

class tradeInterfaceGUIClass(GUIbaseClass):
	def __init__ (self):
		super().__init__()
		self.doneButton = dButton(200, 990, 200, 80, "Done")
		self.proposeButton = dButton(700, 990, 200, 80, "Propose")
		self.activeButtons.append(self.doneButton)
		self.partnerSelected = False
		self.guiComponentList = []
		self.activePlayerAssets = tradeIntAssetsClass(self, (200, 200), "active")
		self.secondPlayerAssets = tradeIntAssetsClass(self, (1060, 200), "second")
		self.activePlayerAddMoney = tradeAddMoneyClass(self, (200,200), self.activePlayerAssets)
		self.secondPlayerAddMoney = tradeAddMoneyClass(self, (1060, 200), self.secondPlayerAssets)
		self.selectTradePartner = tradeSelectPartnerClass(self, (960, 300))
		self.guiComponentList.extend([self.activePlayerAssets, self.secondPlayerAssets, self.selectTradePartner, self.activePlayerAddMoney, self.secondPlayerAddMoney])
		self.activePlayer = None
		self.secondPlayer = None
	
	def setActivePlayer(self, player):
		self.activePlayer = player
		self.activeButtons.append(spriteButton(200, 100, self.activePlayer.token.image, "."))
		self.stringsToPrint.append(GUIstring(self.activePlayer.PlayerName + " is trading with:", (250, 100)))
	
	def setSecondPlayer(self, player):
		self.secondPlayer = player
		self.activeButtons.append(spriteButton(1060, 100, self.secondPlayer.token.image, "ChangeSP"))
		self.stringsToPrint.append(GUIstring(self.secondPlayer.PlayerName, (1110, 100)))
	
	def drawGUI (self):
		self.activePlayerAssets.player = self.activePlayer
		self.secondPlayerAssets.player = self.secondPlayer
		print(self.guiComponentList)
		if self.partnerSelected == True and self.activePlayerAssets.hasAssets == True and self.secondPlayerAssets.hasAssets == True:
			self.activeButtons.append(self.proposeButton)
		elif self.proposeButton in self.activeButtons:
			self.activeButtons.pop(self.activeButtons.index(self.proposeButton))
		for i in self.guiComponentList:
			if i.isActive == True:
				i.drawGUI()
		super().drawGUI()
			
		
mainMenuGUI = mainMenuGUIClass()
newGamePlayerNumberGUI = newGamePlayerNumberGUIClass()
newGamePlayerNameGUI = newGamePlayerNameGUIClass()
newGameSelectTokenGUI = newGameSelectTokenGUIClass()
gameLoopGUI = gameLoopGUIClass()
readActionCardGUI = readActionCardGUIClass()
rollThreeGUI = rollThreeGUIClass()
improvePropsPickGroupGUI = improvePropsPickGroupGUIClass()
unimprovePropsGUI = unimprovePropsGUIClass()
improvePropsGUI = improvePropsGUIClass()
unimprovePropsPickGroupGUI = unimprovePropsPickGroupGUIClass()
mortgagePropsGUI = mortgagePropertiesGUIClass()
unmortgagePropsGUI = unmortgagePropertiesGUIClass()
tradeInterfaceGUI = tradeInterfaceGUIClass()

class Player:
	def __init__(self, name, number, tokenChoice):
		self.Playernumber = number
		self.PlayerName = name
		self.BoardPosition = [1,0]
		self.PlayerMoney = 3200
		self.OwnedProps = []
		self.mortgagedProps = []
		self.IsInJail = False
		self.turnsInJail = 0
		self.isBankrupt = False
		self.heldTravelVouchers = [actionCards.travelVoucherDeck[0]]
		actionCards.travelVoucherDeck.pop(0)
		self.heldChanceCards = []
		self.heldChestCards = []
		self.heldRollThreeCards = [actionCards.rollThreeDeck[0]]
		actionCards.rollThreeDeck.pop(0)
		self.ownedColorGroups = {}
		self.ownsImprovableCG = False
		self.ownsImprovements = False
		self.ownedStock = {}
		self.playerTokenName = tokenChoice
		self.token = Token(tokenChoice)
		self.turnActive = False
		self.setBoardPosition([1,0])
	
	def __repr__(self):
		return self.PlayerName
	def __str__(self):
		return self.PlayerName
		
	def setBoardPosition(self, coords):
		self.BoardPosition = coords
		self.token.gbCoords = self.BoardPosition
		self.token.MoveDraw()
	
	def hasUnmortgagedProps(self):
		for i in self.OwnedProps:
			if Gameboard.propList[i][4] == "unmortgaged":
				return(True)
		return(False)
	def hasMortgagedProps(self):
		for i in self.OwnedProps:
			if Gameboard.propList[i][4] == "mortgaged":
				return(True)
		return(False)
		
	def turnsInJailString(self):
		if self.turnsInJail == 0:
			return "First"
		elif self.turnsInJail == 1:
			return "Second"
		elif self.turnsInJail == 2:
			return "Third"
	
	#ownedColorGroups = {"CGName": [improvableLevel, [propNum, ofEach], numOfImp]}
	def checkForCG(self):
		for i in range(len(self.OwnedProps)):
			if Gameboard.propList[self.OwnedProps[i]][1] == "CG":
				if Gameboard.propList[self.OwnedProps[i]][5] in self.ownedColorGroups:
					if self.ownedColorGroups[Gameboard.propList[self.OwnedProps[i]][5]][1].count(self.OwnedProps[i]) == 0:
						self.ownedColorGroups[Gameboard.propList[self.OwnedProps[i]][5]][1].append(self.OwnedProps[i])
					else:
						pass
				else:
					self.ownedColorGroups[Gameboard.propList[self.OwnedProps[i]][5]] = [0, [self.OwnedProps[i]], 0]
				if len(self.ownedColorGroups[Gameboard.propList[self.OwnedProps[i]][5]][1]) > Gameboard.propList[self.OwnedProps[i]][11] / 2:
					self.ownedColorGroups[Gameboard.propList[self.OwnedProps[i]][5]][0] = 1
					if len(self.ownedColorGroups[Gameboard.propList[self.OwnedProps[i]][5]][1]) == Gameboard.propList[self.OwnedProps[i]][11]:
						self.ownedColorGroups[Gameboard.propList[self.OwnedProps[i]][5]][0] = 2
					self.ownsImprovableCG = True
		for i in list(self.ownedColorGroups):
			if i in self.ownedColorGroups:
				j = 0
				#print(self.ownedColorGroups)
				#print(i)
				length = len(self.ownedColorGroups[i][1])
				while j < length:
					if Gameboard.propList[self.ownedColorGroups[i][1][j]][2] != self.Playernumber:
						self.ownedColorGroups[i][1].pop(j)
						j = j - 1
						#print("we popped one")
						if len(self.ownedColorGroups[i][1]) == 0:
							del self.ownedColorGroups[i]
							break
						elif len(self.ownedColorGroups[i][1]) < Gameboard.propList[self.ownedColorGroups[i][1][0]][11] and len(self.ownedColorGroups[i][1]) > Gameboard.propList[self.ownedColorGroups[i][1][0]][11] / 2:
							self.ownedColorGroups[i][0] = 1
						elif len(self.ownedColorGroups[i][1]) < Gameboard.propList[self.ownedColorGroups[i][1][0]][11] / 2:
							self.ownedColorGroups[i][0] = 0
					j = j + 1
			else:
				continue
		for i in self.ownedColorGroups:
			self.ownedColorGroups[i][1].sort()
		
class tradeObject:
	def __init__(self, playerProposing, playerProposed, outstandingDebt = 0):
		self.proposedBy = playerProposing
		self.proposedTo = playerProposed
		self.proposedByMoney = 0
		self.proposedToMoney = 0
		self.proposedByProps = []
		self.proposedToProps = []
		self.debtsOutstanding = outstandingDebt
		
	def viewTrade(self):
		print("The trade consists of:")
		print("From", self.proposedBy.PlayerName, "to", self.proposedTo.PlayerName)
		print(self.proposedByMoney, "dollars")
		if len(self.proposedByProps) > 0:
			for i in range(len(self.proposedByProps)):
				print(Gameboard.propList[self.proposedByProps[i]][0])
		print("From", self.proposedTo.PlayerName, "to", self.proposedBy.PlayerName)
		print(self.proposedToMoney, "dollars")
		if len(self.proposedToProps)> 0:
			for i in range(len(self.proposedToProps)):
				print(Gameboard.propList[self.proposedToProps[i]][0])
				
	def finalize(self):
		print(self.proposedBy.PlayerName, "gave", self.proposedByMoney, "dollars to", self.proposedTo.PlayerName)
		self.proposedBy.PlayerMoney = self.proposedBy.PlayerMoney - self.proposedByMoney
		self.proposedTo.PlayerMoney = self.proposedTo.PlayerMoney + self.proposedByMoney
		if len(self.proposedByProps) > 0:
			print(self.proposedBy.PlayerName, "gave the following properties to", self.proposedTo.PlayerName)
			for i in range(len(self.proposedByProps)):
				print(Gameboard.propList[self.proposedByProps[i]][0])
			for i in range(len(self.proposedByProps)):
				removeProp(self.proposedBy, self.proposedByProps[i])
				assignProp(self.proposedTo, self.proposedToProps[i])
		print(self.proposedTo.PlayerName, "gave", self.proposedToMoney, "dollars to", self.proposedBy.PlayerName)
		self.proposedTo.PlayerMoney = self.proposedTo.PlayerMoney - self.proposedToMoney
		self.proposedBy.PlayerMoney = self.proposedBy.PlayerMoney + self.proposedToMoney
		if len(self.proposedToProps) > 0:
			print(self.proposedTo.PlayerName, "gave the following properties to", self.proposedBy.PlayerName)
			for i in range(len(self.proposedToProps)):
				print(Gameboard.propList[self.proposedToProps[i]][0])
			for i in range(len(self.proposedToProps)):
				removeProp(self.proposedTo, self.proposedToProps[i])
				assignProp(self.proposedBy, self.proposedByProps[i])

class Diceclass:
	def __init__(self):
		self.State = [random.randint(1,6), random.randint(1,6)]
	
	def Sum(self):
		return self.State[0] + self.State[1]
	def Roll(self):
		return [random.randint(1,6), random.randint(1,6)]
Dice = Diceclass()

class mostRecentMoveClass:
	def __init__(self):
		self.displayMove = False
		self.displayStringLine1 = ""
		self.displayStringLine2 = ""
		self.displayStringLine3 = ""
		self.dialogString1 = ""
		self.dialogString2 = ""
		
		
	def clearMRV(self):
		self.displayMove = False
		self.displayStringLine1 = ""
		self.displayStringLine2 = ""
		self.displayStringLine3 = ""
		self.dialogString1 = ""
		self.dialogString2 = ""
mostRecentMove = mostRecentMoveClass()

class titleDeed:
	def __init__(self, name):
		self.deedName = name
		deedPath = os.path.join(deedDirectory, name + ".png")
		self.deedImage = pygame.image.load(deedPath).convert()
		self.deedRect = self.deedImage.get_rect()
		self.deedImageS = pygame.transform.smoothscale(self.deedImage, (100,115)).convert()
		self.deedRectS = self.deedImageS.get_rect()
		
	def __str__(self):
		return self.deedName
	def __repr__(self):
		return self.deedName
		
class stockCertClass:
	def __init__(self, name):
		self.certName = name
		certPath = os.path.join(deedDirectory, name + ".png")
		self.deedImage = pygame.image.load(deedPath).convert()
		self.deedRect = self.deedImage.get_rect()
		self.deedImageS = pygame.transform.smoothscale(self.deedImage, (100,115)).convert()
		self.deedRectS = self.deedImageS.get_rect()
		
	def __str__(self):
		return self.deedName
	def __repr__(self):
		return self.deedName

class actionCardSpriteClass:
	def __init__(self, name, cardtype):
		self.cardName = name
		if cardtype == "chance":
			cardPath = os.path.join(chanceDirectory, name + ".png")
		elif cardtype == "commChest":
			cardPath = os.path.join(commChestDirectory, name + ".png")
		elif cardtype == "travelVoucher":
			cardPath = os.path.join(travelVoucherDirectroy, name + ".png")
		elif cardtype == "rollThree":
			cardPath = os.path.join(rollThreeDirectory, name + ".png")
		self.cardImage = pygame.image.load(cardPath).convert()
		self.cardImage = pygame.transform.smoothscale(self.cardImage, (598,350)).convert()
		self.cardRect = self.cardImage.get_rect()
		self.cardImageS = pygame.transform.smoothscale(self.cardImage, (90,53)).convert()
		self.cardRectS = self.cardImageS.get_rect()
		
	def __str__(self):
		return self.cardName
	def __repr__(self):
		return self.cardName

class rollThreeNumberImagesClass:
	def __init__(self):
		self.one = pygame.image.load(os.path.join(rollThreeDirectory, "One.png")).convert()
		self.two = pygame.image.load(os.path.join(rollThreeDirectory, "Two.png")).convert()
		self.three = pygame.image.load(os.path.join(rollThreeDirectory, "Three.png")).convert()
		self.four = pygame.image.load(os.path.join(rollThreeDirectory, "Four.png")).convert()
		self.five = pygame.image.load(os.path.join(rollThreeDirectory, "Five.png")).convert()
		self.six = pygame.image.load(os.path.join(rollThreeDirectory, "Six.png")).convert()
	
	def getImage(self, number):
		if number == 1:
			return self.one
		if number == 2:
			return self.two
		if number == 3:
			return self.three
		if number == 4:
			return self.four
		if number == 5:
			return self.five
		if number == 6:
			return self.six
rollThreeNumberImages = rollThreeNumberImagesClass()
	
class rollThreeCardSpriteClass:
	def __init__(self, numbers):
		self.cardNumbers = numbers
		self.cardName = str(numbers)
		self.cardImage = pygame.image.load(os.path.join(rollThreeDirectory, "BlankRollThree.png")).convert()
		self.cardImage.blits(((rollThreeNumberImages.getImage(self.cardNumbers[0]), (61, 165)), (rollThreeNumberImages.getImage(self.cardNumbers[1]), (284, 165)), (rollThreeNumberImages.getImage(self.cardNumbers[2]), (506, 165))))
		self.cardImage = pygame.transform.smoothscale(self.cardImage, (598,350)).convert()
		self.cardRect = self.cardImage.get_rect()
		self.cardImageS = pygame.transform.smoothscale(self.cardImage, (90, 53)).convert()
		self.cardRectS = self.cardImageS.get_rect()
		
class Gameboardclass:
	def __init__(self):
		self.listspace = [["Free Parking", "Lake Street", "Community Chest (Outer 1)", "Nicollet Avenue", "Hennepin Avenue", "Bus Ticket", "Checker Cab Company", "Reading Railroad", "Esplanade Avenue", "Canal Street", "Chance (Outer 1)", "Cable Company", "Magazine Street", "Bourbon Street", "Holland Tunnel Outer", "Auction", "Katy Freeway", "Westheimer Road", "Internet Service Provider", "Kirby Drive", "Cullen Boulevard", "Chance (Outer 2)", "Black & White Cab Company", "Dekalb Avenue", "Community Chest (Outer 2)", "Andrew Young Intl Boulevard", "Decatur Street", "Peachtree Street", "Payday",    "Randolph Street", "Chance (Outer 3)", "Lake Shore Drive", "Wacker Drive", "Michigan Avenue", "Yellow Cab Company", "B&O Railroad Outer", "Community Chest (Outer 3)", "South Temple", "West Temple", "Trash Collector", "North Temple", "Temple Square", "Subway", "South Street", "Broad Street", "Walnut Street", "Community Chest (Outer 4)", "Market Street", "Bus Ticket", "Sewage System", "Ute Cab Company", "Birthday Gift", "Mulholland Drive", "Ventura Boulevard", "Chance (Outer 4)", "Rodeo Drive"],["Go",        "Mediterranean Avenue", "Community Chest (Middle 1)", "Baltic Avenue", "Income Tax", "Reading Railroad Middle", "Oriental Avenue", "Chance (Middle 1)", "Vermont Avenue", "Connecticut Avenue", "Roll Three", "St Charles Place", "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad Middle", "St James Place", "Community Chest (Middle 2)", "Tennessee Avenue", "New York Avenue", "In Jail / Just Visiting", "Kentucky Avenue", "Chance (Middle 2)", "Indiana Avenue", "Illinois Avenue", "B&O Railroad Middle", "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens", "Squeeze Play", "Pacific Avenue", "North Carolina Avenue", "Community Chest (Middle 3)", "Pennsylvania Avenue", "Short Line Middle", "Chance (Middle 3)", "Park Place", "Luxury Tax", "Boardwalk"], ["Go to Jail", "The Embarcadero", "Fishermans Wharf", "Telephone Company", "Community Chest (Inner)", "Beacon Street", "Bonus",    "Boylston Street", "Newbury Street", "Pennsylvania Railroad Inner", "Fifth Avenue", "Madison Avenue", "Stock Exchange", "Wall Street", "Tax Refund", "Gas Company", "Chance (Inner)", "Florida Avenue", "Holland Tunnel Inner", "Miami Avenue", "Biscayne Avenue", "Short Line Inner", "Reverse Direction", "Lombard Street"]]
		self.spaceType = [["Free Parking", "Property",    "Community Chest",           "Property",        "Property",        "Bus Ticket", "Property",            "Property",         "Property",         "Property",     "Chance",           "Property",      "Property",        "Property",       "Holland Tunnel",       "Auction", "Property",     "Property",        "Property",                  "Property",    "Property",         "Chance",           "Property",                  "Property",      "Community Chest",           "Property",                    "Property",       "Property",         "Paycorner", "Property",        "Chance",           "Property",         "Property",     "Property",        "Property",           "Property",           "Community Chest",           "Property",     "Property",    "Property",        "Property",     "Property",      "Subway", "Property",     "Property",     "Property",      "Community Chest",           "Property",      "Bus Ticket", "Property",      "Property",        "Birthday Gift", "Property",         "Property",          "Chance",           "Property"],   ["Paycorner", "Property",             "Community Chest",            "Property",      "Income Tax", "Property",                "Property",        "Chance",            "Property",       "Property",           "Roll Three", "Property",         "Property",         "Property",      "Property",        "Property",                     "Property",       "Community Chest",            "Property",         "Property",        "Jail",                    "Property",        "Chance",            "Property",       "Property",        "Property",            "Property",        "Property",       "Property",    "Property",       "Squeeze Play", "Property",       "Property",              "Community Chest",            "Property",            "Property",          "Chance",            "Property",   "Luxury Tax", "Property"],  ["Go to Jail", "Property",        "Property",         "Property",          "Community Chest",         "Property",      "Paycorner", "Property",        "Property",       "Property",                    "Property",     "Property",       "Stock Exchange", "Property",    "Tax Refund", "Property",    "Chance",        "Property",       "Holland Tunnel",       "Property",     "Property",        "Property",         "Reverse Direction", "Property"]]
		self.propNum =   [[-1,              0,            -1,                          1,                 2,                 -1,           3,                     4,                  5,                  6,              -1,                 7,               8,                 9,                -1,                     -1,        10,             11,                12,                          13,            14,                 -1,                 15,                          16,              -1,                          17,                            18,               19,                 -1,          20,                -1,                 21,                 22,             23,                24,                   25,                   -1,                          26,             27,            28,                29,             30,              -1,       31,             32,             33,              -1,                          34,              -1,           35,              36,                -1,              37,                 38,                  -1,                 39],           [-1,          40,                     -1,                           41,              -1,           4,                         42,                -1,                  43,               44,                   -1,           45,                 46,                 47,              48,                49,                             50,               -1,                           51,                 52,                -1,                        53,                -1,                  54,               55,                25,                    56,                57,               58,            59,               -1,             60,               61,                      -1,                           62,                   63,                  -1,                   64,           -1,           65,],         [-1,           70,                71,                 72,                  -1,                        73,              -1,         74,                75,               49,                            76,             77,               -1,               78,            -1,           79,            -1,               66,               -1,                     67,             68,                63,                 -1,                  69]]
		self.colorBarCoords = {"Lake Street": (883,947,0), "Nicollet Avenue": (759,947,0), "Hennepin Avenue": (697,947,0), "Esplanade Avenue": (449,947,0), "Canal Street": (385,947,0), "Magazine Street": (197,947,0), "Bourbon Street": (135,947,0), "Katy Freeway": (113,821,270), "Westheimer Road": (113,759,270), "Kirby Drive": (113,635,270), "Cullen Boulevard": (113,573,270), "Dekalb Avenue": (113,383,270), "Andrew Young Intl Boulevard": (113,259,270), "Decatur Street": (113,197,270), "Peachtree Street": (113,135,270), "Randolph Street": (135,113,180), "Lake Shore Drive": (259,113,180), "Wacker Drive": (321,113,180), "Michigan Avenue": (383,113,180), "South Temple": (635,113,180), "West Temple": (697,113,180), "North Temple": (821,113,180), "Temple Square": (883,113,180), "South Street": (947,135,90), "Broad Street": (947,197,90), "Walnut Street": (947,259,90), "Market Street": (947,383,90), "Mulholland Drive": (947,697,90), "Ventura Boulevard": (947,759,90), "Rodeo Drive": (947,883,90), "Mediterranean Avenue": (754,816,0), "Baltic Avenue": (630,816,0), "Oriental Avenue": (448,816,0), "Vermont Avenue": (326,816,0), "Connecticut Avenue": (264,816,0), "St Charles Place": (242,754,270), "States Avenue": (242,630,270), "Virginia Avenue": (242,568,270), "St James Place": (242,448,270), "Tennessee Avenue": (242,326,270), "New York Avenue": (242,262,270), "Kentucky Avenue": (262,242,180), "Indiana Avenue": (386,242,180), "Illinois Avenue": (448,242,180), "Atlantic Avenue": (568,242,180), "Ventnor Avenue": (630,242,180), "Marvin Gardens": (754,242,180), "Pacific Avenue": (816,262,90), "North Carolina Avenue": (816,326,90), "Pennsylvania Avenue": (816,448,90), "Park Place": (816,630,90), "Boardwalk": (816,754,90), "Lombard Street": (693,628,90), "The Embarcadero": (628,693,0), "Fishermans Wharf": (566,693,0), "Beacon Street": (389,693,0), "Boylston Street": (366,628,270), "Newbury Street": (366,566,270), "Fifth Avenue": (366,451,270), "Madison Avenue": (366,389,270), "Wall Street": (389,366,180), "Florida Avenue": (628,366,180), "Miami Avenue": (693,389,90), "Biscayne Avenue": (693,451,90)}
		#[0."name", 1."property type", 2."Current owner", 3.price, 4."mortgageStatus", 5."color group name", 6.collectionLevel, 7.developmentLevel, 8.[(base rent), (one house), (two house), (three house), (four house), (hotel), (skyscraper)], 9.mortgagePrice, 10.improvementCost, 11.numberInGroup, 12.[titleDeed("nameF"),titleDeed("nameB")]]
		#[0."name", 1."property type", 2."Current owner", 3.price, 4."mortgageStatus", 5.[(rent or multiplier w/1), [(r/m w/2), (r/m w/3), (r/m w/4), (m w/5), (m w/6), (m w/7), (m w/8], 6.mortgagePrice, 7.[titleDeed("nameF",titleDeed("nameB"]]
		self.propList = [["Lake St.", "CG", "bank", 30, "unmortgaged", "Rose", 0,0, [1,5,15,45,80,125,625], 15, 50, 3, [titleDeed("LakeStF"),titleDeed("LakeStB")]],
		["Nicollet Ave.", "CG", "bank", 30, "unmortgaged", "Rose", 0,0, [1,5,15,45,80,125,625], 15, 50, 3, [titleDeed("NicolletAveF"),titleDeed("NicolletAveB")]],
		["Hennepin Ave.", "CG", "bank", 60, "unmortgaged", "Rose", 0,0, [3,15,45,120,240,350,850], 30, 50, 3, [titleDeed("HennepinAveF"),titleDeed("HennepinAveB")]],
		["Checker Cab Co.", "CabCo", "bank", 300, "unmortgaged", [30,60,120,240], 150, [titleDeed("CheckerCabCoF"),titleDeed("CheckerCabCoB")]],
		["Reading Railroad", "Railroad", "bank", 200, "unmortgaged", [25,50,100,200], 100, [titleDeed("ReadingRRF"),titleDeed("ReadingRRB")]],
		["The Esplanade", "CG", "bank", 90, "unmortgaged", "Light Green", 0,0, [5,25,80,225,360,600,1000], 50, 50, 4, [titleDeed("TheEsplanadeF"),titleDeed("TheEsplanadeB")]],
		["Canal St.", "CG", "bank", 90, "unmortgaged", "Light Green", 0,0, [5,25,80,225,360,600,1000], 50, 50, 4, [titleDeed("CanalStF"),titleDeed("CanalStB")]],
		["Cable Company", "Utility", "bank", 150, "unmortgaged", [4,10,20,40,80,100,120,150], 75, [titleDeed("CableCompanyF"),titleDeed("CableCompanyB")]],
		["Magazine St.", "CG", "bank", 120, "unmortgaged", "Light Green", 0,0, [8,40,100,300,450,600,1100], 60, 50, 4, [titleDeed("MagazineStF"),titleDeed("MagazineStB")]],
		["Bourbon St.", "CG", "bank", 120, "unmortgaged", "Light Green", 0,0, [8,40,100,300,450,600,1100], 60, 50, 4, [titleDeed("BourbonStF"),titleDeed("BourbonStB")]],
		["Katy Freeway", "CG", "bank", 150, "unmortgaged", "Light Yellow", 0,0, [11,55,160,475,650,800,1300], 70, 100, 4, [titleDeed("KatyFreewayF"),titleDeed("KatyFreewayB")]],
		["Westheimer Rd.", "CG", "bank", 150, "unmortgaged", "Light Yellow", 0,0, [11,55,160,475,650,800,1300], 70, 100, 4, [titleDeed("WestheimerRdF"),titleDeed("WestheimerRdB")]],
		["Internet Service Provider", "Utility", "bank", 150, "unmortgaged", [4,10,20,40,80,100,120,150], 75, [titleDeed("InternetServiceProviderF"),titleDeed("InternetServiceProviderB")]],
		["Kirby Dr.", "CG", "bank", 180, "unmortgaged", "Light Yellow", 0,0, [14,70,200,550,750,950,1450], 80, 100, 4, [titleDeed("KirbyDrF"),titleDeed("KirbyDrB")]],
		["Cullen Blvd.", "CG", "bank", 180, "unmortgaged", "Light Yellow", 0,0, [14,70,200,550,750,950,1450], 80, 100, 4, [titleDeed("CullenBlvdF"),titleDeed("CullenBlvdB")]],
		["Black & White Cab Co.", "CabCo", "bank", 300, "unmortgaged", [30,60,120,240], 150, [titleDeed("BlackAndWhiteCabCoF"),titleDeed("BlackAndWhiteCabCoB")]],
		["Dekalb Ave.", "CG", "bank", 210, "unmortgaged", "Teal", 0,0, [17,85,240,670,840,1025,1525], 90, 100, 4, [titleDeed("DekalbAveF"),titleDeed("DekalbAveB")]],
		["Young Int'l Blvd.", "CG", "bank", 210, "unmortgaged", "Teal", 0,0, [17,85,240,670,840,1025,1525], 90, 100, 4, [titleDeed("YoungIntlBlvdF"),titleDeed("YoungIntlBlvdB")]],
		["Decatur St.", "CG", "bank", 240, "unmortgaged", "Teal", 0,0, [20,100,300,750,925,1100,1600], 100, 100, 4, [titleDeed("DecaturStF"),titleDeed("DecaturStB")]],
		["Peachtree St.", "CG", "bank", 240, "unmortgaged", "Teal", 0,0, [20,100,300,750,925,1100,1600], 100, 100, 4, [titleDeed("PeachtreeStF"),titleDeed("PeachtreeStB")]],
		["Randolph St.", "CG", "bank", 270, "unmortgaged", "Maroon", 0,0, [23,115,345,825,1010,1180,2180], 110, 150, 4, [titleDeed("RandolphStF"),titleDeed("RandolphStB")]],
		["Lake Shore Dr.", "CG", "bank", 270, "unmortgaged", "Maroon", 0,0, [23,115,345,825,1010,1180,2180], 110, 150, 4, [titleDeed("LakeShoreDrF"),titleDeed("LakeShoreDrB")]],
		["Wacker Dr.", "CG", "bank", 300, "unmortgaged", "Maroon", 0,0, [26,130,390,900,1100,1275,2275], 120, 150, 4, [titleDeed("WackerDrF"),titleDeed("WackerDrB")]],
		["Michigan Ave.", "CG", "bank", 300, "unmortgaged", "Maroon", 0,0, [26,130,390,900,1100,1275,2275], 120, 150, 4, [titleDeed("MichiganAveF"),titleDeed("MichiganAveB")]],
		["Yellow Cab Co.", "CabCo", "bank", 300, "unmortgaged", [30,60,120,240], 150, [titleDeed("YellowCabCoF"),titleDeed("YellowCabCoB")]],
		["B. & O. Railroad", "Railroad", "bank", 200, "unmortgaged", [25,50,100,200], 100, [titleDeed("BAndORRF"),titleDeed("BAndORRB")]],
		["South Temple", "CG", "bank", 330, "unmortgaged", "Brown", 0,0, [32,160,470,1050,1250,1500,2500], 130, 200, 4, [titleDeed("SouthTempleF"),titleDeed("SouthTempleB")]],
		["West Temple", "CG", "bank", 330, "unmortgaged", "Brown", 0,0, [32,160,470,1050,1250,1500,2500], 130, 200, 4, [titleDeed("WestTempleF"),titleDeed("WestTempleB")]],
		["Trash Collector", "Utility", "bank", 150, "unmortgaged", [4,10,20,40,80,100,120,150], 75, [titleDeed("TrashCollectorF"),titleDeed("TrashCollectorB")]],
		["North Temple", "CG", "bank", 360, "unmortgaged", "Brown", 0,0, [38,170,520,1125,1425,1600,2650], 140, 200, 4, [titleDeed("NorthTempleF"),titleDeed("NorthTempleB")]],
		["Temple Square", "CG", "bank", 360, "unmortgaged", "Brown", 0,0, [38,170,520,1125,1425,1600,2650], 140, 200, 4, [titleDeed("TempleSquareF"),titleDeed("TempleSquareB")]],
		["South St.", "CG", "bank", 390, "unmortgaged", "Peach", 0,0, [45,210,575,1300,1600,1800,3300], 150, 250, 4, [titleDeed("SouthStF"),titleDeed("SouthStB")]],
		["Broad St.", "CG", "bank", 390, "unmortgaged", "Peach", 0,0, [45,210,575,1300,1600,1800,3300], 150, 250, 4, [titleDeed("BroadStF"),titleDeed("BroadStB")]],
		["Walnut St.", "CG", "bank", 420, "unmortgaged", "Peach", 0,0, [55,225,630,1450,1750,2050,3550], 160, 250, 4, [titleDeed("WalnutStF"),titleDeed("WalnutStB")]],
		["Market St.", "CG", "bank", 420, "unmortgaged", "Peach", 0,0, [55,225,630,1450,1750,2050,3550], 160, 250, 4, [titleDeed("MarketStF"),titleDeed("MarketStB")]],
		["Sewage System", "Utility", "bank", 150, "unmortgaged", [4,10,20,40,80,100,120,150], 75, [titleDeed("SewageSystemF"),titleDeed("SewageSystemB")]],
		["Ute Cab Co.", "CabCo", "bank", 300, "unmortgaged", [30,60,120,240], 150, [titleDeed("UteCabCoF"),titleDeed("UteCabCoB")]],
		["Mulholland Blvd.", "CG", "bank", 450, "unmortgaged", "Dark Red", 0,0, [70,350,750,1600,1850,2100,3600], 175, 300, 3, [titleDeed("MulhollandBlvdF"),titleDeed("MulhollandBlvdB")]],
		["Ventura Blvd.", "CG", "bank", 480, "unmortgaged", "Dark Red", 0,0, [80,400,825,1800,2175,2550,4050], 200, 300, 3, [titleDeed("VenturaBlvdF"),titleDeed("VenturaBlvdB")]],
		["Rodeo Dr.", "CG", "bank", 510, "unmortgaged", "Dark Red", 0,0, [90,450,900,2000,2500,3000,4500], 250, 300, 3, [titleDeed("RodeoDrF"),titleDeed("RodeoDrB")]],
		["Mediterranean Ave.", "CG", "bank", 60, "unmortgaged", "Purple", 0,0, [2,10,30,90,160,250,750], 30, 50, 2, [titleDeed("MediterraneanAveF"),titleDeed("MediterraneanAveB")]],
		["Baltic Ave.", "CG", "bank", 60, "unmortgaged", "Purple", 0,0, [4,20,60,180,320,450,900], 30, 50, 2, [titleDeed("BalticAveF"),titleDeed("BalticAveB")]],
		["Oriental Ave.", "CG", "bank", 100, "unmortgaged", "Light Blue", 0,0, [6,30,90,270,400,550,1050], 50, 50, 3, [titleDeed("OrientalAveF"),titleDeed("OrientalAveB")]],
		["Vermont Ave.", "CG", "bank", 100, "unmortgaged", "Light Blue", 0,0, [6,30,90,270,400,550,1050], 50, 50, 3, [titleDeed("VermontAveF"),titleDeed("VermontAveB")]],
		["Connecticut Ave.", "CG", "bank", 120, "unmortgaged", "Light Blue", 0,0, [8,40,100,300,450,600,1100], 60, 50, 3, [titleDeed("ConnecticutAveF"),titleDeed("ConnecticutAveB")]],
		["St. Charles Place", "CG", "bank", 140, "unmortgaged", "Pink", 0,0, [10,50,150,450,625,750,1250], 70, 100, 3, [titleDeed("StCharlesPlaceF"),titleDeed("StCharlesPlaceB")]],
		["Electric Company", "Utility", "bank", 150, "unmortgaged", [4,10,20,40,80,100,120,150], 75, [titleDeed("ElectricCompanyF"),titleDeed("ElectricCompanyB")]],
		["States Ave.", "CG", "bank", 140, "unmortgaged", "Pink", 0,0, [10,50,150,450,625,750,1250], 70, 100, 3, [titleDeed("StatesAveF"),titleDeed("StatesAveB")]],
		["Virginia Ave.", "CG", "bank", 160, "unmortgaged", "Pink", 0,0, [12,60,180,500,700,900,1400], 80, 100, 3, [titleDeed("VirginiaAveF"),titleDeed("VirginiaAveB")]],
		["Pennsylvania R.R.", "Railroad", "bank", 200, "unmortgaged", [25,50,100,200], 100, [titleDeed("PennsylvaniaRRF"),titleDeed("PennsylvaniaRRB")]],
		["St. James Place", "CG", "bank", 180, "unmortgaged", "Light Orange", 0,0, [14,70,200,550,750,950,1450], 90, 100, 3, [titleDeed("StJamesPlaceF"),titleDeed("StJamesPlaceB")]],
		["Tennessee Ave.", "CG", "bank", 180, "unmortgaged", "Light Orange", 0,0, [14,70,200,550,750,950,1450], 90, 100, 3, [titleDeed("TennesseeAveF"),titleDeed("TennesseeAveB")]],
		["New York Ave.", "CG", "bank", 200, "unmortgaged", "Light Orange", 0,0, [16,80,220,600,800,1000,1500], 100, 100, 3, [titleDeed("NewYorkAveF"),titleDeed("NewYorkAveB")]],
		["Kentucky Ave.", "CG", "bank", 220, "unmortgaged", "Light Red", 0,0, [18,90,250,700,875,1050,2050], 100, 150, 3, [titleDeed("KentuckyAveF"),titleDeed("KentuckyAveB")]],
		["Indiana Ave.", "CG", "bank", 220, "unmortgaged", "Light Red", 0,0, [18,90,250,700,875,1050,2050], 100, 150, 3, [titleDeed("IndianaAveF"),titleDeed("IndianaAveB")]],
		["Illinois Ave.", "CG", "bank", 240, "unmortgaged", "Light Red", 0,0, [20,100,300,750,925,1100,2100], 120, 150, 3, [titleDeed("IllinoisAveF"),titleDeed("IllinoisAveB")]],
		["Atlantic Ave.", "CG", "bank", 260, "unmortgaged", "Dark Yellow", 0,0, [22,110,330,800,975,1150,2150], 130, 150, 3, [titleDeed("AtlanticAveF"),titleDeed("AtlanticAveB")]],
		["Ventnor Ave.", "CG", "bank", 260, "unmortgaged", "Dark Yellow", 0,0, [22,110,330,800,975,1150,2150], 130, 150, 3, [titleDeed("VentnorAveF"),titleDeed("VentnorAveB")]],
		["Water Works", "Utility", "bank", 150, "unmortgaged", [4,10,20,40,80,100,120,150], 75, [titleDeed("WaterWorksF"),titleDeed("WaterWorksB")]],
		["Marvin Gardens", "CG", "bank", 280, "unmortgaged", "Dark Yellow", 0,0, [24,120,350,850,1025,1200,2200], 140, 150, 3, [titleDeed("MarvinGardensF"),titleDeed("MarvinGardensB")]],
		["Pacific Ave.", "CG", "bank", 300, "unmortgaged", "Dark Green", 0,0, [26,130,390,900,1100,1275,2275], 150, 200, 3, [titleDeed("PacificAveF"),titleDeed("PacificAveB")]],
		["No. Carolina Ave.", "CG", "bank", 300, "unmortgaged", "Dark Green", 0,0, [26,130,390,900,1100,1275,2275], 150, 200, 3, [titleDeed("NCarolinaAveF"),titleDeed("NCarolinaAveB")]],
		["Pennsylvania Ave.", "CG", "bank", 320, "unmortgaged", "Dark Green", 0,0, [28,150,450,1000,1200,1400,2400], 160, 200, 3, [titleDeed("PennsylvaniaAveF"),titleDeed("PennsylvaniaAveB")]],
		["Short Line", "Railroad", "bank", 200, "unmortgaged", [25,50,100,200], 100, [titleDeed("ShortLineF"),titleDeed("ShortLineB")]],
		["Park Place", "CG", "bank", 350, "unmortgaged", "Dark Blue", 0,0, [35,175,500,1100,1300,1500,2500], 200, 200, 2, [titleDeed("ParkPlaceF"),titleDeed("ParkPlaceB")]],
		["Boardwalk", "CG", "bank", 400, "unmortgaged", "Dark Blue", 0,0, [50,200,600,1400,1700,2000,3000], 200, 200, 2, [titleDeed("BoardwalkF"),titleDeed("BoardwalkB")]],
		["Florida Ave.", "CG", "bank", 130, "unmortgaged", "Dark Orange", 0,0, [9,45,120,350,500,700,1200], 65, 50, 3, [titleDeed("FloridaAveF"),titleDeed("FloridaAveB")]],
		["Miami Ave.", "CG", "bank", 130, "unmortgaged", "Dark Orange", 0,0, [9,45,120,350,500,700,1200], 65, 50, 3, [titleDeed("MiamiAveF"),titleDeed("MiamiAveB")]],
		["Biscayne Ave.", "CG", "bank", 150, "unmortgaged", "Dark Orange", 0,0, [11,55,160,475,650,800,1300], 65, 50, 3, [titleDeed("BiscayneAveF"),titleDeed("BiscayneAveB")]],
		["Lombard St.", "CG", "bank", 210, "unmortgaged", "White", 0,0, [17,85,240,475,670,1025,1525], 105, 100, 3, [titleDeed("LombardStF"),titleDeed("LombardStB")]],
		["The Embarcadero", "CG", "bank", 210, "unmortgaged", "White", 0,0, [17,85,240,475,670,1025,1525], 105, 100, 3, [titleDeed("TheEmbarcaderoF"),titleDeed("TheEmbarcaderoB")]],
		["Fishermans Wharf", "CG", "bank", 250, "unmortgaged", "White", 0,0, [21,105,320,780,950,1125,1625], 125, 100, 3, [titleDeed("FishermansWharfF"),titleDeed("FishermansWharfB")]],
		["Telephone Company", "Utility", "bank", 150, "unmortgaged", [4,10,20,40,80,100,120,150], 75, [titleDeed("TelephoneCompanyF"),titleDeed("TelephoneCompanyB")]],
		["Beacon St.", "CG", "bank", 330, "unmortgaged", "Black", 0,0, [30,160,470,1050,1250,1500,2500], 165, 200, 3, [titleDeed("BeaconStF"),titleDeed("BeaconStB")]],
		["Boylston St.", "CG", "bank", 330, "unmortgaged", "Black", 0,0, [30,160,470,1050,1250,1500,2500], 165, 200, 3, [titleDeed("BoylstonStF"),titleDeed("BoylstonStB")]],
		["Newbury St.", "CG", "bank", 380, "unmortgaged", "Black", 0,0, [40,185,550,1100,1500,1700,2700], 190, 200, 3, [titleDeed("NewburyStF"),titleDeed("NewburyStB")]],
		["Fifth Ave.", "CG", "bank", 430, "unmortgaged", "Gray", 0,0, [60,220,650,1500,1800,2100,3600], 215, 300, 3, [titleDeed("FifthAveF"),titleDeed("FifthAveB")]],
		["Madison Ave.", "CG", "bank", 430, "unmortgaged", "Gray", 0,0, [60,220,650,1500,1800,2100,3600], 215, 300, 3, [titleDeed("MadisonAveF"),titleDeed("MadisonAveB")]],
		["Wall St.", "CG", "bank", 500, "unmortgaged", "Gray", 0,0, [80,300,800,1800,2200,2700,4200], 250, 300, 3, [titleDeed("WallStF"),titleDeed("WallStB")]],
		["Gas Company", "Utility", "bank", 150, "unmortgaged", [4,10,20,40,80,100,120,150], 75, [titleDeed("GasCompanyF"),titleDeed("GasCompanyB")]]]
		
		self.poolMoney = 0
		self.unownedProps = []
		
		self.stocksInBank = {"Motion Pictures": 5, "Allied Steamships": 5, "National Utilities": 5, "General Radio": 5, "United Railways": 5, "Acme Motors": 5}
		self.stocksParValues = {"Motion Pictures": 100, "Allied Steamships": 110, "National Utilities": 120, "General Radio": 130, "United Railways": 140, "Acme Motors": 150}
		self.stocksDividendCharts = {"Motion Pictures": [10 ,40, 90, 160, 250], "Allied Steamships": {11, 44, 99, 176, 275}, "National Utilities": [12, 48, 108, 192, 300], "General Radio": [13, 52, 117, 208, 325], "United Railways": [14, 56, 126, 224, 350], "Acme Motors": [15, 60, 135, 240, 375]}
	
	def ref(self, coords):
		return self.listspace[coords[0]][coords[1]]
	def deref(self, propNumber):
		for i in range(3):
			for j in range(len(self.propNum[i])):
				if self.propNum[i][j] == propNumber:
					return [i,j]
	def countUnownedProps(self):
		self.unownedProps = []
		for i in range(len(self.propList)):
			if self.propList[i][2] == "bank":
				self.unownedProps.append(i)

class aCardClass:
	def __init__(self):
		#action card decks are represented as a list of numbers that will get shuffled. Each number references the list of action cards.
		self.chanceDeck = [0,1,2,2,2,2,2,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,16,17,18,19,20,20,21,21,22,23,24,25,26,26,26,26,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]
		#[0. "title", 1. "text", 2. "handler", 3. [handlerdata], 4. actionCardSpriteClass(filename, chance)]
		self.chanceCards = [["Advance to Illinois Ave.", "", "ast", [1,24], actionCardSpriteClass("AdvanceToIllinoisAve", "chance")],
		["Advance to Saint Charles Place.", "", "ast", [1,11], actionCardSpriteClass("AdvanceToSaintCharlesPlace", "chance")],
		["Advance to the Stock Exchange", "", "ast", [2,12], actionCardSpriteClass("AdvanceToTheStockExchange", "chance")],
		["Advance to Boardwalk", "", "ast", [1,39], actionCardSpriteClass("AdvanceToBoardwalk", "chance")],
		["Ride on the Reading", "", "ast", [1,5], actionCardSpriteClass("RideOnTheReading", "chance")],
		["Occupy Wall Street", "", "ast", [2,13], actionCardSpriteClass("OccupyWallStreet", "chance")],
		["Get Rollin'", "", "ast", [1,10], actionCardSpriteClass("GetRollin", "chance")],
		["Advance to Boylston Street", "", "ast", [2,7], actionCardSpriteClass("AdvanceToBoylstonStreet", "chance")],
		["Advance to Lombard Street", "", "ast", [2,23], actionCardSpriteClass("AdvanceToLombardStreet", "chance")],
		["HEY! TAXI!!! *whistle*", "", "ast", [0,22], actionCardSpriteClass("HeyTaxi", "chance")],
		["Advance to Squeeze Play", "", "ast", [1,30], actionCardSpriteClass("AdvanceToSqueezePlay", "chance")],
		["Garbage Day", "", "ast", [1,30], actionCardSpriteClass("GarbageDay", "chance")],
		["Advance to the Pay Corner", "", "apc", 0, actionCardSpriteClass("AdvanceToThePayCorner", "chance")],
		["Advance to the Nearest Utility", "", "atn", "utility", actionCardSpriteClass("AdvanceToTheNearestUtility", "chance")],
		["Advance to the Nearest Railroad", "", "atn", "railroad", actionCardSpriteClass("AdvanceToTheNearestRailroad", "chance")],
		["Taxi Wars are not Fare!", "", "atcsp", 0, actionCardSpriteClass("TaxiWarsAreNotFare", "chance")], 
		["Advance to Tax Refund", "", "astpep", [[2,14], 50], actionCardSpriteClass("AdvanceToTaxRefund", "chance")],
		["Ride the Subway", "", "mdst", [0,42], actionCardSpriteClass("RideTheSubway", "chance")],
		["MARDI GRAS!", "", "amdst", [0,9], actionCardSpriteClass("MardiGras", "chance")],
		["Get Taken for a Ride", "", "mdnpdr", "cabco", actionCardSpriteClass("GetTakenForARide", "chance")],
		["Changing Lanes", "", "mdud", "down", actionCardSpriteClass("ChangingLanesB", "chance")],
		["Changing Lanes", "", "mdud", "up", actionCardSpriteClass("ChangingLanesA", "chance")],
		["GPS is not working", "", "mdc", 0, actionCardSpriteClass("GPSIsNotWorking", "chance")],
		["Go to Jail!", "", "gtj", 0, actionCardSpriteClass("GoToJail", "chance")],
		["Pay Back!", "", "gtjnr", 0, actionCardSpriteClass("PayBack", "chance")],
		["Get Out of Jail Free!", "", "keep", "gojf", actionCardSpriteClass("GetOutOfJailFree", "chance")],
		["Just Say 'NO'!", "", "keep", "jsn", actionCardSpriteClass("JustSayNo", "chance")],
		["Buyer's Market!", "", "keep", "mduopbd", actionCardSpriteClass("BuyersMarket", "chance")],
		["Excellent Accounting", "", "keep", "atfca", actionCardSpriteClass("ExcellentAccounting", "chance")],
		["Strong-armed Deal", "", "keep", "mft", actionCardSpriteClass("StrongArmedDeal", "chance")],
		["See You In Court!", "", "keep", "sap", actionCardSpriteClass("SeeYouInCourt", "chance")],
		["Slick Move", "", "keep", "stap", actionCardSpriteClass("SlickMove", "chance")],
		["Foreclosed Property Sale!", "", "keep", "camp", actionCardSpriteClass("ForeclosedPropertySale", "chance")],
		["Zero Dollars Down!", "", "keep", "bfh", actionCardSpriteClass("ZeroDollarsDown", "chance")],
		["Always Bank on Family", "", "keep", "iaub", actionCardSpriteClass("AlwaysBankOnFamily", "chance")],
		["Comped Room", "", "keep", "pnr", actionCardSpriteClass("CompedRoom", "chance")],
		["School Fees", "", "pmp", 150, actionCardSpriteClass("SchoolFees", "chance")],
		["Party Time", "", "pmp", 25, actionCardSpriteClass("PartyTime", "chance")],
		["Loan Matures!", "", "cmb", 150, actionCardSpriteClass("LoanMatures", "chance")],
		["Holiday Bonus!", "", "cmb", 100, actionCardSpriteClass("HolidayBonus", "chance")],
		["Gain Interest from Savings", "", "cmb", 50, actionCardSpriteClass("GainInterestFromSavings", "chance")],
		["Win the Marathon!", "", "ccpc", 0, actionCardSpriteClass("WinTheMarathon", "chance")],
		["You are elected as the Chairperson", "", "pep", 50, actionCardSpriteClass("YouAreElectedAsTheChairperson", "chance")],
		["Social Media Fail!", "", "pep", 50, actionCardSpriteClass("SocialMediaFail", "chance")],
		["New Fitness Craze", "", "pep", 50, actionCardSpriteClass("NewFitnessCraze", "chance")],
		["Shouldn't the Train be here already?", "", "ifrailpep", 50, actionCardSpriteClass("ShouldntTheTrainBeHereAlready", "chance")],
		["Go Back Three (3) Spaces", "", "mxs", -3, actionCardSpriteClass("GoBackThreeSpaces", "chance")],
		["Forward Thinker", "", "mxs", 3, actionCardSpriteClass("ForwardThinker", "chance")],
		["Stock Market CRASH!", "", "retstk", 0, actionCardSpriteClass("StockMarketCrash", "chance")],
		["Video Killed the Radio Star!", "", "reddiv", "general radio", actionCardSpriteClass("VideoKilledtheRadioStar", "chance")],
		["Entertainment Rocks!", "", "coldiv", ["motion pictures", "general radio"], actionCardSpriteClass("EntertainmentRocks", "chance")],
		["Travel is all the Rage!", "", "coldiv", ["united railways", "acme motors", "allied steamships"], actionCardSpriteClass("TravelIsAllTheRage", "chance")],
		["Electric Car Shocking Success!", "", "coldivec", ["acme motors", "national utilities"], actionCardSpriteClass("ElectricCarShockingSuccess", "chance")],
		["Caught Insider Trading!", "", "fjifs", 0, actionCardSpriteClass("CaughtInsiderTrading", "chance")],
		["Business Trip", "", "travvou", 1, actionCardSpriteClass("BusinessTrip", "chance")],
		["Hurricane makes landfall!", "", "remhou", 0, actionCardSpriteClass("HurricaneMakesLandfall", "chance")],
		["Make General Repairs to all your properties.", "", "ppimp", [25,25,100], actionCardSpriteClass("MakeGeneralRepairsToAllYourProperties", "chance")],
		["Property Taxes", "", "ppp", 25, actionCardSpriteClass("PropertyTaxes", "chance")],
		["Assets Seized!", "", "surprop", 0, actionCardSpriteClass("AssetsSeized", "chance")]]
		
		self.chestDeck = [0,0,0,0,0,0,1,2,3,4,5,6,6,7,7,8,9,10,11,12,12,12,12,12,12,13,14,15,16,17,18,19,20,21,22,23,24,25,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57]
		
		self.chestCards = [["Advance to the Stock Exchange", "", "ast", [2,12], actionCardSpriteClass("AdvanceToTheStockExchange", "commChest")],
		["Advance to this Track's Pay Corner", "", "apc", 0, actionCardSpriteClass("AdvanceToThisTracksPayCorner", "commChest")],
		["Advance to Bonus", "", "astcmb", [[2,6], 300], actionCardSpriteClass("AdvanceToBonus", "commChest")],
		["Shopping Spree", "", "mdstpmp", [[0,55], 150], actionCardSpriteClass("ShoppingSpree", "commChest")],
		["April 15, Taxes Due!", "", "mdstgtj", [1,4] , actionCardSpriteClass("April15TaxesDue", "commChest")],
		["Discount Travel", "", "mdncbd", 0, actionCardSpriteClass("DiscountTravel", "commChest")],
		["Changing Lanes", "", "mdud", "down", actionCardSpriteClass("ChangingLanesB", "commChest")],
		["Changing Lanes", "", "mdud", "up", actionCardSpriteClass("ChangingLanesA", "commChest")],
		["A Moving Experience", "", "mdcr", 0, actionCardSpriteClass("AMovingExperience", "commChest")],
		["Go to Jail!", "", "gtj", 0, actionCardSpriteClass("GoToJail", "commChest")],
		["Get Out of Jail Free!", "", "keep", "gojf", actionCardSpriteClass("GetOutOfJailFree", "commChest")],
		["Just Say 'NO'!'", "", "keep", "jsn", actionCardSpriteClass("JustSayNo", "commChest")],
		["Sale of Stock Bonus", "", "keep", "ssp", actionCardSpriteClass("SaleOfStockBonus", "commChest")],
		["Special Online Pricing", "", "keep", "phr", actionCardSpriteClass("SpecialOnlinePricing", "commChest")],
		["Elected District Attorney", "", "keep", "apgtj", actionCardSpriteClass("ElectedDistrictAttorney", "commChest")],
		["Renovation Success", "", "keep", "cexr", actionCardSpriteClass("RenovationSuccess", "commChest")],
		["Deal Buster", "", "keep", "cppur", actionCardSpriteClass("DealBuster", "commChest")],
		["Hostile Takeover", "", "keep", "stealprop", actionCardSpriteClass("HostileTakeover", "commChest")],
		["Bargain Business!", "", "keep", "buyfrx", actionCardSpriteClass("BargainBusiness", "commChest")],
		["Reverse Rent!", "", "keep", "revren", actionCardSpriteClass("ReverseRent", "commChest")],
		["The Rent is Too Darn High!", "", "keep", "renisx", actionCardSpriteClass("TheRentIsTooDarnHigh", "commChest")],
		["Insider Trading", "", "keep", "discstk", actionCardSpriteClass("InsiderTrading", "commChest")],
		["Lawyer on Retainer", "", "keep", "antifine", actionCardSpriteClass("LawyerOnRetainer", "commChest")],
		["Share in their Good Fortune", "", "keep", "collr3", actionCardSpriteClass("ShareInTheirGoodFortune", "commChest")],
		["Insurance Premiums Due", "", "pmp", 50, actionCardSpriteClass("InsurancePremiumsDue", "commChest")],
		["Doctor's Fee", "", "pmp", 50, actionCardSpriteClass("DoctorsFee", "commChest")],
		["Pay Hospital Bills", "", "pmp", 100, actionCardSpriteClass("PayHospitalBills", "commChest")],
		["Tech Bubble Bursts", "", "pmp", 150, actionCardSpriteClass("TechBubbleBursts", "commChest")],
		["Vehicle Impounded!", "", "pmpmdstlt", [50, [1,20]], actionCardSpriteClass("VehicleImpounded", "commChest")],
		["You Inherit $100", "", "cmb", 100, actionCardSpriteClass("YouInherit100", "commChest")],
		["Receive Consultancy Fee", "", "cmb", 25, actionCardSpriteClass("ReceiveConsultancyFee", "commChest")],
		["Bank Error in Your Favor!", "", "cmb", 200, actionCardSpriteClass("BankErrorInYourFavor", "commChest")],
		["Income Tax Refund!", "", "cmb", 20, actionCardSpriteClass("IncomeTaxRefund", "commChest")],
		["You Won a Crossword Contest!", "", "cmb", 100, actionCardSpriteClass("YouWonACrosswordContest", "commChest")],
		["Life Insurance Matures", "", "cmb", 20, actionCardSpriteClass("LifeInsuranceMatures", "commChest")],
		["You Win 2nd Place in a Board Game Remix Design Contest!", "", "cmb", 10, actionCardSpriteClass("YouWin2ndPlaceInABoardGameRemixDesignContest", "commChest")],
		["Fluffy Takes First!", "", "cmb", 75, actionCardSpriteClass("FluffyTakesFirst", "commChest")],
		["IPO", "", "cmb", 500, actionCardSpriteClass("IPO", "commChest")],
		["Kickstart some Fun!", "", "cmb", 200, actionCardSpriteClass("KickstartSomeFun", "commChest")],
		["The Insider's Edge", "", "iftrkxcmbx", [250, 0, -50], actionCardSpriteClass("TheInsidersEdge", "commChest")],
		["Opening Night Tickets!", "", "cep", 50, actionCardSpriteClass("OpeningNightTickets", "commChest")],
		["Happy Birthday!", "", "cep", 10, actionCardSpriteClass("HappyBirthday", "commChest")],
		["Entrepreneur of the Year!", "", "cep", 50, actionCardSpriteClass("EntrepreneurOfTheYear", "commChest")],
		["You're getting Married", "", "cep", 25, actionCardSpriteClass("YoureGettingMarried", "commChest")],
		["Always Tip your Driver", "", "pepwithx", ["cabco", 50], actionCardSpriteClass("AlwaysTipYourDriver", "commChest")],
		["Game Night!", "", "rcfl", 200, actionCardSpriteClass("GameNight", "commChest")],
		["Be Kind, Rewind", "", "ramb", 0, actionCardSpriteClass("BeKindRewind", "commChest")],
		["Inherit Stock", "", "freestk", 0, actionCardSpriteClass("InheritStock", "commChest")],
		["Utility Regulation", "", "findiv", ["national utilities"], actionCardSpriteClass("UtilityRegulation", "commChest")],
		["Scandal in Hollywood!", "", "findiv", ["motion pictures", "general radio"], actionCardSpriteClass("ScandalInHollywood", "commChest")],
		["Unions on Strike", "", "findiv", ["united railways", "acme motors", "allied steamships"], actionCardSpriteClass("UnionsOnStrike", "commChest")],
		["Business Trip", "", "travvou", 2, actionCardSpriteClass("BusinessTrip2", "commChest")],
		["Business Trip", "", "travvou", 1, actionCardSpriteClass("BusinessTrip", "commChest")],
		["Finders Keepers", "", "stealtrav", 0, actionCardSpriteClass("FindersKeepers", "commChest")],
		["Losers Weepers", "", "losetrav", 0, actionCardSpriteClass("LosersWeepers", "commChest")],
		["HOUSE CONDEMNED", "", "sellhous", 0, actionCardSpriteClass("HouseCondemned", "commChest")],
		["Tornado Hits!", "", "remhou", 0, actionCardSpriteClass("TornadoHits", "commChest")],
		["Assessed for Street Repairs", "", "ppimp", 0, actionCardSpriteClass("AssessedForStreetRepairs", "commChest")]]
		
		self.travelVoucherDeck = [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
		self.travelVoucherCards = [["Transit Token", actionCardSpriteClass("TransitToken", "travelVoucher"), "tt"],
		["Bus Ticket", actionCardSpriteClass("BusTicketRegular", "travelVoucher"), "bt"],
		["Bus Ticket", actionCardSpriteClass("BusTicketExpireAll", "travelVoucher"), "btx"],
		["Free Cab Fare", actionCardSpriteClass("CabFareBackOne", "travelVoucher"), "fcfb", 1],
		["Free Cab Fare", actionCardSpriteClass("CabFareBackTwo", "travelVoucher"), "fcfb", 2],
		["Free Cab Fare", actionCardSpriteClass("CabFareBackThree", "travelVoucher"), "fcfb", 3],
		["Free Cab Fare", actionCardSpriteClass("CabFareAheadOne", "travelVoucher"), "fcfa", 1],
		["Free Cab Fare", actionCardSpriteClass("CabFareAheadTwo", "travelVoucher"), "fcfa", 2],
		["Free Cab Fare", actionCardSpriteClass("CabFareAheadThree", "travelVoucher"), "fcfa", 3]]
		
		self.rollThreeDeck = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
		self.rollThreeCards = [(1,2,3),(1,2,4),(1,2,5),(1,2,6),(1,3,4),(1,3,5),(1,3,6),(1,4,5),(1,4,6),(1,5,6),(2,3,4),(2,3,5),(2,3,6),(2,4,5),(2,4,6),(2,5,6),(3,4,5),(3,4,6),(3,5,6),(4,5,6)]
		self.rollThreeImages = []
		for i in self.rollThreeCards:
			self.rollThreeImages.append(rollThreeCardSpriteClass(i))
		
		random.shuffle(self.chanceDeck)
		random.shuffle(self.chestDeck)
		random.shuffle(self.travelVoucherDeck)
		random.shuffle(self.rollThreeDeck)
		
	def imageFromNumber(self, number):
		pass
	
def tradeInterface(token, outstandingDebt = False):
	inputLoop = True
	window.fill((55,171,200))
	tradeButtonList = []
	
def assignProp(token, propnum):
	Gameboard.propList[propnum][2] = token.Playernumber
	token.OwnedProps.append(propnum)
	token.OwnedProps.sort()
	token.checkForCG()
	Gameboard.countUnownedProps()

def payCorner(cornerName, token):
	if cornerName == "Go":
		gameLoopGUI.stringStack.append("You have received 200 dollars for passing Go")
		token.PlayerMoney = token.PlayerMoney + 200
	if cornerName == "Bonus":
		if token.BoardPosition == [2,6]:
			gameLoopGUI.stringStack.append("You have received 300 dollars for landing on Bonus")
			token.PlayerMoney = token.PlayerMoney + 300
		else:
			gameLoopGUI.stringStack.append("You have received 250 dollars for passing Bonus")
			token.PlayerMoney = token.PlayerMoney + 250
	if cornerName == "Payday":
		if Dice.Sum() % 2 == 0:
			gameLoopGUI.stringStack.append("You have received 400 dollars for passing Payday")
			token.PlayerMoney = token.PlayerMoney + 400
		else:
			gameLoopGUI.stringStack.append("You have received 300 dollars for passing Payday")
			token.PlayerMoney = token.PlayerMoney + 300

def purchaseFromBank(token, coords, priceMultiplier = 1):
	token.PlayerMoney = token.PlayerMoney - int(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][3] * priceMultiplier)
	assignProp(token, Gameboard.propNum[coords[0]][coords[1]])
	gameLoopGUI.stringStack.append("You have purchased " + Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][0] + " for $" + str(int(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][3] * priceMultiplier)) + ".")

def auctioneer(propNumber):
	pass
	
def numberOwned(creditor, propType):
	count = 0
	for i in range(len(creditor.OwnedProps)):
		if Gameboard.propList[creditor.OwnedProps[i]][1] == propType:
			count = count + 1
	return count

def declareBankruptcy(token, creditor):
	print("bankruptcy declared")
	if creditor == "bank":
		for i in range(len(token.OwnedProps)):
			Gameboard.propList[token.OwnedProps[i]][2] = "bank"
			Gameboard.propList[token.OwnedProps[i]][4] = "unmortgaged"
			if Gameboard.propList[token.OwnedProps[i]][1] == "CG":
				Gameboard.propList[token.OwnedProps[i]][6] = 0
				Gameboard.propList[token.OwnedProps[i]][7] = 0
		gameLoopGUI.stringStack.append(token.PlayerName + "has declared bankruptcy to the Bank")
		token.PlayerMoney = 0
		token.OwnedProps = []
		token.ownedColorGroups = {}
		token.isBankrupt = True
		token.turnActive = False
	else:
		gameLoopGUI.stringStack.append(token.PlayerName + " has declared bankruptcy to " + listPlayers[creditor].PlayerName)
		listPlayers[creditor].PlayerMoney = listPlayers[creditor].PlayerMoney + token.PlayerMoney
		token.PlayerMoney = 0
		for i in range(len(token.OwnedProps)):
			assignProp(listPlayers[creditor], token.OwnedProps[i])
			#Gameboard.propList[token.OwnedProps[i]][2] = listPlayers[creditor].Playernumber
		#print(listPlayers[creditor].OwnedProps)
		#print(token.OwnedProps)
		#listPlayers[creditor].OwnedProps.extend(token.OwnedProps)
		#print(listPlayers[creditor].OwnedProps)
		#listPlayers[creditor].OwnedProps.sort()
		target = token.Playernumber
		token.isBankrupt = True
		token.turnActive = False
	globalVars.recentBankruptcyFlag = True

def checkForWinner():
	activePlayers = 0
	winner = 0
	for i in range(len(listPlayers)):
		if listPlayers[i].isBankrupt == False:
			activePlayers = activePlayers + 1
		#print(activePlayers)
	if activePlayers > 1:
		#print("returnFalse")
		return "no winner"
	else:
		for i in range(len(listPlayers)):
			if listPlayers[i].isBankrupt == False:
				winner = i
		#print("return", winner)
		return winner

def payRentTo(token, rent, landlord, isRent = True):
	paymentComplete = False
	while paymentComplete == False:
		if token.PlayerMoney > rent:
			token.PlayerMoney = token.PlayerMoney - rent
			listPlayers[landlord].PlayerMoney = listPlayers[landlord].PlayerMoney + rent
			if token.Playernumber == globalVars.currentPlayer:
				gameLoopGUI.stringStack.append("You paid $" + str(rent) + " to " + listPlayers[landlord].PlayerName + ".")
			else:
				gameLoopGUI.stringStack.append(token.PlayerName + " paid $" + str(rent) + " to " + listPlayers[landlord].PlayerName + ".")
			paymentComplete = True
		else:
			while paymentComplete == False:
				print("Not enough for rent")
				if isRent == True:
					gameLoopGUI.stringStack.append(token.PlayerName + " you do not have enough money for rent. $" + str(rent))
				else:
					gameLoopGUI.stringStack.append(token.PlayerName + " you do not have enough money for your fee to " + listPlayers[landlord].PlayerName + " of $" + str(rent))
				gameLoopGUI.buttonInactive(gameLoopGUI.primaryActionButton)
				gameLoopGUI.buttonInactive(gameLoopGUI.secondaryActionButton)
				gameLoopGUI.tertiaryActionButton.text = "Declare bankruptcy"
				gameLoopGUI.buttonActive(gameLoopGUI.tertiaryActionButton)
				gameLoopGUI.drawGUI(token)
				response = gameLoopGUI.getUserInput()
				if response == gameLoopGUI.tertiaryActionButton.text:
					declareBankruptcy(token, landlord)
					gameLoopGUI.buttonInactive(gameLoopGUI.tertiaryActionButton)
					paymentComplete = True
				elif response == gameLoopGUI.tradeButton:
					tradeInterface(token)
				elif response == gameLoopGUI.unimproveButton:
					sellImprovements(token)
				elif response == gameLoopGUI.mortgageButton:
					mortgageProperties(token)

def payFineToPool(token, fine):
	paymentComplete = False
	while paymentComplete == False:
		if token.PlayerMoney > fine:
			token.PlayerMoney = token.PlayerMoney - fine
			Gameboard.poolMoney = Gameboard.poolMoney + fine
			gameLoopGUI.stringStack.append("You paid $" + str(fine) + " to the Pool")
			paymentComplete = True
		else:
			inputLoop = True
			print("You do not have enough money for your fine")
			while inputLoop == True:
		#		print("Attempt a (t)rade")
		#		print("(M)ortgage propery")
		#		print("(S)ell improvements")
				print("Declare (b)ankruptcy")
				response = input("What would you like to do?")
		#		if response == "t":
		#			makeTrade(token)
		#		if response == "m":
		#			mortgageProps(token)
				if response == "b":
					declareBankruptcy(token, "bank")
					inputLoop = False
					paymentComplete = True

def moneyFromBank(token, payment):
	token.PlayerMoney = token.PlayerMoney + payment

def landOnProperty(token, coords, rentMultiplier = 1):
	if Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2] == "bank":
		inputLoop = True
		gameLoopGUI.stringStack.append("The bank owns " + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][0]) + ".")
		gameLoopGUI.stringStack.append("The price for this property is $" + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][3]) + ".")
		if token.PlayerMoney > int(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][3] * rentMultiplier):
			gameLoopGUI.primaryActionButton.text = "Purchase ($" + str(int(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][3] * rentMultiplier)) + ")"
		else:
			gameLoopGUI.buttonInactive(gameLoopGUI.primaryActionButton)
		gameLoopGUI.secondaryActionButton.text = "Auction it"
		gameLoopGUI.buttonActive(gameLoopGUI.secondaryActionButton)
		gameLoopGUI.drawGUI(token)
		commandText = gameLoopGUI.getUserInput()
		if token.PlayerMoney > Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][3] and commandText == gameLoopGUI.primaryActionButton.text:
			purchaseFromBank(token, coords, rentMultiplier)
		if commandText == gameLoopGUI.secondaryActionButton.text:
			auctioneer(Gameboard.propNum[coords[0]][coords[1]])
		gameLoopGUI.allButtonsInactive()
	elif Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2] == token.Playernumber:
		gameLoopGUI.stringStack.append("You already own " + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][0]) + ".")
	elif Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][4] == "mortgaged":
		gameLoopGUI.stringStack.append(listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]].PlayerName + " has mortgaged " + Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][0] + " no rent is due.")
	else:
		if Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][1] == "CG":
			gameLoopGUI.stringStack.append("Player " + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2] + 1) + ", " + listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]].PlayerName + " owns " + Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][0] + ".")
			if listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]].ownedColorGroups[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][5]][0] == 0:
				gameLoopGUI.stringStack.append("They do not have majority ownership, the rent is $" + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][8][0]) + ".")
				#if rentMultiplier != 1:
				#	print(token.PlayerName, "paid", rentMultiplier, "times the normal rent")
				payRentTo(token, int(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][8][0] * rentMultiplier), Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2])
			elif Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][7] > 0:
				gameLoopGUI.stringStack.append("They own " + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][7]) + " improvement(s) on this property, the rent is $" + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][8][Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][7]]) + ".")
				#if rentMultiplier != 1:
				#	print(token.PlayerName, "paid", rentMultiplier, "times the normal rent")
				payRentTo(token, int(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][8][Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][7]] * rentMultiplier), Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2])
			else:
				gameLoopGUI.stringStack.append("They own a majority, the rent is doubled from $" + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][8][0]) + ".")
				#if rentMultiplier != 1:
				#	print(token.PlayerName, "paid", rentMultiplier, "times the normal rent")
				payRentTo(token, int((Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][8][0] * 2) * rentMultiplier), Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2])
		if Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][1] == "CabCo":
			count = numberOwned(listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]], "CabCo")
			gameLoopGUI.stringStack.append("Player " + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2] + 1) + ", " + listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]].PlayerName + " owns " + Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][0] + ".")
			gameLoopGUI.stringStack.append("They own " + str(count) + " Cab Companies, the rent is $" + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][5][count - 1]) + ".")
			#if rentMultiplier != 1:
			#	print(token.PlayerName, "paid", rentMultiplier, "times the normal rent")
			payRentTo(token, int(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][5][count - 1] * rentMultiplier), Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2])
		if Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][1] == "Railroad":
			count = numberOwned(listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]], "Railroad")
			gameLoopGUI.stringStack.append("Player " + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2] + 1) + ", " + listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]].PlayerName + " owns " + Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][0] + ".")
			gameLoopGUI.stringStack.append("They own " + str(count) + " Railroads, the rent is $" + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][5][count - 1]) + ".")
			#if rentMultiplier != 1:
			#	print(token.PlayerName, "paid", rentMultiplier, "times the normal rent")
			payRentTo(token, int(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][5][count - 1] * rentMultiplier), Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2])
		if Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][1] == "Utility":
			count = numberOwned(listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]], "Utility")
			Dice.Roll()
			gameLoopGUI.stringStack.append("Player " + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2] + 1) + ", " + listPlayers[Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2]].PlayerName + " owns " + Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][0] + ". ")
			gameLoopGUI.stringStack.append("They own " + str(count) + " utilities, the rent is " + str(Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][5][count - 1] ) + " times " + str(Dice.Sum()) + ", which is $" + str(Dice.Sum() * Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][5][count - 1]) + ".")
			#if rentMultiplier != 1:
			#	print(token.PlayerName, "paid", rentMultiplier, "times the normal rent")
			payRentTo(token, int(Dice.Sum() * Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][5][count - 1] * rentMultiplier), Gameboard.propList[Gameboard.propNum[coords[0]][coords[1]]][2])

def improvementLevelString(impLev):
	if impLev == 0:
		return "unimproved"
	elif impLev == 1:
		return "one house"
	elif impLev == 2:
		return "two houses"
	elif impLev == 3:
		return "three houses"
	elif impLev == 4:
		return "four houses"
	elif impLev == 5:
		return "hotel"
	elif impLev == 6:
		return "skyscraper"

def goToJail(token):
	token.IsInJail = True
	token.turnActive = False
	token.setBoardPosition([1,20])
	token.turnsInJail = 0
	gameLoopGUI.stringStack.append("You have been placed in Jail")

def payFineToEveryPlayer(token, fine):
	for i in listPlayers:
		if i != token and i.isBankrupt == False:
			payRentTo(token, fine, i.Playernumber, False)

def collectMoneyFromEveryPlayer(token, fine):
	for i in listPlayers:
		if i != token:
			payRentTo(i, fine, token.Playernumber, False)
	
def stockExchangePass():
	pass

def moveDirectly(token, coords, priceModifier = 1):
	gameLoopGUI.stringStack.append("You have moved directly to " + Gameboard.ref(coords) + ".")
	token.setBoardPosition(coords)
	landOnSpace(token, coords, priceModifier)

def advanceMove(token, coords, priceModifier = 1):
	gameLoopGUI.stringStack.append("You advanced to " + Gameboard.ref(coords) + ".")
	if token.BoardPosition[0] == coords[0]:
		if token.BoardPosition[0] == 0:
			if token.BoardPosition[1] < coords[1] and token.BoardPosition[1] < 28 and coords[1] > 27:
				payCorner("Payday", token)
			if token.BoardPosition[1] > coords[1] and token.BoardPosition[1] > 27 and coords[1] > 27:
				payCorner("Payday", token)
			if token.BoardPosition[1] > coords[1] and token.BoardPosition[1] < 28 and coords[1] < 28:
				payCorner("Payday", token)
				
		if token.BoardPosition[0] == 1:
			if token.BoardPosition[1] > coords[1]:
				payCorner("Go", token)
				
		if token.BoardPosition[0] == 2:
			if token.BoardPosition[1] < coords[1] and token.BoardPosition[1] < 6 and coords[1] > 5:
				payCorner("Bonus", token)
			if token.BoardPosition[1] > coords[1] and token.BoardPosition[1] > 5 and coords[1] > 5:
				payCorner("Bonus", token)
			if token.BoardPosition[1] > coords[1] and token.BoardPosition[1] < 6 and coords[1] < 6:
				payCorner("Bonus", token)
				
			if token.BoardPosition[1] < coords[1] and token.BoardPosition[1] < 12 and coords[1] > 11:
				stockExchangePass()
			if token.BoardPosition[1] > coords[1] and token.BoardPosition[1] > 11 and coords[1] > 11:
				stockExchangePass()
			if token.BoardPosition[1] > coords[1] and token.BoardPosition[1] < 12 and coords[1] < 12:
				stockExchangePass()
				
	else:
		if token.BoardPosition[0] > coords[0]:
			while token.BoardPosition[0] > coords[0]:
				if token.BoardPosition[0] == 2:
					if token.BoardPosition[1] > 21 or token.BoardPosition[1] < 10:
						if token.BoardPosition[1] < 6 or token.BoardPosition[1] > 7:
							payCorner("Bonus", token)
						token.BoardPosition = [1,15]
					else:
						if token.BoardPosition[1] < 12 and token.BoardPosition[1] > 9:
							stockExchangePass()
						token.BoardPosition = [1,35]
				elif token.BoardPosition[0] == 1:
					if token.BoardPosition[1] > 25 or token.BoardPosition[1] < 6:
						if token.BoardPosition[1] < 40:
							payCorner("Go", token)
						token.BoardPosition = [0,7]
					else:
						token.BoardPosition = [0,35]
			if token.BoardPosition[0] == 1:
				if token.BoardPosition[1] == 15 and coords[1] < 15:
					payCorner("Go", token)
				if token.BoardPosition[1] == 35 and coords[1] < 35:
					payCorner("Go", token)
			elif token.BoardPosition[0] == 0:
				if token.BoardPosition[1] == 7:
					if coords[1] > 27 or coords[1] < 7:
						payCorner("Payday", token)
				if token.BoardPosition[1] == 35:
					if coords[1] >27 and coords[1] < 35:
						payCorner("Payday", token)
						
		elif token.BoardPosition[0] < coords[0]:
			while token.BoardPosition[0] < coords[0]:
				if token.BoardPosition[0] == 0:
					if token.BoardPosition[1] > 35 or token.BoardPosition[1] < 8:
						token.BoardPosition = [1,5]
					else:
						if token.BoardPosition[1] < 28:
							payCorner("Payday", token)
						token.BoardPosition = [1,25]
				elif token.BoardPosition[0] == 1:
					if token.BoardPosition[1] > 34 or token.BoardPosition[1] < 16:
						if token.BoardPosition[1] > 34:
							payCorner("Go", token)
						token.BoardPosition = [2,9]
					else:
						token.BoardPosition = [2,21]
			if token.BoardPosition[0] == 1:
				if token.BoardPosition[1] == 5 and coords[1] < 5:
					payCorner("Go", token)
				if token.BoardPosition[1] == 25 and coords[1] < 25:
					payCorner("Go", token)
			elif token.BoardPosition[0] == 2:
				if token.BoardPosition[1] == 9:
					if coords[1] > 5 and coords[1] < 9:
						payCorner("Bonus", token)
				if token.BoardPosition[1] == 21:
					if coords[1] > 5 and coords[1] < 21:
						payCorner("Bonus", token)
	token.setBoardPosition(coords)
	landOnSpace(token, coords)

def readActionCard(pulledCard, token, coords):
	#print(pulledCard[0])
	#print(pulledCard[1])
	readActionCardGUI.__init__()
	cardType = pulledCard[2]
	if cardType == "atcsp":
		cabcos = []
		for i in Gameboard.propList:
			if i[2] == "CabCo":
				cabcos.append(i)
		cabcoStealable == False
		cabcoBuyable == False
		for i in cabcos:
			if Gameboard.propList[i][2] not in ["bank", token.playerNum]:
				cabcoStealable = True
			elif Gameboard.propList[i][2] == "bank":
				cabcoBuyable = True
		if cabcoStealable == False and cabcoBuyable == False:
			gameLoopGUI.stringStack.append("You already own all of the Cab Companies.")
			readActionCardGUI.stringsToPrint.append(GUIstring("You already own of of the Cab Companies.", (420, 60)))
		elif cabcoBuyable == True and cabcoStealable == False:
			readActionCardGUI.buttonInactive(readActionCardGUI.dialogButtonA)
			readActionCardGUI.stringsToPrint.append(GUIstring("There are no owned Cab Companies. Choose one to purchase:", (420, 60)))
			for i in cabcos:
				if Gameboard.propList[i][2] == "bank":
					readActionCardGUI.activeButtons.append(spriteButton(440, posW, Gameboard.propList[i][7][0].deedImageS, i))
					posW = posW + 100
		else:
			readActionCardGUI.buttonInactive(readActionCardGUI.dialogButtonA)
			readActionCardGUI.stringsToPrint.append(GUIstring("You may steal one of the following Cab Companies:", (420, 60)))
			for i in cabcos:
				if Gameboard.propList[i][2] not in ["bank", token.playerNum]:
					readActionCardGUI.activeButtons.append(spriteButton(440, posW, Gameboard.propList[i][7][0].deedImageS, i))
					posW = posW + 100
	elif cardType == "mdstgtj":
		readActionCardGUI.dialogButtonA.text = "Pay Taxes"
		readActionCardGUI.dialogButtonB.text = "Go To Jail"
		readActionCardGUI.buttonActive(readActionCardGUI.dialogButtonB)
	elif cardType == "mdncbd":
		if token.BoardPosition == [0,2]:
			cabCoNearest = [[0,6],[0,22],[0,34],[0,50]]
			railroadNearest = [[0,7],[1,15],[0,35],[1,35]]
		elif token.BoardPosition == [0,24]:
			cabCoNearest = [[0,34],[0,50],[0,6],[0,22]]
			railroadNearest = [[0,35],[1,35],[0,7],[1,15]]
		elif token.BoardPosition == [0,36] or token.BoardPosition == [0,46]:
			cabCoNearest = [[0,50],[0,6],[0,22],[0,34]]
			railroadNearest = [[0,7],[1,15],[0,35],[1,35]]
		elif token.BoardPosition == [1,2]:
			cabCoNearest = [[0,22],[0,34],[0,50],[0,6]]
			railroadNearest = [[1,5],[1,15],[1,25],[1,35]]
		elif token.BoardPosition == [1,22]:
			cabCoNearest = [[0,50],[0,6],[0,22],[0,34]]
			railroadNearest = [[1,15],[1,25],[1,35],[1,5]]
		elif token.BoardPosition == [1,33]:
			cabCoNearest = [[0,22],[0,34],[0,50],[0,6]]
			railroadNearest = [[1,25],[1,35],[1,5],[1,15]]
		elif token.BoardPosition == [2,4]:
			cabCoNearest = [[0,50],[0,6],[0,22],[0,34]]
			railroadNearest = [[2,9],[1,25],[2,21],[1,5]]
		for i in cabCoNearest:
			if Gameboard.propList[Gameboard.propNum[i[0]][i[1]]][3] != "bank":
				cabCoNearest.pop(cabCoNearest.index(i))
		for i in railroadNearest:
			if Gameboard.propList[Gameboard.propNum[i[0]][i[1]]][3] != "bank":
				railroadNearest.pop(railroadNearest.index(i))
		if len(cabCoNearest) == 0 and len(railroadNearest) == 0:
			readActionCardGUI.stringsToPrint.append(GUIstring("There are no unowned railroads or cab companies to move to. Nothing happens.", (420, 60)))
		elif len(cabCoNearest) == 0:
			readActionCardGUI.stringsToPrint.append(GUIstring("There are no unowned cab companies. The nearest unowned railroad is " + Gameboard.listspace[railroadNearest[0][0]][railroadNearest[0][1]], (420, 60)))
		elif len(railroadNearest) == 0:
			readActionCardGUI.stringsToPrint.append(GUIstring("There are no unowned railroads. The nearest unowned cab company is " + Gameboard.listspace[cabCoNearest[0][0]][cabCoNearest[0][1]], (420,60)))
		else:
			readActionCardGUI.stringsToPrint.append(GUIstring("The nearest unowned cab company is " + Gameboard.listspace[cabCoNearest[0][0]][cabCoNearest[0][1]] + " and the nearest unowned railroad is " + Gameboard.listspace[cabCoNearest[0][0]][cabCoNearest[0][1]], (420,60)))
			readActionCardGUI.activeButtons.append(spriteButton(300, 600, Gameboard.propList[Gameboard.propNum[cabCoNearest[0][0]][cabCoNearest[0][1]]][7][0].deedImageS, cabCoNearest[0]))
			readActionCardGUI.activeButtons.append(spriteButton(300, 600, Gameboard.propList[Gameboard.propNum[railroadNearest[0][0]][railroadNearest[0][1]]][7][0].deedImageS, railroadNearest[0]))
			readActionCardGUI.buttonInactive(readActionCardGUI.dialogButtonA)
	inputLoop = True
	while inputLoop == True:
		readActionCardGUI.drawGUI(pulledCard)
		commandText = readActionCardGUI.getUserInput()
		if commandText != ".":
			inputLoop = False
	if cardType == "ast":
	#advance to single target
		advanceMove(token, pulledCard[3])
	elif cardType == "apc":
	#advance to pay corner
		if token.BoardPosition[0] == 0:
			token.setBoardPosition([0,28])
			payCorner("Payday", token)
		elif token.BoardPosition[0] == 1:
			token.setBoardPosition([1,0])
			payCorner("Go", token)
		elif token.BoardPosition[0] == 2:
			token.setBoardPosition([2,6])
			payCorner("Bonus", token)
	elif cardType == "atn":
	#advance to nearest
		if pulledCard[3] == "railroad":
			if token.BoardPosition == [0,10] or token.BoardPosition == [0,21] or token.BoardPosition == [0,30]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [0,35])
				else:
					advanceMove(token, [1,25])
			if token.BoardPosition == [0,54]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [0,7])
				else:
					advanceMove(token, [1,5])
			if token.BoardPosition == [1,7]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [1,15])
				else:
					advanceMove(token, [2,9])
			if token.BoardPosition == [1,22]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [1,25])
				else:
					advanceMove(token, [0,35])
			if token.BoardPosition == [1,36]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [1,5])
				else:
					advanceMove(token, [0,7])
			if token.BoardPosition == [2,16]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [2,21])
				else:
					advanceMove(token, [1,35])
		if pulledCard[3] == "utility":
			if token.BoardPosition == [0,10]:
				advanceMove(token, [0,11])
			if token.BoardPosition == [0,21] or token.BoardPosition == [0,30]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [0,39])
				else:
					advanceMove(token, [1,28])
			if token.BoardPosition == [0,54]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [0,11])
				else:
					advanceMove(token, [1,12])
			if token.BoardPosition == [1,7]:
				advanceMove(token, [1,12])
			if token.BoardPosition == [1,22]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [1,28])
				else:
					advanceMove(token, [0,39])
			if token.BoardPosition == [1,36]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [1,12])
				else:
					advanceMove(token, [0,11])
			if token.BoardPosition == [2,16]:
				if Dice.Sum() % 2 == 1:
					advanceMove(token, [2,3])
				else:
					advanceMove(token, [0,11])
	elif cardType == "atcsp":
	#advance to choice and steal or purchase
		#cabcoSteal(token)
		if commandText in cabcos:
			if Gameboard.propList[commandText][2] == "bank":
				advanceMove(token, Gameboard.deref(commandText))
			else:
				listPlayers[Gameboard.propList[i][2]].OwnedProps.pop(listPlayers[Gameboard.propList[i][2]].OwnedProps.index(i))
				assignProp(token, i)
	elif cardType == "astpep":
	#advance to single target and pay every player
		advanceMove(token, pulledCard[3][1])
		payFineToEveryPlayer(token, pulledCard[4])
	elif cardType == "astcmb":
	#advance to single target and collect
		advanceMove(token, [pulledCard[3][0][0], pulledCard[3][0][1]])
		print("You collected", pulledCard[4], "from the bank")
		token.PlayerMoney = token.PlayerMoney + pulledCard[3][1]
	elif cardType == "mdst":
	#move directly to single target
		moveDirectly(token, pulledCard[3])
	elif cardType == "mdstpmp":
	#move directly to single target and pay to pool
		moveDirectly(token, pulledCard[3][0])
		payFineToPool(token, pulledCard[3][1])
	elif cardType == "mdstgtj":
	#move directly to single target or go to jail
		if commandText == "Pay Taxes":
			advanceMove(token, pulledCard[3])
		else:
			goToJail(token)
	elif cardType == "amdst":
	#all players move directly to single target
		if Gameboard.propList[6][2] == "bank":
			auctioneer(6)
		for i in range(len(listPlayers)):
			moveDirectly(listPlayers[i], pulledCard[3])
	elif cardType == "mdnpdr":
	#move directly to nearest of type (cabco)
		if token.BoardPosition == [0,10] or token.BoardPosition == [0,21] or token.BoardPosition == [1,36] or token.BoardPosition == [2,16]:
			moveDirectly(token, [0,22])
		elif token.BoardPosition == [0,30]:
			moveDirectly(token, [0,34])
		elif token.BoardPosition == [0,54]:
			moveDirectly(token, [0,6])
		elif token.BoardPosition == [1,7] or token.BoardPosition == [1,22]:
			moveDirectly(token, [0,50])
		gameLoopGUI.stringStack.append("The nearest CabCo is" + Gameboard.propList[Gameboard.propNum[token.BoardPosition[0]][token.BoardPosition[1]]][0])
		if Gameboard.propList[Gameboard.propNum[token.BoardPosition[0]][token.BoardPosition[1]]][2] != "bank":
			gameLoopGUI.stringStack.append("It is owned by" + listPlayers[Gameboard.propList[Gameboard.propNum[token.BoardPosition[0]][token.BoardPosition[1]]][2]].PlayerName + "they are entitled to double rent, if applicable")
			landOnProperty(token, token.BoardPosition, 2)
		else:
			gameLoopGUI.stringStack.append("It is unowned. Nothing happens.")
	elif cardType == "mdncbd":
	#move directly to nearest of choice of type and purchase at discount
		if len(cabCoNearest) > 0 and len(railroadNearest) == 0:
			moveDirectly(token, cabCoNearest[0])
		elif len(cabCoNearest) == 0 and len(railroadNearest) > 0:
			moveDirectly(token, railroadNearest[0])
		elif len(cabCoNearest) > 0 and len(railroadNearest) > 0:
			moveDirectly(token, response)
	elif cardType == "mdud":
	#move directly up or down
		if pulledCard[3] == "up":
			if token.BoardPosition == [0,2] or token.BoardPosition == [0,54]:
				moveDirectly(token, [1,0])
			if token.BoardPosition == [0,10]:
				moveDirectly(token, [1,8])
			if token.BoardPosition == [0,21]:
				moveDirectly(token, [1,15])
			if token.BoardPosition == [0,24]:
				moveDirectly(token, [1,18])
			if token.BoardPosition == [0,30]:
				moveDirectly(token, [1,20])
			if token.BoardPosition == [0,36]:
				moveDirectly(token, [1,26])
			if token.BoardPosition == [0,46]:
				moveDirectly(token, [1,32])
			if token.BoardPosition == [1,2]:
				moveDirectly(token, [2,0])
			if token.BoardPosition == [1,7]:
				moveDirectly(token, [2,5])
			if token.BoardPosition == [1,17]:
				moveDirectly(token, [2,11])
			if token.BoardPosition == [1,22]:
				moveDirectly(token, [2,12])
			if token.BoardPosition == [1,33]:
				moveDirectly(token, [2,13])
			if token.BoardPosition == [1,36]:
				moveDirectly(token, [2,22])
			if token.BoardPosition == [2,4] or token.BoardPosition == [2,16]:
				gameLoopGUI.stringStack.append("No higher track to move to.")
		if pulledCard[3] == "down":
			if token.BoardPosition == [2,4]:
				moveDirectly(token, [1,6])
			if token.BoardPosition == [2,16]:
				moveDirectly(token, [1,16])
			if token.BoardPosition == [1,2]:
				moveDirectly(token, [0,4])
			if token.BoardPosition == [1,7]:
				moveDirectly(token, [0,9])
			if token.BoardPosition == [1,17]:
				moveDirectly(token, [0,23])
			if token.BoardPosition == [1,22]:
				moveDirectly(token, [0,32])
			if token.BoardPosition == [1,33]:
				moveDirectly(token, [0,47])
			if token.BoardPosition == [1,36]:
				moveDirectly(token, [0,50])
			if token.BoardPosition[0] == 0:
				gameLoopGUI.stringStack.append("No lower track to move to.")
	elif cardType == "mdc":
	#move directly to any space the player to your left chooses
		pass
		#TODO
	elif cardType == "mdcr":
	#move directly to transportation property of your choice
		pass
		#TODO
	elif cardType == "gtj":
	#go to jail
		goToJail(token)
	elif cardType == "gtjnr":
	#go to jail and do not collect rent
		goToJail(token)
		#TODO: add no rent functionality
	elif cardType == "keep":
	#keep this card
		pass
	elif cardType == "pmp":
	#pay money to the pool
		payFineToPool(token, pulledCard[3])
	elif cardType == "pmpmdstlt":
	#pay money to the pool and move directly to a single target and lose 1 turn
		payFineToPool(token, pulledCard[3][0])
		moveDirectly(token, pulledCard[3][1])
		#TODO: lose turn funtionality
	elif cardType == "cmb":
	#collect money from the bank
		gameLoopGUI.stringStack.append("You collected $" + str(pulledCard[3]) + " from the bank")
		token.PlayerMoney = token.PlayerMoney + pulledCard[3]
	elif cardType == "iftrkxcmbx":
	#if on track x collect money from bank x
		pass
		if token.BoardPosition[0] == 0:
			moneyFromBank(token, pulledCard[3][0])
		elif token.BoardPosition[0] == 1:
			moneyFromBank(token, pulledCard[3][1])
		elif token.BoardPosition[0] == 2:
			payFineToPool(token, pulledCard[3][2])
	elif cardType == "cep":
	#collect from every player
		collectMoneyFromEveryPlayer(token, pulledCard[3])
	elif cardType == "ccpc":
		pass
	elif cardType == "pep":
	#pay every player
		payFineToEveryPlayer(token, pulledCard[3])
	elif cardType == "ifrailpep":
		pass
	elif cardType == "pepwithx":
		pass
	elif cardType == "rcfl":
		pass
	elif cardType == "mxs":
		pass
	elif cardType == "ramb":
		pass
	elif cardType == "retstk":
		pass
	elif cardType == "freestk":
		pass
	elif cardType == "reddiv":
		pass
	elif cardType == "coldiv":
		pass
	elif cardType == "fjifs":
		pass
	elif cardType == "travvou":
		pass
	elif cardType == "stealtrav":
		pass
	elif cardType == "losetrav":
		pass
	elif cardType == "remhou":
		pass
	elif cardType == "ppimp":
		pass
	elif cardType == "ppp":
		pass
	elif cardType == "surprop":
		pass
	return pulledCard[0]
		
def pullChanceCard(token, coords):
	pulledCard = actionCards.chanceCards[actionCards.chanceDeck[0]]
	#print(pulledCard[0])
	gameLoopGUI.stringStack.append("You landed on Chance and pulled the '" + pulledCard[0] + "' card.")
	readActionCard(pulledCard, token, coords)
	if pulledCard[2] != "keep":
		actionCards.chanceDeck.append(actionCards.chanceDeck[0])
	else:
		token.heldChanceCards.append(actionCards.chanceDeck[0])
		#print(token.heldChanceCards)
	actionCards.chanceDeck.pop(0)
	
def pullCommChestCard(token, coords):
	pulledCard = actionCards.chestCards[actionCards.chestDeck[0]]
	#print(pulledCard[0])
	gameLoopGUI.stringStack.append("You landed on Community Chest and pulled the '" + pulledCard[0] + "' card.")
	readActionCard(pulledCard, token, coords)
	if pulledCard[2] != "keep":
		actionCards.chestDeck.append(actionCards.chestDeck[0])
	else:
		token.heldChestCards.append(actionCards.chestDeck[0])
		#print(token.heldChestCards)
	actionCards.chestDeck.pop(0)
	return(pulledCard[0])

def landOnRollThree(token):
	pulledCard = actionCards.rollThreeDeck[0]
	pulledNumbers = actionCards.rollThreeCards[pulledCard]
	stringPos = 460	
	totalPayout = 0
	rollThreeGUI.stringsToPrint.append(GUIstring("You have collected the " + str(pulledNumbers[0]) + ", " + str(pulledNumbers[1]) + ", " + str(pulledNumbers[2]) + " roll three card.", (600, 420)))
	rollThreeDice = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
	rollThreeDice.sort()
	rollThreeGUI.stringsToPrint.append(GUIstring("The Roll Three dice are: " + str(rollThreeDice[0]) + ", " + str(rollThreeDice[1]) + ", and " + str(rollThreeDice[2]) + ".", (600, 440)))
	for i in token.heldRollThreeCards:
		cardNumbers = actionCards.rollThreeCards[i]
		if rollThreeDice[0] in cardNumbers and rollThreeDice[1] in cardNumbers and rollThreeDice[2] in cardNumbers:
			rollThreeGUI.stringsToPrint.append(GUIstring("Your " + str(cardNumbers[0]) + ", " + str(cardNumbers[1]) + ", " + str(cardNumbers[2]) + "card matched all three numbers. $1500 payout", (600, stringPos)))
			moneyFromBank(token, 1500)
			totalPayout = totalPayout + 1500
			stringPos = stringPos + 20
		elif (rollThreeDice[0] in cardNumbers and rollThreeDice[1] in cardNumbers) or (rollThreeDice[0] in cardNumbers and rollThreeDice[2] in cardNumbers) or (rollThreeDice[1] in cardNumbers and rollThreeDice[2] in cardNumbers):
			rollThreeGUI.stringsToPrint.append(GUIstring("Your " + str(cardNumbers[0]) + ", " + str(cardNumbers[1]) + ", " + str(cardNumbers[2]) + "card matched two numbers. $200 payout", (600, 420)))
			moneyFromBank(token, 200)
			totalPayout = totalPayout + 200
			stringPos = stringPos + 20
		elif rollThreeDice[0] in cardNumbers or rollThreeDice[1] in cardNumbers or rollThreeDice[2] in cardNumbers:
			rollThreeGUI.stringsToPrint.append(GUIstring("Your " + str(cardNumbers[0]) + ", " + str(cardNumbers[1]) + ", " + str(cardNumbers[2]) + "card matched one number. $50 payout", (600, stringPos)))
			moneyFromBank(token, 50)
			totalPayout = totalPayout + 50
			stringPos = stringPos + 20
	for i in listPlayers:
		if i == token:
			pass
		else:
			for j in token.heldRollThreeCards:
				cardNumbers = actionCards.rollThreeCards[j]
				if rollThreeDice[0] in cardNumbers and rollThreeDice[1] in cardNumbers and rollThreeDice[2] in cardNumbers:
					rollThreeGUI.stringsToPrint.append(GUIstring(i.PlayerName + "'s " + str(cardNumbers[0]) + ", " + str(cardNumbers[1]) + ", " + str(cardNumbers[2]) + "card matched all three numbers. $1000 payout", (600, stringPos)))
					moneyFromBank(i, 1000)
					totalPayout = totalPayout + 1000
					stringPos = stringPos + 20
				elif (rollThreeDice[0] in cardNumbers and rollThreeDice[1] in cardNumbers) or (rollThreeDice[0] in cardNumbers and rollThreeDice[2] in cardNumbers) or (rollThreeDice[1] in cardNumbers and rollThreeDice[2] in cardNumbers):
					rollThreeGUI.stringsToPrint.append(GUIstring(i.PlayerName + "'s " + str(cardNumbers[0]) + ", " + str(cardNumbers[1]) + ", " + str(cardNumbers[2]) + "card matched two numbers. $200 payout", (600, stringPos)))
					moneyFromBank(i, 200)
					totalPayout = totalPayout + 200
					stringPos = stringPos + 20
				elif rollThreeDice[0] in cardNumbers or rollThreeDice[1] in cardNumbers or rollThreeDice[2] in cardNumbers:
					rollThreeGUI.stringsToPrint.append(GUIstring(i.PlayerName + "'s " + str(cardNumbers[0]) + ", " + str(cardNumbers[1]) + ", " + str(cardNumbers[2]) + "card matched one number. $50 payout", (600, stringPos)))
					moneyFromBank(i, 50)
					totalPayout = totalPayout + 50
					stringPos = stringPos + 20
	rollThreeGUI.drawGUI(token, pulledCard)
	rollThreeGUI.getUserInput()
	gameLoopGUI.stringStack.append("A total of $" + str(totalPayout) + "was awarded for Roll Three winnings.")
	 	
def collectTravelVoucher(token):
	if len(actionCards.travelVoucherDeck) > 0:
		token.heldTravelVouchers.append(actionCards.travelVoucherDeck[0])
		gameLoopGUI.stringStack.append("You collected a '" + actionCards.travelVoucherCards[actionCards.travelVoucherDeck[0]][0] + "' card.")
		actionCards.travelVoucherDeck.pop(0)

def landOnSpace(token, coords, priceModifier = 1):
	if Gameboard.spaceType[coords[0]][coords[1]] == "Property":
		landOnProperty(token, coords, priceModifier)
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Chance":
		pullChanceCard(token, coords)
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Community Chest":
		pullCommChestCard(token, coords)
	#elif Gameboard.spaceType[coords[0]][coords[1]] == "Auction":
	#	Gameboard.countUnownedProps()
	#	print(Gameboard.unownedProps)
	#	for i in range(len(Gameboard.unownedProps)):
	#		print(i+1, Gameboard.propList[Gameboard.unownedProps[i]][0])
	#	if len(Gameboard.unownedProps) > 0:
	#		inputLoop = True
	#		while inputLoop == True:
	#			print("You may put one unowned property up for auction.")
	#			response = input("Enter the number corresponding to the property you would like to put up for auction:")
	#			if response.isnumeric():
	#				response = int(response) - 1
	#				inputLoop = False
	#			else:
	#				print("Invalid Response")
	#		auctioneer(Gameboard.unownedProps[response])
	#	else:
	#		payRentDict = {}
	#		rentList = []
	#		for i in range(len(Gameboard.propList)):
	#			if Gameboard.propList[i][1] == "CG" and Gameboard.propList[i][2] != "bank" and Gameboard.propList[i][2] != token.Playernumber:
	#				payRentDict[Gameboard.propList[i][8][Gameboard.propList[i][6]]] = i
	#		print(payRentDict)
	#		rentList = list(payRentDict)
	#		print(rentList)
	#		rentList.sort(reverse = True)
	#		print(rentList)
	#		if len(rentList) > 0:
	#			gotoS = Gameboard.deref(payRentDict[rentList[0]])
	#			moveDirectly(token, gotoS)
	if Gameboard.spaceType[coords[0]][coords[1]] == "Bus Ticket":
		gameLoopGUI.stringStack.append("You have landed on Bus Ticket")
		collectTravelVoucher(token)
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Free Parking":
		gameLoopGUI.stringStack.append("You landed on Free Parking and nothing happened")
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Holland Tunnel":
		if token.BoardPosition == [0,14]:
			token.setBoardPosition([2,18])
			gameLoopGUI.stringStack.append("You took the Holland Tunnel from the Outer track to the Inner track")
		elif token.BoardPosition == [2,18]:
			token.setBoardPosition([0,14])
			gameLoopGUI.stringStack.append("You took the Holland Tunnel from the Inner track to the Outer track")
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Paycorner":
		pass
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Subway":
		pass
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Birthday Gift":
		gameLoopGUI.stringStack.append("You have landed on Birthday Gift. Collect $100 or a travel voucher.")
		gameLoopGUI.primaryActionButton.text = "Collect $100"
		gameLoopGUI.buttonActive(gameLoopGUI.primaryActionButton)
		gameLoopGUI.secondaryActionButton.text = "Travel Voucher"
		gameLoopGUI.buttonActive(gameLoopGUI.secondaryActionButton)
		gameLoopGUI.drawGUI(token)
		commandText = gameLoopGUI.getUserInput()
		if commandText == gameLoopGUI.primaryActionButton:
			moneyFromBank(token, 100)
		elif commandText == gameLoopGUI.secondaryActionButton:
			collectTravelVoucher(token)
		gameLoopGUI.allButtonsInactive
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Income Tax":
		gameLoopGUI.stringStack.append("You have landed on Income Tax. Pay $200 or 10% of the value of all your assets to the pool.")
		assetValue = token.PlayerMoney
		for i in range(len(token.OwnedProps)):
			if Gameboard.propList[token.OwnedProps[i]][1] == "CG":
				assetValue = assetValue + Gameboard.propList[token.OwnedProps[i]][9]
				assetValue = assetValue + Gameboard.propList[token.OwnedProps[i]][7] * Gameboard.propList[token.OwnedProps[i]][10]
			else:
				assetValue = assetValue + Gameboard.propList[token.OwnedProps[i]][6]	
		gameLoopGUI.primaryActionButton.text = "Pay $200"
		gameLoopGUI.buttonActive(gameLoopGUI.primaryActionButton)
		gameLoopGUI.secondaryActionButton.text = "Pay 10% ($" + str(int(assetValue * 0.1)) + ")"
		gameLoopGUI.buttonActive(gameLoopGUI.secondaryActionButton)
		gameLoopGUI.drawGUI(token)
		commandText = gameLoopGUI.getUserInput()
		if commandText == gameLoopGUI.primaryActionButton.text:
			payFineToPool(token, 200)
		if commandText == gameLoopGUI.secondaryActionButton.text:
			payFineToPool(token, int(assetValue * 0.1))
		gameLoopGUI.allButtonsInactive()
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Roll Three":
		gameLoopGUI.stringStack.append("You have landed on Roll Three")
		landOnRollThree(token)
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Jail":
		gameLoopGUI.stringStack.append("You are visiting Jail")
	#elif Gameboard.spaceType[coords[0]][coords[1]] == "Squeeze Play":
	#	landOnSqueezePlay(token)
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Luxury Tax":
		gameLoopGUI.stringStack.append("You have landed on Luxury Tax, you must pay 75 dollars to the pool.")
		payFineToPool(token, 75)
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Go to Jail":
		gameLoopGUI.stringStack.append("You have landed on Go to Jail")
		goToJail(token)
	#elif Gameboard.spaceType[coords[0]][coords[1]] == "Stock Exchange":
	#	landOnStockExchange(token)
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Tax Refund":
		gameLoopGUI.stringStack.append("You collected $" + str(int(Gameboard.poolMoney / 2)) + " from the pool for your tax refund.")
		token.PlayerMoney = token.PlayerMoney + int(Gameboard.poolMoney / 2)
		Gameboard.poolMoney = int(Gameboard.poolMoney / 2)
	elif Gameboard.spaceType[coords[0]][coords[1]] == "Reverse Direction":
		pass

def improveProps(token):
	improvePropsPickGroupGUI.drawGUI(token)
	selectedColorGroup = improvePropsPickGroupGUI.getUserInput()
	if selectedColorGroup in token.ownedColorGroups:
		inputLoop = True
		while inputLoop == True:
			improvePropsGUI.drawGUI(token, selectedColorGroup)
			response = improvePropsGUI.getUserInput()
			print(response)
			if response == "Done":
				inputLoop = False
			if response in token.ownedColorGroups[selectedColorGroup][1]:
				if token.PlayerMoney > Gameboard.propList[response][10]:
					token.PlayerMoney = token.PlayerMoney - Gameboard.propList[response][10]
					Gameboard.propList[response][7] = Gameboard.propList[response][7] + 1
					token.ownedColorGroups[selectedColorGroup][2] = token.ownedColorGroups[selectedColorGroup][2] + 1
					if token.ownsImprovements == False:
						token.ownsImprovements = True
 	
def sellImprovements(token):
	unimprovePropsPickGroupGUI.drawGUI(token)
	selectedColorGroup = unimprovePropsPickGroupGUI.getUserInput()
	if selectedColorGroup in token.ownedColorGroups:
		inputLoop = True
		while inputLoop == True:
			unimprovePropsGUI.drawGUI(token, selectedColorGroup)
			response = unimprovePropsGUI.getUserInput()
			print(response)
			if response == "Done":
				inputLoop = False
			if response in token.ownedColorGroups[selectedColorGroup][1]:
				token.PlayerMoney = token.PlayerMoney + (Gameboard.propList[response][10] // 2)
				Gameboard.propList[response][7] = Gameboard.propList[response][7] - 1
				token.ownedColorGroups[selectedColorGroup][2] = token.ownedColorGroups[selectedColorGroup][2] - 1
				if token.ownsImprovements == False:
					token.ownsImprovements = True
	
def mortgageProperties(token):
	mortgagePropsGUI.drawGUI(token)
	response = mortgagePropsGUI.getUserInput()
	
	if response in token.OwnedProps:
		Gameboard.propList[response][4] = "mortgaged"
		token.mortgagedProps.append(response)
		if Gameboard.propList[response][1] == "CG":
			moneyFromBank(token, Gameboard.propList[response][9])
		else:
			moneyFromBank(token, Gameboard.propList[response][6])
		print(response)
		
def unmortgageProperties(token):
	unmortgagePropsGUI.drawGUI(token)
	response = unmortgagePropsGUI.getUserInput()
	
	if response in token.mortgagedProps:
		if Gameboard.propList[response][1] == "CG":
			if token.PlayerMoney > int(Gameboard.propList[response][9] * 1.1):
				Gameboard.propList[response][4] = "unmortgaged"
				token.mortgagedProps.pop(index(response))
				token.PlayerMoney = token.PlayerMoney - int(Gameboard.propList[response][9] * 1.1)
			else:
				Gameboard.propList[response][4] = "unmortgaged"
				token.mortgagedProps.pop(index(response))
				token.PlayerMoney = token.PlayerMoney - int(Gameboard.propList[response][9] * 1.1)

def tradeInterface(token):
	inputLoop = True
	tradeInterfaceGUI.__init__()
	tradeInterfaceGUI.setActivePlayer(token)
	tradeInterfaceGUI.activePlayerAssets.isActive = True
	while inputLoop == True:
		if tradeInterfaceGUI.partnerSelected == False:
			tradeInterfaceGUI.selectTradePartner.isActive = True
		else:
			tradeInterfaceGUI.secondPlayerAssets.isActive = True
		tradeInterfaceGUI.drawGUI()
		response = tradeInterfaceGUI.getUserInput()
		if response == "Done":
			inputLoop = False
		elif tradeInterfaceGUI.partnerSelected == False and type(response) == int and response != token.Playernumber:
			tradeInterfaceGUI.setSecondPlayer(listPlayers[response])
			tradeInterfaceGUI.selectTradePartner.makeInactive()
			tradeInterfaceGUI.partnerSelected = True
		elif tradeInterfaceGUI.partnerSelected == True and response == "ChangeSP":
			tradeInterfaceGUI.secondPlayerAddMoney.makeInactive()
			tradeInterfaceGUI.secondPlayerAssets.__init__(tradeInterfaceGUI, (1060, 200), "second")
			tradeInterfaceGUI.secondPlayerAssets.makeInactive()
			tradeInterfaceGUI.selectTradePartner.isActive = True
			tradeInterfaceGUI.partnerSelected == False
		elif tradeInterfaceGUI.activePlayerAddMoney.isActive == True:
			if response in ["-100", "-10", "-1", "+1", "+10", "+100"]:
				tradeInterfaceGUI.activePlayerAddMoney.addMoneyFunc(response)
			if response == "Finished":
				tradeInterfaceGUI.activePlayerAddMoney.makeInactive()
				tradeInterfaceGUI.activePlayerAssets. isActive = True
		elif tradeInterfaceGUI.secondPlayerAddMoney.isActive == True:
			if response in ["-100", "-10", "-1", "+1", "+10", "+100"]:
				tradeInterfaceGUI.secondPlayerAddMoney.addMoneyFunc(response)
			if response == "Finished":
				tradeInterfaceGUI.secondPlayerAddMoney.makeInactive()
				tradeInterfaceGUI.secondPlayerAssets. isActive = True
		elif type(response) == list:
			if response[0] == "Add/remove money":
				if response[1] == "active":
					tradeInterfaceGUI.activePlayerAddMoney.isActive = True
					tradeInterfaceGUI.activePlayerAssets.makeInactive()
				elif response[1] == "second":
					tradeInterfaceGUI.secondPlayerAddMoney.isActive = True
					tradeInterfaceGUI.secondPlayerAssets.makeInactive()
			if response[0] == "Prop":
				if response[1] == "active":
					if response[2] == "bottom":
						if not(response[3] in tradeInterfaceGUI.activePlayerAssets.proposedProps):
							tradeInterfaceGUI.activePlayerAssets.proposedProps.append(response[3])
							tradeInterfaceGUI.activePlayerAssets.proposedProps.sort()
					elif response[2] == "top":
						tradeInterfaceGUI.activePlayerAssets.proposedProps.pop(tradeInterfaceGUI.activePlayerAssets.proposedProps.index(response[3]))
				elif response[1] == "second":
					if response[2] == "bottom":
						if not(response[3] in tradeInterfaceGUI.secondPlayerAssets.proposedProps):
							tradeInterfaceGUI.secondPlayerAssets.proposedProps.append(response[3])
							tradeInterfaceGUI.secondPlayerAssets.proposedProps.sort()
					elif response[2] == "top":
						tradeInterfaceGUI.secondPlayerAssets.proposedProps.pop(tradeInterfaceGUI.secondPlayerAssets.proposedProps.index(response[3]))
		else:
			print(response)

def moveToken(token, distance):
	#Normal movement
	oldPosition = [0,0]
	oldPosition[0] = token.BoardPosition[0]
	oldPosition[1] = token.BoardPosition[1]
	if distance % 2 == 1:
		#No level shifting
		#print("Non-level shifting")
		newPosition = token.BoardPosition[1] + distance
		#print(newPosition)
		#check for passing origin point
		if token.BoardPosition[0] == 0 and newPosition > 55:
			#print("Origin pass, OT")
			newPosition = newPosition - 56
		if token.BoardPosition[0] == 1 and newPosition > 39:
			#print("Origin pass, MT")
			newPosition = newPosition - 40
		if token.BoardPosition[0] == 2 and newPosition > 23:
			#print("Origin pass, IT")
			newPosition = newPosition - 24
		#print(newPosition)
		token.setBoardPosition([token.BoardPosition[0],newPosition])
		#check for passing paycorner
		if token.BoardPosition[0] == 0:
			if oldPosition[1] < 28 and oldPosition[1] + distance > 27:
				payCorner("Payday", token)
			if oldPosition[1] > 27 and oldPosition[1] + distance - 55 > 27:
				payCorner("Payday", token)
		if token.BoardPosition[0] == 1:
			if oldPosition[1] + distance > 39:
				payCorner("Go", token)
		if token.BoardPosition[0] == 2:
			if oldPosition[1] < 6 and oldPosition[1] + distance > 5:
				payCorner("Bonus", token)
			if oldPosition[1] > 5 and oldPosition[1] + distance - 23 > 5:
				payCorner("Bonus", token)
			#if oldPosition[1] < 12 and oldPosition[1] + distance > 11:
				#stockExchangePass()
			#if oldPosition[1] > 11 and oldPosition[1] + distance - 23 > 11:
				#stockExchangePass()
	else:
		#Level shifting movement
		#print("Level shifting")
		while distance > 0:
			oldPosition = [0,0]
			oldPosition[0] = token.BoardPosition[0]
			oldPosition[1] = token.BoardPosition[1]
			if token.BoardPosition[0] == 0:
				#print("Outer track")
				if token.BoardPosition[1] > 34 and token.BoardPosition[1] + distance > 55:
					#print("pass origin")
					distance = distance - (56 - token.BoardPosition[1])
					token.setBoardPosition([0,0])
				if token.BoardPosition[1] < 7 and token.BoardPosition[1] + distance > 6:
					#print("level up RR")
					distance = distance - (7 - token.BoardPosition[1])
					token.setBoardPosition([1,5])
				elif token.BoardPosition[1] > 6 and token.BoardPosition[1] < 35 and token.BoardPosition[1] + distance > 34:
					#print("level up BOR")
					if oldPosition[1] < 28 and oldPosition[1] + distance > 27:
						payCorner("Payday", token)
					distance = distance - (35 - token.BoardPosition[1])
					token.setBoardPosition([1,25])
				else:
					#print("finish move")
					if oldPosition[1] < 28 and oldPosition[1] + distance > 27:
						payCorner("Payday", token)
					token.setBoardPosition([0,token.BoardPosition[1] + distance])
					distance = 0
			elif token.BoardPosition[0] == 1:
				#print("Middle Track")
				if token.BoardPosition[1] > 34 and token.BoardPosition[1] + distance > 39:
					#print("Pass origin")
					payCorner("Go", token)
					distance = distance - (40 - token.BoardPosition[1])
					token.setBoardPosition([1,0])
				if token.BoardPosition[1] < 5 and token.BoardPosition[1] + distance > 4:
					#print("level down RR")
					distance = distance - (5 - token.BoardPosition[1])
					token.setBoardPosition([0,7])
				elif token.BoardPosition[1] > 4 and token.BoardPosition[1] < 15 and token.BoardPosition[1] + distance > 14:
					#print("level up PR")
					distance = distance - (15 - token.BoardPosition[1])
					token.setBoardPosition([2,9])
				elif token.BoardPosition[1] > 14 and token.BoardPosition[1] < 25 and token.BoardPosition[1] + distance > 24:
					#print("level down BOR")
					distance = distance - (25 - token.BoardPosition[1])
					token.setBoardPosition([0,35])
				elif token.BoardPosition[1] > 24 and token.BoardPosition[1] < 35 and token.BoardPosition[1] + distance > 34:
					#print("level up SL")
					distance = distance - (35 - token.BoardPosition[1])
					token.setBoardPosition([2,21])
				else:
					#print("finish move")
					token.setBoardPosition([1,token.BoardPosition[1] + distance])
					distance = 0
			elif token.BoardPosition[0] == 2:
				#print("Inner Track")
				if token.BoardPosition[1] > 20 and token.BoardPosition[1] + distance > 23:
					#print("pass origin")
					distance = distance - (24 - token.BoardPosition[1])
					token.setBoardPosition([2,0])
				if token.BoardPosition[1] < 9 and token.BoardPosition[1] + distance > 8:
					#print("Level down PR")
					if oldPosition[1] < 6 and oldPosition[1] + distance > 5:
						payCorner("Bonus", token)
					distance = distance - (9 - token.BoardPosition[1])
					token.setBoardPosition([1,15])
				elif token.BoardPosition[1] > 8 and token.BoardPosition[1] < 21 and token.BoardPosition[1] + distance > 20:
					#print("level down SL")
					#if oldPosition[1] < 12 and oldPosition[1] + distance > 11:
						#stockExchangePass()
					distance = distance - (21 - token.BoardPosition[1])
					token.setBoardPosition([1,35])
				else:
					if oldPosition[1] < 6 and oldPosition[1] + distance > 5:
						payCorner("Bonus", token)
					#if oldPosition[1] < 12 and oldPosition[1] + distance > 11:
						#stockExchangePass()
					token.setBoardPosition([2,token.BoardPosition[1] + distance])
					distance = 0

def setUpNewGame():
	inputLoop = True
	while inputLoop:
		newGamePlayerNumberGUI.drawGUI()
		response = newGamePlayerNumberGUI.getUserInput()
		if response == "Confirm":
			inputLoop = False
	playerNum = newGamePlayerNumberGUI.newGamePlayerCount
	for j in range(playerNum):
		inputLoop = True
		inputString = ""
		globalVars.activePlayerNumber = j
		newGamePlayerNameGUI.drawGUI()
		inputString = newGamePlayerNameGUI.inputTextField()

		newGameSelectTokenGUI.updateName(inputString)
		newGameSelectTokenGUI.drawGUI()
		inputLoop = True
		while inputLoop == True:
			response = newGameSelectTokenGUI.getUserInput()
			if response in newGameSelectTokenGUI.availableTokens:
				selectedTokenName = response
				inputLoop = False
		listPlayers.append(Player(inputString,j,selectedTokenName))
		newGameSelectTokenGUI.takenTokenNames.append(selectedTokenName)
		newGamePlayerNameGUI.__init__()
		#listPlayers[i].heldRollThreeCards.append(actionCards.rollThreeDeck[0])
		#actionCards.rollThreeDeck.pop(0)
	return True

def drawBackground():
	window.fill((55,171,200))
	window.blit(gameboardBackground,(0,0))
	for i in range(len(listPlayers)):
		window.blit(listPlayers[i].token.image,listPlayers[i].token.rect)
	for i in range(len(Gameboard.listspace)):
		for j in range(len(Gameboard.listspace[i])):
			if Gameboard.spaceType[i][j] == "Property":
				if Gameboard.propList[Gameboard.propNum[i][j]][1] == "CG":
					if Gameboard.listspace[i][j] in Gameboard.colorBarCoords:
						if Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2] == 0 or Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2] == 180:
							hOffset = 1
							vOffset = 0
						else:
							hOffset = 0
							vOffset = 1
						if Gameboard.propList[Gameboard.propNum[i][j]][7] == 1:
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 20), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 20)))
						elif Gameboard.propList[Gameboard.propNum[i][j]][7] == 2:
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 10), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 10)))
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 30), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 30)))
						elif Gameboard.propList[Gameboard.propNum[i][j]][7] == 3:
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0], Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1]))
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 20), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 20)))
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 40), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 40)))
						elif Gameboard.propList[Gameboard.propNum[i][j]][7] == 4:
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0], Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1]))
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 15), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 15)))
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 30), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 30)))
							window.blit(pygame.transform.rotate(houseSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 45), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 45)))
						elif Gameboard.propList[Gameboard.propNum[i][j]][7] == 5:
							window.blit(pygame.transform.rotate(hotelSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 10), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 10)))
						elif Gameboard.propList[Gameboard.propNum[i][j]][7] == 6:
							window.blit(pygame.transform.rotate(skyscraperSprite.image, Gameboard.colorBarCoords[Gameboard.listspace[i][j]][2]), (Gameboard.colorBarCoords[Gameboard.listspace[i][j]][0] + (hOffset * 10), Gameboard.colorBarCoords[Gameboard.listspace[i][j]][1] + (vOffset * 10)))

def victoryMessage(token):
	print("victory message")
	window.fill((55,171,200))
	window.blit(fontBig.render("Congratulations!", True, (255,255,255)), (700,300))
	window.blit(font.render(token.PlayerName + ", you have won this game of Ultimate Monopoly.", True, (255,255,255)), (700,400))
	window.blit(token.token.image, (700,500))
	pygame.display.update()
	waiting = True
	while waiting == True:
		for event in pygame.event.get():
			if event.type == KEYUP or event.type == MOUSEBUTTONDOWN:
				print("Thank you for playing")
				sys.exit()

def readSaveFile():
	savFile = open("ultimate_game_two.sav", "r")
	readSaveFormat = json.loads(savFile.readline())
	if readSaveFormat == saveFileVersion:
		globalVars.currentPlayer = json.loads(savFile.readline())
		#Gameboard.stocksInBank = json.loads(savFile.readline())
		actionCards.chanceDeck = json.loads(savFile.readline())
		actionCards.chestDeck = json.loads(savFile.readline())
		actionCards.travelVoucherDeck = json.loads(savFile.readline())
		actionCards.rollThreeDeck = json.loads(savFile.readline())
		playerNum = json.loads(savFile.readline())
		for i in range(playerNum):
			readNumber = json.loads(savFile.readline())
			if readNumber != i:
				print("Something is probably wrong")
			playerNameFile = json.loads(savFile.readline())
			playerTokenFile = json.loads(savFile.readline())
			listPlayers.append(Player(playerNameFile, i, playerTokenFile))
			listPlayers[i].setBoardPosition(json.loads(savFile.readline()))
			listPlayers[i].PlayerMoney = json.loads(savFile.readline())
			listPlayers[i].OwnedProps = json.loads(savFile.readline())
			ownedPropsImprovements = json.loads(savFile.readline())
			for j in range(len(listPlayers[i].OwnedProps)):
				Gameboard.propList[listPlayers[i].OwnedProps[j]][2] = listPlayers[i].Playernumber
				if Gameboard.propList[listPlayers[i].OwnedProps[j]][1] == "CG":
					Gameboard.propList[listPlayers[i].OwnedProps[j]][7] = ownedPropsImprovements[j]
			listPlayers[i].mortgagedProps = json.loads(savFile.readline())
			for j in range(len(listPlayers[i].mortgagedProps)):
				Gameboard.propList[listPlayers[i].mortgagedProps[j]][2] = listPlayers[i].Playernumber
				Gameboard.propList[listPlayers[i].mortgagedProps[j]][4] = "mortgaged"
			#print(listPlayers[i].OwnedProps)
			listPlayers[i].IsInJail = json.loads(savFile.readline())
			#print(listPlayers[i].IsInJail)
			listPlayers[i].turnsInJail = json.loads(savFile.readline())
			listPlayers[i].isBankrupt = json.loads(savFile.readline())
			listPlayers[i].heldTravelVouchers = json.loads(savFile.readline())
			listPlayers[i].heldChanceCards = json.loads(savFile.readline())
			listPlayers[i].heldChestCards = json.loads(savFile.readline())
			listPlayers[i].heldRollThreeCards = json.loads(savFile.readline())
			listPlayers[i].ownedColorGroups = json.loads(savFile.readline())
			listPlayers[i].ownsImprovableCG = json.loads(savFile.readline())
			listPlayers[i].ownsImprovements = json.loads(savFile.readline())
			listPlayers[i].ownedStock = json.loads(savFile.readline())
			listPlayers[i].turnActive = json.loads(savFile.readline())
			resumingFromFile = True
	else:
		print("The save file is invalid or a different version, unable to load")
		setUpNewGame()
	savFile.close()

def writeSaveFile():
	savFile = open("ultimate_game_two.sav", "w")
	json.dump(saveFileVersion, savFile)
	savFile.write("\n")
	json.dump(globalVars.currentPlayer, savFile)
	savFile.write("\n")
	#json.dump(Gameboard.stocksInBank, savFile)
	#savFile.write("\n")
	json.dump(actionCards.chanceDeck, savFile)
	savFile.write("\n")
	json.dump(actionCards.chestDeck, savFile)
	savFile.write("\n")
	json.dump(actionCards.travelVoucherDeck, savFile)
	savFile.write("\n")
	json.dump(actionCards.rollThreeDeck, savFile)
	savFile.write("\n")
	json.dump(len(listPlayers), savFile)
	savFile.write("\n")
	for i in range(len(listPlayers)):
		json.dump(listPlayers[i].Playernumber, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].PlayerName, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].playerTokenName, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].BoardPosition, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].PlayerMoney, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].OwnedProps, savFile)
		savFile.write("\n")
		ownedPropsImprovements = []
		for j in range(len(listPlayers[i].OwnedProps)):
			if Gameboard.propList[listPlayers[i].OwnedProps[j]][1] == "CG":
				ownedPropsImprovements.append(Gameboard.propList[listPlayers[i].OwnedProps[j]][7])
			else:
				ownedPropsImprovements.append(0)
		json.dump(ownedPropsImprovements, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].mortgagedProps, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].IsInJail, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].turnsInJail, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].isBankrupt, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].heldTravelVouchers, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].heldChanceCards, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].heldChestCards, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].heldRollThreeCards, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].ownedColorGroups, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].ownsImprovableCG, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].ownsImprovements, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].ownedStock, savFile)
		savFile.write("\n")
		json.dump(listPlayers[i].turnActive, savFile)
		savFile.write("\n")
	savFile.close()

def quitGame():
	inputLoop = True
	window.fill((55,171,200))
	buttonYes = dButton(300, 500, 200, 100, "Yes")
	buttonNo = dButton(600, 500, 200, 100, "No")
	buttonYes.draw()
	buttonNo.draw()
	window.blit(font.render("Would you like to save this game?", True, (255,255,255)), (300,400))
	pygame.display.update()
	while inputLoop:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				mouseDownPos = pygame.mouse.get_pos()
				if buttonYes.buttonRect.collidepoint(mouseDownPos):
					writeSaveFile()
					inputLoop = False
				if buttonNo.buttonRect.collidepoint(mouseDownPos):
					inputLoop = False
	print("Thank you for playing")
	sys.exit()

def drawHUD():
	pass

globalVars.currentPlayer = 0
listPlayers = []
gameboardBackground = pygame.image.load("umbg.png")
houseSprite = houseSpriteClass("houseS")
hotelSprite = houseSpriteClass("HotelS")
skyscraperSprite = houseSpriteClass("SkyscraperS")
displaySize = pygame.display.get_desktop_sizes()[0]
dispHeight = displaySize[1]
Gameboard = Gameboardclass()
commandText = ""
actionCards = aCardClass()
#recentBankruptcyFlag = False
gameboardBackground = pygame.transform.smoothscale(gameboardBackground, (displaySize[1],displaySize[1]))
buttonList = []
cheating = False
cheaterLevel = 0

mainMenuGUI.drawGUI()
response = mainMenuGUI.getUserInput()
if response == "Yes":
	readSaveFile()
elif response == "No":
	setUpNewGame()
	print(listPlayers)
	globalVars.currentPlayer = 0
	listPlayers[globalVars.currentPlayer].turnActive = True

running = True
rollDoublesCount = 0

while running:
	if globalVars.recentBankruptcyFlag == True:
		#print("recent bankruptcy")
		chickenDinner =	checkForWinner()
		#print(chickenDinner)
		if chickenDinner in range(len(listPlayers)):
			victoryMessage(listPlayers[chickenDinner])
	if cheating == False:
		if listPlayers[globalVars.currentPlayer].turnActive == True and listPlayers[globalVars.currentPlayer].IsInJail == False:
			gameLoopGUI.primaryActionButton.text = "Roll dice"
			gameLoopGUI.buttonActive(gameLoopGUI.primaryActionButton)
			gameLoopGUI.buttonInactive(gameLoopGUI.secondaryActionButton)
		elif listPlayers[globalVars.currentPlayer].IsInJail == True:
			if listPlayers[globalVars.currentPlayer].turnsInJail < 3 and listPlayers[globalVars.currentPlayer].turnActive == True:
				gameLoopGUI.primaryActionButton.text = "Roll for doubles"
				gameLoopGUI.buttonActive(gameLoopGUI.primaryActionButton)
			if listPlayers[globalVars.currentPlayer].PlayerMoney >= 50:
				gameLoopGUI.secondaryActionButton.text = "Pay fine"
				gameLoopGUI.buttonActive(gameLoopGUI.secondaryActionButton)
			elif listPlayers[globalVars.currentPlayer].turnsInJail >= 3:
				gameLoopGUI.secondaryActionButton.text = "Declare bankruptcy"
				gameLoopGUI.buttonActive(secondaryActionButton)
		elif listPlayers[globalVars.currentPlayer].turnActive == False and listPlayers[globalVars.currentPlayer].turnsInJail < 2:
			gameLoopGUI.primaryActionButton.text = "End turn"
			gameLoopGUI.buttonActive(gameLoopGUI.primaryActionButton)
			gameLoopGUI.buttonInactive(gameLoopGUI.secondaryActionButton)
		if listPlayers[globalVars.currentPlayer].ownsImprovableCG == True:
			gameLoopGUI.improveButton.text = "Improve property"
			gameLoopGUI.buttonActive(gameLoopGUI.improveButton)
		if listPlayers[globalVars.currentPlayer].ownsImprovements == True:
			gameLoopGUI.unimproveButton.text = "Sell improvements"
			gameLoopGUI.buttonActive(gameLoopGUI.unimproveButton)
		if listPlayers[globalVars.currentPlayer].hasUnmortgagedProps():
			gameLoopGUI.mortgageButton.text = "Mortgage property"
			gameLoopGUI.buttonActive(gameLoopGUI.mortgageButton)
		if listPlayers[globalVars.currentPlayer].hasMortgagedProps():
			gameLoopGUI.unmortgageButton.text = "Unmortgage property"
			gameLoopGUI.buttonActive(gameLoopGUI.unmortgageButton)
	else:
		pass
		#buttonA.text = "Free money"
		#buttonManager.addButton(buttonA)
		#buttonB.text = "All your base"
		#buttonManager.addButton(buttonB)
		#buttonC.text = "Enter Roll"
		#buttonManager.addButton(buttonC)
		#buttonD.text = "buttonD"
		#buttonManager.addButton(buttonD)
		#buttonE.text = "buttonE"
		#buttonManager.addButton(buttonE)
		#buttonF.text = "buttonF"
		#buttonManager.addButton(buttonF)
		#buttonG.text = "buttonG"
		#buttonManager.addButton(buttonG)
	gameLoopGUI.drawGUI(listPlayers[globalVars.currentPlayer])
	commandText = gameLoopGUI.getUserInput()
		#if event.type == KEYUP:
		#	if event.key == K_ESCAPE:
		#		commandText = buttonQ.text
		#	if event.key == K_c and cheaterLevel == 0 and buttonQ.buttonRect.collidepoint(pygame.mouse.get_pos()):
		#		cheaterLevel = 1
		#	if event.key == K_h and cheaterLevel == 1 and buttonQ.buttonRect.collidepoint(pygame.mouse.get_pos()):
		#		cheaterLevel = 2
		#	if event.key == K_e and cheaterLevel == 2 and buttonQ.buttonRect.collidepoint(pygame.mouse.get_pos()):
		#		cheaterLevel = 3
		#	if event.key == K_a and cheaterLevel == 3 and buttonQ.buttonRect.collidepoint(pygame.mouse.get_pos()):
		#		cheaterLevel = 4
		#	if event.key == K_t and cheaterLevel == 4 and buttonQ.buttonRect.collidepoint(pygame.mouse.get_pos()):
		#		cheaterLevel = 0
		#		cheating = True
	#Make a trade
	if commandText == "Trade":
		tradeInterface(listPlayers[globalVars.currentPlayer])
	#Improve Property
	if listPlayers[globalVars.currentPlayer].ownsImprovableCG == True and commandText == "Improve property":
		improveProps(listPlayers[globalVars.currentPlayer])
	#Sell Improvements
	if listPlayers[globalVars.currentPlayer].ownsImprovements == True and commandText == "Sell improvements":
		sellImprovements(listPlayers[globalVars.currentPlayer])
	#Unmortgage
	if listPlayers[globalVars.currentPlayer].hasMortgagedProps() and commandText == "Unmortgage property":
		unmortgageProperties(listPlayers[globalVars.currentPlayer])
	#Mortgage
	if listPlayers[globalVars.currentPlayer].hasUnmortgagedProps() and commandText == "Mortgage property":
		mortgageProperties(listPlayers[globalVars.currentPlayer])
	#Roll Dice for standard turn
	if listPlayers[globalVars.currentPlayer].turnActive == True and listPlayers[globalVars.currentPlayer].IsInJail == False and commandText == "Roll dice":
		Dice.State = Dice.Roll()
		if listPlayers[globalVars.currentPlayer].IsInJail == False:
			moveToken(listPlayers[globalVars.currentPlayer], Dice.Sum())
			gameLoopGUI.stringStack.append("You have rolled " + str(Dice.State[0]) + " and " + str(Dice.State[1]) + " total of " + str(Dice.Sum()) + " and landed on " + Gameboard.ref(listPlayers[globalVars.currentPlayer].BoardPosition) + ".")
			landOnSpace(listPlayers[globalVars.currentPlayer], listPlayers[globalVars.currentPlayer].BoardPosition)
			if not(rollDoublesCount == 0):
				listPlayers[globalVars.currentPlayer].turnActive = False
		if Dice.State[0] == Dice.State[1] and rollDoublesCount == 2:
			gameLoopGUI.stringStack.append("You have rolled doubles 3 times in a row.")
			goToJail(listPlayers[globalVars.currentPlayer])
			listPlayers[globalVars.currentPlayer].turnActive = False
		if Dice.State[0] == Dice.State[1] and rollDoublesCount < 2:
			rollDoublesCount = rollDoublesCount + 1
			gameLoopGUI.stringStack.append("You have rolled doubles " + str(rollDoublesCount) + " times.")
		else:
			rollDoublesCount = 0
			listPlayers[globalVars.currentPlayer].turnActive = False
	#Roll for doubles if in Jail
	if listPlayers[globalVars.currentPlayer].turnActive == True and listPlayers[globalVars.currentPlayer].IsInJail == True and commandText == "Roll for doubles":
			Dice.State = Dice.Roll()
			if Dice.State[0] == Dice.State[1]:
				listPlayers[globalVars.currentPlayer].IsInJail == False
				moveToken(listPlayers[globalVars.currentPlayer], Dice.Sum())
				gameLoopGUI.stringStack.append("You have rolled " + str(Dice.State[0]) + " and " + str(Dice.State[1]) + " total of " + str(Dice.Sum()) + ", left Jail and landed on " + Gameboard.ref(listPlayers[globalVars.currentPlayer].BoardPosition))
				landOnSpace(listPlayers[globalVars.currentPlayer], listPlayers[globalVars.currentPlayer].BoardPosition)
				listPlayers[globalVars.currentPlayer].turnActive == False
				listPlayers[globalVars.currentPlayer].turnsInJail = 0
			else:
				listPlayers[globalVars.currentPlayer].turnsInJail = listPlayers[globalVars.currentPlayer].turnsInJail + 1
				listPlayers[globalVars.currentPlayer].turnActive = False
			gameLoopGUI.secondaryActionButton.text = ""
			gameLoopGUI.buttonInactive(gameLoopGUI.secondaryActionButton)
	#Pay fines in Jail
	if listPlayers[globalVars.currentPlayer].IsInJail == True and commandText == "Pay fine":
		payFineToPool(listPlayers[globalVars.currentPlayer], 50)
		listPlayers[globalVars.currentPlayer].IsInJail = False
		listPlayers[globalVars.currentPlayer].turnsInJail = 0
		gameLoopGUI.stringStack.append("You have payed $50 to the pool and left Jail.")
	#End turn
	elif listPlayers[globalVars.currentPlayer].turnActive == False and commandText == "End turn":
		if globalVars.currentPlayer + 1 < len(listPlayers):
			globalVars.currentPlayer = globalVars.currentPlayer + 1
		else:
			globalVars.currentPlayer = 0
		mostRecentMove.clearMRV()
		listPlayers[globalVars.currentPlayer].turnActive = True
	#Free money cheat
	if commandText == "Free money":
		listPlayers[globalVars.currentPlayer].PlayerMoney = listPlayers[globalVars.currentPlayer].PlayerMoney + 3200
		cheating = False
		#for i in range(len(buttonManager.buttonsOnScreen)):
		#	buttonManager.buttonsOnScreen[i].text = ""
		buttonQ.text = "Quit"
		print("cheatButtonActivated")
	#All your base cheat
	if commandText == "All your base":
		for i in range(len(Gameboard.propList)):
			assignProp(listPlayers[globalVars.currentPlayer],i)
		cheating = False
		#for i in range(len(buttonManager.buttonsOnScreen)):
		#	buttonManager.buttonsOnScreen[i].text = ""
		buttonQ.text = "Quit"
	#Roll entry cheat
	if commandText == "Enter Roll":
		Dice.State[0] = 0
		while Dice.State[0] == 0:
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.unicode.isnumeric():
						Dice.State[0] = int(event.unicode)
		Dice.State[1] = 0
		while Dice.State[1] == 0:
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.unicode.isnumeric():
						Dice.State[1] = int(event.unicode)
		moveToken(listPlayers[globalVars.currentPlayer], Dice.Sum())
		mostRecentMove.displayStringLine1 = 'You have "rolled" ' + str(Dice.State[0]) + " and " + str(Dice.State[1]) + " total of " + str(Dice.Sum()) + " and landed on " + Gameboard.ref(listPlayers[globalVars.currentPlayer].BoardPosition)
		mostRecentMove.displayMove = True
		landOnSpace(listPlayers[globalVars.currentPlayer], listPlayers[globalVars.currentPlayer].BoardPosition)
		cheating = False
		#for i in range(len(buttonManager.buttonsOnScreen)):
		#	buttonManager.buttonsOnScreen[i].text = ""
		buttonQ.text = "Quit"
	elif commandText == "Quit":
		quitGame()
	if listPlayers[globalVars.currentPlayer].isBankrupt == True:
			if globalVars.currentPlayer + 1 < len(listPlayers):
				globalVars.currentPlayer = globalVars.currentPlayer + 1
			else:
				globalVars.currentPlayer = 0
			listPlayers[globalVars.currentPlayer].turnActive = True
	pygame.display.update()

pygame.quit()