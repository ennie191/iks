def get_shlokas():
    """
    Returns a list of Sanskrit shlokas organized by categories
    Each shloka has explanations in multiple languages
    
    Returns:
        list: A list of category dictionaries, each containing shlokas
    """
    categories = [
        {
            "id": "mathematics",
            "name": "Mathematics",
            "shlokas": [
                {
                    "id": "math_1",
                    "sanskrit": "एकं च दश च शतं च सहस्रं चायुतं च नियुतं च प्रयुतम्‌ ।",
                    "transliteration": "Ekam cha dasha cha shatam cha sahasram chayutam cha niyutam cha prayutam.",
                    "explanations": {
                        "english": "This shloka describes the decimal place value system in Sanskrit. It refers to one, ten, hundred, thousand, ten thousand, hundred thousand, and million.",
                        "hindi": "यह श्लोक संस्कृत में दशमलव स्थान मूल्य प्रणाली का वर्णन करता है। यह एक, दस, सौ, हजार, दस हजार, लाख और दस लाख को संदर्भित करता है।",
                        "marathi": "हा श्लोक संस्कृतमध्ये दशमान पद्धतीचे वर्णन करतो. एक, दहा, शंभर, हजार, दहा हजार, लाख आणि दहा लाख यांचा उल्लेख केला आहे.",
                        "kannada": "ಈ ಶ್ಲೋಕವು ಸಂಸ್ಕೃತದಲ್ಲಿ ದಶಮಾಂಶ ಸ್ಥಾನ ಮೌಲ್ಯ ವ್ಯವಸ್ಥೆಯನ್ನು ವಿವರಿಸುತ್ತದೆ. ಇದು ಒಂದು, ಹತ್ತು, ನೂರು, ಸಾವಿರ, ಹತ್ತು ಸಾವಿರ, ಲಕ್ಷ ಮತ್ತು ಹತ್ತು ಲಕ್ಷಗಳನ್ನು ಸೂಚಿಸುತ್ತದೆ."
                    }
                },
                {
                    "id": "math_2",
                    "sanskrit": "त्रिभुजस्य फलशरीरम् समदलकोटिभुजयोर्घातम्‌ ।",
                    "transliteration": "Tribhujasya phalashariram samadalakoṭibhujayorghātam.",
                    "explanations": {
                        "english": "The area of a triangle is the product of half the base and the height. This is the Sanskrit formulation of the standard formula for calculating a triangle's area.",
                        "hindi": "त्रिभुज का क्षेत्रफल आधा आधार और ऊंचाई का गुणनफल है। यह त्रिभुज के क्षेत्रफल की गणना के लिए मानक सूत्र का संस्कृत प्रतिपादन है।",
                        "marathi": "त्रिकोणाचे क्षेत्रफळ हे पायाच्या अर्ध्या लांबी आणि उंची यांच्या गुणाकारातून मिळते. हे त्रिकोणाच्या क्षेत्रफळाच्या मानक सूत्राचे संस्कृत स्वरूप आहे.",
                        "kannada": "ತ್ರಿಕೋಣದ ಕ್ಷೇತ್ರಫಲವು ಅರ್ಧ ಬುಡದ ಮತ್ತು ಎತ್ತರದ ಗುಣಲಬ್ಧವಾಗಿದೆ. ಇದು ತ್ರಿಕೋಣದ ಕ್ಷೇತ್ರಫಲವನ್ನು ಲೆಕ್ಕ ಮಾಡಲು ಸಂಸ್ಕೃತದಲ್ಲಿ ಪ್ರಮಾಣಿತ ಸೂತ್ರದ ರೂಪವಾಗಿದೆ."
                    }
                },
                {
                    "id": "math_3",
                    "sanskrit": "पूर्णांक संख्यानां योगः अभाज्य संख्या न भवति।",
                    "transliteration": "Pūrṇanka sankhyānām yogaḥ abhājya sankhyā na bhavati.",
                    "explanations": {
                        "english": "The sum of integers is not always a prime number. This shloka expresses an important concept in number theory about the properties of integers and prime numbers.",
                        "hindi": "पूर्णांक संख्याओं का योग हमेशा अभाज्य संख्या नहीं होता है। यह श्लोक पूर्णांक और अभाज्य संख्याओं के गुणों के बारे में संख्या सिद्धांत में एक महत्वपूर्ण अवधारणा व्यक्त करता है।",
                        "marathi": "पूर्णांक संख्यांची बेरीज नेहमीच मूळ संख्या नसते. हा श्लोक संख्याशास्त्रातील पूर्णांक आणि मूळ संख्यांच्या गुणधर्मांबद्दल एक महत्त्वाची संकल्पना व्यक्त करतो.",
                        "kannada": "ಪೂರ್ಣಾಂಕಗಳ ಮೊತ್ತವು ಯಾವಾಗಲೂ ಅವಿಭಾಜ್ಯ ಸಂಖ್ಯೆಯಾಗಿರುವುದಿಲ್ಲ. ಈ ಶ್ಲೋಕವು ಪೂರ್ಣಾಂಕಗಳು ಮತ್ತು ಅವಿಭಾಜ್ಯ ಸಂಖ್ಯೆಗಳ ಗುಣಲಕ್ಷಣಗಳ ಬಗ್ಗೆ ಸಂಖ್ಯಾ ಸಿದ್ಧಾಂತದಲ್ಲಿ ಒಂದು ಮಹತ್ವದ ಪರಿಕಲ್ಪನೆಯನ್ನು ವ್ಯಕ್ತಪಡಿಸುತ್ತದೆ."
                    }
                }
            ]
        },
        {
            "id": "science",
            "name": "Science",
            "shlokas": [
                {
                    "id": "science_1",
                    "sanskrit": "अणोरणीयान् महतो महीयान्।",
                    "transliteration": "Aṇoraṇīyān mahato mahīyān.",
                    "explanations": {
                        "english": "Smaller than the smallest, greater than the greatest. This phrase from the Upanishads describes the concept of atoms and the vastness of the universe, showing early scientific thinking in ancient Sanskrit texts.",
                        "hindi": "सूक्ष्म से भी सूक्ष्म, महान से भी महान। उपनिषदों का यह वाक्य परमाणुओं की अवधारणा और ब्रह्मांड की विशालता का वर्णन करता है, जो प्राचीन संस्कृत ग्रंथों में प्रारंभिक वैज्ञानिक सोच को दर्शाता है।",
                        "marathi": "सूक्ष्मात सूक्ष्म, महानात महान. उपनिषदांतील हे वाक्य अणूंची संकल्पना आणि विश्वाच्या विशालतेचे वर्णन करते, जे प्राचीन संस्कृत ग्रंथांमध्ये प्रारंभिक वैज्ञानिक विचारसरणी दर्शवते.",
                        "kannada": "ಅತ್ಯಂತ ಸಣ್ಣದಕ್ಕಿಂತ ಸಣ್ಣದು, ಅತ್ಯಂತ ದೊಡ್ಡದಕ್ಕಿಂತ ದೊಡ್ಡದು. ಉಪನಿಷತ್ತುಗಳಿಂದ ಈ ವಾಕ್ಯವು ಪರಮಾಣುಗಳ ಪರಿಕಲ್ಪನೆ ಮತ್ತು ವಿಶ್ವದ ವಿಶಾಲತೆಯನ್ನು ವಿವರಿಸುತ್ತದೆ, ಇದು ಪ್ರಾಚೀನ ಸಂಸ್ಕೃತ ಗ್ರಂಥಗಳಲ್ಲಿ ಆದಿ ವೈಜ್ಞಾನಿಕ ಚಿಂತನೆಯನ್ನು ತೋರಿಸುತ್ತದೆ."
                    }
                },
                {
                    "id": "science_2",
                    "sanskrit": "गतिः प्रकाशस्य सर्वदा समाना एव भवति।",
                    "transliteration": "Gatiḥ prakāśasya sarvadā samānā eva bhavati.",
                    "explanations": {
                        "english": "The speed of light is always constant. This shloka remarkably anticipates Einstein's theory of relativity, which established that the speed of light is constant regardless of the observer's reference frame.",
                        "hindi": "प्रकाश की गति हमेशा समान ही रहती है। यह श्लोक उल्लेखनीय रूप से आइंस्टाइन के सापेक्षता के सिद्धांत का पूर्वानुमान करता है, जिसने स्थापित किया कि प्रकाश की गति प्रेक्षक के संदर्भ ढांचे की परवाह किए बिना स्थिर है।",
                        "marathi": "प्रकाशाचा वेग नेहमीच समान असतो. हा श्लोक आइनस्टाईनच्या सापेक्षतेच्या सिद्धांताचे लक्षणीय पूर्वानुमान करतो, ज्याने हे स्थापित केले की प्रकाशाचा वेग निरीक्षकाच्या संदर्भ चौकटीकडे दुर्लक्ष करून स्थिर असतो.",
                        "kannada": "ಬೆಳಕಿನ ವೇಗವು ಯಾವಾಗಲೂ ಸ್ಥಿರವಾಗಿರುತ್ತದೆ. ಈ ಶ್ಲೋಕವು ಐನ್‌ಸ್ಟೈನ್‌ನ ಸಾಪೇಕ್ಷತಾ ಸಿದ್ಧಾಂತವನ್ನು ಗಮನಾರ್ಹವಾಗಿ ಮುನ್ಸೂಚಿಸುತ್ತದೆ, ಇದು ವೀಕ್ಷಕನ ಉಲ್ಲೇಖ ಚೌಕಟ್ಟನ್ನು ಲೆಕ್ಕಿಸದೆ ಬೆಳಕಿನ ವೇಗವು ಸ್ಥಿರವಾಗಿರುತ್ತದೆ ಎಂದು ಸ್ಥಾಪಿಸಿತು."
                    }
                },
                {
                    "id": "science_3",
                    "sanskrit": "यथा पिण्डे तथा ब्रह्माण्डे।",
                    "transliteration": "Yathā piṇḍe tathā brahmāṇḍe.",
                    "explanations": {
                        "english": "As is the atom, so is the universe. This profound concept suggests that the same principles that govern the microcosm also govern the macrocosm, anticipating modern fractal theory and the recurring patterns found throughout nature.",
                        "hindi": "जैसा पिंड में, वैसा ब्रह्मांड में। यह गहन अवधारणा सुझाती है कि जो सिद्धांत सूक्ष्म जगत को नियंत्रित करते हैं, वे ही बृहत जगत को भी नियंत्रित करते हैं, जो आधुनिक फ्रैक्टल सिद्धांत और प्रकृति में पाए जाने वाले आवर्ती पैटर्न का पूर्वानुमान करती है।",
                        "marathi": "जसे पिंडामध्ये, तसे ब्रह्मांडामध्ये. ही गहन संकल्पना सुचवते की जे नियम सूक्ष्म विश्वावर नियंत्रण ठेवतात, तेच विशाल विश्वावरही नियंत्रण ठेवतात, जे आधुनिक फ्रॅक्टल सिद्धांत आणि निसर्गात आढळणाऱ्या पुनरावर्ती नमुन्यांचे पूर्वानुमान करते.",
                        "kannada": "ಕಣದಂತೆಯೇ ವಿಶ್ವವೂ ಸಹ. ಈ ಆಳವಾದ ಪರಿಕಲ್ಪನೆಯು ಸೂಕ್ಷ್ಮಲೋಕವನ್ನು ನಿಯಂತ್ರಿಸುವ ಅದೇ ತತ್ವಗಳು ಬೃಹತ್ ಲೋಕವನ್ನೂ ನಿಯಂತ್ರಿಸುತ್ತವೆ ಎಂದು ಸೂಚಿಸುತ್ತದೆ, ಇದು ಆಧುನಿಕ ಫ್ರ್ಯಾಕ್ಟಲ್ ಸಿದ್ಧಾಂತ ಮತ್ತು ಪ್ರಕೃತಿಯಲ್ಲಿ ಕಂಡುಬರುವ ಆವರ್ತಕ ಮಾದರಿಗಳನ್ನು ಮುನ್ಸೂಚಿಸುತ್ತದೆ."
                    }
                }
            ]
        },
        {
            "id": "youth",
            "name": "Youth",
            "shlokas": [
                {
                    "id": "youth_1",
                    "sanskrit": "युवा सुभाषितश्चैव व्यसने च दृढव्रतः।",
                    "transliteration": "Yuvā subhāṣitaścaiva vyasane ca dṛḍhavrataḥ.",
                    "explanations": {
                        "english": "A youth should be well-spoken and steadfast in difficult times. This shloka emphasizes the importance of developing good communication skills and resilience from a young age.",
                        "hindi": "युवा को सुभाषित (अच्छी तरह से बोलने वाला) और कठिन समय में दृढ़ संकल्प वाला होना चाहिए। यह श्लोक कम उम्र से ही अच्छे संचार कौशल और लचीलेपन के विकास के महत्व पर जोर देता है।",
                        "marathi": "तरुणांनी सुभाषित (चांगले बोलणारे) आणि कठीण काळात दृढनिश्चयी असावे. हा श्लोक लहान वयापासूनच चांगले संवाद कौशल्य आणि लवचिकता विकसित करण्याच्या महत्त्वावर भर देतो.",
                        "kannada": "ಯುವಕರು ಸುಭಾಷಿತರಾಗಿರಬೇಕು (ಚೆನ್ನಾಗಿ ಮಾತನಾಡುವವರು) ಮತ್ತು ಕಷ್ಟದ ಸಮಯದಲ್ಲಿ ದೃಢವಾಗಿರಬೇಕು. ಈ ಶ್ಲೋಕವು ಯುವ ವಯಸ್ಸಿನಿಂದಲೇ ಉತ್ತಮ ಸಂವಹನ ಕೌಶಲ್ಯಗಳು ಮತ್ತು ಸ್ಥಿತಿಸ್ಥಾಪಕತ್ವವನ್ನು ಬೆಳೆಸುವ ಮಹತ್ವವನ್ನು ಒತ್ತಿ ಹೇಳುತ್ತದೆ."
                    }
                },
                {
                    "id": "youth_2",
                    "sanskrit": "अकाले नैव निद्रायाः वशगः स्यात् युवावस्थायाम्।",
                    "transliteration": "Akāle naiva nidrāyāḥ vaśagaḥ syāt yuvāvasthāyām.",
                    "explanations": {
                        "english": "In youth, one should not become a slave to sleeping at improper times. This shloka advises young people to maintain discipline in their daily routines and make good use of their energetic years.",
                        "hindi": "युवावस्था में, अनुचित समय पर नींद के वश में नहीं होना चाहिए। यह श्लोक युवाओं को अपनी दैनिक दिनचर्या में अनुशासन बनाए रखने और अपने ऊर्जावान वर्षों का अच्छा उपयोग करने की सलाह देता है।",
                        "marathi": "तरुणपणात, अयोग्य वेळी झोपण्याचे गुलाम होऊ नये. हा श्लोक तरुणांना त्यांच्या दैनंदिन दिनचर्येत शिस्त राखण्याचा आणि त्यांच्या उत्साही वर्षांचा चांगला उपयोग करण्याचा सल्ला देतो.",
                        "kannada": "ಯೌವನದಲ್ಲಿ, ಅಸಮಯದಲ್ಲಿ ನಿದ್ರೆಗೆ ಗುಲಾಮನಾಗಬಾರದು. ಈ ಶ್ಲೋಕವು ಯುವಜನರಿಗೆ ಅವರ ದೈನಂದಿನ ದಿನಚರಿಯಲ್ಲಿ ಶಿಸ್ತನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಲು ಮತ್ತು ಅವರ ಚುರುಕಾದ ವರ್ಷಗಳನ್ನು ಉತ್ತಮವಾಗಿ ಬಳಸಿಕೊಳ್ಳಲು ಸಲಹೆ ನೀಡುತ್ತದೆ."
                    }
                },
                {
                    "id": "youth_3",
                    "sanskrit": "यौवने साधनं विद्या धने धर्मः सदा गतिः।",
                    "transliteration": "Yauvane sādhanaṃ vidyā dhane dharmaḥ sadā gatiḥ.",
                    "explanations": {
                        "english": "In youth, one should acquire knowledge; in wealth, one should always follow dharma (righteousness). This shloka emphasizes the importance of learning during youth and maintaining ethics when successful.",
                        "hindi": "यौवन में विद्या का अर्जन और धन में हमेशा धर्म का पालन करना चाहिए। यह श्लोक युवावस्था के दौरान सीखने और सफल होने पर नैतिकता बनाए रखने के महत्व पर जोर देता है।",
                        "marathi": "तरुणपणी ज्ञान मिळवावे; संपत्तीमध्ये नेहमी धर्माचे (सदाचाराचे) पालन करावे. हा श्लोक तरुणपणी शिक्षण घेण्याच्या आणि यशस्वी झाल्यावर नैतिकता टिकवून ठेवण्याच्या महत्त्वावर भर देतो.",
                        "kannada": "ಯೌವನದಲ್ಲಿ ಜ್ಞಾನವನ್ನು ಪಡೆಯಬೇಕು; ಸಂಪತ್ತಿನಲ್ಲಿ ಯಾವಾಗಲೂ ಧರ್ಮವನ್ನು (ನ್ಯಾಯವನ್ನು) ಅನುಸರಿಸಬೇಕು. ಈ ಶ್ಲೋಕವು ಯೌವನದಲ್ಲಿ ಕಲಿಯುವುದರ ಮಹತ್ವವನ್ನು ಮತ್ತು ಯಶಸ್ವಿಯಾದಾಗ ನೈತಿಕತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳುವ ಮಹತ್ವವನ್ನು ಒತ್ತಿ ಹೇಳುತ್ತದೆ."
                    }
                }
            ]
        },
        {
            "id": "honesty",
            "name": "Honesty",
            "shlokas": [
                {
                    "id": "honesty_1",
                    "sanskrit": "सत्यं ब्रूयात् प्रियं ब्रूयात् न ब्रूयात् सत्यमप्रियम्।",
                    "transliteration": "Satyaṃ brūyāt priyaṃ brūyāt na brūyāt satyamapriyam.",
                    "explanations": {
                        "english": "Speak the truth, speak pleasantly, do not speak the truth that is unpleasant. This advice from ancient texts encourages honesty but with kindness and consideration for others' feelings.",
                        "hindi": "सत्य बोलें, प्रिय बोलें, अप्रिय सत्य न बोलें। प्राचीन ग्रंथों की यह सलाह ईमानदारी को प्रोत्साहित करती है, लेकिन दूसरों की भावनाओं के लिए दयालुता और विचार के साथ।",
                        "marathi": "सत्य बोलावे, प्रिय बोलावे, अप्रिय सत्य बोलू नये. प्राचीन ग्रंथांतील हा सल्ला प्रामाणिकपणाला प्रोत्साहन देतो, परंतु इतरांच्या भावनांसाठी दयाळूपणा आणि विचारपूर्वक.",
                        "kannada": "ಸತ್ಯವನ್ನು ಮಾತನಾಡಿ, ಇಷ್ಟವಾಗುವಂತೆ ಮಾತನಾಡಿ, ಅಪ್ರಿಯವಾದ ಸತ್ಯವನ್ನು ಮಾತನಾಡಬೇಡಿ. ಪ್ರಾಚೀನ ಗ್ರಂಥಗಳಿಂದ ಈ ಸಲಹೆಯು ಪ್ರಾಮಾಣಿಕತೆಯನ್ನು ಪ್ರೋತ್ಸಾಹಿಸುತ್ತದೆ, ಆದರೆ ಇತರರ ಭಾವನೆಗಳಿಗೆ ದಯೆ ಮತ್ತು ಪರಿಗಣನೆಯೊಂದಿಗೆ."
                    }
                },
                {
                    "id": "honesty_2",
                    "sanskrit": "अहिंसा परमो धर्मः सत्यं वचनमुत्तमम्।",
                    "transliteration": "Ahimsā paramo dharmaḥ satyaṃ vacanamuttamam.",
                    "explanations": {
                        "english": "Non-violence is the highest virtue, truthful speech is the best utterance. This fundamental principle from the Mahabharata places honesty as one of the most essential qualities alongside non-violence.",
                        "hindi": "अहिंसा सर्वोच्च धर्म है, सत्य वचन उत्तम है। महाभारत का यह मौलिक सिद्धांत ईमानदारी को अहिंसा के साथ सबसे आवश्यक गुणों में से एक के रूप में रखता है।",
                        "marathi": "अहिंसा हा परम धर्म आहे, सत्य बोलणे हे सर्वोत्तम आहे. महाभारतातील हे मूलभूत तत्त्व प्रामाणिकपणाला अहिंसेसह सर्वात आवश्यक गुणांपैकी एक म्हणून स्थान देते.",
                        "kannada": "ಅಹಿಂಸೆ ಪರಮ ಧರ್ಮವಾಗಿದೆ, ಸತ್ಯವಾದ ಮಾತು ಉತ್ತಮವಾಗಿದೆ. ಮಹಾಭಾರತದಿಂದ ಈ ಮೂಲಭೂತ ತತ್ವವು ಪ್ರಾಮಾಣಿಕತೆಯನ್ನು ಅಹಿಂಸೆಯೊಂದಿಗೆ ಅತ್ಯಂತ ಅಗತ್ಯವಾದ ಗುಣಗಳಲ್ಲಿ ಒಂದೆಂದು ಪರಿಗಣಿಸುತ್ತದೆ."
                    }
                },
                {
                    "id": "honesty_3",
                    "sanskrit": "वरं प्राणपरित्यागः न तु सत्यस्य विस्मृतिः।",
                    "transliteration": "Varaṃ prāṇaparityāgaḥ na tu satyasya vismṛtiḥ.",
                    "explanations": {
                        "english": "Better to sacrifice one's life than to forget truth. This powerful shloka emphasizes the paramount importance of honesty and integrity, even when facing severe consequences.",
                        "hindi": "प्राण त्यागना श्रेष्ठ है, किंतु सत्य को भूलना नहीं। यह शक्तिशाली श्लोक गंभीर परिणामों का सामना करते हुए भी ईमानदारी और सत्यनिष्ठा के सर्वोपरि महत्व पर जोर देता है।",
                        "marathi": "प्राण त्यागणे चांगले, परंतु सत्य विसरणे नाही. हा शक्तिशाली श्लोक गंभीर परिणामांना तोंड देताना देखील प्रामाणिकपणा आणि सचोटीच्या सर्वोच्च महत्त्वावर भर देतो.",
                        "kannada": "ಸತ್ಯವನ್ನು ಮರೆಯುವುದಕ್ಕಿಂತ ಪ್ರಾಣತ್ಯಾಗ ಮಾಡುವುದು ಉತ್ತಮ. ಈ ಶಕ್ತಿಶಾಲಿ ಶ್ಲೋಕವು ತೀವ್ರ ಪರಿಣಾಮಗಳನ್ನು ಎದುರಿಸುವಾಗಲೂ ಪ್ರಾಮಾಣಿಕತೆ ಮತ್ತು ಸಮಗ್ರತೆಯ ಪರಮ ಮಹತ್ವವನ್ನು ಒತ್ತಿ ಹೇಳುತ್ತದೆ."
                    }
                }
            ]
        },
        {
            "id": "education",
            "name": "Education",
            "shlokas": [
                {
                    "id": "education_1",
                    "sanskrit": "विद्या ददाति विनयं विनयाद् याति पात्रताम्।",
                    "transliteration": "Vidyā dadāti vinayaṃ vinayād yāti pātratām.",
                    "explanations": {
                        "english": "Education gives humility, from humility comes worthiness. This shloka emphasizes that true education should lead to humility, which in turn makes a person worthy of respect and responsibilities.",
                        "hindi": "विद्या विनय देती है, विनय से पात्रता आती है। यह श्लोक इस बात पर जोर देता है कि सच्ची शिक्षा से विनम्रता आनी चाहिए, जो बदले में एक व्यक्ति को सम्मान और जिम्मेदारियों के योग्य बनाता है।",
                        "marathi": "शिक्षण नम्रता देते, नम्रतेतून पात्रता येते. हा श्लोक यावर भर देतो की खरे शिक्षण नम्रतेकडे नेले पाहिजे, जे बदल्यात व्यक्तीला आदर आणि जबाबदाऱ्यांच्या योग्य बनवते.",
                        "kannada": "ಶಿಕ್ಷಣವು ವಿನಯವನ್ನು ನೀಡುತ್ತದೆ, ವಿನಯದಿಂದ ಯೋಗ್ಯತೆ ಬರುತ್ತದೆ. ಈ ಶ್ಲೋಕವು ನಿಜವಾದ ಶಿಕ್ಷಣವು ವಿನಯಕ್ಕೆ ಕಾರಣವಾಗಬೇಕು ಎಂದು ಒತ್ತಿ ಹೇಳುತ್ತದೆ, ಇದು ವ್ಯಕ್ತಿಯನ್ನು ಗೌರವ ಮತ್ತು ಜವಾಬ್ದಾರಿಗಳಿಗೆ ಯೋಗ್ಯನನ್ನಾಗಿ ಮಾಡುತ್ತದೆ."
                    }
                },
                {
                    "id": "education_2",
                    "sanskrit": "गुरुर्ब्रह्मा गुरुर्विष्णुः गुरुर्देवो महेश्वरः।",
                    "transliteration": "Gururbrahmā gururviṣṇuḥ gururdevo maheśvaraḥ.",
                    "explanations": {
                        "english": "The teacher is Brahma, the teacher is Vishnu, the teacher is Lord Maheshwara (Shiva). This famous shloka elevates teachers to the status of deities, highlighting the profound importance of educators in society.",
                        "hindi": "गुरु ब्रह्मा है, गुरु विष्णु है, गुरु देव महेश्वर (शिव) है। यह प्रसिद्ध श्लोक शिक्षकों को देवताओं के स्तर तक ऊंचा करता है, जो समाज में शिक्षकों के गहन महत्व को उजागर करता है।",
                        "marathi": "गुरु ब्रह्मा आहे, गुरु विष्णू आहे, गुरु देव महेश्वर (शिव) आहे. हा प्रसिद्ध श्लोक शिक्षकांना देवतांच्या दर्जापर्यंत उंचावतो, जे समाजातील शिक्षकांचे गहन महत्त्व अधोरेखित करतो.",
                        "kannada": "ಗುರುವೇ ಬ್ರಹ್ಮ, ಗುರುವೇ ವಿಷ್ಣು, ಗುರುವೇ ದೇವ ಮಹೇಶ್ವರ (ಶಿವ). ಈ ಪ್ರಸಿದ್ಧ ಶ್ಲೋಕವು ಶಿಕ್ಷಕರನ್ನು ದೇವರ ಸ್ಥಾನಕ್ಕೆ ಏರಿಸುತ್ತದೆ, ಇದು ಸಮಾಜದಲ್ಲಿ ಶಿಕ್ಷಕರ ಆಳವಾದ ಮಹತ್ವವನ್ನು ಎತ್ತಿ ತೋರಿಸುತ್ತದೆ."
                    }
                },
                {
                    "id": "education_3",
                    "sanskrit": "सा विद्या या विमुक्तये।",
                    "transliteration": "Sā vidyā yā vimuktaye.",
                    "explanations": {
                        "english": "That is knowledge which liberates. This concise but profound shloka defines true education as that which frees the mind from ignorance and leads to liberation of thought.",
                        "hindi": "वही विद्या है जो मुक्ति दे। यह संक्षिप्त लेकिन गहन श्लोक सच्ची शिक्षा को ऐसे परिभाषित करता है जो मन को अज्ञान से मुक्त करता है और विचार की स्वतंत्रता की ओर ले जाता है।",
                        "marathi": "तेच ज्ञान आहे जे मुक्त करते. हा संक्षिप्त परंतु गहन श्लोक खऱ्या शिक्षणाची व्याख्या अशा प्रकारे करतो जे मनाला अज्ञानातून मुक्त करते आणि विचारांच्या स्वातंत्र्याकडे नेते.",
                        "kannada": "ಯಾವುದು ಮುಕ್ತಿಗೊಳಿಸುತ್ತದೆಯೋ ಅದೇ ಜ್ಞಾನ. ಈ ಸಂಕ್ಷಿಪ್ತ ಆದರೆ ಆಳವಾದ ಶ್ಲೋಕವು ನಿಜವಾದ ಶಿಕ್ಷಣವನ್ನು ಮನಸ್ಸನ್ನು ಅಜ್ಞಾನದಿಂದ ಮುಕ್ತಗೊಳಿಸಿ ವಿಚಾರದ ಮುಕ್ತಿಗೆ ಕಾರಣವಾಗುವುದು ಎಂದು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ."
                    }
                }
            ]
        }
    ]
    
    return categories