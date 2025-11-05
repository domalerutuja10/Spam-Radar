function getBotResponse(input) {
    //questions-responses
    if (input == "what if we give OTP to someone?") {
        return "you are duped into revealing OTP to fraudster on call/Sms/email";
    } else if (input == "what spam radar actually do?") {
        return "Spam radar is a software which tells that whether the messagfe is spam or not";
     } else if (input == "why the cyber security is important?") {
        return "Cybersecurity is critical because it helps to protect organizations and individuals from cyber attacks. Cybersecurity can help to prevent data breaches, identity theft, and other types of cybercrime.";
    }

    // simple responses
    if (input == "cyber security") {
        return "Cyber security refers to every aspect of protecting an organization and its employees and assets against cyber threats. As cyberattacks become more common and sophisticated and corporate networks grow more complex, a variety of cyber security solutions are required to mitigate corporate cyber risk.";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}