// Testimonials Data extracted from Google doc
const testimonials = [
    {
        name: "Priti Malhotra",
        text: "My son joined only for Abacus, but we saw such good improvement in focus that later we enrolled him in Vedic Maths also. The difference is clearly visible. Teachers really work on the basics.",
        stars: 5
    },
    {
        name: "Rahul Bansal",
        text: "Very nice environment, small batches and proper attention. Along with studies they also work on personality development and speaking skills which I liked a lot.",
        stars: 5
    },
    {
        name: "Kunal Jain",
        text: "Joined handwriting class for my son even though his writing was okay, but now it is much neater. He even started calligraphy and learned a few basic styles.",
        stars: 5
    },
    {
        name: "Ruchi Sharma",
        text: "My son joined for maths tuition here. Slowly, his interest came back; earlier he used to avoid doing sums. Now he sits on his own, which is a big change for us.",
        stars: 5
    },
    {
        name: "Anjali Mehra",
        text: "The daycare facility is really helpful for us as working parents. My son never used to eat fruits at home, but here Suman ma’am made him habitual of eating healthy snacks daily. Big relief for us.",
        stars: 5
    },
    {
        name: "Rohit Gupta",
        text: "We were very stressed about our child’s school performance. After joining tuition and Abacus here, his marks slowly improved and even his school teacher has noticed and appreciated the progress.",
        stars: 5
    },
    {
        name: "Pooja Saini",
        text: "My son used to fumble a lot while speaking English. We tried other spoken English classes also, but after almost a year, I can clearly see better pronunciation and confidence.",
        stars: 5
    },
    {
        name: "Kavita Sharma",
        text: "Hindi was always difficult for my daughter because of matra and spelling. With Suman ma’am’s help, she is now reading and writing much better and even speaks more fluently.",
        stars: 5
    }
];

document.addEventListener('DOMContentLoaded', () => {

    // --- Testimonials Slider Setup ---
    const track = document.getElementById('testimonialTrack');

    // Populate track if it exists
    if (track) {
        testimonials.forEach(item => {
            const starHTML = Array(item.stars).fill('<i class="fa-solid fa-star"></i>').join('');
            const card = document.createElement('div');
            card.className = 'testimonial-card';
            card.innerHTML = `
                <div class="stars">${starHTML}</div>
                <div class="testimonial-text">"${item.text}"</div>
                <div class="testimonial-author">- ${item.name}</div>
            `;
            track.appendChild(card);
        });

        // Slider Logic
        let currentIndex = 0;
        const cards = document.querySelectorAll('.testimonial-card');
        const totalCards = cards.length;

        const updateSlider = () => {
            const translateValue = -(currentIndex * 100);
            track.style.transform = `translateX(${translateValue}%)`;
        };

        const nextBtn = document.getElementById('nextBtn');
        const prevBtn = document.getElementById('prevBtn');

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (currentIndex < totalCards - 1) {
                    currentIndex++;
                } else {
                    currentIndex = 0; // loop back
                }
                updateSlider();
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (currentIndex > 0) {
                    currentIndex--;
                } else {
                    currentIndex = totalCards - 1; // loop to end
                }
                updateSlider();
            });
        }

        // Auto-advance slider
        setInterval(() => {
            if (currentIndex < totalCards - 1) {
                currentIndex++;
            } else {
                currentIndex = 0;
            }
            updateSlider();
        }, 5000);
    }

    // --- Navbar Scroll Effect ---
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.style.boxShadow = '0 4px 6px rgba(118, 74, 157, 0.1)';
                navbar.style.padding = '12px 0';
            } else {
                navbar.style.boxShadow = 'none';
                navbar.style.padding = '16px 0';
            }
        });
    }

    // --- Mobile Menu Toggle ---
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');
    
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            navLinks.classList.toggle('active');
            
            // Toggle hamburger icon between bars and times (X)
            const icon = menuToggle.querySelector('i');
            if (icon) {
                if (navLinks.classList.contains('active')) {
                    icon.className = 'fa-solid fa-xmark';
                } else {
                    icon.className = 'fa-solid fa-bars';
                }
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!menuToggle.contains(e.target) && !navLinks.contains(e.target)) {
                navLinks.classList.remove('active');
                const icon = menuToggle.querySelector('i');
                if (icon) {
                    icon.className = 'fa-solid fa-bars';
                }
            }
        });
    }
});
