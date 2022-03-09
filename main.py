def get_fragrance_fresh(f1,f2,f3):
    for key, value in male_fragrances["Clean fresh"].items():
        if {f1,f2,f3} == value:
            return key
    return "There is no such Fragrance"
def get_fragrance_sweet(s1,s2,s3):
    for key, value in male_fragrances["Sweet sexy"].items():
        if {s1,s2,s3} == value:
            return key
    return "There is no such Fragrance"
def get_fragrance_bold(b1,b2,b3):
    for key, value in male_fragrances["Bold loud"].items():
        if {b1,b2,b3} == value:
            return key
    return "There is no such Fragrance"

male_fragrances = {
    "Clean fresh": {
        "Prada L'homme L'Eau": {"iris","ginger","powder"},
        "Dior Homme Cologne": {"bergamot","blossom","musk"},
        "Versace Pour Homme": {"bergamot","neroli","tonka"},
        "Azzaro Chrome": {"rosemary","pineapple","neroli"},
        "Ermenegildo Zegna Uomo": {"violet leafs","vetiver","cedar"},
        "Bleu de Channel": {"grapefruit","ginger","incense"},
        "Dior Sauvage": {"bergamot","lavender","ambroxan"},
        "Aqua di Gio Profondo": {"rosemary","cypress","aquatic"},
        "Montblanc Individuel": {"raspberry","jasmine","sandalwood"},
        "Guerlain L'homme Cologne": {"grapefruit","almond","musk"}
        },
    "Sweet sexy": {
        "Dior Homme Intense": {"iris","ambrette","cedar"},
        "Prada Luna Rossa Black": {"bergamot","amber","tonka"},
        "Armani Code Absolu": {"tonka","vanila","suede"},
        "Yves Saint Laurent Y Parfum": {"grapefruit","tonka","geranium"},
        "Versace Oud Noir": {"pepper","safron","cardamom"},
        "Versace Eros": {"mint","apple","tonka"},
        "Guerlain L'homme Eau de Parfum": {"cherry","almond","leather"},
        "Jean Paul Gualtier Le Male": {"lavender","cinnamon","vanila"},
        "Azzaro Wanted by Night ": {"orange","cinnamon","cedar"},
        "Dolce & Gabbana The One Intense": {"cardamom","amber","tobacco"}
        },
    "Bold loud": {
        "Tomford Tobacco Vanille": {"tobacco","vanila","cacao"},
        "Tomford Tobacco Oud": {"oud","tobacco","cinnamon"},
        "Bentley for Men Intense": {"leather","rum","incense"},
        "Paco Rabbane 1 Million Parfum": {"grapefruit","leather","tonka"},
        "Mugler A*Men Pure Havane": {"Honey","tobacco","amber"},
        "Jean Paul Gaultier Ultra Male": {"bergamot","cinnamon","amber"},
        "Dior Homme Parfum": {"iris","leather","ambrette"},
        "Maison Francis Kurkdjian Baccarat Rouge 540": {"almond","cedar","ambergris"},
        "Armani Code Profumo": {"tonka","amber","cardamom"},
        "Salvatore Ferragamo Uomo Signature": {"cinnamon","tonka","coffee"}
        }
    }


ques_1 = input("What fragrance gender [male or female] would you like to have?")

while ques_1 != "male" and ques_1 != "female":
    ques_1 = input("Enter you answer again")
if ques_1 == "male":
    print("I will return the male list.")
    ques_2 = input("What do you want to smell like [Fresh clean, Sweet sexy, or Bold loud]?")

    if ques_2 == "Fresh clean":
        print("Your clean fresh fragrane will be right up, ",
            "answer a few more question.")

        small_ques1 = input("What is your style [playful, formal, etc.]?")
        if small_ques1 == "playful":
            note1 = "raspberry"
        elif small_ques1 == "badass":
            note1 = "cypress"
        elif small_ques1 == "formal":
            note1 = "iris"
        elif small_ques1 == "sexy":
            note1 = "grapefruit"
        elif small_ques1 == "timeless":
            note1 = "vetiver"
        elif small_ques1 == "unique":
            note1 = "pineapple"
        elif small_ques1 == "casual":
            note1 = "bergamot"

        small_ques2 = input("What message do you want to send to the world?")
        if small_ques2 == "successful":
            note2 = "neroli"
        elif small_ques2 == "confident":
            note2 = "musk"
        elif small_ques2 == "lovely":
            note2 = "lavender"
        elif small_ques2 == "classy":
            note2 = "sandalwood"
        elif small_ques2 == "normal":
            note2 = "aquatic"
        elif small_ques2 == "mature":
            note2 = "incense"
        elif small_ques2 == "introvert":
            note2 = "violet leafs"
        elif small_ques2 == "careful":
            note2 = "powder" 

        small_ques3 = input("What type of smell do you prefer [woody, citrusy, aromatic, spicy, etc.]?")
        if small_ques3 == "woody":
            note3 = "cedar"
        elif small_ques3 == "modern":
            note3 = "blossom"
        elif small_ques3 == "soft":
            note3 = "ginger"
        elif small_ques3 == "spicy":
            note3 = "rosemary"
        elif small_ques3 == "creamy":
            note3 = "almond"
        elif small_ques3 == "blue":
            note3 = "ambroxan"
        elif small_ques3 == "green":
            note3 = "jasmine"
        elif small_ques3 == "seductive":
            note3 == "tonka"
        print(get_fragrance_fresh(note1,note2,note3))

    elif ques_2 == "Sweet sexy":
        print("Your sweet and sexy fragrane will be right up, ",
            "answer a few more question.")
        small_ques1 = input("What is your style [playful, formal, etc.]?")
        if small_ques1 == "playful":
            note1 = "tonka"
        elif small_ques1 == "badass":
            note1 = "tobacco"
        elif small_ques1 == "formal":
            note1 = "iris"
        elif small_ques1 == "sexy":
            note1 = "almond"
        elif small_ques1 == "timeless":
            note1 = "neroli"
        elif small_ques1 == "unique":
            note1 = "ambrette"
        elif small_ques1 == "casual":
            note1 = "bergamot"
        small_ques2 = input("What message do you want to send to the world?")
        if small_ques2 == "successful":
            note2 = ""
        elif small_ques2 == "confident":
            note2 = ""
        elif small_ques2 == "lovely":
            note2 = ""
        elif small_ques2 == "risk-taker":
            note2 = ""
        elif small_ques2 == "introvert":
            note2 = ""
        elif small_ques2 == "normal":
            note2 = ""
        elif small_ques2 == "mature":
            note2 = ""
        small_ques3 = input("What type of smell do you prefer [woody, citrusy, aromatic, spicy, etc.]?")
        if small_ques3 == "woody":
            note3 = ""
        elif small_ques3 == "citrusy":
            note3 = ""
        elif small_ques3 == "spicy":
            note3 = ""
        elif small_ques3 == "warm":
            note3 = ""
        elif small_ques3 == "green":
            note3 = ""
        elif small_ques3 == "brisk":
            note3 = ""
        elif small_ques3 == "blue":
            note3 = ""

else:
    print("I will return the female list.")
    ues_2 = input("What mood would you like your fragrance to have?")
    if ques_2 == "fresh-clean":
        print("Your clean and fresh fragrance will be right up")
    ques_3 = input("What is your style [street, elegant, etc.]?")
   

