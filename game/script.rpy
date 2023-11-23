# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n_nvl = Character("Takeshita", kind=nvl)
define e_nvl = Character("Ryoji", kind=nvl)
define f_nvl = Character("Odakatsu", kind=nvl)
define s_nvl = Character("Sara", kind=nvl)


define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

define i = Character("Interogerator")
define c = Character("Police Chief")
define e = Character("Police Man Kur")
define f = Character("Police Man Bara")
define p = Character("Furuya")
define t = Character("Thoughts")
define s = Character("Sara")


# The game starts here.

label start:

    # Music, Background and Sprites attribution + Story heavily inspired by "I was wrong" #
    # fishy project presents #
    # Chapter 0 : After All #

    scene police office


    show police man

    # These display lines of dialogue.

    i "So, What you say is... you guys were going back home and you tripped and caused her to fall infront of the Car. Correct?"

    p "y..yes"

    f "I think it's safe to say that he is tellling the truth. All the testimonies match, also the witness said the same thing. It's been three days since he has been here, I think this is substancial information to close this 'case' ."

    f "Boss just Let Him Go, I can't watch this anymore. That kid looks ready to cry any secound now."

    e "Chief? Anything you want me to question him about?"

    c "Look here Guys, I know what you want to tell me. But this is our Job. We have to do this, even for that innocent kid we need to make sure there is no trouble for him later in his Life."

    e " .... "

    f " .... "

    "Silence Envelops the Room just to be broken soon After by the Police Chief."

    c "However,  The case being that there is nothing more to ask . Let me tell the interrogator that he can let the kid go now."

    " The Chief turns on the Microphone to the Interrogeration Room"

    c "You May release him Now."

    " Upon hearing that, the investigator streaches his arm and breathes a sigh of relief and tells me in an informal tone."
    
    i "As you can hear, You can leave now."

    "I give him a slight nod. Still Trying to process my feelings. Seeing that he pitifully tells me."

    i " I'm sorry Kid. I would rather not do this as well, but it's to also ensure you don't have any trouble later"

    p "I understand."

    # walk from interrogation room to the main hall #

    "After I reached the main hall, I sat down onto a chair in the corner of the room. I saw a police man standing there. He looked at me and started walking towards me. "

    p " ... "

    f " Finally Done with this right?"

    p " Yeah... I think it's over. Thank You! "

    f " You know, I had a daughter a little smaller than you. But one day when I went to pick her up, she was not there. Next thing I know, I was informed she killed herself. So, I know how you feel right now."

    "You Don't Know How I feel."

    f " So, don't do anything rash kid. The person you are Missing won't want you to join them so soon."

    "You Are Wrong about that."

    p " T-Thank you.... I know that. I just need some time for myself right now."

    " The officer stands up and goes back to his room. "

    " Without waiting for my parents, I quietly walk back to my house."

    # Here You need TO add a sequence of going from the police office to the road to his home and room WITH sound #

    " I fall face down, onto the bed trying to figure out how I feel right now. "

    " I feel the phone buzz on the bed. "

    p "Oh! That's right!"

    "My girlfriend died."

    "My phone is continously flooded with messages from worried friends."

    nvl_narrator "You Have 99+ Unread Messages in the group!"
    n_nvl "You've been absent for 4 days. U okay bro?"
    e_nvl "I can tell the teacher if you're going to be away today..."
    f_nvl "C'mon dude. Check your messages"
    f_nvl "Let us know if you need any help."
    n_nvl "Reply to us dude, will you? We are all worried about you."
    nvl clear


    " It was an unfortunate accident. She got hit by a car."

    " I could'nt accept that my girlfriend was no longer in this world. That's why I have'nt gone to school for the past four days."

    " I thought I'd be able to see her everyday. I took that for granted. "

    " I wasn't able to do anything for her. "

    " That's what everyone thinks happened. "

    " But the truth is ..... "

    "  I killed her.  "

    # Chapter 1 : Back Then #

    # while shifting from classroom door to class in school#
    "Back then, I had no idea things would turn out this way." 
    
    #trying to put him out of the zoned out state#
    
    s "Hey, Furuya Kun..."
    s "Furuya KUN !!!"

    "Who called me just now?"
    p " O...! "
    "I see, it was Sara. Sara is the cutest girl at our school."

    s "Furuya-Kun you dropped your eraser."

    "I felt slightly nervous talking to her."
    p "Oh, Sorry about that."

    "As I looked at her holding my eraser my heart skipped a beat."
    p " ... "
    p " T-thank you...."

    " Ah! She smells like flowers today as well. "
    " She has long eyebrows that matched perfectly with her big round eyes. "
    " And with her kind voice. It was not a shock that she not only captivated me.."
    " but all the boys around her. "

    s "Furuya-kun, do you need to tell me something?"
    
    " Shit! I was staring at her this whole time. She must feel un-comfortable."

    p " Oh! I'm sorry, it's nothing. "

    s " Say Furuya-kun, "
    " She dropped her head down to the level of my ear and whispered. "
    s " Would you mind comming behind the store after school? "

    "I could'nt focus on a word she said. The way she whispered tickled my ears. Also she was so close to me that I could feel my clothes heating up. But she continued speaking."

    s " Will you? "
    " She spoke softly with pleading eyes. There was absolutely no way I would be able to say No, or would say No to her."

    p " Yes! I will."

    " She started to smile and gave me a suprised look, almost as if she was not expecting that. I did'nt want to get my hopes up, but with the way she told it there was no way I could keep my hopes low. "
    " I kept thinking, smirking and Imagining what she had called me for throughout the class. I was deep in thought."

    # bell rings here #
    p " Wha... The last class is over too."

    " I looked at Sara, who was looking at me. Sara averted her gaze and left the classroom in a rush. "

    " I quickly packed my bags and left the classroom in a hurry. As I got closer and closer to the gym, I could feel my body heat up and my heart making my breath longer and louder. "

    " I saw Sara's back, she was standing there waiting for me. I slowly walked to her and stood infront of her, flustered. "

    s " Uh.. Umm , Furuya-Kun... "
    s " I like you! Please go out with me. "

    " What? Really?"
    " I had tried so hard, I worked on my clothing, on my hair. I talked to her so much, but right now I can't accept this as reality."

    s " It's ok if you-"

    p " I like you too Sara! I will go out with you! "
    " Never in my wildest dreams did I think, She would confess her feelings to me. "
    " From the moment I realized that this wonderful girl would be my girlfriend, My head has been in the Clouds." 
    " That's Why I can't possibly wimp out in this situation. "

    s " I'm So happy about this. "
    p " Me too! "

    " She spoke with a slightly flustered and happy face. "
    s " Now we can stay together all day!"

    " After saying that she ran away, before I got to react to anything I felt my phone buzz in my pocket. "  

  
    nvl_narrator "You have a Message from Sara. "
    s_nvl " Don't follow me!!! "
    s_nvl " I'm too embarrased to talk to you. ミ⁠●⁠﹏⁠☉⁠ミ"
    s_nvl " I will text you back when I am at home amd clamd down."
    s_nvl " and* "
    s_nvl " calmed* "

    

    
    


    return
