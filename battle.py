import time
import random

print()
print('-' * 65)

print('A wild Crackhead appears! ')
time.sleep(0.5)
print('👁 👅 👁')
print('...the background music changes...')
time.sleep(0.5)
print('You only have one Bratz Doll, Jade! ')
time.sleep(0.5)
print('I choose you Jade!!! ')
time.sleep(0.5)
print()

# set the starting health values 
Jade_hp = 150
crackhead_hp = 170
time.sleep(0.5)
print()
	
while Jade_hp > 0 and crackhead_hp > 0:
	pass
	print('Choose your battle move:')
	print('- [1] Spray Perfume')
	time.sleep(0.3)
	print('- [2] Dance battle')
	time.sleep(0.3)
	print('- [3] Spray Perfume')
	time.sleep(0.3)
	print('- [4] Bite')
	time.sleep(0.3)
	print('- [5] Capture')
	time.sleep(0.3)
	print('- [6] Run Away')
	print()

	player_move = input('Pick a move using the corresponding number: ')
	player_move = int(player_move)

	if player_move == 1:
		crackhead_hp = crackhead_hp - 100
		print('Jade uses Spray Perfume and deals 100 HP of damage.')
	elif player_move == 2:
		damage = random.randint(60,90)
		crackhead_hp == crackhead_hp - damage
		print('Jade uses Dance battle and deals ' + str(damage) + ' HP of damege. ')
	elif player_move == 3:
		Jade_hp = Jade_hp + 100
		print('Jade uses Spray Perfume and recovers 100 HP. ')
	elif player_move == 4:
		crackhead_hp = crackhead_hp - 20
		print('Jade uses Bite and deals 20 HP. ')
	elif player_move == 5:
		capture_roll = random.randint(0,170)
		if capture_roll > crackhead_hp:
			print('You have captured Crackhead.')
			break 
		else:
			print('You have tried to capture Crackhead but failed')
	
	elif player_move == 6:
		runaway = random.randint(0,150)
		if runaway > Jade_hp:
			print('You ran away.')
			break 
		else:
			print('You have tried to run way but failed')


	time.sleep(0.5)
	print()

	#enemy battle choice
	enemy_move = random.randint(1,2)
	if enemy_move == 1:
		Jade_hp = Jade_hp - 30
		print('Crackhead uses Slap and deals 30 HP of damage. ')
	elif enemy_move == 2:
		Jade_hp = Jade_hp - 20
		crackhead_hp = crackhead_hp + 10
		print('Crackhead uses Scream and deals 20 HP of damage while also recovering 10 HP of health. ')
	time.sleep(0.5)
	print()

	if Jade_hp < 0:
		Jade_hp = 0
	if crackhead_hp < 0:
		crackhead_hp = 0

	print('Updated HP: ')
	print('Jade HP: ' + str(Jade_hp))
	print('Crackhead HP: ' + str(crackhead_hp))
	time.sleep(0.5)
	print()
if Jade_hp > 0 and crackhead_hp == 0:
	print('Wild Crackhead has fainted. Jade wins!')
if Jade_hp == 0 and crackhead_hp > 0:
	print('You have no remaining Bratz Doll, you lose.')



