import random

subjects= [
    "Salman Khan",
    "Doremon",
    "Baba Ramdev",
    "PM Modi",
    "Rahul Gandhi",
    "Ananya Pandey",
    "Kapil Sharma",
    "Munna Bhai MBBS",
    "Elon Musk",
    "Arvind Kejriwal",
    "Kangana Ranaut",
    "Virat Kohli",
    "Ranveer Singh",
    "Rajnikanth",
    "Alia Bhatt",
    "Zakir Khan",
    "Sunny Leone",
    "Shaktimaan",
    "Sanjay Dutt",
    "Bhuvan Bam",
    "Ambani Uncle",
    "Tony Kakkar",
    "Chandrayaan-3 Scientist",
    "Bigg Boss Contestant",
    "A drunk Minion",
    "Manmohan Singh (finally speaking)",
    "CID’s ACP Pradyuman",
    "Chhota Bheem",
    "Jethalal",
    "Taarak Mehta"
]

actions = [
    "eating wadapav",
    "selling pirated Netflix accounts",
    "dancing to ‘Naatu Naatu’",
    "doing Zumba in slow motion",
    "crying over tomato price hike",
    "running away from a cat",
    "hosting a gully cricket tournament",
    "fighting with an auto driver",
    "learning coding from ChatGPT",
    "doing makeup in a moving train",
    "painting walls with ketchup",
    "playing PUBG in real life",
    "arguing with a traffic signal",
    "opening a pani puri stall",
    "challenging Dhoni for a sprint race",
    "mimicking Arnab Goswami",
    "hiding behind a tree from fans",
    "binge-watching saas-bahu serials",
    "feeding samosas to pigeons",
    "taking selfies with potholes",
    "predicting weather by licking air",
    "doing yoga while skydiving",
    "drinking tea with a goat",
    "narrating horror stories to cows",
    "writing love letters to their laptop",
    "practicing rap in Sanskrit",
    "arguing with Siri",
    "singing lullabies to traffic policemen",
    "rehearsing a film with street dogs",
    "pretending to be Spiderman in rain"
]

places_or_things = [
    "at India Gate",
    "inside Mumbai local",
    "on top of Qutub Minar",
    "behind a dhobi ghat",
    "inside a Delhi metro ladies coach",
    "on the moon (virtually)",
    "under a vada pav stall",
    "in a panipuri eating contest",
    "near Ambani’s Antilia",
    "on a moving scooter",
    "in Bigg Boss bathroom",
    "outside a haunted house",
    "inside a washing machine showroom",
    "under a banyan tree",
    "in front of Mantralaya",
    "inside an old DD1 studio",
    "behind Raju Chaiwala’s tapri",
    "stuck in a mall elevator",
    "on the set of Taarak Mehta",
    "under a leaking water tank",
    "at Marine Drive with cows",
    "at the foot of Himalayas",
    "during a power cut in Bihar",
    "inside SRK’s Mannat compound",
    "in a Zoom meeting gone wrong",
    "on a banana peel rally",
    "beside a UFO landing site",
    "with aliens in Ladakh",
    "near a firecracker godown",
    "in front of a TikTok headquarters"
]


def generate_news():
   
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    return f"BREAKING NEWS: {subject} {action} {place_or_thing}"
        # return heading
        # print("\n"+ heading)
        # user_input = input("\nDo you want to generate again? (yes-no)").strip().lower()
        # if user_input == "no":
        #     break

    # print("Thanks for using fake news!!!")