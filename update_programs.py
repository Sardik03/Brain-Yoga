import re
import os

with open("programs.html", "r") as f:
    content = f.read()

# Helper function to replace modal body
def replace_modal(content, modal_id, new_body):
    pattern = re.compile(r'(<div id="' + modal_id + r'" class="modal">.*?<div class="modal-body">).*?(                </div>\s*</div>\s*</div>)', re.DOTALL)
    if not pattern.search(content):
        print(f"Modal {modal_id} not found!")
    return pattern.sub(r'\1\n' + new_body + r'\n\2', content)

# 1. ABACUS
abacus_html = """                    <h2>Abacus Training</h2>
                    <p>Why Are Abacus Classes Important for Brain Development and Fast Calculation in Kids?</p>
                    <p>Brain Yoga Classes offer one of the best Abacus classes for kids who need better concentration, faster calculation skills, and stronger memory from an early age.</p>
                    <p>Our Abacus program is specially designed for young children to develop their brain during the most important learning years. It helps children perform calculations quickly without using fingers or calculators, building confidence in maths from the start.</p>
                    <p>In today’s digital world, children are becoming more dependent on screens and shortcuts, which reduces their ability to focus and think independently. That is why many parents now actively search for abacus classes for kids that focus on real brain development instead of just academic learning.</p>
                    
                    <h3>What Are The Benefits of Abacus?</h3>
                    <p>How Do Abacus Classes Improve Concentration, Memory, and Mental Maths Skills?<br>
                    Abacus works by training both sides of the brain through visualization and practice. Children first learn using beads and gradually shift to solving calculations mentally.</p>
                    <p>With consistent training, children develop:</p>
                    <ul>
                        <li>Faster calculation speed</li>
                        <li>Better concentration</li>
                        <li>Strong memory retention</li>
                    </ul>
                    <p>This method improves overall thinking ability and helps children perform better in school as well as daily activities.</p>
                    <p>Parents looking for effective mental maths classes for kids often choose Abacus because it builds long-term cognitive skills.</p>
                    
                    <h3>Why Do Children Today Need Abacus Training More Than Ever?</h3>
                    <p>Most children today struggle with short attention span, lack of focus, and fear of maths. This happens due to increased screen time and reduced mental practice.</p>
                    <p>Abacus provides a structured way to train the brain and improve these areas. It helps children stay attentive, process information faster, and solve problems with confidence. That is why Abacus is widely recommended as one of the most effective brain development classes for children.</p>
                    
                    <h3>What Do Children Learn By Doing Abacus?</h3>
                    <p>After completing the program, children show noticeable improvement in:</p>
                    <ul>
                        <li>Mental calculation ability</li>
                        <li>Focus and attention span</li>
                        <li>Academic confidence</li>
                        <li>Logical thinking skills</li>
                    </ul>
                    <p>Children who once found maths difficult start solving problems quickly and accurately.</p>
                    
                    <h3>Why Choose Brain Yoga Classes for Abacus Training?</h3>
                    <p>We focus on actual results and improvement:</p>
                    <ul>
                        <li>Step-by-step structured learning</li>
                        <li>Individual attention for every child</li>
                        <li>Regular practice sessions</li>
                        <li>Supportive and child-friendly environment</li>
                    </ul>
                    <p>Our goal is to ensure that every child develops strong brain skills, not just basic calculation ability.</p>
                    
                    <h3>Is This the Right Age to Start Abacus Classes?</h3>
                    <p>Yes. Early childhood is the best time to train the brain. Starting at the right age helps children build strong learning habits, better focus, and faster thinking ability that stays with them for life.</p>
                    
                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 4 to 10 Years</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 2.5-3 Months (Each Level) / 12hr Monthly</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000/month</p>
                    </div>"""

# 2. VEDIC MATHS
vedic_html = """                    <h2>Vedic Maths</h2>
                    <p><strong>What Are Vedic Maths Classes?</strong><br>
                    Vedic Maths is based on ancient Indian techniques that help solve complex calculations quickly without lengthy steps. It makes maths simpler, faster, and more interesting for students who otherwise find it difficult or time-consuming.</p>
                    <p>Brain Yoga Classes offers one of the best Vedic Maths classes for students who want to improve calculation speed, accuracy, and confidence in mathematics. Our Vedic Maths course is specially designed for school students as well as those preparing for competitive exams like UPSC, CSAT, SSC, Banking, NDA and other entrance exams where time and accuracy matter the most.</p>
                    <p>Students today face time pressure in exams and often lose marks due to slow calculations. That is why many parents now actively look for Vedic Maths classes for students that can give their child a real advantage.</p>
                    
                    <h3>How Does Vedic Maths Help Students?</h3>
                    <p>Vedic Maths focuses on smart techniques instead of traditional long methods. It trains the brain to process numbers faster and more efficiently. With regular practice, students learn to:</p>
                    <ul>
                        <li>Solve calculations in seconds</li>
                        <li>Reduce mistakes in exams</li>
                        <li>Improve accuracy under pressure</li>
                    </ul>
                    <p>Our structured approach ensures that students understand each concept step-by-step with proper guidance, practice worksheets, and continuous improvement tracking. This is especially useful for students preparing for competitive exams where speed is a key factor.</p>
                    
                    <h3>Can Vedic Maths Help Students Struggling With Maths?</h3>
                    <p>Many students are scared of mathematics. But struggle isn’t just faced by your child; in fact today many students struggle with maths because methods are lengthy and confusing, lack of practice reduces confidence, and time pressure creates stress.</p>
                    <p>But by choosing Brain Yoga Classes, you are opting for the best Vedic Maths classes near you, which are changing the approach of normal education and teaching through the method of Vedic times teaching. Instead of memorising steps, students learn patterns and shortcuts that make problem-solving quicker and easier. This reduces fear and builds confidence naturally.</p>
                    
                    <h3>What Will Your Child Gain from Vedic Maths?</h3>
                    <p>After completing the course, students experience clear improvements:</p>
                    <ul>
                        <li>Faster problem-solving ability</li>
                        <li>Better performance in exams</li>
                        <li>Increased confidence in maths</li>
                        <li>Strong logical thinking skills</li>
                    </ul>
                    <p>The program not only improves marks but also develops a sharper and more active mind.</p>

                    <h3>Why Choose Brain Yoga Classes for Vedic Maths?</h3>
                    <ul>
                        <li>We focus on practical results, not just teaching.</li>
                        <li>Step-by-step learning approach</li>
                        <li>Regular practice and revision</li>
                        <li>Individual attention to each student</li>
                        <li>Proven improvement in speed and accuracy</li>
                    </ul>
                    <p>If your child is preparing for exams or struggling with calculation speed, this is the right time to start.</p>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 8+ Years</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 1-1.5 Years</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000/month</p>
                    </div>"""

# 3. HINDI
hindi_html = """                    <h2>Hindi Language Development</h2>
                    <p><strong>Why Are Hindi Classes Important Today?</strong><br>
                    Today many children grow up focusing more on English, while Hindi slowly becomes a weak area. Over time, they start finding it difficult to read properly, write without mistakes, or understand what is being taught in school. The problem is not the child. The problem is how the language is taught. Hindi is often portrayed as a complex subject, full of rules, and difficult to learn, which leads children to lose interest early.</p>
                    <p>At Brain Yoga Classes, we change this approach completely. We teach Hindi in a way that feels simple and natural. Just like a child learns to speak, we help them read, write, and understand step by step not just by filling their copies with notes. That is exactly what we focus on.</p>
                    
                    <h3>Why Are Parents Choosing Hindi Classes?</h3>
                    <p>Parents today understand the importance of English, but they also realise that ignoring Hindi creates gaps in learning from our surroundings. A child who is not comfortable in Hindi often struggles in exams, school instructions, and even basic communication.</p>
                    <p>Even educated parents now choose Hindi classes because:</p>
                    <ul>
                        <li>Strong Hindi improves overall academic performance</li>
                        <li>It helps in a better understanding of subjects in school</li>
                        <li>It builds confidence in reading and writing</li>
                        <li>It connects children to their roots and daily communication</li>
                    </ul>
                    <p>We give equal importance to both English and Hindi, because both are necessary for a child’s complete development.</p>

                    <h3>What Makes Our Hindi Classes Different?</h3>
                    <p>Most centres focus only on finishing school work. Children copy answers but do not understand the language. This creates confusion and fear.</p>
                    <p>We work differently. We understand that every child learns at a different pace and has a different level of comfort with Hindi. Our approach focuses on:</p>
                    <ul>
                        <li>Making Hindi easy instead of complicated</li>
                        <li>Teaching in a way that builds children's interest</li>
                        <li>Exercises like storytelling, role-plays and fun activities to signal their brain neurons</li>
                    </ul>

                    <h3>What Will Your Child Gain?</h3>
                    <p>With proper guidance and practice, children show real improvement in reading Hindi smoothly, writing clearly without mistakes, understanding lessons in school, and speaking with confidence. They stop memorising and start understanding.</p>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 5+ Years to adults</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 2-3 months per level/ 8hr Monthly</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000/month</p>
                    </div>"""

# 4. HANDWRITING
handwriting_html = """                    <h2>Handwriting Improvement</h2>
                    <p><strong>Why Do Children Lose Marks Even When They Know the Answer?</strong><br>
                    Many parents notice this: The child studies well, answers correctly, but marks are still low. When you look closely, the issue is not knowledge; it is presentation. If the writing is unclear, cramped, or uneven, the answer is hard to read, regardless of the language. Teachers move on, and the child loses marks.</p>
                    <p>This is where handwriting becomes important not for beauty, but for clarity. A child should be able to write in a way that anyone can read without effort.</p>
                    
                    <h3>What Is Actually Wrong with the Way Children Write?</h3>
                    <p>Most children are never taught how to write properly. They are told to write more, write faster, and complete work. No one shows them how letters should sit on the line, how much space to leave, or how to hold the pencil correctly.</p>
                    <p>Over time, each child creates their own style. Some write too big, some too small, some join letters wrongly, and some press too hard. These habits become fixed, and then writing starts looking messy even after practice. The problem is not the child; just the right method is missing.</p>

                    <h3>What Do We Do Differently at Brain Yoga Classes?</h3>
                    <p>We do not start with pages of writing. We first slow things down. We observe how the child writes, where the mistake is, and why it is happening. Then we correct one thing at a time. If spacing is wrong, we fix spacing. If letters are not clear, we fix formation. If speed is the issue, we first fix control.</p>
                    <p>Children are not asked to write more. They are shown how to write better. We also use guided sheets and short practice tasks instead of long, boring pages.</p>

                    <h3>How Does a Child Improve?</h3>
                    <p>Improvement does not happen in one day. It happens when small mistakes are corrected regularly. Children practise in a way that:</p>
                    <ul>
                        <li>Each letter becomes clear and readable.</li>
                        <li>Words are spaced properly.</li>
                        <li>Writing stays neat even after a full page.</li>
                        <li>Speed improves only after control is built.</li>
                    </ul>
                    <p>We also make children recheck their own writing. This habit alone changes how they write in school.</p>

                    <h3>What Changes Will You See?</h3>
                    <p>Writing becomes easier to read. School notebooks start looking neat. Teachers stop complaining about handwriting. Children feel less pressure while writing. Most importantly, the child stops rushing and starts writing with control.</p>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 5+ Years</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 1-2 months per level</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000/month</p>
                    </div>"""

# 5. SPEAKING
speaking_html = """                    <h2>Public Speaking</h2>
                    <p><strong>Why does a child stay silent even when they know the answer?</strong><br>
                    Have you ever noticed your child knows the answer at home but becomes quiet in class or in front of others? This is very common. It is not because the child does not understand. It is because they are not comfortable expressing their thoughts in front of people. Schools focus on writing and learning, but speaking is often left to chance. Over time, this hesitation becomes a habit.</p>
                    <p>At Brain Yoga Classes, we treat speaking as a daily skill, not a one-time activity. Parents who search for public speaking classes for kids are usually not looking for stage performance. They want their child to speak normally and confidently in everyday situations. That is exactly where we begin.</p>
                    
                    <h3>What actually happens when a child tries to speak?</h3>
                    <p>When a child is suddenly asked to speak, they worry about forgetting words. They think others might laugh. They are unsure how to start. So even before they speak, they lose confidence.</p>
                    <p>Children need a system. They need small steps that make speaking feel safe and natural. That is why many parents today look for communication skills classes for students where children are guided properly instead of being pushed.</p>

                    <h3>So what do we actually do in class?</h3>
                    <p>We do not start with speeches. We start with comfort. Children begin with simple activities:</p>
                    <ul>
                        <li>Talking about something they like</li>
                        <li>Answering small questions</li>
                        <li>Speaking in pairs before speaking in a group</li>
                        <li>Listening and responding to others</li>
                    </ul>
                    <p>Once they get used to speaking, we slowly move to short presentations, storytelling, topic-based speaking, and expressing opinions clearly.</p>

                    <h3>What skills does a child actually develop?</h3>
                    <p>We do not just make children speak. We teach them how to speak. They learn:</p>
                    <ul>
                        <li>How to begin without hesitation</li>
                        <li>How to organise thoughts before speaking</li>
                        <li>How to speak clearly so others understand</li>
                        <li>How to stay calm while speaking</li>
                    </ul>

                    <h3>Why do many classes not give real results?</h3>
                    <p>A child memorises a speech, performs once, and then goes back to the same hesitation. Confidence comes from repetition. From speaking again and again in different situations.</p>
                    <p>At Brain Yoga Classes, every child gets time to speak in each session. Practice is regular, mistakes are corrected gently, and progress is built step by step.</p>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 6+ Years</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 2-3 months</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000 onwards</p>
                    </div>"""

# 6. TUITION
tuition_html = """                    <h2>Tuition Classes</h2>
                    <p><strong>Why Do Students Need Proper Tuition Support Today?</strong><br>
                    School teaching is often fast, lacking attention on each student and not every child is able to understand everything in the same explained concept or theory. Many students hesitate to ask doubts in class and slowly start falling behind. But that’s not the issue with Brain Yoga unlike other tuition classes.</p>
                    <p>At Brain Yoga Classes, we provide tuition classes for students from Class I to X where every child is guided properly and every concept is explained until it is fully understood. Parents searching for tuition classes near me usually want a place where their child is not ignored. That is exactly what we focus on.</p>
                    
                    <h3>What Is Different About Our Tuition Classes?</h3>
                    <p>Most tuition centres only focus on completing homework or finishing the syllabus. Children attend classes but still remain confused, unaware of their chapters, confused over concepts and in fear of marking. We focus on:</p>
                    <ul>
                        <li>Teaching until the child understands</li>
                        <li>Giving time to every student</li>
                        <li>Explaining basics before moving ahead</li>
                        <li>Regular checking of progress</li>
                    </ul>
                    <p>We do not rush. We make sure learning is complete.</p>

                    <h3>What Do Students Learn Here?</h3>
                    <p>Students are taught in a simple and clear way so they do not feel pressure. They receive chapter wise explanation of subjects, proper notes for easy revision, homework support and practice, and regular tests to check understanding.</p>

                    <h3>How Brain Yoga Classes Solves This Problem</h3>
                    <p>Many tuition centres fail students because there are too many students in one batch, no personal attention, and only focus on completing syllabus. We focus on each child, not just the class.</p>
                    <ul>
                        <li>Small batches so every child gets attention</li>
                        <li>Doubt solving in every session</li>
                        <li>Extra help for weak subjects</li>
                        <li>Regular communication with parents</li>
                    </ul>

                    <h3>What Will Your Child Gain?</h3>
                    <p>With regular learning, students improve in school marks and performance, understanding of subjects, confidence during exams, and focus and study habits. Children who were earlier confused start studying on their own.</p>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: Class I to X</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: Ongoing</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000 - ₹3000/month</p>
                    </div>"""

# 7. SPOKEN ENGLISH
english_html = """                    <h2>Spoken English</h2>
                    <p><strong>Why Are Spoken English Classes Important for Children Today?</strong><br>
                    In today’s world, English is not just a subject but an equally important spoken language. Even in schools and all their cultural programs, students with clear pronunciation and language are preferred more.</p>
                    <p>At Brain Yoga Classes, we offer one of the best spoken English classes for children, especially for those who want to improve their speaking skills, pronunciation, and gain an upper hand in the language from an early stage.</p>
                    
                    <h3>What Do Children Learn in Spoken English Classes?</h3>
                    <p>Spoken English is not about memorising grammar rules or huge long spellings. It is about learning and understanding how to use the language naturally in daily life without making mistakes.</p>
                    <p>Children are taught step by step to:</p>
                    <ul>
                        <li>Understand the logic behind the languages grammar and words</li>
                        <li>Speak clearly with correct pronunciation</li>
                        <li>Use proper grammar while speaking</li>
                        <li>Build a strong vocabulary</li>
                        <li>Form sentences confidently without hesitation</li>
                    </ul>
                    <p>Through regular speaking practice, children slowly become comfortable expressing their thoughts in English.</p>

                    <h3>Why Children Struggle with English Speaking?</h3>
                    <p>Many children understand English but hesitate while speaking because they are afraid of making mistakes, lack of practice sessions reduces their confidence, focus is only on writing not speaking abilities, and lack of knowledge and guidance on proper pronunciation.</p>

                    <h3>How Do Spoken English Classes Help?</h3>
                    <p>At Brain Yoga Classes, our prime focus is always on practical learning not just going by theory or books. Children learn through daily speaking activities, interactive conversations, group activities and plays, role play and real-life situations, and continuous correction and guidance. This helps children improve naturally without taking in pressure.</p>

                    <h3>What Will Your Child Gain?</h3>
                    <p>After completing the course, children show clear improvement in confidence while speaking, pronunciation and fluency, vocabulary usage, and communication skills in school and daily life. They no longer hesitate to speak in front of others.</p>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 5+ Years</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 2-4 Months</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000/month</p>
                    </div>"""

# 8. ART
art_html = """                    <h2>Art & Craft / Painting Classes</h2>
                    <p><strong>Is art just a hobby or an important skill?</strong><br>
                    Many people see art as a time pass. But think about this. When a child draws, colours, or creates something, they are thinking, imagining, and expressing. These are skills that help in every subject and in life. Parents searching for art and craft classes for kids usually want their child to learn properly, not just stay busy.</p>
                    
                    <h3>What is missing in most art classes?</h3>
                    <p>Children are often told: “Draw this” or “Colour like this” they simply copy. They finish. But do they learn how to draw? Not really. At Brain Yoga Classes, we focus on teaching the process, not just the result.</p>
                    
                    <h3>What do children actually learn?</h3>
                    <p>Children are guided step by step:</p>
                    <ul>
                        <li>Understanding shapes and structure</li>
                        <li>Drawing with proportion</li>
                        <li>Colouring with proper technique</li>
                        <li>Using different materials</li>
                        <li>Creating their own ideas</li>
                    </ul>
                    <p>Let me ask you. If a child understands how to draw, will they need to copy? That is the difference we create.</p>

                    <h3>Why do children improve better here?</h3>
                    <p>Because we teach basics first, give time for practice, encourage creativity, and guide instead of controlling. This helps children enjoy learning and improve at the same time.</p>
                    <p>Parents looking for painting classes for kids often prefer structured learning instead of random activities.</p>

                    <h3>What changes will you notice?</h3>
                    <ul>
                        <li>Better drawing skills</li>
                        <li>More creative thinking</li>
                        <li>Improved focus</li>
                        <li>Interest in learning new things</li>
                    </ul>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 5+ Years</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 2 to 3 months</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000 onwards</p>
                    </div>"""

# 9. PERSONALITY
personality_html = """                    <h2>Personality Development</h2>
                    <p><strong>What do parents really mean when they say “my child should be confident”?</strong><br>
                    Do they mean speaking on stage? Or something more basic? Most parents are actually talking about everyday situations. Can the child answer properly in class? Can they talk to elders respectfully? Can they express what they feel without hesitation? This is where personality starts showing.</p>
                    <p>At Brain Yoga Classes, we do not treat personality development as a fancy subject. We focus on daily behaviour, communication, and thinking. Parents searching for personality development classes for kids usually want their child to become more confident in real life, not just in activities.</p>
                    
                    <h3>So what is actually missing in most children today?</h3>
                    <p>Children are taught subjects every day, but are they taught how to respond when someone asks a question? How to handle a new situation? How to express disagreement politely? Most of the time, the answer is no.</p>
                    <p>This creates a gap. The child may be intelligent but still feel unsure in social situations. That is why many parents now look for confidence building classes for children that go beyond studies.</p>

                    <h3>What do we actually do in class?</h3>
                    <p>We do not make children sit and listen. We involve them. Children participate in:</p>
                    <ul>
                        <li>Real-life situation activities</li>
                        <li>Group discussions</li>
                        <li>Speaking and response exercises</li>
                        <li>Behaviour-based guidance</li>
                    </ul>
                    <p>Confidence becomes natural when it is practised, not forced.</p>

                    <h3>What makes our approach different?</h3>
                    <p>Most places focus only on speaking or only on discipline. We combine both. We help children speak clearly, listen properly, think before reacting, and build self-control.</p>
                    <p>We also understand that every child is different. Some are quiet, some are active, some are unsure. We guide each child based on their behaviour, not with one fixed method.</p>

                    <h3>What changes will you notice over time?</h3>
                    <p>Parents start noticing the child responds more clearly, behaviour becomes more balanced, confidence improves in school, and the child becomes more aware and responsible.</p>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 6+ Years</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 2 to 3 months</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000 onwards</p>
                    </div>"""

# 10. CALLIGRAPHY
calligraphy_html = """                    <h2>Calligraphy Classes</h2>
                    <p><strong>Is calligraphy just neat writing or something deeper?</strong><br>
                    Many parents think calligraphy is just about writing nicely. But let’s look at it differently. When a child writes with control, focus, and patience, they are not just improving handwriting. They are developing discipline, attention, and creativity at the same time.</p>
                    <p>Parents searching for calligraphy classes for kids often want something meaningful beyond regular studies. This is where calligraphy becomes useful.</p>
                    
                    <h3>What is the common mistake in learning calligraphy?</h3>
                    <p>Many places teach multiple styles quickly. Children learn a little of everything but master nothing. At Brain Yoga Classes, we focus on one style at a time. We give enough time for practice before moving ahead.</p>

                    <h3>What do children actually learn?</h3>
                    <p>Children are trained step by step:</p>
                    <ul>
                        <li>Proper pen holding</li>
                        <li>Basic strokes and patterns</li>
                        <li>Letter formation with consistency</li>
                        <li>Spacing and alignment</li>
                    </ul>
                    <p>We do not rush. We make sure the child understands each step.</p>

                    <h3>Why do children enjoy this class?</h3>
                    <p>Because it feels different. It is calm. It is focused. It is creative. Children are not under pressure to perform. They are guided to improve.</p>

                    <h3>What changes will you notice?</h3>
                    <p>Over time, children show better control in writing, improved focus and patience, cleaner and more organised work, and interest in creative writing.</p>

                    <div class="course-details-box">
                        <p><i class="fa-solid fa-child" style="width: 20px;"></i> Age Group: 7+ Years</p>
                        <p><i class="fa-regular fa-clock" style="width: 20px;"></i> Duration: 2 to 3 months</p>
                        <p><i class="fa-solid fa-indian-rupee-sign" style="width: 20px;"></i> Fees: ₹2000 onwards</p>
                    </div>"""

content = replace_modal(content, 'modal_abacus', abacus_html)
content = replace_modal(content, 'modal_vedic', vedic_html)
content = replace_modal(content, 'modal_hindi', hindi_html)
content = replace_modal(content, 'modal_handwriting', handwriting_html)
content = replace_modal(content, 'modal_speaking', speaking_html)
content = replace_modal(content, 'modal_tuition', tuition_html)
content = replace_modal(content, 'modal_english', english_html)
content = replace_modal(content, 'modal_art', art_html)
content = replace_modal(content, 'modal_personality', personality_html)
content = replace_modal(content, 'modal_calligraphy', calligraphy_html)

with open("programs.html", "w") as f:
    f.write(content)

print("Updated programs.html successfully!")
