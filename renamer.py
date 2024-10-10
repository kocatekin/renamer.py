import random
import os

def main():
    #formatname = input("which file format? enter such : txt \n")
    formatname = "mp4"
    for file in os.listdir():
        if file.endswith(formatname):
            os.rename(file, f"{rndfilename()}.{formatname}")


def rndfilename():
    adjectives = ["Brave", "Clever", "Fierce", "Quick", "Bold", "Quiet", "Loyal", "Noble", "Strong", "Sharp", "Calm", "Daring", "Gentle", "Wise", "Mighty", "Cunning", "Swift", "Brilliant", "Fearless", "Honest", "Patient", "Agile", "Diligent", "Radiant", "Vigilant", "Sturdy", "Fiery", "Bold", "Curious","Humble", "Jovial", "Keen", "Luminous", "Majestic", "Persistent", "Resilient", "Serene", "Tenacious","Unwavering", "Valiant", "Zesty", "Eager", "Inventive", "Prudent", "Sincere", "Truthful", "Vibrant", "Witty"]
    verbs = ["Running","Jumping", "Flying", "Dashing", "Exploring", "Building", "Guarding", "Crafting", "Hunting", "Searching","Swimming", "Climbing", "Dancing", "Hiding", "Sprinting", "Riding", "Lifting", "Writing", "Fighting","Shouting", "Singing", "Speaking", "Teaching", "Learning", "Painting", "Drinking", "Celebrating", "Escaping","Helping", "Marching", "Baking", "Weaving", "Forging", "Drawing", "Rescuing", "Healing", "Discovering", "Scouting", "Crafting", "Chasing", "Repairing", "Organizing", "Plotting", "Planning", "Training", "Dodging", "Casting"]
    names = ["Harry","Hermione", "Ron", "Dumbledore", "Snape", "Voldemort", "Frodo", "Aragorn", "Gandalf", "Sam","Legolas", "Gollum", "Bilbo", "Elrond", "Galadriel", "Tyrion", "Daenerys", "Jon", "Cersei","Sansa", "Bran", "Ned", "Jaime", "Tywin", "Theon", "Joffrey", "Brienne", "Drogo","Varys", "Ramsay", "Bronn", "Missandei", "Tormund", "Ygritte", "Hagrid", "Lupin", "Sirius","Bellatrix", "Draco", "Neville", "Cho", "Cedric", "Barty", "Dobby", "Fleur", "Ginny"]
    return f"{random.choice(adjectives)}{random.choice(verbs)}{random.choice(names)}"



main()
