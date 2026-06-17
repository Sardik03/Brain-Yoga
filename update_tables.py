import re

with open("programs.html", "r") as f:
    content = f.read()

def replace_course_box(content, modal_id, new_table_html):
    pattern = re.compile(r'(<div id="' + modal_id + r'" class="modal">.*?)(<div class="course-details-box">.*?</div>)(.*?</div>\s*</div>\s*</div>)', re.DOTALL)
    if not pattern.search(content):
        print(f"Modal {modal_id} not found or course-details-box missing!")
    return pattern.sub(r'\1' + new_table_html + r'\3', content)

tables = {
    'modal_abacus': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>4 to 10 Years</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>2.5-3 Months (Each Level) / 12hr Monthly</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2000 per month</td>
                        </tr>
                        <tr>
                            <td>Registration</td>
                            <td>₹750 (one-time)</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",
    
    'modal_vedic': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>12+ Years</td>
                        </tr>
                        <tr>
                            <td>Duration Per Level</td>
                            <td>2–3 Months</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2500 per month</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",

    'modal_hindi': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>5+ Years to adults</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>2-3 months per level/ 8hr Monthly</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2000 per month</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",

    'modal_handwriting': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>5+ Years</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>1-2 months per level</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2000 per month</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",

    'modal_speaking': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>6+ Years</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>2 to 3 months</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2000 Onwards</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",

    'modal_tuition': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>Class I to X</td>
                        </tr>
                        <tr>
                            <td>Subjects</td>
                            <td>All major subjects</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>Ongoing</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2000 to ₹3000 per month</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",

    'modal_english': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>6+ Years</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>2-3 Months (Per Level)</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2500 per month</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",

    'modal_art': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>5+ Years</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>2 to 3 months</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2000 onwards</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",

    'modal_personality': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>6+ Years</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>2 to 3 months</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2000 onwards</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>""",

    'modal_calligraphy': """<table class="course-details-table">
                    <thead>
                        <tr>
                            <th>Detail</th>
                            <th>Information</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Age Group</td>
                            <td>7+ Years</td>
                        </tr>
                        <tr>
                            <td>Duration</td>
                            <td>2 to 3 months</td>
                        </tr>
                        <tr>
                            <td>Fees</td>
                            <td>₹2000 onwards</td>
                        </tr>
                    </tbody>
                </table>

                <div class="modal-enroll-container">
                    <a href="admissions.html" class="modal-enroll-btn">
                        <i class="fa-solid fa-graduation-cap"></i> Want to Apply? - CLICK HERE
                    </a>
                </div>"""
}

for modal_id, table_html in tables.items():
    content = replace_course_box(content, modal_id, table_html)

with open("programs.html", "w") as f:
    f.write(content)

print("Updated programs.html successfully!")
