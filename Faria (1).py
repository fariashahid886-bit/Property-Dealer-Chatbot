print("================================")
print("     CHATBOT       ")
print("================================")
print("Type 'help' to see what you can ask, or 'bye' to exit.")

while True:
    question = input("\nAsk something about my Baba: ").lower()

    if "help" in question:
        print("You can ask about: name, age, city, food, or his personality.")

    elif "name" in question:
        print("His name is Muhammad Shahid.")

    elif "age" in question:
        print("He is 45 years old.")

    elif "city" in question:
        print("He lives in the beautiful city of Multan.")

    elif "food" in question:
        print("His favorite food is simple and healthy—he loves a good plate of Sabzi!")

    elif "personality" in question or "angry" in question or "mood" in question:
        print("Haha, well... let’s just say he’s a bit of an 'Angry Bird'! He can be quick-tempered, but his heart is in the right place.")
    
    elif "work" in question or "routine" in question:
        print("He's a very hardworking man. He usually stays busy with his daily routine, keeping everything in order.")

    elif "advice" in question or "wisdom" in question:
        print("He’s very direct. If you ask for advice, he’ll give you the truth, even if it’s tough to hear. But it always helps.")

    elif "hobby" in question or "fun" in question:
        print("He keeps it simple! He enjoys relaxing, observing things, and sometimes just enjoying his peace.")

    elif "relationship" in question or "close" in question:
        print("We have a real bond. Even though he’s an 'Angry Bird', we understand each other perfectly.")

    elif "multan" in question:
        print("He loves the culture and the people of Multan. He says there’s no place like home.")
    
    elif "morning" in question:
        print("He's an early riser—the house is always quiet and peaceful when he starts his day.")
    
    elif "Daily routine" in question:
        print("Vo ghr pr ami k sath kam krwata han!")
    
    elif "bad news" in question or "problem" in question:
        print("He keeps a cool head. Even when things go wrong, he tries to stay focused on the solution.")
        
    elif "laugh" in question:
        print("When he actually does laugh, it’s infectious! It’s rare, so it always makes the moment special.")
        
    elif "work ethic" in question or "hard work" in question:
        print("He believes that if you're going to do something, you should do it with full honesty.")
        
    elif "future" in question:
        print("He is very optimistic. He always tells me that hard work today will pay off tomorrow.")
        
    elif "people" in question or "company" in question:
        print("He loves spending time with people who are genuine. He doesn't like show-offs.")
        
    elif "quiet" in question or "peace" in question:
        print("He values his 'me-time.' Sometimes he just likes to sit quietly and reflect on his thoughts.")
        
    elif "childhood" in question:
        print("He sometimes tells stories about Multan from back in the day—it’s like listening to a different era.")
        
    elif "strength" in question:
        print("His consistency. Even when he's being an 'Angry Bird,' you know exactly where you stand with him.")

    elif "bye" in question:
        print("Goodbye! Take care.")
        break

    else:
        print("I'm not sure about that. Try asking 'help' to see what you can ask me!")