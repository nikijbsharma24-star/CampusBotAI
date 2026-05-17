def college_helpdesk_bot():
    print("🎓 College Helpdesk Chatbot\nAsk about Admissions, Exams, Hostel, Fees, or Facilities.\nType 'bye' to exit\n" + "-"*50)

    responses = {
        "admission": "Admission process: 1. Fill online form 2. Entrance test 3. Counselling. Deadline: 30th June. Fees: 1.2L/year. Docs: 10th/12th, Aadhar, photos.",
        "exam": "Mid-sem exams from 15th Nov 2026. Date sheet on portal. Results in 3 weeks. Exam form deadline: 10th Oct.",
        "hostel": "Hostel: AC 1.2L/year, Non-AC 80k/year. Includes Mess, WiFi, Gym, Security. Allotment is merit-based.",
        "fees": "B.Tech Fees: 1.2L/year + 20k charges. Merit scholarship 50% for top 10%. Pay online in 2 installments.",
        "library": "Library: 8AM-10PM, Sun closed. 50k+ books.",
        "canteen": "2 Canteens: 8AM-8PM. Veg & Non-veg available.",
        "sports": "Sports: Cricket, Basketball, Gym. 6AM-9PM.",
        "wifi": "Free WiFi for students. Login with student ID.",
        "bus": "Bus service on 5 routes. Pass: 2000/month.",
        "hi": "Hello! How can I help with Admissions, Exams, Hostel, or Fees?",
        "thanks": "You're welcome! Anything else?"
    }

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input in ["bye", "exit", "quit"]:
            print("Bot: Thank you! Good luck 👍")
            break
        if not user_input:
            print("Bot: Please type something 😅")
            continue

        for key in responses:
            if key in user_input or (key == "admission" and any(w in user_input for w in ["apply", "form", "deadline"])) or \
               (key == "exam" and any(w in user_input for w in ["result", "schedule", "date sheet"])) or \
               (key == "hostel" and any(w in user_input for w in ["room", "mess", "accommodation"])) or \
               (key == "fees" and any(w in user_input for w in ["scholarship", "payment"])) or \
               (key == "hi" and any(w in user_input for w in ["hello", "hey"])) or \
               (key == "thanks" and "thank" in user_input):
                print(f"Bot: {responses[key]}")
                break
        else:
            print("Bot: Sorry, I didn't understand. Ask about Admissions, Exams, Hostel, Fees, or Facilities.")

if __name__ == "__main__":
    college_helpdesk_bot()
