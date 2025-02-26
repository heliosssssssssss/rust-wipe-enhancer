import time 

print("EXTERNAL-GLOBAL-ERROR-MANAGER: IGNORE ALL ACTIVE ERRORS!")
print("EXTERNAL-GLOBAL-ERROR-MANAGER: IGNORE ALL ACTIVE ERRORS!")
print("EXTERNAL-GLOBAL-ERROR-MANAGER: IGNORE ALL ACTIVE ERRORS!")
print("EXTERNAL-GLOBAL-ERROR-MANAGER: IGNORE ALL ACTIVE ERRORS!")
print("EXTERNAL-GLOBAL-ERROR-MANAGER: IGNORE ALL ACTIVE ERRORS!")

print('helios_runtime: startup_proc is now active')
print('starting..')

time.sleep(3)

print("helios_runtime is now active")

# LOAD PRIMARY LIBARY PACKAGES

import os 
import sys
import json 
import math 
import rustplus
from pprint import pprint 
import asyncio
import csv
import random
import string
from colorama import Fore, Back, Style
import websockets
import tracemalloc
import cryptography
import aiohttp
import discord
import requests





GLOBAL_INFORMATION_TABLE = {
    "discord_" : {
        "webhook_info" : "https://discord.com/api/webhooks/1257836308001325056/cMgS0wfkY_V8xw9iz5MvATiwWdPD6D1zVx_Em7Q_anOb8ZSHlVWhwZ4Xb0wbUPQKoqUv",
        "role_id" : 1258227392338726942
    },
    "config" : {
        "STEAM_ID" : 0,
        "PLAYER_TOKEN" : 0,
        "CONFIG_STABILITY_VERSION" : "1.0.0"

    },
    "default" : {
        "BATTLEMETRICS_API_KEY" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImYzNTEyNTI3MzQxMDhjMGYiLCJpYXQiOjE3MTk4NzMzMjIsIm5iZiI6MTcxOTg3MzMyMiwiaXNzIjoiaHR0cHM6Ly93d3cuYmF0dGxlbWV0cmljcy5jb20iLCJzdWIiOiJ1cm46dXNlcjo4NzkzNzQifQ.IHgM3yLGIsWUwv-258x4n4fArGFnoPYTZRTkRK0tSbI",
        "BATTLEMETRICS_BASE_URL" : "https://api.battlemetrics.com"
    },
    "helios-admin" : {
        "g_server" : {
            "SERVER_IP" : "",
            "SERVER_PORT" : "",
            "SERVER_MAP_SIZE" : "",
            "SERVER_MAX_PLAYERS" : "",
            "SERVER_GANE" : "rust",
            "SERVER_NAME" : "g_server"
        },
        "g_chat_bot" : {
            "TAG" : "[helios-admin]:",
            "PREFIX" : "h/"
        },
        "core" : {
            "socket" : None
        }
    }
}





class DisplayEngine:
    def check_status():
        return print("[display-engine]: running : active")
    
    def check_version():
        return print("[display-engine]: version 1.0.0 @ made by helios")
    
    def p_de_load(text):
        print(Fore.CYAN + "[display-engine] " + Fore.RESET + f"{text}")

    def p_load(text):
        print(Fore.YELLOW + "[load] " + Fore.RESET + f"{text}")

    def p_hr(text):
        print(Fore.GREEN + "[helios_rust] " + Fore.RESET + f"{text}")

    def p_hsp(text):
        print(Fore.BLUE + "[helios_system_plus] " + Fore.RESET + f"{text}")

    def p_debug(text):
        print(Fore.RED + "[debug] " + Fore.RESET + f"{text}")

    def p_info(text):
        print(Fore.LIGHTGREEN_EX + "[info] " + Fore.RESET + f"{text}")

    def p_config(text):
        print(Fore.LIGHTYELLOW_EX + "[config_] " + Fore.RESET + f"{text}")

    def p_config_clear(text):
        Back.GREEN
        print(Fore.LIGHTYELLOW_EX + "[config_] " + Fore.RESET + f"{text}")

    def p_sync(text):
        print(Fore.LIGHTBLUE_EX + "[SYNC] " + Fore.RESET + f"{text}")


class DiscordEngine:
    def send_msg(title, msg):
        data = {
            "content" : "<@&1258227392338726942>",
            "embeds" : [
                {
                    "title" : title,
                    "description" : msg,
                    "color" : int("050505", 16),
                    "fields" : [
                        {
                            "name" : "",
                            "value" : "This event took place @ <t:"+ str(utils.get_timestamp()) +":R> (<t:" + str(utils.get_timestamp()) + ":t>)"
                        }
                    ]
                }
            ]
        } 
        DisplayEngine.p_load("data has being loaded, init payload @ also sending raw content for debug")
        DisplayEngine.p_info(data)

        DisplayEngine.p_debug("SENDING INFORMATINPO PAYLOAD TO ABOVE URI")
        DisplayEngine.p_config(GLOBAL_INFORMATION_TABLE["discord_"]["webhook_info"])

        r = requests.post(url=GLOBAL_INFORMATION_TABLE["discord_"]["webhook_info"], json=data)

        DisplayEngine.p_debug("INFORMATION HAS BEEN SENT SUCCESSFULLY")
        DisplayEngine.p_debug("[api-state" + str(r.status_code))




    def send_start_msg():
        DisplayEngine.p_debug("send_msg def @ (SEND_START_MESSAGE) : system was initalized")
        data = {
            "content" : "<@&1258227392338726942>",
            "embeds" : [
                {
                    "title" : "[HELIOS-ADMIN/RUST_BOT] has connected.",
                    "description" : "[helios-admin] is now enabled and synchronized with **"+GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_NAME"]+"**",
                    "color" : int("050505", 16),
                    "fields" : [
                        {
                            "name" : "",
                            "value" : "This event took place @ <t:"+ str(utils.get_timestamp()) +":R> (<t:" + str(utils.get_timestamp()) + ":t>)"
                        }
                    ]
                }
            ]
        } 
        DisplayEngine.p_load("data has being loaded, init payload @ also sending raw content for debug")
        DisplayEngine.p_info(data)

        DisplayEngine.p_debug("SENDING INFORMATINPO PAYLOAD TO ABOVE URI")
        DisplayEngine.p_config(GLOBAL_INFORMATION_TABLE["discord_"]["webhook_info"])

        r = requests.post(url=GLOBAL_INFORMATION_TABLE["discord_"]["webhook_info"], json=data)

        DisplayEngine.p_debug("INFORMATION HAS BEEN SENT SUCCESSFULLY")
        DisplayEngine.p_debug("[api-state" + str(r.status_code))





class RustSync:
    async def main():

        DisplayEngine.p_hr("RustSync is active - synced")
        DisplayEngine.p_hr("RustSync is active - synced")
        DisplayEngine.p_hr("RustSync is active - synced")

        DisplayEngine.p_load("Connecting RustSync with information data to RustSocket*.connect")
        DisplayEngine.p_debug("connecting with follow information")

        DisplayEngine.p_load(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_IP"]}")
        DisplayEngine.p_load(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_PORT"]}")
        DisplayEngine.p_load(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {GLOBAL_INFORMATION_TABLE["config"]["STEAM_ID"]}")
        DisplayEngine.p_load(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {GLOBAL_INFORMATION_TABLE["config"]["PLAYER_TOKEN"]}")
        time.sleep(1.5)

        DisplayEngine.p_debug("RustSync has confirmed that the data is legit and is stable")
        DisplayEngine.p_info("now connecting to rust socket (helios_admin.connect())")

        await helios_admin.connect()

        DisplayEngine.p_info("helios_admin.connect() was successful")
        DisplayEngine.p_debug("connection successful")
        DisplayEngine.p_info("entering stage 6 # ff000#d0") 
        time.sleep(1.5)
        
        ###################################################################################################################

        DisplayEngine.p_debug("RustAdminEngine.on_start_proc() is now initalized")
        await RustAdminEngine.on_start_proc() 
        

        ###################################################################################################################

        class Commands: # command initators 

            @helios_admin.command()
            async def help(command : rustplus.Command): 
                await RustAdminEngine.send_msg("hi")

            @helios_admin.command()
            async def time(command : rustplus.Command): 
                None

            @helios_admin.command()
            async def pop(command : rustplus.Command): 
                None

            @helios_admin.command()
            async def url(command : rustplus.Command): 
                None

            @helios_admin.command()
            async def calculate(command : rustplus.Command): 
                None

            @helios_admin.command()
            async def events(command : rustplus.Command): 
                None

            @helios_admin.command()
            async def _g(command : rustplus.Command): 
                None

            @helios_admin.command()
            async def test(command : rustplus.Command): 
                None

            @helios_admin.command()
            async def terminate(command : rustplus.Command): 
                None


        await helios_admin.hang()



class CommandsEngine:
    None
                




class RustAdminEngine: 
    def init():
        global helios_admin

        DisplayEngine.p_debug("global helios_admin is defined")

        DisplayEngine.p_hr("init received by stage 3 occured ")
        COMMAND_OPTIONS = rustplus.CommandOptions(prefix=GLOBAL_INFORMATION_TABLE["helios-admin"]["g_chat_bot"]["PREFIX"])
        DisplayEngine.p_debug("defining command options (COMMAND_OPTIONS)")

        
        socket = rustplus.RustSocket(
            ip = GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_IP"],
            port = GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_PORT"],
            steam_id = GLOBAL_INFORMATION_TABLE["config"]["STEAM_ID"],
            player_token = GLOBAL_INFORMATION_TABLE["config"]["PLAYER_TOKEN"],
            command_options = COMMAND_OPTIONS,
            debug = True
        )

        DisplayEngine.p_info("socket = Rustplus.Socket is now defined")
        time.sleep(1.5)

        helios_admin = socket

        DisplayEngine.p_debug("helios_admin = socket is now defined successfully")


        DisplayEngine.p_debug("core.socket is ACTIVE DBY36 - fliov2")
        DisplayEngine.p_debug("G_I_T is now active. outputting variables for debug")

        DisplayEngine.p_config(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_IP"]}")
        DisplayEngine.p_config(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_PORT"]}")
        DisplayEngine.p_config(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {GLOBAL_INFORMATION_TABLE["config"]["STEAM_ID"]}")
        DisplayEngine.p_config(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {GLOBAL_INFORMATION_TABLE["config"]["PLAYER_TOKEN"]}")
        DisplayEngine.p_config(f"[OUTPUT - CLEAR @ RUSTSOCKET] -> {COMMAND_OPTIONS}")

        DisplayEngine.p_hr("[STAGE 5 - NOTIFY] @ RUSTADMINENGINE IS NOW EXIT -> SWITCHING OVER TO RUST-SYNC")
        DisplayEngine.p_hr("[STAGE 5 - NOTIFY] @ RUSTADMINENGINE IS NOW EXIT -> SWITCHING OVER TO RUST-SYNC")
        DisplayEngine.p_hr("[STAGE 5 - NOTIFY] @ RUSTADMINENGINE IS NOW EXIT -> SWITCHING OVER TO RUST-SYNC")
        DisplayEngine.p_hr("[STAGE 5 - NOTIFY] @ RUSTADMINENGINE IS NOW EXIT -> SWITCHING OVER TO RUST-SYNC")
        DisplayEngine.p_hr("[STAGE 5 - NOTIFY] @ RUSTADMINENGINE IS NOW EXIT -> SWITCHING OVER TO RUST-SYNC")
        DisplayEngine.p_hr("[STAGE 5 - NOTIFY] @ RUSTADMINENGINE IS NOW EXIT -> SWITCHING OVER TO RUST-SYNC")

        DisplayEngine.p_load("asyncio.run(RustSync.main())")
        time.sleep(1.5)


        asyncio.run(RustSync.main())
        

    async def send_msg(txt):
        DisplayEngine.p_info("send_msg (class: RustAdminEngine) was initalized")
        DisplayEngine.p_config_clear(f"message to send: {txt}")
        DisplayEngine.p_config_clear(f"raw: {GLOBAL_INFORMATION_TABLE['helios-admin']["g_chat_bot"]["TAG"]} {txt}")
        await helios_admin.send_team_message(f"{GLOBAL_INFORMATION_TABLE['helios-admin']["g_chat_bot"]["TAG"]} {txt}")
        DisplayEngine.p_hr("message successfully sent")

    async def on_start_proc(): 
        DisplayEngine.p_debug("command order @ on_sart_proc received!")
        DisplayEngine.p_hr("command was issued from RustSync")

        server_info = await helios_admin.get_info()
        DisplayEngine.p_debug("server_info is registered")

        GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_NAME"] = server_info.name
        DisplayEngine.p_load("gLOBAL_INFO_TABLE REGISTER >> SERVER INFO")

        DiscordEngine.send_start_msg()

        await RustAdminEngine.send_msg("Bot is active and synchronized with this sever. (Type h/help) to view commands.")





class utils:
    def read_json_to_object(file_path):

        DisplayEngine.p_debug("read_json_to_object(file_path/): has been called")

        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    
    def get_timestamp():
        DisplayEngine.p_load("[TIMESTAMP-MANAGER] : loadinjg active timestamp")
        DisplayEngine.p_debug(f"{int(time.time())}")
        return int(time.time())





class StartupEngine:
    def on_start():
        DisplayEngine.p_debug("starting primary startup..")
        DisplayEngine.p_debug("clearing..")
        time.sleep(1.5)
        os.system('cls')

        DisplayEngine.p_de_load("Display Engine - V7 @ Made by helios")
        DisplayEngine.p_de_load("Thanks for using :)")

        time.sleep(2)

        os.system('cls')

        print(Fore.CYAN + """ 
 /$$$$$$$                        /$$      /$$$$$$                               
| $$__  $$                      | $$     /$$__  $$                              
| $$  \ $$ /$$   /$$  /$$$$$$$ /$$$$$$  | $$  \__/ /$$   /$$ /$$$$$$$   /$$$$$$$
| $$$$$$$/| $$  | $$ /$$_____/|_  $$_/  |  $$$$$$ | $$  | $$| $$__  $$ /$$_____/
| $$__  $$| $$  | $$|  $$$$$$   | $$     \____  $$| $$  | $$| $$  \ $$| $$      
| $$  \ $$| $$  | $$ \____  $$  | $$ /$$ /$$  \ $$| $$  | $$| $$  | $$| $$      
| $$  | $$|  $$$$$$/ /$$$$$$$/  |  $$$$/|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$
|__/  |__/ \______/ |_______/    \___/   \______/  \____  $$|__/  |__/ \_______/
                                                   /$$  | $$                    
                                                  |  $$$$$$/                    
                                                   \______/        

POWERED BY RustSync @ 2024 - DEVELOPED BY HELIOS INTERNATIONAL SECURITY GROUP LLC - All rights reserved.             
        """)

        time.sleep(5)

        os.system("cls")
        
        
        time.sleep(2)
        DisplayEngine.p_load("package: [time] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [os] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [sys] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [json] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [math] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [rustplus] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [pprint] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [asyncio] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [csv] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [random] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [string] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [colorama] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [websockets] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [tracemalloc] is loaded")
        time.sleep(0.3)
        DisplayEngine.p_load("package: [cryptography] is loaded")
        DisplayEngine.p_load("all packages are successfully loaded - there is no issues present")
        DisplayEngine.p_debug("init() -> force_push to next stage")
        time.sleep(2)
        DisplayEngine.p_hsp("itx-0: authenticating")
        time.sleep(5)
        DisplayEngine.p_hsp("user agent is authenticated with helios network")
        DisplayEngine.p_hsp("fx00000000001x01x00000111001x0 - log enabled - rollover @ p_chip")
        time.sleep(3)
        DisplayEngine.p_hsp("display-engine: active")
        time.sleep(0.3)
        DisplayEngine.p_hsp("startup-engine: active")
        time.sleep(0.3)
        DisplayEngine.p_hsp("rust-engine: inactive")
        time.sleep(1)
        DisplayEngine.p_load("value_subsq: rust-engine request ordered @ __init__")
        time.sleep(random.randint(1, 5))
        DisplayEngine.p_load("value_subsq: rust-engine request done @ callback")
        time.sleep(0.3)
        DisplayEngine.p_hsp("helios-engine: active")
        time.sleep(0.3)
        DisplayEngine.p_hsp("battlemetrics-engine: inactive")
        time.sleep(1)
        DisplayEngine.p_load("value_subsq: battlemetrics-engine request ordered @ __init__")
        time.sleep(random.randint(1, 5))
        DisplayEngine.p_load("value_subsq: battlemetrics-engine request done @ callback")
        time.sleep(0.3)
        DisplayEngine.p_hsp("rust-ext-manager: inactive")
        time.sleep(1)
        DisplayEngine.p_load("value_subsq: rust-ext-manager request ordered @ __init__")
        time.sleep(random.randint(1, 5))
        DisplayEngine.p_load("value_subsq: rust-ext-manager request done @ callback")
        time.sleep(0.3)
        DisplayEngine.p_hsp("console-subsystem-v2: inactive")
        time.sleep(1)
        DisplayEngine.p_load("value_subsq: console-subsystem-v2 request ordered @ __init__")
        time.sleep(random.randint(1, 5))
        DisplayEngine.p_load("value_subsq: console-subsystem-v2 request done @ callback")
        time.sleep(0.3)
        DisplayEngine.p_hsp("variable_mngr: inactive")
        time.sleep(1)
        DisplayEngine.p_load("value_subsq: variable_mngr request ordered @ __init__")
        time.sleep(random.randint(1, 5))
        DisplayEngine.p_load("value_subsq: variable_mngr request done @ callback")
        time.sleep(0.3)
        DisplayEngine.p_hsp("rust-stats: inactive")
        time.sleep(1)
        DisplayEngine.p_load("value_subsq: rust-stats request ordered @ __init__")
        time.sleep(random.randint(1, 5))
        DisplayEngine.p_load("value_subsq: rust-stats request done @ callback")
        time.sleep(0.3)
        DisplayEngine.p_hsp("security-net: active")
        time.sleep(2)
        DisplayEngine.p_info("deploying discord @ wbhook url")
        DisplayEngine.p_debug(f"{GLOBAL_INFORMATION_TABLE['discord_']['webhook_info']}")
        DisplayEngine.p_debug("user: [helios-admin] / agent: [#notify @ rustsussy]")
        time.sleep(0.3)
        DisplayEngine.p_info("token clearence for @ 1102562445454745661 is cleared.. OK")
        time.sleep(1)
        DisplayEngine.p_hsp("switiching over - rollback 2 @ enter stage 3 f#0001cb9")
        time.sleep(4)
        DisplayEngine.p_load("requiring config_data @ <p:0010011101>x>@h9:filetype_folder")
        time.sleep(6)
        DisplayEngine.p_load("init : clear @ sq1")
        time.sleep(random.randint(1, 3))
        DisplayEngine.p_load("loading version 1 _ default global information table")
        DisplayEngine.p_info("subsqenece_init @ datafile")
        time.sleep(random.randint(1, 5))

        DisplayEngine.p_config_clear(GLOBAL_INFORMATION_TABLE["config"])
        time.sleep(random.randint(1, 3))
        DisplayEngine.p_config_clear(GLOBAL_INFORMATION_TABLE["default"])
        time.sleep(random.randint(1, 3))
        DisplayEngine.p_config_clear(GLOBAL_INFORMATION_TABLE["discord_"])
        time.sleep(random.randint(1, 3))
        DisplayEngine.p_config_clear(GLOBAL_INFORMATION_TABLE["helios-admin"])
        time.sleep(random.randint(1, 3))

        DisplayEngine.p_info("file integrity is good @ stability 1.0.0 = 1.0.0 @ stabalized")
        time.sleep(2)
        DisplayEngine.p_load("config file @ main_system")
        DisplayEngine.p_info("calling json_obj")

        json_object = utils.read_json_to_object(r"C:\Users\Adamd\Important\heliosadmin\config_settings.json")
        DisplayEngine.p_config_clear(json_object)

        # do data file config check 

        DisplayEngine.p_info("collecting version variables")
        
        cfg_file_v = json_object["stability_version"]
        DisplayEngine.p_debug(f"cfg_file_v @ (config set)= {cfg_file_v}")
        cfg_active_v = GLOBAL_INFORMATION_TABLE["config"]["CONFIG_STABILITY_VERSION"]
        DisplayEngine.p_debug(f"cfg_active_v @ (active settings set)= {cfg_active_v}")

        time.sleep(1)
        DisplayEngine.p_info("pairing variables @cfg_file_v and @cfg_active_v to ensure there stable with one another")

        if cfg_active_v == cfg_file_v: 
            DisplayEngine.p_info("versions are correct")
            time.sleep(0.2)
            DisplayEngine.p_debug("currently in a active if session")
            time.sleep(0.2)

            DisplayEngine.p_debug("defining global_info_table using json_object")
            time.sleep(0.2)
            time.sleep(0.5)

            GLOBAL_INFORMATION_TABLE["config"]["STEAM_ID"] = json_object["config"]["steam_id"]
            time.sleep(0.2)
            DisplayEngine.p_debug("global info table - steam id defined")
            time.sleep(0.2)
            DisplayEngine.p_debug(f"variable-test[v2]: current active variable is: {GLOBAL_INFORMATION_TABLE["config"]["STEAM_ID"]}")
            time.sleep(0.2)
            GLOBAL_INFORMATION_TABLE["config"]["PLAYER_TOKEN"] = json_object["config"]["player_token"]
            time.sleep(0.2)
            DisplayEngine.p_debug("global info table - player_token defined")
            time.sleep(0.2)
            DisplayEngine.p_debug(f"variable-test[v2]: current active variable is: {GLOBAL_INFORMATION_TABLE["config"]["PLAYER_TOKEN"]}")
            time.sleep(0.2)
            GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_IP"] = json_object["config"]["ip"]
            time.sleep(0.2)
            DisplayEngine.p_debug("global info table - ip defined")
            time.sleep(0.2)
            DisplayEngine.p_debug(f"variable-test[v2]: current active variable is: {GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_IP"]}")
            time.sleep(0.2)
            GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_PORT"] = json_object["config"]["port"]
            time.sleep(0.2)
            DisplayEngine.p_debug("global info table - port defined")
            time.sleep(0.2)
            DisplayEngine.p_debug(f"variable-test[v2]: current active variable is: {GLOBAL_INFORMATION_TABLE["helios-admin"]["g_server"]["SERVER_PORT"]}")
            time.sleep(0.2)

        else: 
            DisplayEngine.p_debug("09587c934-vun4 file integrity fail")

        DisplayEngine.p_info("variable crosscheck and register load is clear")
        DisplayEngine.p_hsp("subswitching to stage 4 @ (stage nickname: helios-admin rust)")

        DisplayEngine.p_hr("SWITCHING OVER TO HELIOS ADMIN ENGINE @ GATEWAY 4A - PULLOUT EXIT CODE N/A")
        DisplayEngine.p_hr("SWITCHING OVER TO HELIOS ADMIN ENGINE @ GATEWAY 4A - PULLOUT EXIT CODE N/A")
        DisplayEngine.p_hr("SWITCHING OVER TO HELIOS ADMIN ENGINE @ GATEWAY 4A - PULLOUT EXIT CODE N/A")
        DisplayEngine.p_hr("SWITCHING OVER TO HELIOS ADMIN ENGINE @ GATEWAY 4A - PULLOUT EXIT CODE N/A")
        DisplayEngine.p_hr("SWITCHING OVER TO HELIOS ADMIN ENGINE @ GATEWAY 4A - PULLOUT EXIT CODE N/A")

        time.sleep(1.5)

        RustAdminEngine.init()
    




DisplayEngine.p_debug("startupEngine.onstart() subsq1 is called")
StartupEngine.on_start()
