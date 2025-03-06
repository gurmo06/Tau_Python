# Imports
import enum
import re
import os
import discord

# Specific Module Imports
import arithmetic

#Set Intents
intents = discord.Intents.default()
intents.message_content = True

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
    
    except ValueError:
        return "Syntax Error: Arithmetic commands must be in the form of #<command> <num1> <num2>"
    
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
        await message.channel.send("Arithmetic Commands: #add, #sub, #mul, #div, #mod, #pow")
    
    
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
        
        
    #Invalid Command    
    elif message.content.startswith("#"):
        await message.channel.send("Invalid Command. Type #help for list of commands.")
        
        

#Run Client
client.run(os.getenv("TOKEN"))