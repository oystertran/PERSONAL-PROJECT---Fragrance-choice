def get_fragrance_fresh_male(f1,f2,f3):
    for key, value in male_fragrances["Clean fresh"].items():
        if {f1,f2,f3} == value:
            return key
    return "There is no such Fragrance"
def get_fragrance_sweet_male(s1,s2,s3):
    for key, value in male_fragrances["Sweet sexy"].items():
        if {s1,s2,s3} == value:
            return key
    return "There is no such Fragrance"

def get_fragrance_fresh_female(f1,f2,f3):
    for key, value in female_fragrances["Clean fresh"].items():
        if {f1,f2,f3} == value:
            return key
    return "There is no such Fragrance"
def get_fragrance_sweet_female(s1,s2,s3):
    for key, value in female_fragrances["Sweet sexy"].items():
        if {s1,s2,s3} == value:
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
        "Prada Luna Rossa Black": {"citrus","amber","tonka"},
        "Armani Code Absolu": {"tonka","vanilla","suede"},
        "Yves Saint Laurent Y Parfum": {"citrus","tonka","geranium"},
        "Versace Oud Noir": {"pepper","safron","cardamom"},
        "Versace Eros": {"mint","citrus","tonka"},
        "Guerlain L'homme Eau de Parfum": {"cherry","almond","leather"},
        "Jean Paul Gualtier Le Male": {"lavender","cinnamon","vanilla"},
        "Azzaro Wanted by Night ": {"orange","cinnamon","cedar"},
        "Dolce & Gabbana The One Intense": {"cardamom","amber","tobacco"}
        }
    }

female_fragrances = {
    "Clean fresh": {
        "Prada La Femme": {"bergamot","Ylang-Ylang","vanilla"},
        "Chanel Chance Eau Tendre": {"grapefruit","jasmine","cedar"},
        "Hermes Twilly D'Hermes": {"bergamot","tuberose","sandalwood"},
        "Chanel Coco Madamoiselle": {"bergamot","Ylang-Ylang","tonka"},
        "Dolce & Gabbana Light Blue Eau Intense": {"bergamot","jasmine","musk"},
        "Jo Malone Wood Sage & Sea Salt": {"sea salt","grapefruit","sage"},
        "Chanel Gardenia": {"orange blossom","tuberose","sandalwood"},
        "Amouage Reflection Woman": {"water violet","jasmine","amber"},
        "Dior Pure Poison": {"bergamot","orange blossom","sandalwood"},
        "Kayali Citrus 08": {"grapefruit","rose","tonka"}
        },
    "Sweet sexy": {
        "Mon Guerlain": {"lavender","jasmine","vanilla"},
        "Lancome La Vie Est Belle": {"black currant","iris","vanilla"},
        "Dior Poison Girl": {"bregamot","rose","tonka"},
        "Jean Paul Gaultier Scandal": {"blood orange","honey","caramel"},
        "Carolina Herrera Good Girl": {"almond","rose","cacao"},
        "Ariana Grande Cloud": {"bergamot","coconut","musk"},
        "Aqualina Pink Sugar": {"bergamot","tuberose","vanilla"},
        "Britney Spear Fantasy": {"kiwi","jasmine","musk"},
        "Paco Rabanne Olympea": {"jasmine","sandalwood","vanilla"},
        "Tomford Lost Cherry": {"cherry","rose","vanilla"}
        }
    }

ques_1 = input("What fragrance gender [male or female] would you like to have?").lower()

while ques_1 != "male" and ques_1 != "female":
    ques_1 = input("Enter you answer again").lower()
if ques_1 == "male":
    print("I will return the male list.")
    ques_2 = input("What do you want to smell like [Fresh clean or Sweet sexy]?").lower()
    if ques_2 == "fresh clean":
        print("Your clean fresh fragrane will be right up,",
            "answer a few more question.")
        small_ques1 = input("What is your style?").lower()
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

        small_ques2 = input("What mood do you want your fragrance to have?").lower()
        if small_ques2 == "successful":
            note2 = "neroli"
        elif small_ques2 == "confident":
            note2 = "musk"
        elif small_ques2 == "sophisticated":
            note2 = "lavender"
        elif small_ques2 == "happy":
            note2 = "sandalwood"
        elif small_ques2 == "bright":
            note2 = "aquatic"
        elif small_ques2 == "rich":
            note2 = "incense"
        elif small_ques2 == "light":
            note2 = "violet leafs"
        elif small_ques2 == "powdery":
            note2 = "powder" 

        small_ques3 = input("What approaching do you want your fragrance to have?").lower()
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
        elif small_ques3 == "floral":
            note3 = "jasmine"
        elif small_ques3 == "seductive":
            note3 == "tonka"
        print(get_fragrance_fresh_male(note1,note2,note3))

    elif ques_2 == "sweet sexy":
        print("Your sweet and sexy fragrane will be right up, ",
            "answer a few more question.")
        small_ques1 = input("What is your style [playful, formal, etc.]?").lower()
        if small_ques1 == "playful":
            note1 = "tonka"
        elif small_ques1 == "badass":
            note1 = "leather"
        elif small_ques1 == "formal":
            note1 = "lavender"
        elif small_ques1 == "masculine":
            note1 = "tobacco"
        elif small_ques1 == "timeless":
            note1 = "cedar"
        elif small_ques1 == "casual":
            note1 = "pepper"
        
        small_ques2 = input("What mood do you want your fragrance to have?").lower()
        if small_ques2 == "successful":
            note2 = "iris"
        elif small_ques2 == "cozy":
            note2 = "cinnamon"
        elif small_ques2 == "sexy":
            note2 = "cherry"
        elif small_ques2 == "fruity":
            note2 = "bergamot"
        elif small_ques2 == "spicy":
            note2 = "cardamom"
        elif small_ques2 == "uplifting":
            note2 = "citrus"
        elif small_ques2 == "rich":
            note2 = "suede"
        
        small_ques3 = input("What type of smell do you prefer?").lower()
        if small_ques3 == "woody":
            note3 = "amber"
        elif small_ques3 == "citrusy":
            note3 = "orange"
        elif small_ques3 == "warm":
            note3 = "almond"
        elif small_ques3 == "bright":
            note3 = "mint"
        elif small_ques3 == "brisk":
            note3 = "vanilla"
        elif small_ques3 == "blue":
            note3 = "safron"
        elif small_ques3 == "floral":
          note3 = "geranium"
        elif small_ques3 == "nutty":
          note3 = "ambrette"
        print(get_fragrance_sweet_male(note1,note2,note3))


else:
    print("I will return the female list.")
    ques_2 = input("What do you want to smell like [Fresh clean or Sweet sexy]?").lower()
    if ques_2 == "fresh clean":
        print("Your clean fresh fragrane will be right up,",
            "answer a few more question.")

        small_ques1 = input("What is your style?").lower()
        if small_ques1 == "playful":
            note1 = "water violet"
        elif small_ques1 == "formal":
            note1 = "orange blossom"
        elif small_ques1 == "sexy":
            note1 = "rose"
        elif small_ques1 == "timeless":
            note1 = "cedar"
        elif small_ques1 == "unique":
            note1 = "sea salt"
        elif small_ques1 == "casual":
            note1 = "bergamot"

        small_ques2 = input("What mood do you want your fragrance to have?").lower()
        if small_ques2 == "successful":
            note2 = "vanilla"
        elif small_ques2 == "confident":
            note2 = "tuberose"
        elif small_ques2 == "sophisticated":
            note2 = "blossom"
        elif small_ques2 == "happy":
            note2 = "sandalwood"
        elif small_ques2 == "rich":
            note2 = "tonka"
        elif small_ques2 == "light":
            note2 = "jasmine"
        elif small_ques2 == "earthy":
            note2 = "sage" 

        small_ques3 = input("What approaching do you want your fragrance to have?").lower()
        if small_ques3 == "woody":
            note3 = "sandalwood"
        elif small_ques3 == "fruity":
            note3 = "grapefruit"
        elif small_ques3 == "smoky":
            note3 = "amber"
        elif small_ques3 == "blue":
            note3 = "musk"
        elif small_ques3 == "floral":
            note3 = "Ylang-Ylang"
        print(get_fragrance_fresh_female(note1,note2,note3))

    elif ques_2 == "sweet sexy":
        print("Your sweet and sexy fragrane will be right up, ",
            "answer a few more question.")
        small_ques1 = input("What is your style?").lower()
        if small_ques1 == "playful":
            note1 = "tonka"
        elif small_ques1 == "formal":
            note1 = "vanila"
        elif small_ques1 == "unique":
            note1 = "cacao"
        elif small_ques1 == "sexy":
            note1 = "honey"
        elif small_ques1 == "casual":
            note1 = "musk"
        
        small_ques2 = input("What mood do you want your fragrance to have?").lower()
        if small_ques2 == "successful":
            note2 = "iris"
        elif small_ques2 == "cozy":
            note2 = "jasmine"
        elif small_ques2 == "sexy":
            note2 = "cherry"
        elif small_ques2 == "fruity":
            note2 = "bergamot"
        elif small_ques2 == "rich":
            note2 = "caramel"
        elif small_ques2 == "creamy":
            note2 = "almond"
        
        small_ques3 = input("What type of smell do you prefer?").lower()
        if small_ques3 == "citrusy":
            note3 = "black currant"
        elif small_ques3 == "woody":
            note3 = "sandalwood"
        elif small_ques3 == "spicy":
            note3 = "lavender"
        elif small_ques3 == "green":
            note3 = "kiwi"
        elif small_ques3 == "powdery":
            note3 = "coconut"
        elif small_ques3 == "fruity":
            note3 = "blood orange"
        elif small_ques3 == "floral":
          note3 = "rose"
        print(get_fragrance_sweet_female(note1,note2,note3))
