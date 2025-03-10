# Imports
import enum
import re
import os
import discord

# Specific Module Imports
import arithmetic
import trigonometric

#Set Intents
intents = discord.Intents.default()
intents.message_content = True #Temporarily Set to True for easier Debugging

#Init Client
client = discord.Client(intents=intents)


#Global Variables and Enums
msg_num = 0 #Debug
class Arith_Type(enum.Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MOD = 5
    POW = 6
    SQRT = 7


class Trig_Type(enum.Enum):
    SIN = 1
    COS = 2
    TAN = 3
    COT = 4
    SEC = 5
    CSC = 6
    ASIN = 7
    ACOS = 8
    ATAN = 9
    ACOT = 10
    ASEC = 11
    ACSC = 12



#Executes Artihmetic Operations
def exec_arith(arith_type, msg):
    parts = re.split(r"[\s,]+", msg)
    return_var = 0

    #Try-Catch for Syntax Errors  
    try:
        if (arith_type == Arith_Type.ADD):
            return_var = arithmetic.add(float(parts[1]), float(parts[2]))

        if (arith_type == Arith_Type.SUB):
            return_var = arithmetic.sub(float(parts[1]), float(parts[2]))

        if (arith_type == Arith_Type.MUL):
            return_var = arithmetic.mul(float(parts[1]), float(parts[2]))

        if (arith_type == Arith_Type.DIV):
            return_var = arithmetic.div(float(parts[1]), float(parts[2]))

        if (arith_type == Arith_Type.MOD):
            return_var = arithmetic.mod(float(parts[1]), float(parts[2]))

        if (arith_type == Arith_Type.POW):
            return_var = arithmetic.pow(float(parts[1]), float(parts[2]))
            
        if (arith_type == Arith_Type.SQRT):
            return_var = arithmetic.sqrt(float(parts[1]))

    except ValueError:
        return "Syntax Error: Arithmetic commands must be in the form of #<command> <num1> <num2> (or #<command> <num1> for sqrt)"
    
    except ZeroDivisionError:
        return "Arithmetic Error: Division by Zero"
    
    return return_var


#Handle Trigonometric Commands
def exec_trig(trig_type, msg):
    parts = re.split(r"[\s,]+", msg)
    return_var = 0

    #Try-Catch for Syntax Errors
    try:
        if (trig_type == Trig_Type.SIN):
            return_var = trigonometric.sin(float(parts[1]))

        if (trig_type == Trig_Type.COS):
            return_var = trigonometric.cos(float(parts[1]))

        if (trig_type == Trig_Type.TAN):
            return_var = trigonometric.tan(float(parts[1]))

        if (trig_type == Trig_Type.COT):
            return_var = trigonometric.cot(float(parts[1]))

        if (trig_type == Trig_Type.SEC):
            return_var = trigonometric.sec(float(parts[1]))

        if (trig_type == Trig_Type.CSC):
            return_var = trigonometric.csc(float(parts[1]))

        if (trig_type == Trig_Type.ASIN):
            return_var = trigonometric.asin(float(parts[1]))

        if (trig_type == Trig_Type.ACOS):
            return_var = trigonometric.acos(float(parts[1]))

        if (trig_type == Trig_Type.ATAN):
            return_var = trigonometric.atan(float(parts[1]))

        if (trig_type == Trig_Type.ACOT):
            return_var = trigonometric.acot(float(parts[1]))

        if (trig_type == Trig_Type.ASEC):
            return_var = trigonometric.asec(float(parts[1]))

        if (trig_type == Trig_Type.ACSC):
            return_var = trigonometric.acsc(float(parts[1]))

    except ValueError:
        return "Syntax Error: Trigonometric commands must be in the form of #<command> <num1>"
    
    return return_var

#Message On Start
@client.event
async def on_ready():
    print("Logged on as", client.user)


#Handle Bot Messages
@client.event
async def on_message(message):
    #Print Message
    global msg_num
    print("$", msg_num, " ", message.content, sep = "")
    msg_num += 1

    #Ignore Own Messages
    if message.author == client.user:
        return
    

    #Help Command
    if message.content.startswith("#help"):
        help_message = "Arithmetic Commands (#<command> <num1> <num2>): #add, #sub, #mul, #div, #mod, #pow\n"
        help_message += "Trigonometric Commands (#<command> <num1>): #sin, #cos, #tan, #cot, #sec, #csc, #asin, #acos, #atan, #acot, #asec, #acsc"
        await message.channel.send(help_message)
    
    
    #Handle Arithmetic Commands
    elif message.content.startswith("#add"):
        await message.channel.send(exec_arith(Arith_Type.ADD, message.content))

    elif message.content.startswith("#sub"):
        await message.channel.send(exec_arith(Arith_Type.SUB, message.content))
     
    elif message.content.startswith("#mul"):
        await message.channel.send(exec_arith(Arith_Type.MUL, message.content))
    
    elif message.content.startswith("#div"):
        await message.channel.send(exec_arith(Arith_Type.DIV, message.content))
    
    elif message.content.startswith("#mod"):
        await message.channel.send(exec_arith(Arith_Type.MOD, message.content))
    
    elif message.content.startswith("#pow"):
        await message.channel.send(exec_arith(Arith_Type.POW, message.content))
        
    elif message.content.startswith("#sqrt"):
        await message.channel.send(exec_arith(Arith_Type.SQRT, message.content))
    
    
    #Handle Trigonometric Commands
    elif message.content.startswith("#sin"):
        await message.channel.send(exec_trig(Trig_Type.SIN, message.content))
    
    elif message.content.startswith("#cos"):
        await message.channel.send(exec_trig(Trig_Type.COS, message.content))
    
    elif message.content.startswith("#tan"):
        await message.channel.send(exec_trig(Trig_Type.TAN, message.content))
    
    elif message.content.startswith("#cot"):
        await message.channel.send(exec_trig(Trig_Type.COT, message.content))
    
    elif message.content.startswith("#sec"):
        await message.channel.send(exec_trig(Trig_Type.SEC, message.content))
    
    elif message.content.startswith("#csc"):
        await message.channel.send(exec_trig(Trig_Type.CSC, message.content))
    
    elif message.content.startswith("#asin"):
        await message.channel.send(exec_trig(Trig_Type.ASIN, message.content))
    
    elif message.content.startswith("#acos"):
        await message.channel.send(exec_trig(Trig_Type.ACOS, message.content))
    
    elif message.content.startswith("#atan"):
        await message.channel.send(exec_trig(Trig_Type.ATAN, message.content))
    
    elif message.content.startswith("#acot"):
        await message.channel.send(exec_trig(Trig_Type.ACOT, message.content))
    
    elif message.content.startswith("#asec"):
        await message.channel.send(exec_trig(Trig_Type.ASEC, message.content))
    
    elif message.content.startswith("#acsc"):
        await message.channel.send(exec_trig(Trig_Type.ACSC, message.content))
    
    
    #Invalid Command    
    elif message.content.startswith("#"):
        await message.channel.send("Invalid Command. Type #help for list of commands.")



#Run Client
client.run(os.getenv("TOKEN"))