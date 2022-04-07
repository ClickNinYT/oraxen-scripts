# Simple custom armor generator for Oraxen
# By ClickNin

# *actually this is really ez to write though*

from numpy import random
import os
import sys
import random
import uuid

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

def AttributeModifiersEditor(armor_type):
    print("Enter the attribute you want to add. \nA complete list of attributes supported by Spigot can be found at https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html")
    attribute = input(">> Attribute Name: ")
    print("Enter the attribute operation. \n0 for adding number (a.k.a, setting it)\n1 for adding scalar\n2 for multipling scalar 1\nChoosing 0 are prefered for most of people.")
    operation = input(">> Attribute Opeartion: ")
    print("Enter the value of the attribute you want to add.")
    value = input(">> Attribute Value: ")
    uuid_ = str(uuid.uuid4())
    if armor_type == "HELMET": slot = "HEAD"
    if armor_type == "CHESTPLATE": slot = "CHEST"
    if armor_type == "LEG": slot = "LEGS"
    if armor_type == "BOOT": slot = "FEET"
    with open('generated.txt', 'a') as f:
        line1 = "    - {{ name: \"oraxen\", attribute: {0}, amount: {1}, operation: {2},\n".format(attribute, value, operation)
        line2 = "        uuid: {0}, slot: {1} }}\n".format(uuid_, slot)
        f.writelines([line1, line2])
        f.close()
    print("Attribute(s) added! Do you want to add more?")
    yorn2 = input(">> [Y/n] ")
    if yorn2 == "Y" or yorn2 == "y":
        AttributeModifiersEditor(armor_type)
    else:
        return

def Generator():
    print("Enter the raw name of the armor below, this will be used in Oraxen config.")
    raw_name = input(">> Raw name: ")
    print("Enter the Display Name of the armor below, this will be used for armor's ingame display name.")
    display_name = input(">> Display name: ")
    print("Enter your Armor type (material) below, valid values are HELMET, CHESTPLATE, LEG and BOOT.")
    armor_type = input(">> Armor type: ")
    print("Enter the RBG value you want below (R, B, G), leave blank to randomize it.")
    color = input(">> RBG value: ")
    if not color:
        color = "{0}, {1}, {2}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    with open('generated.txt', 'a') as f:
        line1 = "{0}: \n".format(raw_name)
        line2 = "  displayname: '{0}' \n".format(display_name)
        if armor_type == "HELMET":
            line3 = "  material: LEATHER_HELMET\n"
        if armor_type == "CHESTPLATE":
            line3 = "  material: LEATHER_CHESTPLATE\n"
        if armor_type == "LEG":
            line3 = "  material: LEATHER_LEGGINGS\n"
        if armor_type == "BOOT":
            line3 = "  material: LEATHER_BOOTS\n"
        line4 = "  color: {0}\n".format(color)
        f.writelines([line1, line2, line3, line4])
        f.close()
    print("Do you want to add a lore to your armor?")
    yorn4 = input(">> [Y/n] ")
    if yorn4 == "Y" or yorn4 == "y":
        with open('generated.txt', 'a') as f:
            f.seek(0)
            f.writelines("  lore:\n")
            f.close()
        LoreEditor()
    print("Enter your armor's durability below.")
    durability = input(">> Durability: ")
    print("Enter the texture path to your armor below.")
    texture = input(">> Texture: ")
    with open('generated.txt', 'a') as f:
        line7 = "  Pack:\n    generate_model: true\n    parent_model: \"item/generated\"\n    textures:\n      - {0}\n      - {1}\n".format(texture, texture)
        f.write(line7)
        if durability:
            line6 = "  Mechanics:\n    durability:\n      value: {0}\n".format(durability)
            f.writelines(line6)
        f.close()
    print("Do you want to add additional Attribute Modifiers?")
    print("This will allow you to set custom properties for your armor. \nArmorGen will guide you though it.")
    yorn = input(">> [Y/n] ")
    if yorn == "Y" or yorn == "y":
        with open('generated.txt', 'a') as f:
            f.writelines("  AttributeModifiers:\n")
            f.close()
        AttributeModifiersEditor(armor_type)
    print("Done! Generated config are in your current working directory\nwith the name \"generated.txt\"")

if __name__ == '__main__':
    print("Oraxen Custom Armor Config Generator")
    print("==============VERSION 0.0.1==================")
    Generator()
