from mcpi.minecraft import Minecraft
from mcpi import block
import time
from random import randint

air = 0
ironblock = 42
snow = 80
whitewool = 35
redwool = 35,14
bluewool = 35,11
greenwool = 35,13
yellowwool = 35,4
purplewool = 35,10
pinkwool = 35,6
cyanwool = 35,9
orangewool = 35,1

#mc = Minecraft.create("127.0.0.1", 4711)
mc = Minecraft.create("10.183.3.25", 4711)
r = randint(0,9)
	
if r == 1:
	wool = whitewool;
elif r == 2:
		wool = redwool;
elif r == 3:
	wool = bluewool;
elif r == 4:
	wool = greenwool;
elif r == 5:
	wool = yellowwool;
elif r == 6:
	wool = purplewool;
elif r == 7:
	wool = pinkwool;
elif r == 8:
	wool = cyanwool;
else:
	wool = orangewool
		

def init():
	mc = Minecraft.create("127.0.0.1", 4711)
	#mc = Minecraft.create("10.183.3.25", 4711)
	x, y, z = mc.player.getPos()
	return mc
				
def clear_with_air(mc,x,y,z,h,k,l):
	mc.setBlocks(x-75,y-75,z-75,x+75,y+75,z+75, air)
	
def ground(mc,x,y,z):
	mc.setBlocks(x-50,y-1,z-50,x+50,y,z+50, snow)
	
def leg1(mc,x,y,z,x1,y1,z1):
	mc.player.setPos(x1,y1,z1,x1+15,y1,z1+15)
	mc.setBlocks(x-2,y,z-2,x+2,y+1,z+2, ironblock)
	mc.setBlocks(x-1,y,z-1,x+1,y+10,z+1, ironblock)
	
def leg2(mc,x,y,z,x1,y1,z1):
	mc.player.setPos(x,y,z,x+10,y,z)
	mc.setBlocks(x-2,y,z-2,x+2,y+1,z+2, ironblock)
	mc.setBlocks(x-1,y,z-1,x+1,y+10,z+1, ironblock)
	
def leg3(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x-2,y,z-2,x+2,y+1,z+2, ironblock)
	mc.setBlocks(x-1,y,z-1,x+1,y+10,z+1, ironblock)
	
def leg4(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x-2,y,z-2,x+2,y+1,z+2, ironblock)
	mc.setBlocks(x-1,y,z-1,x+1,y+10,z+1, ironblock)
	
def body(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+14,y+9,z-26,x-2,y,z+2, ironblock)
	
def body2(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+14,y+11,z+5,x-2,y,z-11, ironblock)
	
def body3(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+14,y+10,z+6,x-2,y,z-12, ironblock)
	
def body4(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+8,y-2,z-20,x,y,z, ironblock)
	
def cockpit(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+3,y+3,z+9,x-3,y-1,z, ironblock)
	
def cockpit2(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+2,y+2,z+7,x-2,y,z, air)
	
def cpconnector(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+1,y,z+2,x-1,y-1,z, ironblock)
	
def cpview(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+1,y,z,x-1,y,z, wool)
	
def leftturret(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x,y,z+3,x,y,z, ironblock)
	
def rightturret(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x,y,z+3,x,y,z, ironblock)
	
def cockpit3(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+2,y+2,z,x-2,y,z, ironblock)
	
def leftturret2(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x,y,z+2,x,y,z, ironblock)
	
def rightturret2(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x,y,z+2,x,y,z, ironblock)
	
def cockpit4(mc,x,y,z,x1,y1,z1):
	mc.setBlocks(x+2,y,z,x-2,y,z, ironblock)
	
def turretlaser():
	mc.postToChat("YIKES")
	mc.setBlock(10,19,18, wool)
	mc.setBlock(2,19,18, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,18, air)
	mc.setBlock(2,19,18, air)
	mc.setBlock(10,19,19, wool)
	mc.setBlock(2,19,19, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,19, air)
	mc.setBlock(2,19,19, air)
	mc.setBlock(10,19,20, wool)
	mc.setBlock(2,19,20, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,20, air)
	mc.setBlock(2,19,20, air)
	mc.setBlock(10,19,21, wool)
	mc.setBlock(2,19,21, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,21, air)
	mc.setBlock(2,19,21, air)
	mc.setBlock(10,19,22, wool)
	mc.setBlock(2,19,22, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,22, air)
	mc.setBlock(2,19,22, air)
	mc.setBlock(10,19,23, wool)
	mc.setBlock(2,19,23, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,23, air)
	mc.setBlock(2,19,23, air)
	mc.setBlock(10,19,24, wool)
	mc.setBlock(2,19,24, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,24, air)
	mc.setBlock(2,19,24, air)
	mc.setBlock(10,19,25, wool)
	mc.setBlock(2,19,25, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,25, air)
	mc.setBlock(2,19,25, air)
	mc.setBlock(10,19,26, wool)
	mc.setBlock(2,19,26, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,26, air)
	mc.setBlock(2,19,26, air)
	mc.setBlock(10,19,27, wool)
	mc.setBlock(2,19,27, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,27, air)
	mc.setBlock(2,19,27, air)
	mc.setBlock(10,19,28, wool)
	mc.setBlock(2,19,28, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,28, air)
	mc.setBlock(2,19,28, air)
	mc.setBlock(10,19,29, wool)
	mc.setBlock(2,19,29, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,29, air)
	mc.setBlock(2,19,29, air)
	mc.setBlock(10,19,30, wool)
	mc.setBlock(2,19,30, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,30, air)
	mc.setBlock(2,19,30, air)
	mc.setBlock(10,19,31, wool)
	mc.setBlock(2,19,31, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,31, air)
	mc.setBlock(2,19,31, air)
	mc.setBlock(10,19,32, wool)
	mc.setBlock(2,19,32, wool)
	time.sleep(0.1)
	mc.setBlock(10,19,32, air)
	mc.setBlock(2,19,32, air)

def main():
	mc = init()
	x1, y1, z1 = 0, 5, 0
	mc.player.setPos(0,5,0)
	x,y,z = mc.player.getPos()
	h,k,l = 25,25,25
	clear_with_air(mc,x,y,z,h,k,l)
	ground(mc,x,y,z)
	leg1(mc,x,y,z,x1,y1,z1)
	leg2(mc,x+12,y,z,x1,y1,z1)
	leg3(mc,x,y,z-24,x1,y1,z1)
	leg4(mc,x+12,y,z-24,x1,y1,z1)
	mc.player.setPos(7,6,0)
	body(mc,x,y+11,z,x1,y1,z1)
	mc.player.setPos(7,6,-9)
	body2(mc,x,y+11,z-9,x1,y1,z1)
	body3(mc,x,y+11,z-9,x1,y1,z1)
	body4(mc,x+2,y+11,z-2,x1,y1,z1)
	cockpit(mc,x+6,y+13,z+5,x1,y1,z1)
	cockpit2(mc,x+6,y+13,z+6,x1,y1,z1)
	cpconnector(mc,x+6,y+14,z+2,x1,y1,z1)
	rightturret(mc,x+10,y+14,z+14,x1,y1,z1)
	leftturret(mc,x+2,y+14,z+14,x1,y1,z1)
	cockpit3(mc,x+6,y+13,z+15,x1,y1,z1)
	rightturret2(mc,x+8,y+11,z+14,x1,y1,z1)
	leftturret2(mc,x+4,y+11,z+14,x1,y1,z1)
	cockpit4(mc,x+6,y+14,z+16,x1,y1,z1)
	cpview(mc,x+6,y+14,z+16,x1,y1,z1)


main()
	
while air == 0:	
	for hitBlock in mc.events.pollBlockHits():
		if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.IRON_BLOCK.id:
			turretlaser()
