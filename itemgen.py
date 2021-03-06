# Simple custom item generator for Oraxen
# By ClickNin

# *actually this is really ez to write though*
# but write this one is very time consuming, as oraxen has an incredible amount of features/mechanics

from numpy import random
import os
import sys
import random
import uuid

isGenModel = False

def CommandMechanicEditor():
    print("Where the command should get executed? Valid values are CONSOLE, PLAYER and OP. Default to PLAYER.")
    execLocation = input(">> Execution Type: ")
    print("Enter the command you want to execute.")
    command = input(">> Command: ")
    with open('generated.txt', 'a') as f:
        if not execLocation:
            line15 = "      player:\n      - \"{0}\"\n".format(command)
        if execLocation == "CONSOLE":
            line15 = "      console:\n      - \"{0}\"\n".format(command)
        elif execLocation == "PLAYER":
            line15 = "      player:\n      - \"{0}\"\n".format(command)
        elif execLocation == "OP":
            line15 = "      opped_player:\n      - \"{0}\"\n".format(command)
        else:
            line15 = "      player:\n      - \"{0}\"\n".format(command)
        f.write(line15)
        f.close()
    return

def PreEnchantmentsEditor():
    print("Enter the enchantment you want to pre add. A list of it can be found at https://docs.oraxen.com/configuration/items-advanced")
    enchant = input(">> Enchantment: ")
    with open('generated.txt', 'a') as f:
        line1 = "    {0}\n".format(enchant)
        f.write(line1)
        f.close()
    print("Enchantments(s) added! Do you want to add more?")
    yorn7 = input(">> [Y/n] ")
    if yorn7 == "Y" or yorn7 == "y":
        PreEnchantmentsEditor()
    else:
        return

def PotionEffectEditor():
    print("Enter the effect type you want to add. A list of available effects are here https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html")
    effect = input(">> Effect: ")
    print("Enter effect's duration below.")
    duration = input(">> Duration: ")
    print("Enter effect's amplifier below.")
    amplifier = input(">> Amplifier: ")
    print("Should your effect produce more particles in ambient? Leave blank will set it to true.")
    ambient = input(">> [Y/n] ")
    print("Show effect's particles? Leave blank will set it to true.")
    particles = input(">> [Y/n] ")
    print("Show effect's icon? Leave blank will set it to true.")
    icon = input(">> [Y/n] ")
    with open('generated.txt', 'a') as f:
        line1 = "    - {{ type: {0},\n        duration: {1},\n        amplifier: {2},\n".format(effect, duration, amplifier)
        if ambient == "N" or ambient == "n":
            line2 = "        ambient: false,\n"
        else:
            line2 = "        ambient: true,\n"
        if particles == "N" or particles == "n":
            line3 = "        particles: false,\n"
        else:
            line3 = "        particles: true,\n"
        if icon == "N" or icon == "n":
            line4 = "        icon: false }\n"
        else:
            line4 = "        icon: true }\n"
        f.writelines([line1,line2,line3,line4])
        f.close()
    print("Effect(s) added! Do you want to add more?")
    yorn5 = input(">> [Y/n] ")
    if yorn5 == "Y" or yorn5 == "y":
        PotionEffectEditor()
    else:
        return

def ItemFlagEditor():
    print("Enter a flag you want to add. A list of available flags are here https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/inventory/ItemFlag.html")
    flag = input(">> Flag: ")
    with open('generated.txt', 'a') as f:
        line1 = "    - {0}\n".format(flag)
        f.write(line1)
        f.close()
    print("Flag(s) added! Do you want to add more?")
    yorn1 = input(">> [Y/n] ")
    if yorn1 == "Y" or yorn1 == "y":
        ItemFlagEditor()
    else:
        return

def LoreEditor():
    print("Enter the lore you want to add.")
    lore = input(">> Lore: ")
    with open('generated.txt', 'a') as f:
        line1 = "    - {0}\n".format(lore)
        f.write(line1)
        f.close()
    print("Lore(s) added! Do you want to add more?")
    yorn3 = input(">> [Y/n] ")
    if yorn3 == "Y" or yorn3 == "y":
        LoreEditor()
    else:
        return

def AttributeModifiersEditor():
    print("Enter the attribute you want to add. \nA complete list of attributes supported by Spigot can be found at https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html")
    attribute = input(">> Attribute Name: ")
    print("Enter the attribute operation. \n0 for adding number (a.k.a, setting it)\n1 for adding scalar\n2 for multipling scalar 1\nChoosing 0 are prefered for most of people.")
    operation = input(">> Attribute Opeartion: ")
    print("Enter the value of the attribute you want to add.")
    value = input(">> Attribute Value: ")
    uuid_ = str(uuid.uuid4())
    print("Enter a slot in the player that the attribute will apply.\nValid values are HAND, OFF_HAND, FEET, LEGS, CHEST or HEAD.")
    slot = input(">> Slot: ")
    with open('generated.txt', 'a') as f:
        line1 = "    - {{ name: \"oraxen\", attribute: {0}, amount: {1}, operation: {2},\n".format(attribute, value, operation)
        line2 = "        uuid: {0}, slot: {1} }}\n".format(uuid_, slot)
        f.writelines([line1, line2])
        f.close()
    print("Attribute(s) added! Do you want to add more?")
    yorn2 = input(">> [Y/n] ")
    if yorn2 == "Y" or yorn2 == "y":
        AttributeModifiersEditor()
    else:
        return

def Generator():
    global isGenModel
    print("Enter the raw name of the item below, this will be used in Oraxen config.")
    raw_name = input(">> Raw name: ")
    print("Enter the Display Name of the item below, this will be used for item's ingame display name.")
    display_name = input(">> Display name: ")
    print("Enter your Item's type (Material) below.\nYou can enter in these value AXE, SWORD, PICKAXE, SHOVEL, HOE, BOW, CROSSBOW, PAPER or CUSTOM.\nEntering CUSTOM will allow you to specify your prefered material. Leave blank will set it to PAPER!")
    item_type = input(">> Item Type: ")
    if not item_type:
        item_type = "PAPER"
    if item_type == "CUSTOM":
        print("Specify your item's material below.")
        material = input(">> Material: ")
        if material:
            item_type = None
            item_type = material
            print(item_type)
        else:
            item_type = None
            item_type = "PAPER"
    print("Should we inject ID for this item? This will allow Oraxen to recognise your item.\nLeave blank will set it to true. Don't set it unless you know what you are doing.")
    injectID = input(">> [Y/n] ")
    print("Enter in the number of damage your item cause. Leave this blank for more customizations.")
    damage = input(">> Damage: ")
    bow = "BOW"
    crossbow = "CROSSBOW"
    if item_type != bow and item_type != crossbow:
        print("Should we generate a model for this item?\nLeave blank will generate it from a texture, entering N will allow you to use a existing model.")
        genModel = input(">> [Y/n] ")
        if genModel == "N" or genModel == "n":
            print("Enter your model location.")
            model = input(">> Model: ")
            isGenModel = True
        elif genModel == "Y" or genModel == "y" or not genModel:
            print("Enter your item's texture location.")
            texture = input(">> Texture: ")
            print("Enter the model type you want to generate.\nLeave blank to set it to \"item/generated\".\nFor weapon and tool, set it to \"item/handheld\" instead.")
            modelType = input(">> Model Type: ")
    else:
        print("Please specify your bow/crossbow model.")
        bowModel = input(">> Bow Model: ")
        print("Please specify the pulling models.\nJust enter the first part of the model name (for example, you have a_1, a_2, a_3, only enter in a_.)")
        bowPullingModel = input(">> Bow Pulling Model: ")
        bpmStage0 = bowPullingModel + "0"
        bpmStage1 = bowPullingModel + "1"
        bpmStage2 = bowPullingModel + "2"
    with open('generated.txt', 'a') as f:
        line1 = "{0}:\n".format(raw_name)
        line2 = "  displayname: '{0}'\n".format(display_name)
        if item_type == "AXE":
            line3 = "  material: DIAMOND_AXE\n"
        elif item_type == "SWORD":
            line3 = "  material: DIAMOND_SWORD\n"
        elif item_type == "PICKAXE":
            line3 = "  material: DIAMOND_PICKAXE\n"
        elif item_type == "SHOVEL":
            line3 = "  material: DIAMOND_SHOVEL\n"
        elif item_type == "HOE":
            line3 = "  material: DIAMOND_HOE\n"
        elif item_type == "PAPER":
            line3 = "  material: PAPER\n"
        elif item_type == "BOW":
            line3 = "  material: BOW\n"
        elif item_type == "CROSSBOW":
            line3 = "  material: CROSSBOW\n"
        elif item_type == "CUSTOM":
            line3 = "  material: {0}\n".format(material)
        if injectID == "N" or injectID == "n":
            line4 = "  injectID: false\n"
        else:
            line4 = ""
        if isGenModel == True:
            line5 = "  Pack:\n    generate_model: false\n    model: {0}\n".format(model)
        else:
            if not modelType:
                line5 = "  Pack:\n    generate_model: true\n    parent_model: \"item/generated\"\n    textures:\n      - {1}\n".format(modelType, texture)
            else:
                line5 = "  Pack:\n    generate_model: true\n    parent_model: \"{0}\"\n    textures:\n      - {1}\n".format(modelType, texture)
            if item_type == "BOW" or item_type == "CROSSBOW":
                line5 - "  Pack:\n    generate_model: false\n    model: \"{0}\"\n    pulling_models:\n      - {1}\n      - {2}\n      - {3}\n".format(bowModel, bpmStage0, bpmStage1, bpmStage2)
        f.writelines([line1,line2,line3,line4,line5])
        if damage:
            line6 = "  durability: {0}".format(damage)
            f.write(line6)
        f.close()
    print("Do you want to add custom Item Flags?\nThe flags will allow you to customize some properties of the item such as where your item can be placed, etc.\nItemGen will guide you though it.")
    yorn = input(">> [Y/n] ")
    if yorn == "Y" or yorn == "y":
        with open('generated.txt', 'a') as f:
            f.write("  ItemFlags:\n")
            f.close()
        ItemFlagEditor()
    print("Do you want to add a lore to your item?")
    yorn2 = input(">> [Y/n] ")
    if yorn2 == "Y" or yorn2 == "y":
        with open('generated.txt', 'a') as f:
            f.write("  lore:\n")
            f.close()
        LoreEditor()
    print("Do you want to add additional Attribute Modifiers?")
    print("This will allow you to set custom properties for your item. \nItemGen will guide you though it.")
    yorn3 = input(">> [Y/n] ")
    if yorn3 == "Y" or yorn3 == "y":
        with open('generated.txt', 'a') as f:
            f.writelines("  AttributeModifiers:\n")
            f.close()
        AttributeModifiersEditor()
    print("Do you want to add potion effects to your item?\nThis will allow you to set what effect to give the player when your item is used.")
    yorn4 = input(">> [Y/n] ")
    if yorn4 == "Y" or yorn4 == "y":
        with open('generated.txt', 'a') as f:
            f.write("  PotionEffects:\n")
            f.close()
        PotionEffectEditor()
    print("Do you want to exclude this item from Oraxen's inventory?\nLeave blank will set it to false, you can still get the item by using Oraxen's give command if you set it to true.")
    excludeInv = input(">> [Y/n] ")
    print("Want to make this item unbreakable? Leave blank will set it to false.")
    unbreakable = input(">> [Y/n] ")
    with open('generated.txt', 'a') as f:
        if excludeInv == "Y" or excludeInv == "y":
            line7 = "  excludeFromInventory: true\n"
        else:
            line7 = ""
        if unbreakable == "Y" or unbreakable == "y":
            line8 = "  unbreakable: true\n"
        else:
            line8 = ""
        f.writelines([line7,line8])
        f.close()
    print("Do you want to add Pre Enchantments to your item?\nThese enchantments will comes with your items at the start.")
    yorn6 = input(">> [Y/n] ")
    if yorn6 == "Y" or yorn6 == "y":
        with open('generated.txt', 'a') as f:
            f.write("  Enchantments:")
            f.close()
        PreEnchantmentsEditor()
    print("Do you want to add mechanics to your item? This allow your item to have special behavior.\nItemGen will guide you though it. (Leave blank to ignore)")
    yorn10 = input(">> [Y/n] ")
    if yorn10 == "Y" or yorn10 == "y":
        with open('generated.txt', 'a') as f:
            f.write("  Mechanics:\n")
            f.close()
        print("Do you want to add durability to your item? Leave blank to ignore.")
        yorn9 = input(">> [Y/n] ")
        if yorn9 == "Y" or yorn9 == "y":
            print("Enter the durability.")
            durability = input(">> Durability: ")
            with open('generated.txt', 'a') as f:
                line9 = "    durability:\n      value: {0}\n".format(durability)
                f.write(line9)
                f.close()
        print("Do you want to make your item repairable? Leave blank will ignore this.")
        yorn8 = input(">> [Y/n] ")
        if yorn8 == "Y" or yorn8 == "y":
            print("Enter the repair ratio.")
            ratio = input(">> Ratio: ")
            print("How much durability point you want to add when repaired?")
            durabilityPoint = input(">> Durability Point: ")
            with open('generated.txt', 'a') as f:
                line10 = "    repair:\n      ratio: {0}\n      fixed_amount: {1}\n".format(ratio, durabilityPoint)
                f.write(line10)
                f.close()
        print("Do you want to execute command when the item is used?")
        yorn11 = input(">> [Y/n] ")
        if yorn11 == "Y" or yorn11 == "y":
            print("Enter command cooldown (Delay between execution). Leave blank to ignore it.")
            cooldown = input(">> Execution Cooldown: ")
            print("Enter the permission needed to execute the command. Leave blank to ignore it.")
            permission = input(">> Execution Permission: ")
            print("Should the amount decrease when used? Leave blank will set it to false.")
            decreaseAmount = input(">> [Y/n] ")
            with open('generated.txt', 'a') as f:
                line11 = "    commands:\n"
                if cooldown:
                    line12 = "      cooldown: {0}\n".format(cooldown)
                else:
                    line12 = ""
                if permission:
                    line13 = "      permission: {0}\n".format(permission)
                else:
                    line13 = ""
                if decreaseAmount == "Y" or decreaseAmount == "y":
                    line14 = "      one_usage: true\n"
                else:
                    line14 = "      one_usage: false\n"
                f.writelines([line11,line12,line13,line14])
                f.close()
            CommandMechanicEditor()
        print("Do you want to show an aura when player is holding the item? (a.k.a, cool particles effect when holding the item)")
        yorn12 = input(">> [Y/n] ")
        if yorn12 == "Y" or yorn12 == "y":
            print("Enter the particle type. Available types are \"simple\", \"ring\" and \"helix\". \"simple\" will be used as default.")
            partType = input(">> Particle Type: ")
            print("Enter the particle that will be shown. A complete list of that can be found here https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html")
            partShow = input(">> Particle: ")
            with open('generated.txt', 'a') as f:
                if not partType:
                    line16 = "    aura:\n      type: simple\n      particle: {0}\n".format(partShow)
                else:
                    line16 = "    aura:\n      type: {0}\n      particle: {1}\n".format(partType, partShow)
                f.write(line16)
                f.close()
        print("Do you want your item to be wearable in your head? (HAT). Leave blank to ignore.")
        yorn13 = input(">> [Y/n] ")
        if yorn13 == "Y" or yorn13 == "y":
            with open('generated.txt', 'a') as f:
                f.write("    hat:\n      enabled: true\n")
                f.close()
        print("Do you want the player to have a chance to keep the item when they die? (Only keeping this item)")
        yorn14 = input(">> [Y/n] ")
        if yorn14 == "Y" or yorn14 == "y":
            with open('generated.txt', 'a') as f:
                f.write("    soulbound:\n")
                f.close()
            print("Specify the lose chance (optional).\nThis will make the player still have a chance to lose the item. Default set to 0.")
            loseChance = input(">> Lose Chance: ")
            with open('generated.txt', 'a') as f:
                if not loseChance:
                    line1 = "      lose_chance: 0\n"
                else:
                    line1 = "      lose_chance: {0}".format(loseChance)
                f.write(line1)
                f.close()
        print("Do you want to add advanced mechanics? These mechanics will applies to some specific type of your item.\nIt allow you to even make your item more cooler. Leave blank to ignore.")
        yorn15 = input(">> [Y/n] ")
        if yorn15 == "Y" or yorn15 == "y":
            print("Do you want your item to throw lighting bolts when used? Leave blank to ignore.")
            yorn16 = input(">> [Y/n] ")
            if yorn16 == "Y" or yorn16 == "y":

            print("Do you want your item to steal enemy's hearts when hit? Leave blank to ignore.")
            yorn17 = input(">> [Y/n] ")
            if yorn17 == "Y" or yorn17 == "y":
                
            print("Do you want to create a cone of particles to attack enemies? Leave blank to ignore.")
            yorn18 = input(">> [Y/n] ")
            if yorn18 == "Y" or yorn18 == "y":
                
            print("Do you want your item to launch wither skulls when right clicking? Leave blank to ignore.")
            yorn19 = input(">> [Y/n] ")
            if yorn19 == "Y" or yorn19 == "y":
                
            print("Do you want your item to automatically recolt and replant wheat when havesting? (ONLY APPLIES TO ITEM TYPE HOE.\nLeave blank to ignore.")
            yorn20 = input(">> [Y/n] ")
            if yorn20 == "Y" or yorn20 == "y":
                
            print("Do you want to mine blocks in a certin radius when used? (ONLY APPLIES TO ITEM TYPE PICKAXE).\nLeave blank to ignore. Useful if you are going to create hammers.")
            yorn21 = input(">> [Y/n] ")
            if yorn21 == "Y" or yorn21 == "y":
                
            print("Do you want to automatically smelt Iron Ore and Gold Ore when mine? (ONLY APPLIES TO ITEM TYPE PICKAXE).\nLeave blank to ignore.")
            yorn22 = input(">> [Y/n] ")
            if yorn22 == "Y" or yorn22 == "y":
                
            print("Do you want your item to convert a certin amount of your Experience into Bottle of Experience when used?\nLeave blank to ignore.")
            yorn23 = input(">> [Y/n] ")
            if yorn23 == "Y" or yorn23 == "y":
                
            print("Do you want your item to have the ability to break bedrock? Leave blank to ignore.")
            yorn24 = input(">> [Y/n] ")
            if yorn24 == "Y" or yorn24 == "y":
                
    print("Done! Generated config are in your current working directory with the name \"generated.txt\"")

if __name__ == '__main__':
    print("Oraxen Custom Items Config Generator")
    print("==============VERSION 0.0.1==================")
    Generator()
