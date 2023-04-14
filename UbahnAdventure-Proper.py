print("Berlin Subway Expat Adventure.\nCopyright Maciej Ruminkiewicz.\n4 April 2023.")
print("\n")
print('   Welcome to "Berlin Subway Expat Adventure" text adventure game!\n')
print("HOW TO PLAY:\n1. You will be given a prompt that looks like this:\n\nType '...' to ... .\n->\n\n2. Write whatever command is within ' ' without typing the apostrophes!\n3. For example:\n\nType 'word' to see the example.\n\n-> word")
print("\n")
print("Now let's give it a try.\n")
input("Type 'next' to begin the game.\n\n->")
print("\n")

#Chapter 0
print("   Chapter 0: Intro\n")
print("   You have enough of Berlin. You don't have rich parents. You've already terminated your apartment. With the last money you had, you've booked a plane to your homeland. You just need to catch your train at Hauptbahnhof to escape Berlin. But there's one task left for you.\n   You must reach Hauptbahnhof by U-Bahn. And you're still in Neukoelln...\n   Good luck!\n")
next = input("Type anything to proceed to Chapter 1.\n\n->")
print("\n")

#Chapter 1
print("   Chapter 1: Hermannstrasse\n")

print("   You start here. You have only 20 euro in cash with you. Nobody accepts card payments in Berlin. Spend your money wisely.\n   Before you begin your journey, you need a ticket.\n")
euro = int(20)

print("The ticket costs 3 euros. Will you buy the ticket?")
ticket = input("Type 'buy' to buy the ticket.\nType anything to ride without the ticket.\n\n->")
print("\n")
if ticket == str("buy"):
	euro = euro - 3
	print(f"   You've bought and validated the ticket.\n\nYou have {euro} euros left.\n")
	ticket_valid = bool(True)
else:
	print(f"   You've decided to take the risk and ride without the ticket.\n\nYou have {euro} euros left.\n")
	ticket_valid = bool(False)

next = input("Type anything to proceed to Chapter 2.\n\n->")
print("\n")

#Chapter 2
print("   Chapter 2: Leinestrasse\n")

print('   Your train stops here. A newspaper salesman enters. He pitches a paper titled "Arts of the Working Class." He looks unkempt. He is asking for a spare change.\n')

print("What would you like to do?")
newspaper = input("Type 'donate' to give the salesman 3 euros.\nType anything to ignore the salesman.\n\n->")
print("\n")
if newspaper == str("donate"):
	print("   You've given the salesman a spare change. In return you've received a copy of a newspaper.\n   You read a story about an artist taping a screwdriver to a classical painting on exhibition in Humboldtforum. Author of the story gives praise to such an act of pretentious vandalism.\n")
	euro = euro - 3
	print(f"You have {euro} euros left.\n")
else:
	print("   You continue your journey.\n")
	print(f"You have {euro} euros left.\n")

next = input("Type anything to proceed to Chapter 3.\n\n->")
print("\n")

#Chapter 3
print("   Chapter 3: Boddinstrasse\n")

print("   Here, a group of barbecue enthusiasts from Tempelhofer Feld enter the train. They start making sausages inside. You realize that you feel hungry.\n")

print("What would you like to do?")
BBQ = input("Type anything to join the barbeque.\nType 'extinguish' to put out the barbeque.\n\n->")
print("\n")
if BBQ == str("extinguish"):
	print("   You save the train from catching fire.\n")
else:
	print("   The smoke builds up and suffocates everyone due to the lack of air conditioning.\n\nGAME OVER!")
	quit()

next = input("Type anything to proceed to Chapter 4.\n\n->")
print("\n")

#Chapter 4
print("   Chapter 4: Hermannplatz\n")

print("   A lot of people enter here. The train is packed. You are lucky to have a sitting spot, since you're travelling from the beginning of the line.\n   An old German lady is standing by.\n")

print("What yould you like to do?")
lady = input("Type 'give' to give up your seat for the old lady.\nType anything to stay in your spot, forcing the lady to stand.\n\n->")
print("\n")
if lady == str("give"):
	print("   You let the old lady take your seat. She doesn't even say thank you.\n   Now, you have to stand up with all your heavy baggage. You faint because of a lack of oxygen.\n\nGAME OVER!")
	quit()
else:
	print("   You stay in your place. You have a long trip ahead of you.\n   The lady gets out on the next station anyway.\n")

next = input("Type anything to proceed to Chapter 5.\n\n->")
print("\n")

#Chapter 5
print("   Chapter 5: Schoenleinstrasse\n")

print("   A junkie enters the train. He's walking around collecting spare change.\n")

print("What would you like to do?")
junkie = input("Type 'donate' to give junkie the 2 euros.\nType 'judge' to give the junkie a clear judgmental look.\nType anything to ignore the junkie.\n\n->")
print("\n")
if junkie == str("donate"):
	print("   You've given a junkie some spare change. He collects more money and gets out on the next station.\n   You see him there buying drugs with the money you've just given him.\n")
	euro = euro - 2
	print(f"You have {euro} euros left.\n")
elif junkie == str("judge"):
	print("   You are eyeing the junkie from heads to toes. He catches on your judgmental vibe and becomes aggressive. He starts shouting and getting frenzy. He beats you to pulp.\n\nGAME OVER!")
	quit()
else:
	print(f"   You ignore the junkie and he goes on with his business. He gets out on the next station, and you see him buy the drugs with the money he's got from other passengers.\n\nYou have {euro} euros left.\n")
	
next = input("Type anything to proceed to Chapter 6.\n\n->")
print("\n")

#Chapter 6
print("   Chapter 6: Kottbusser Tor\n")

print("   A beggar enters the train. She carries a picture of her supposed children.\n")

print("What would you like to do?")
beggar = input("Type 'donate' to give 2 euros to the beggar.\nType anything to ignore the beggar.\n\n->")
print("\n")
if beggar == str("donate"):
	print("   You've given lady the 2 euros. She goes on and collects more money. She gets out on the next station.\n   You see her drop her head cloth and losing the hunchback. She reveals to be a male conman.\n")
	euro = euro - 2
	print(f"You have {euro} euros left.\n")
else:
	print(f"   The beggar goes on and collects more money. She gets out on the next station.\n   You see her drop her head cloth and losing the hunchback. She reveals to be a male conman.\n\nYou have {euro} euros left.\n")
	
next = input("Type anything to proceed to Chapter 7.\n\n->")
print("\n")

#Chapter 7
print("   Chapter 7: Moritzplatz\n")

print("   A ticket control officer is entering the train. He's checking the tickets.\n")

print("It's your turn.\n")

next = input("Type anything to have your ticket checked.\n\n->")
print("\n")
if ticket_valid == True:
	print("   Luckily, you've bought your ticket. You may continue your journey.\n")
if ticket_valid == False:
	print("   You're screwed. You didn't buy the ticket. The ticket control officer is asking you to leave the train. He gives you a 160 euro fine.\n\nGAME OVER!")
	quit()
	
next = input("Type anything to proceed to Chapter 8.\n\n->")
print("\n")

#Chapter 8
print("   Chapter 8: Heinrich-Heine-Strasse\n")

print("   A group of black clothed ravers from KitKat enter the train. One of them pulls out a loudspeaker and plays techno.\n")

print("You are feeling the beat. What would you like to do?")
techno = input("Type 'dance' to do a last dance before you leave Berlin for good.\nType anything to let it go.\n\n->")
print("\n")
if techno == str("dance"):
	print("   You dance like a freak. The ravers dig your vibe and invite you to the afterparty.\n")
	print("Would you like to join?")
	afterparty = input("Type 'yes' to join the afterparty.\nType anything to stay boring and continue your journey.\n\n->")
	print("\n")
	if afterparty == str("yes"):
		print("   You come to the afterparty where drugs and frivolous sex encounters are involved. You decide to stay in Berlin after all.\n   Unfortunately, you become addicted to drugs and you turn homeless.\n\nGAME OVER!")
		quit()
	else:
		print("   You politely decline, and exchange your instagrams instead. You continue your journey.\n")
else:
	print("   You've decided to give up on the fun and instead, you responsibly focus on completing your journey.\n")

next = input("Type anything to proceed to Chapter 9.\n\n->")
print("\n")

#Chapter 9
print("   Chapter 9: Jannowitzbruecke\n")

print("   Here, you have a chance to switch to S-Bahn, as it goes in parallel to the U-Bahn you are currently taking. Either way you choose, your next station will be Alexanderplatz, where you have to transfer to the lane U5.\n")

print("What would you like to do?")
bahn = input("Type 'sbahn' to switch to S-Bahn.\nType anything to stay in U-Bahn.\n\n->")
print("\n")
if bahn == str("sbahn"):
	print("   You've switched to the S-Bahn and you are now travelling on a surface. As it is exceptionally sunny day today, you are getting extra vitamine D, which is boosting your mood.\n   You see the city you are about to leave forever. It looks pretty in the sun.\n   You are having second thoughts about leaving Berlin.\n")
else:
	print("   You continue your journey and nothing changes for you.")
print("\n")

next = input("Type anything to proceed to Chapter 10.\n\n->")
print("\n")

#Chapter 10
print("   Chapter 10: Alexanderplatz\n")

if bahn == str("sbahn"):
	print("   You have arrived at your transfer station. The sun is having a good effect on you.\n")

	print("You need to make a decision.")
	decision = input("Type 'leave' to leave the station and go to the city.\nType anything to stay at the station and move back underground to catch your next train.\n\n->")
	print("\n")
	if decision == str("leave"):
		print("   You've left the station and went under the TV tower. You are enjoying the sun and everybody around has a good vibe.\n   Maybe Berlin isn't such a terrible place after all?\n   You decide to stay and try to make your life in Berlin work for you. You cancel your flight and call your friend to let you crash at their place before you can find a new apartment.\n\nCONGRATULATIONS!\nYou've finished the game.\nYou've reached the INSPIRED ENDING.")
		quit()
	else:
		print("   You've decided to continue your journey.\n")
		print("   You've arrived at your transfer station.\n   This is Alexanderplatz.\n   It is a labirynth.\n   You have to find the lane U5 to Hauptbahnhof.\n   Good luck!\n")
else:
	print("   You've arrived at your transfer station.\n   This is Alexanderplatz.\n   It is a labirynth.\n   You have to find the lane U5 to Hauptbahnhof.\n   Good luck!\n")
	
next = input("Type anything to begin Alexanderplatz mini game.\n\n->")
print("\n")

#Alexanderplatz

#Step 1
print("You are currently here:")
print(" ____________________________ \n|                            |\n|     _______________        |\n|    |  U5 ------->  |       |\n|     ---------------        |\n|       ||       ||          |\n|_______||_______||__________|\n|       ||       ||          |\n|____________________________|")
print("\n")
print("Where would you want to go?")
navigate = input("Type 'left' to go left.\nType 'right' to go right.\n\n->")
print("\n")

if navigate == str("left"):
	print("   You've turned towards the U-Bahn security post. They haven't got the memo that Covid-19 restrictions are over. They arrest you for not wearing a facemask.\n\nGAME OVER!")
	quit()

#Step 2
elif navigate == str("right"):
	print("You are currently here:")
	print(" ____________________________ \n|    | |          | |        |\n|_   | |          | |   _____|\n| |  | |__________| |  |     |\n| |  | |::::::::::| |  |     |\n| |  | |::::::::::| |  |     |\n| |__| |::::::::::| |__|     |\n| /  |_|::::::::::|_|  \     |\n|/______________________\____|")
	print("\n")
	print("Where would you want to go?")
	navigate = input("Type 'up' to go upstairs.\nType 'back' to turn around.\n\n->")
	print("\n")
	
	if navigate == str("back"):
		print("   You've turned towards the U-Bahn security post. They haven't got the memo that Covid-19 restrictions are over. They arrest you for not wearing a facemask.\n\nGAME OVER!")
		quit()
	
#Step 3: Kebab, WC, U2, U5
	elif navigate == str("up"):
		print("You are currently here:")
		print(" ____________________________ \n|                            |\n|  ________________________  |\n| | <--- U2 ,,, Kebab ---> | |\n| | <--- U5 ''' WC ------> | |\n|  ------------------------  |\n|     ||              ||     |\n|     ||              ||     |\n|_____||______________||_____|")
		print("\n")
		print("Where would you want to go?")
		navigate = input("Type 'left' to go left.\nType 'right' to go right.\n\n->")
		print("\n")
		if navigate == str("right"):
			print("   You decide to get a kebab. You've been hungry since Boddinstrasse.")
			print("\n")
			print(f"Kebab costs 10 euros. You have {euro} euros left.")
			kebab = input("Type 'buy' to buy a kebab'.\nType anything to stay hungry.\n\n->")
			print("\n")
			if kebab == str("buy"):
				euro = euro - 10
				print("   You've just finished eating a kebab. It was lecker. Suddenly, you start feeling your bowels. You have to take a shit.\n   Luckily, there's a toiled right up ahead.")
				print("\n")
				print("The toilet costs 1 euro to use.")
				WC = input("Type anything to use the toilet.\n\n->")
				print("\n")
				#if WC == str("use"):
				euro = euro - 1
				if euro >= 0:
					print("   You've used the toilet and feel 5 kg lighter. You can now run downstairs to catch your U5.\n")
				if euro < 0:
					print("   You've ran out of money and are unable to use the toilet. You shit your pants in front of everybody. You are in deep in shame.\n\nGAME OVER!")
					quit()
			else:
				print("   You've fainted out of hunger.\n\nGAME OVER!")
				quit()
		
#Step 4 U2, U5
		elif navigate == str("left"):
			print("You are currently here:")
			print(" ____________________________ \n|     |  |          |        |\n|     |  |__________|   /\   |\n|     |  |::::::::::|   ||   |\n|     |  |::::::::::|   U2   |\n|_____|__|::::::::::|   U5   |\n|                   |   ||   |\n|                   |   \/   |\n|___________________|________|")
			print("\n")
			print("Where would you want to go?")
			navigate = input("Type 'up' to go upstairs.\nType 'down' to go downstairs.\n\n->")
			print("\n")
			if navigate == str("up"):
				print("   You've gone upstairs. You board a U2 train to Pankow.\n   You realize it's a wrong train. You switch at the next stop to go back to Alexanderplatz.\n   At Alexanderplatz, you find out that the U5 train to Hauptbahnhof has been cancelled due to an incident at Rotes Rathaus.\n   You are unable to reach Hauptbahnhof on time.\n\nGAME OVER!")
				quit()
			elif navigate == str("down"):
				print("   You've gone downstairs. You board a U5 train to Hauptbahnhof.\n   You continue your journey.")
				print("\n")

			else:
				print("   You've been loitering around for too long. You've missed your train at Hauptbahnhof.\n\nGAME OVER!")
				quit()
	
		else:
			print("   You've been loitering around for too long. You've missed your train at Hauptbahnhof.\n\nGAME OVER!")
			quit()
	
	else:
		print("   You've been loitering around for too long. You've missed your train at Hauptbahnhof.\n\nGAME OVER!")
		quit()
			
else:
	print("   You've been loitering around for too long. You've missed your train at Hauptbahnhof.\n\nGAME OVER!")
	quit()

next = input("Type anything to proceed to Chapter 11.\n\n->")
print("\n")

#Chapter 11
print("   Chapter 11: Rotes Rathaus\n")

print("   Your train arrives here. The doors open and passengers get out.\n   Suddenly, a large fish tank at a nearby SeaLife hotel has just exploded. Water is flooding the subway station.\n")

print("Something needs to be done!")
doors = input("Type 'close' to close the doors.\nType anything to do nothing.\n\n->")
print("\n")
if doors == str("close"):
	print("   The doors close and everybody is safe. You continue the journey.\n")
else:
	print("   The water enters your train and quickly overflows. Everybody drowns.\n\nGAME OVER!")
	quit()
	
next = input("Type anything to proceed to Chapter 12.\n\n->")
print("\n")

#Chapter 12
print("   Chapter 12: Museumsinsel\n")

print("   A lot of tourists enter here. They are maniacally taking photos of every element of the U-Bahn.\n")

print("What would you like to do?")
GDPR = input("Type 'datenschutz' to quote privacy protection laws.\nType 'pose' to pose for a photo.\nType anything to do nothing.\n\n->")
print("\n")
if GDPR == str("datenschutz"):
	print("   The tourists think you are being weird and they don't take you seriously. You call the police.\n")
	
	print("Choose the difficulty level:")
	difficulty = input("Type 'easy' if you speak German.\nType 'hard' if you don't speak German.\n\n->")
	print("\n")
	if difficulty == str("easy"):
		print("   You call the police and manage to make the tourists pay the fine for breaking the GDPR and infringing on your and other passengers' privacy.\n   Maybe you belong to Germany after all?\n")
	elif difficulty == str("hard"):
		print('   You call the police and try speaking English with them. Police does not understand you. You make a fool out of yourself.\n   To add more insult to the injury, one of the tourists snap a photo of you. They post it to their Instagram, captioning it:\n   "A typical strict rule obedient German calling the police when everybody else tries to only exercise their freedom."\n')
	else:
		print("   A police officer answers the phone. You say nothing. At the next station you get arrested for wrongful use of the emergency line.\n\nGAME OVER!")
		quit()
elif GDPR == str("pose"):
	print('   You pretend to the naive tourist to be a true Berliner. You charge 20 euro for a photo of you for a "unique Berlin experience."\n')
	euro = euro + 20
	print(f"You have {euro} euros left.\n")
else:
	print("   You simply continue your journey.\n")

next = input("Type anything to proceed to Chapter 13.\n\n->")
print("\n")

#Chapter 13
print("   Chapter 13: Unter den Linden\n")

print("   Posh businessmen and ambassadors enter here. Next to you stands a lady in a Gucci furcoat. She has a chihuaua dog. The dog is barking at you.\n")

print("The dog is annoying you. Will you do something about it?")
dog = input("Type 'water' to pour water on the dog.\nType anything to do nothing.\n\n->")
print("\n")
if dog == str("water"):
	print("   The dog goes quiet but the owner does otherwise. She's accusing you of an assault on her dog.\n   She demands compensation for her a dog hairdresser.\n")
	compensation = input("Type 'compensate' to pay 35 euro for a hairdresser.\nType '#eattherich' [with hashtag] to disobey the rich.\n\n->")
	print("\n")
	if compensation == str("compensate"):
		euro = euro - 35
		if euro >= 0:
			print("   You've paid the lady 35 euro and she lets you off the hook. You continue your journey in peace.\n")
			print(f"You have {euro} euros left.\n")
		if euro < 0:
			print("   You don't have enough money to pay the lady off.\n\nGAME OVER!")
			quit()
	elif compensation == str("#eattherich"):
		print('   You tell the lady to f**k off. Upon your rebellion, the lady calls the police and has you arrested for, as she claims, "animal cruelty."\n\nGAME OVER!')
		quit()
	else:
		print("   You've just remained calm. The lady looked you up and down and realized you are too poor for her to even bother. She has ignored you.\n   At least you've gotten away with the dog!\n\nACHIEVEMENT UNLOCKED: Dog Pisser\n")
else:
	print("   You've decided to let it go and suffer in silence.\n")

next = input("Type anything to proceed to Chapter 14.\n\n->")
print("\n")

#Chapter 14
print("   Chapter 14: Brandenburger Tor\n")

print("   Here, you have a last chance to take a selfie at the Brandenburg Gate.\n")

print("Would you like to take a selfie?")
selfie = input("Type 'selfie' to take a selfie.\nType anything to continue your journey without a selfie.\n\n->")
print("\n")
if selfie == str("selfie"):
	print("   You've quickly went out on the surface and took a selfie:")
	print("\n")
	print(" ____________________________ \n|         __________         |\n|   _____/          \_____   |\n|  |   __     __     __   |  |\n|  |  |  |   |  |   |  |  |  |\n|  |  |  |    __    |  |  |  |\n| _|  |__|   (OO)   |__|  |_ |\n|/ |__|  |__ /||\ __|  |__| \|\n|_____________/\_____________|")
	print("\n")
else:
	print("   You don't care and you continue your journey.\n")

next = input("Type anything to proceed to Chapter 15.\n\n->")
print("\n")

#Chapter 15
print("   Chapter 15: Bundestag\n")

print("   This is the last station before your destination. You are almost there. There's one more challenge to overcome.\n   You have to beat The Ghost of Angela Merkel and Her Disciples of Beaurocracy. Good luck!\n")

print("You have 100 sanity points left.\n")

input("Type 'fight' to begin your final boss fight.\n\n->")
print("\n")

#Attack 1:
print("   Angela throws Anmeldung Attack at you. It may deal 20 points of damage.\n")

print("What's your defense?")
defense = input("Type anything to idle.\nType 'unmeldung' to de-register from Germany.\n\n->")
print("\n")
if defense == str("unmeldung"):
	print("You successfully de-register yourself from Germany!\n")
	damage1 = bool(False)
else:
	print("You receive 20 points of damage!")
	print("You have 80 sanity points left.\n")
	damage1 = bool(True)

#Attack 2:
print("   Angela throws Gaslighting Attack at you. It may deal 60 points of damage.\n")

#Video
print("What's your defense?")
defense = input("Type anything to idle.\nType 'video' to provide a video proof.\n\n->")
print("\n")
if defense == str("video"):
	damage2 = bool(False)
	print("   Angela uses Datenschutz as her counter attack. It voids the video use in court even if it incriminates the abuser.\n   The reason: The abuser did not consent to be recorded.\n   Angela's counter attack may deal 40 points of damage.\n")

	#Transcript
	print("What's your defense?")
	defense = input("Type anything to idle.\nType 'transcript' to write a transcript of the video.\n\n->")
	print("\n")
	if defense == str("transcript"):
		print("   The transcript can be legally used for your defense.\n")
		damage_transcript = bool(False)
		
		#Delivery
		print("How would you like to deliver your transcript?")
		transcript = input("Type 'email' to send your transcript via e-mail.\nType 'post' to print your transcript and send it by postal service.\n\n->")
		print("\n")
		if transcript == str("email"):
			print("   The transcript sent electronically has been ineffective.\n   The reason: lack of modernization of government's electronic systems.\n")
			print("You receive 40 points of damage!")
			if damage1 == True:
				print("You have 40 sanity points left.\n")
			if damage1 == False:
				print("You have 60 sanity points left.\n")
			damage_delivery = bool(True)
			damage2 = bool(False)
		elif transcript == str("post"):
			print("   The transcript on paper has been effective. So much for forest protection...")
			damage_delivery = bool(False)
		else:
			print("   You insist on using the video as the proof, as it clearly proves who's at fault. You receive 2000 euro fine for breaking the German Datenschutz regulation.\n\nGAME OVER!")
			quit()
		#damage2 = bool(False)
		print("\n")
	else:
		print("You receive 40 points of damage!")
		if damage1 == True:
			print("You have 40 sanity points left.\n")
		if damage1 == False:
			print("You have 60 sanity points left.\n")
		damage_transcript = bool(True)

else:
	print("You receive 60 points of damage!")
	if damage1 == True:
		print("MENTAL HEALTH CRITICAL! You have 20 sanity points left.\n")
	if damage1 == False:
		print("You have 40 sanity points left.\n")
	damage2 = bool(True)
	
#Attack 3:
print("   Angela throws Mandatory Health Insurance Attack at you. It may deal 20 points of damage.\n")

print("You've terminated your work contract and are now required to pay next month's contribution out of your pocket. What's your defense?")
defense = input("Type 'pay' to pay 300 euro for the insurance.\nType anything to provide a proof of insurance abroad.\n\n->")
print("\n")
if defense == str("pay"):
	print("   You are out of funds to cover your insurance.\n")
	print("You receive 20 points of damage!")
	if damage1 == True:
		if damage2 == True:
			print("MENTAL HEALTH DEPLETED!\n\nGAME OVER!")
			quit()
		if damage2 == False:
			if damage_transcript == True:
				print("MENTAL HEALTH CRITICAL! You have 20 sanity points left.\n")
			if damage_transcript == False:
				if damage_delivery == True:
					print("MENTAL HEALTH CRITICAL! You have 20 sanity points left.\n")
				if damage_delivery == False:
					print("You have 60 sanity points left.\n")
			damage3 = bool(True)
	if damage1 == False:
		if damage2 == True:
			print("MENTAL HEALTH CRITICAL! You have 20 sanity points left.\n")
		if damage2 == False:
			if damage_transcript == True:
				print("You have 40 sanity points left.\n")
			if damage_transcript == False:
				if damage_delivery == True:
					print("You have 40 sanity points left.\n")
				if damage_delivery == False:
					print("You have 80 sanity points left.\n")
else:
	print("   Proof of insurance abroad has successfully unsubscribed you from the German health insurance.\n")
	
print("   You've successfully beaten the Ghost of Angela Merkel and her Disciples of Beaurocracy!\n")

next = input("Type anything to proceed to the final chapter.\n\n->")
print("\n")

#Chapter 16
print("   Chapter 16: Hauptbahnhof\n")

print("   Congratulations, you've made it!\n   You're now about to leave Berlin once and for all. You board your outbound train and ride into the sunset. Godspeed on your future endeavours!")
print("\n")
print("   Thank you for playing Berlin Subway Expat Adventure!")
quit()
