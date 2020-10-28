import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
import time
import random
import pickle
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix = "b!")

global Quotes
Quotes = []

global BadQuotes
BadQuotes = []

global Pokemons
Pokemons = dict.fromkeys({})

global snomekoP
snomekoP = dict.fromkeys({})

global SWSHMons
SWSHMons = [4,5,6,10,11,12,25,26,35,36,37,38,43,44,45,50,51,52,
53,58,59,66,67,68,77,78,83,90,91,92,93,94,95,98,99,106,107,109,
110,111,112,118,119,122,129,130,131,132,133,134,135,136,143,151,
163,164,170,171,172,173,175,176,177,178,182,185,194,195,196,197,
202,208,211,213,215,220,221,222,223,224,225,226,236,237,246,247,
248,263,264,270,273,274,275,278,279,280,281,281,282,282,290,291,
292,302,303,309,310,315,320,321,324,328,329,330,334,337,338,339,
340,341,342,343,349,350,355,356,360,361,362,406,415,416,420,421,
422,423,425,426,434,435,436,437,438,439,446,447,448,449,450,451,
452,453,454,458,459,460,461,464,468,470,471,473,475,477,478,479,
497,509,510,517,519,520,521,524,525,526,527,528,529,530,532,533,
534,535,536,537,538,539,546,547,550,554,555,556,557,558,559,560,
561,562,563,568,569,572,573,574,575,576,577,578,579,582,583,584,
588,589,592,593,595,596,597,598,599,600,604,605,606,607,608,609,
610,611,612,613,614,616,617,618,622,623,624,625,627,628,629,630,
631,632,633,634,635,659,660,674,675,677,678,679,680,681,682,683,
684,685,686,687,688,689,694,695,700,701,704,705,706,708,709,710,
711,712,713,714,715,736,737,738,742,743,746,747,748,749,750,751,
752,755,756,757,758,759,760,761,762,763,765,766,767,768,771,772,
773,776,777,778,780,781,782,783,784] + list(range(810,891))

with open("LegendaryQuotes", "rb") as in_file:
    Quotes = pickle.load(in_file)

with open("BadjasQuotes", "rb") as in_bad:
    BadQuotes = pickle.load(in_bad)

global MarkWoord
MarkWoord = ["Lam", "Lul", "Staats", "Mongool", "Brood"]

global Cards
Cards = dict.fromkeys({})

with open("CardCounter", "rb") as in_cards:
    Cards = pickle.load(in_cards)

global Traps
Traps = ["trap.jpg", "trap2.jpg", "trap3.jpg", "trap4.jpg", "trap5.png", "trap7.jpg", "trap8.png"]

global S
S = ["s1.jpg", "s2.jpg", "s3.jpg", "s4.jpg", "s5.jpg", "s6.jpg", "s7.png"]

global Season
Season = ["season1.jpg", "season2.jpg", "season3.jpg", "season4.jpg"]

global Doto
Doto = ["Doto.png", "Doto2.png"]

global Loli
Loli = ["loli1.png", "loli2.png", "loli3.jpg", "loli4.jpg", "loli5.jpg", "loli6.png", "loli7.png", "loli8.png", "loli9.jpg", "loli10.jpg", "loli11.jpg", "loli12.png", "loli13.jpg", "loli14.png", "loli15.jpg", "loli16.jpg", "loli17.jpg", "loli18.jpg"]

global Alfrado
Alfrado = ["Alfrado btw", "Beam btw", "League is for babies btw", "pet btw"]

global Nou
Nou = ["nou1.png", "nou2.png", "nou3.jpeg", "nou4.png", "nou5.jpg", "nou6.png", "nou7.jpg", "nou8.png"]

@tasks.loop(seconds=5.0)
async def Loop():
    date = datetime.datetime(2019, 11, 14, 23)
    newdate = date - datetime.datetime.now()
    hours, remainder = divmod(newdate.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    streamname = '%02d:%02d:%02d' % (int(hours), int(minutes), int(seconds))
    stream = discord.Streaming(name=streamname, url="https://twitch.tv/Batsphemy")
    await client.change_presence(activity=stream)

@client.event
async def on_ready():
    print("BatBot rolling out!")
    Loop.start()
    stream = discord.Streaming(name="Female dog, black guy, cool", url="https://twitch.tv/Batsphemy")
    await client.change_presence(activity=stream)
    loadPokemons()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "JEFF" in message.content.upper() or "<@143799702289121280>" in message.content.upper() or "<@!143799702289121280>" in message.content.upper():
        await message.add_reaction("🍆")

    if "<@!260843280361586688>" in message.content or "<@260843280361586688>" in message.content:
        await message.channel.send(file=discord.File("hyperpinged.png"))

    if message.content.upper() == "EL PSY CONGROO":
        print("Mayushii-des!")
        await message.channel.send(file=discord.File("congroo.jpg"))

    if message.content.upper() == "TUTURUU" or message.content.upper() == "TUTURU":
        await message.channel.send(file=discord.File("mayushii.jpeg"))

    if message.content.upper() == "TRAP" or message.content.upper() == "ITS A TRAP" or message.content.upper() == "IT'S A TRAP":
        await message.channel.send(file=discord.File(random.choice(Traps)))

    if message.content.upper() == "AYY":
        await message.channel.send("Lmao")

    if message.content.upper() == "OMEGALOLI":
        await message.channel.send(file=discord.File("baconz.png"))

    if message.content.upper() == "KAMEHAME":
        await message.channel.send("HAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!")

    if message.content.upper() == "NOBULLY":
        await message.channel.send(file=discord.File("nobully.gif"))

    if message.content.upper() == "NONOBULLY":
        await message.channel.send(file=discord.File("nonobully.jpg"))

    if message.content.upper() == "OMAE WA MOU SHINDEIRU":
        await message.channel.send(file=discord.File("Nani.gif"))

    if message.content.upper() == "SMILE" or message.content.upper() == "SWEET" or message.content.upper() == "SISTER" or message.content.upper() == "SADISTIC" or message.content.upper() == "SURPRISE":
        await message.channel.send(file=discord.File(random.choice(S)))

    if message.content.upper() == "SERVICE":
        await message.channel.send(file=discord.File(S[6]))

    if message.content.upper() == "NARUTO" or message.content.upper() == "NARUTOO" or message.content.upper() == "NARUTOOO":
        await message.channel.send(file=discord.File("sasuke.gif"))

    if message.content.upper() == "NEED SECOND SEASON":
        await message.channel.send(file=discord.File(random.choice(Season)))

    if message.content.upper() == "ALFRADO" or message.content.upper() == "ALF":
        await message.channel.send(file=discord.File(random.choice(Alfrado)))

    if message.content.upper() == "STACKERS?":
        await message.channel.send(file=discord.File(random.choice(Doto)))

    if message.content.upper() == "BAKA":
        await message.channel.send(file=discord.File("baka.jpg"))

    if message.content.upper() == "SPOILERS":
        await message.send("Spoilers ain't cool bruh")

    if message.content.upper() == "B!STATUS":
        await message.send("I'm healthy and alive, cuz Mr Bat feeds me Lolis for breakfast!")

    if message.content.upper().startswith("UR MOM") or message.content.upper().startswith("YOUR MOM") or message.content.upper().startswith("UR MUM") or message.content.upper().startswith("YOUR MUM"):
        await message.send("LMAOOO!!")

    if message.content.upper().startswith("I CHOOSE YOU"):
        if message.content.upper().startswith("I CHOOSE YOU, SANDSLASH"):
            await message.channel.send(file=discord.File("Pokémon Sprites/" + "28.png"))
        elif message.content.upper().startswith("I CHOOSE YOU, LORD HELIX"):
            await message.channel.send(file=discord.File("Pokémon Sprites/" + "139.png"))
        elif message.content.upper() == "I CHOOSE YOU <@!419266806264496138>" or message.content.upper() == "I CHOOSE YOU <@419266806264496138>":
            await message.channel.send(file=discord.File("Diancie.png"))
        else:
            print(message.content)
            await message.channel.send(file=discord.File("Pokémon Sprites/" + str(random.randint(1, 386)) + ".png"))

    if message.content.upper() == "B!TOPTEN":
        msg = ""
        msg += "1. Madoka Magica \n"
        msg += "2. Steins;Gate\n"
        msg += "3. Another\n"
        msg += "4. Mirai Nikki\n"
        msg += "5. Fate/Stay Night UBW\n"
        msg += "6. Gakkou Gurashi\n"
        msg += "7. No Game No Life\n"
        msg += "8. Yuru Yuri\n"
        msg += "9. Angel Beats\n"
        msg += "10. UMAMUSUME: PRETTY DERBY REEEEEEEE"
        await message.channel.send(msg)

    if message.content.upper() == "KILL ME":
        print("Kill me!")
        await message.channel.send(file=discord.File("killme.png"))

    if message.content.upper() == "TIJD TOT POKEMON":
        date = datetime.datetime(2019, 11, 14, 23)
        print(date - datetime.datetime.now())
        await message.channel.send(date - datetime.datetime.now())

    if message.content.upper() == "ZEG MAKKER":
        await message.send("Kokosnoten zijn geen specerijen")


    if message.content.upper() == "LOLI":
        await message.channel.send(file=discord.File(random.choice(Loli)))

    if message.content.upper() == "MIKE SMELLS":
        await message.send("Agreed!")

    if message.content.upper() == "NICE PET":
        await message.channel.send(file=discord.File("aodpet.jpg"))

    if message.content.upper() == "NOU" or message.content.upper() == "NO U":
        await message.channel.send(file=discord.File(random.choice(Nou)))


    args = message.content.split(" ")

    if message.content.upper().startswith("IS HET TIJD VOOR "):
        antwoord = ["Ja", "Nee"]

        a = random.choice(antwoord)
        thingy = " ".join(args[4:])

        if thingy.endswith("?"):
            thingy = thingy[:len(thingy)-1]

        if a == "Ja":
            await message.send("Ja, het is tijd voor " + thingy)
        if a == "Nee":
            await message.channel.send("Nee, het is geen tijd voor " + thingy)

    if args[0].upper() == "B!GIVECARD":

        member = client.get_guild("260825828122689537").get_member(message.author.id)

        if member == None:
            return False

        roles = []
        for role in member.roles:
            roles.append(role.name)

        if "Referee" not in roles:
            await message.channel.send("You need to be a referee to hand out cards.")
        else:
            rec = args[1]
            card = args[2].upper()

            if card != "RED" and card != "YELLOW":
                print(card)
                await message.channel.send("Cards can only be yellow or red.")
            else:
                if rec not in Cards:
                    if card == "RED":
                        c = [0, 1]
                    else:
                        c = [1, 0]
                    Cards[rec] = c
                else:
                    if card == "RED":
                        Cards[rec][1] += 1
                    else:
                        Cards[rec][0] += 1
                with open("CardCounter", "wb") as out_cards:
                    pickle.dump(Cards, out_cards)
                await message.channel.send(rec + " has received a " + ("red" if card == "RED" else "yellow") + " card. Their total count is: " + str(Cards[rec][0]) + " yellow cards and " + str(Cards[rec][1]) + " red cards.")

    if args[0].upper() == "B!MARKWOORD":
        mw = random.choice(MarkWoord) + random.choice(MarkWoord)
        await message.channel.send(mw)

    if args[0].upper() == "SANITY":
        if random.randint(0, 100) == 99:
            await message.channel.send("It's over 9000!!")
        else:
            await message.channel.send("Sanity level: " + str(random.randint(0, 100)))
    if message.content.upper() == "I REALLY REALLY REALLY LIKE THIS IMAGE":
        time.sleep(3)
        await message.channel.send("I like it too")

    if args[0].upper() == "ADDQUOTE" and message.author.id == 260843280361586688:
        quote = " ".join(args[1:])
        Quotes.append(quote)
        await message.add_reaction("👍")
        with open("LegendaryQuotes", "wb") as out_file:
            pickle.dump(Quotes, out_file)

    if args[0].upper() == "ADDBADJASQUOTE" and message.author.id == 260843280361586688:
        quote = " ".join(args[1:])
        BadQuotes.append(quote)
        await message.add_reaction("👍")
        with open("BadjasQuotes", "wb") as out_bad:
            pickle.dump(BadQuotes, out_bad)

    if args[0].upper() == "LEGENDARYQUOTE":
        await message.channel.send(random.choice(Quotes))

    if args[0].upper() == "BADJASQUOTE":
        await message.channel.send(random.choice(BadQuotes))

    if args[0].upper() == "ALLQUOTES" and message.author.id == "260843280361586688":
        i = 0
        for quote in Quotes:
            await message.channel.send(str(i) + ": " + quote)
            i += 1

    if args[0].upper() == "DELQUOTE" and message.author.id == "260843280361586688":
        await message.channel.send("Removed: " + Quotes.pop(int(args[1])))

    if args[0].upper() == "FANCIFY":
        try:
            def strip_non_ascii(string):
                """Returns the string without non ASCII characters."""
                stripped = (c for c in string if 0 < ord(c) < 127)
                return ''.join(stripped)
            text = " ".join(args[1:])
            text = strip_non_ascii(text)
            if len(text.strip()) < 1:
                return await self.client.say(":x: ASCII characters only please!")
            output = ""
            for letter in text:
                if 65 <= ord(letter) <= 90:
                    output += chr(ord(letter) + 119951)
                elif 97 <= ord(letter) <= 122:
                    output += chr(ord(letter) + 119919)
                elif letter == " ":
                    output += " "
            await message.channel.send(output)

        except:
            await message.channnel.send("Can't be done senpai :(")

    if args[0].upper() == "INSULT":
        if args[1] is not None:
            msg = await message.send(args[1] + " smells of farts!")
            time.sleep(5)
            await message.edit_message(msg, ":heart:" + args[1])

    if args[0].upper() == "B!ALLTRAPS":
        for v in Traps:
            await message.channel.send(fiel=discord.File(v))

    if args[0].upper() == "B!AS":

            aps = ((int(args[1]) + int(args[2])) * 0.01) * float(args[3])
            spa = 1/aps
            await message.channel.send("a/s: " + str(aps) + "\ns/a: " + str(spa))

            #await message.channel.send("Something went wrong :)")

    if args[0].upper() == "B!HELP":
        await message.channel.send("LOL you're beyond help my dude!")

    if args[0].upper() == "B!SHINY":
        pokemon = args[1].upper()
        sprite = ''
        spriteShiny = ''
        if pokemon in Pokemons:
            if int(Pokemons[pokemon]) in SWSHMons:
                spriteShiny = 'https://serebii.net/Shiny/SWSH/{}.png'.format(Pokemons[pokemon].zfill(3))
                sprite = 'https://serebii.net/swordshield/pokemon/{}.png'.format(Pokemons[pokemon].zfill(3))
            else:
                spriteShiny = 'https://serebii.net/Shiny/SM/{}.png'.format(Pokemons[pokemon].zfill(3))
                sprite = 'https://serebii.net/sunmoon/pokemon/{}.png'.format(Pokemons[pokemon].zfill(3))

            embed = discord.Embed(
            title = '{} Shiny Form'.format(args[1]),
            colour = discord.Colour(0xff69b4)
            )
            embed.set_thumbnail(url=sprite)
            embed.set_image(url=spriteShiny)

            await message.channel.send(embed=embed)

        else:
            await message.channel.send('{} not found.'.format(args[1]))

    if args[0].upper() == "B!NEXTTARGET":
        pokemonNumber = random.choice(SWSHMons)

        spriteShiny = 'https://serebii.net/Shiny/SWSH/{}.png'.format(str(pokemonNumber).zfill(3))
        sprite = 'https://serebii.net/swordshield/pokemon/{}.png'.format(str(pokemonNumber).zfill(3))

        embed = discord.Embed(
            title = '{}'.format(snomekoP[str(pokemonNumber)]),
            colour = discord.Colour(random.randint(0,16777215))
        )
        embed.set_thumbnail(url=sprite)
        embed.set_image(url=spriteShiny)

        await message.channel.send(embed=embed)

    if args[0].upper() == "B!SHINYODDS": #B!ShinyOdds [i]

        stackedodds = 1

        a = list(map(toUpper, args))
        if "CHARM" in a:
            stackedodds += 2
        if "MASUDA" in a and "EGG" in a:
            stackedodds += 5

        embed = discord.Embed(
            title = 'Shiny Odds',
            colour = discord.Colour(0x008b8b)
            )


        if "EGG" in a:
            onenoshiny = pow(4095/4096,stackedodds)
            noshiny = pow(onenoshiny, int(args[1])) * 100
            oneshiny = pow(onenoshiny, int(args[1]) - 1) * (1 - onenoshiny) * int(args[1]) * 100
            twoshiny = pow(onenoshiny, int(args[1]) - 2) * (1 - onenoshiny) * (1 - onenoshiny) * (int(args[1]) * int(args[1]) - int(args[1])) * 50
            embed.add_field(name='0 Shinies',  value = str(round(noshiny, 2)) + '%')
            embed.add_field(name='1 Shiny',    value = str(round(oneshiny, 2)) + '%')
            embed.add_field(name='2 Shinies',  value = str(round(twoshiny, 2)) + '%')
            embed.add_field(name='>2 Shinies', value = str(round(100 - noshiny - oneshiny - twoshiny)) + '%')
            embed.set_thumbnail(url='https://pngimage.net/wp-content/uploads/2018/06/pokemon-egg-png-2.png')

        else:
            noshinies = probabilityNone(int(args[1]), True if stackedodds == 3 else False) * 100
            oneshiny  = probabilityOnceAfter(int(args[1]), True if stackedodds == 3 else False) * 100
            embed.add_field(name='0 Shinies',  value = str(round(noshinies, 2)) + '%')
            embed.add_field(name='1 Shiny',    value = str(round(oneshiny, 2))  + '%')
            embed.add_field(name='>1 Shinies', value = str(round(100 - noshinies - oneshiny, 2)) + '%')
            embed.set_thumbnail(url='https://serebii.net/Shiny/SWSH/{}.png'.format(random.choice(SWSHMons)))

        embed.set_footer(text='Args: Egg for hatching, Charm for shiny Charm, Masuda for Masuda Method. Currently only works with breeding!')
        await message.channel.send(embed=embed)

def toUpper(n):
    if isinstance(n, str):
        return n.upper()
    else:
        return n

def loadPokemons():
    f = open("Pokemons.txt")
    for line in f:
        m = line.split(",")
        Pokemons[m[0].upper()] = m[1].strip()
        snomekoP[m[1].strip()] = m[0]
    f.close()

def partialProb(i, encounters, ABCDEF, abcdef):
    A,B,C,D,E,F = ABCDEF
    a,b,c,d,e,f = abcdef

    probability = (
        ((a*pow(A, min(1, a))*pow(1-A, max(0, a-1))) if i == 0 else pow(4095/4096, a)) *
        ((b*pow(B, min(1, b))*pow(1-B, max(0, b-1))) if i == 1 else pow(4094/4096, b)) *
        ((c*pow(C, min(1, c))*pow(1-C, max(0, c-1))) if i == 2  else pow(4093/4096, c)) *
        ((d*pow(D, min(1, d))*pow(1-D, max(0, d-1))) if i == 3  else pow(4092/4096, d)) *
        ((e*pow(E, min(1, e))*pow(1-E, max(0, e-1))) if i == 4  else pow(4091/4096, e)) *
        ((f*pow(F, min(1, f))*pow(1-F, max(0, f-1))) if i == 5  else pow(4090/4096, f))
    )

    return probability

def probabilityOnceAfter(encounters, charm):

    x = 0
    if charm: x = 2

    A = (1+x)/4096                  # prob000050
    B = (2+x)/4096                  # prob050100
    C = (3+x)/4096                  # prob100200
    D = (4+x)/4096                  # prob200300
    E = (5+x)/4096                  # prob300500
    F = (6+x)/4096                  # prob500nup

    ABCDEF = [A, B, C, D, E, F]

    n = encounters
    f = max(0, n-500)           # exp500nup
    e = max(0, n-f-300)         # exp300500
    d = max(0, n-f-e-200)       # exp200300
    c = max(0, n-f-e-d-100)     # exp100200
    b = max(0, n-f-e-d-c-50)    # exp050100
    a = n-f-e-d-c-b             # exp000050
    abcdef = [a, b, c, d, e, f]

    res = 0
    for i in range(6):
        if abcdef[i] > 0:
            res += partialProb(i, encounters, ABCDEF, abcdef)

    return res

def probabilityNone(encounters, charm):

    x = 0
    if charm: x = 2

    A = 1 - (1+x)/4096                  # prob000050
    B = 1 - (2+x)/4096                  # prob050100
    C = 1 - (3+x)/4096                  # prob100200
    D = 1 - (4+x)/4096                  # prob200300
    E = 1 - (5+x)/4096                  # prob300500
    F = 1 - (6+x)/4096                  # prob500nup

    ABCDEF = [A, B, C, D, E, F]

    n = encounters
    f = max(0, n-500)           # exp500nup
    e = max(0, n-f-300)         # exp300500
    d = max(0, n-f-e-200)       # exp200300
    c = max(0, n-f-e-d-100)     # exp100200
    b = max(0, n-f-e-d-c-50)    # exp050100
    a = n-f-e-d-c-b             # exp000050

    abcdef = [a, b, c, d, e, f]

    res = 1
    for i in range(6):
        if abcdef[i] > 0:
            res *= pow(ABCDEF[i], abcdef[i])
    return res

client.run("NDE5MjY2ODA2MjY0NDk2MTM4.DXt_kg.zjWGc-4qFV5CgJRDb13CKQqjPpg")
