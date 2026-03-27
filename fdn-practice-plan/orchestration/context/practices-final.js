// DATA.dressPractices — finalized from FDN course modules 09, 10, 11, 12
// Minimum 12 entries required. Each entry verified against its source module.
// All strings plain-language tested. No clinical abbreviations without definitions.

const dressPracticesData = [
  {
    id: 'protein-fat-fiber-every-meal',
    dresComponent: 'diet',
    title: 'Include protein, fat, and fiber at every meal',
    action: 'At each meal, make sure your plate includes a source of protein (such as meat, fish, or eggs), a healthy fat (such as olive oil, butter, or avocado), and fiber-rich vegetables or whole foods. Do not skip meals — skipping meals disrupts blood sugar levels, slows your metabolic rate, and sets you up for cravings. After eating, check in with your body about 90 minutes later: Are you satisfied and free from cravings? Do you have steady energy — not a slump and not nervous energy? Do you feel a general sense of wellbeing? If not, adjust the balance of protein, fat, and carbohydrates at your next meal.',
    why: 'This helps your body keep blood sugar steady between meals, so you avoid the energy crashes, cravings, and irritability that come from blood sugar swings.',
    frequency: 'daily',
    clusters: ['A', 'C', 'D', 'E'],
    priority: 9,
    module: '09'
  },
  {
    id: 'eliminate-refined-carbs-90-day',
    dresComponent: 'diet',
    title: 'Cut out refined carbohydrates for 90 days',
    action: 'Remove refined carbohydrates — such as cookies, white bread, crackers, pastries, and other processed grain-based foods — from your diet for 90 days. These foods are low in fiber and raise blood sugar too quickly. If you eat grains, choose whole grains that still contain the germ and husk. Limit fruit to berries and other low-sugar options during this reset period. Avoid sugar and alcohol for the full 90 days. After 90 days, some lower-sugar options may be reintroduced based on how your body responds.',
    why: 'This helps your body reset its ability to manage blood sugar steadily, since refined carbohydrates strip away the natural nutrients your body needs to process carbohydrates properly.',
    frequency: 'daily',
    clusters: ['A', 'C', 'D', 'E'],
    priority: 8,
    module: '09'
  },
  {
    id: 'track-satiety-energy-after-meals',
    dresComponent: 'diet',
    title: 'Track how you feel after every meal',
    action: 'After each meal, check in with your body about 90 minutes later and note three things: (1) Are you satisfied and free from cravings until your next meal? (2) Do you have steady, lasting energy — not a slump and not nervous energy? (3) Do you feel a general sense of wellbeing — uplifted and not irritated? If any of these are missing, adjust the amounts of protein, fat, or carbohydrates at your next meal. Consider keeping a simple log to track your responses over time.',
    why: 'This helps your body find the right food balance for your unique metabolism, so each meal builds energy and wellbeing instead of leaving you craving more.',
    frequency: 'daily',
    clusters: ['A', 'C', 'D'],
    priority: 5,
    module: '09'
  },
  {
    id: 'sleep-window-10pm-6am',
    dresComponent: 'rest',
    title: 'Go to bed at 10 PM and wake at 6 AM every day',
    action: 'Set a consistent sleep schedule: go to bed at 10 PM and get up at 6 AM every day, including weekends and holidays. Each hour of sleep before midnight is worth 2 hours of sleep after midnight for rebuilding and detoxifying the body and resting the adrenal glands (your stress-response glands, located above your kidneys). Your adrenal glands do most of their recharging between 10 PM and 2 AM, so being asleep during this window is especially important.',
    why: 'This helps your body restore its stress-response system and rebuild energy at the cellular level, since the most restorative hours of sleep happen before midnight.',
    frequency: 'daily',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 10,
    module: '10'
  },
  {
    id: 'sleep-environment-dark-cool-quiet',
    dresComponent: 'rest',
    title: 'Make your bedroom dark, cool, and quiet',
    action: 'Set up your bedroom as a sleep sanctuary: hang blackout curtains to make the room pitch dark, or use a sleep mask. Keep the room slightly cool — no warmer than 70°F (21°C). Keep the room as quiet as possible; use earplugs if needed. Do not have a television in the bedroom. Turn off or remove devices that emit light or wireless signals, such as cell phones and cordless phones. If a nightlight is absolutely necessary, use only a very dim red or orange light.',
    why: 'This helps your body produce melatonin (your natural sleep hormone) and reach the deep, restorative sleep stages where your cells repair and your brain resets.',
    frequency: 'daily',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 8,
    module: '10'
  },
  {
    id: 'no-screens-2-hours-before-bed',
    dresComponent: 'rest',
    title: 'Stop using screens 2 hours before bed',
    action: 'Stop using computers, tablets, phones, and other electronic screens at least 2 hours before your bedtime. Dim the lights in your home in the hour or two before bed. If you must use a device close to bedtime, wear amber- or orange-tinted glasses that block the type of light that disrupts your body\'s sleep signal. Wind down instead with non-stimulating reading, relaxation techniques, meditation, or breathing exercises.',
    why: 'This helps your body start producing its natural sleep hormone on schedule, so you fall asleep more easily and get deeper, more restorative sleep.',
    frequency: 'daily',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 7,
    module: '10'
  },
  {
    id: 'pre-sleep-protein-snack',
    dresComponent: 'rest',
    title: 'Eat a small protein snack before bed',
    action: 'Before bed, eat a small snack that combines protein (such as a few bites of turkey, chicken, nut butter, or a hard-boiled egg), a low-glycemic carbohydrate (such as a small amount of berries or a rice cake), and a small amount of healthy fat. Keep the snack small — just enough to prevent your blood sugar from dropping during the night. A drop in blood sugar is a common cause of waking up between 2 and 3 AM.',
    why: 'This helps your body maintain stable blood sugar through the night, so you stay asleep and get the full restorative benefit of each sleep cycle.',
    frequency: 'daily',
    clusters: ['B', 'E'],
    priority: 5,
    module: '10'
  },
  {
    id: 'mobility-active-recovery-first',
    dresComponent: 'exercise',
    title: 'Begin with gentle movement and stretching',
    action: 'Before adding any intense exercise, start with mobility work and active recovery. Mobility work means exercises specifically aimed at improving your range of motion and joint health — this includes traditional stretching, yoga, Pilates, tai chi, and foam rolling. Active recovery means any lower-intensity activity that promotes blood flow and muscle activation while avoiding excess strain — such as walking, light yoga, or short, easy workouts. Aim for 20–30 minutes of this kind of movement most days. Focus on taking each joint through its comfortable full range of motion. Stay at this level until you have no persistent soreness, your energy is consistent, and you are sleeping well.',
    why: 'This helps your body build its capacity for exercise safely, because adding intense movement too soon to a depleted or stressed system often makes symptoms worse rather than better.',
    frequency: 'daily',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 7,
    module: '11'
  },
  {
    id: 'resistance-training-as-recovery-improves',
    dresComponent: 'exercise',
    title: 'Add strength training when your recovery is consistent',
    action: 'Once you have been doing mobility work consistently for several weeks and your recovery signs are positive — meaning no persistent soreness, steady energy, and good sleep — add resistance training 2 to 3 times per week for 30 to 40 minutes per session. Resistance training means moving your body against weight or resistance, including bodyweight exercises (push-ups, squats, lunges) or lifting weights. Prioritize movements that work multiple muscle groups at once: squats, deadlifts, push-ups, rows, and lunges. Start with a weight that is manageable and allows good form. Aim for 3 to 4 sets of 8 to 10 repetitions per exercise. Start small and work your way up consistently — it is better to exercise twice a week every week than five times a week for a month and then stop.',
    why: 'This helps your body build lean muscle and improve how it manages blood sugar, which supports steady energy levels and long-term health as your recovery strengthens.',
    frequency: 'weekly',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 6,
    module: '11'
  },
  {
    id: 'hiit-after-recovery-baseline',
    dresComponent: 'exercise',
    title: 'Add high-intensity intervals only after recovery is stable',
    action: 'High-intensity interval training (HIIT) — short bursts of maximum effort followed by brief rest — should only be added after you have been consistently doing mobility work and resistance training for several weeks with no signs of poor recovery (such as persistent soreness, poor sleep, low energy, or increased irritability). A beginner HIIT session example: sprint at full effort for 30 seconds, then rest for 15 seconds, and repeat for 10 rounds (about 7 minutes total). This can be done on a treadmill, elliptical, or with bodyweight movements such as jumping jacks, squat jumps, or burpees. Keep HIIT sessions short — 15 to 20 minutes — and limit them to 1 to 2 times per week. HIIT can be done after resistance training or as a standalone session on a separate day.',
    why: 'This helps your body burn fat more efficiently and strengthen your heart and lungs, but only once your system has enough reserve to recover from the added intensity — pushing this too early can increase symptoms and slow healing.',
    frequency: 'weekly',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 5,
    module: '11'
  },
  {
    id: 'daily-water-half-oz-per-pound',
    dresComponent: 'stress',
    title: 'Drink half an ounce of water per pound of body weight each day',
    action: 'Calculate your daily water target: take your body weight in pounds and multiply by 0.5 — that number in ounces is your daily goal. For example, if you weigh 150 pounds, aim for 75 ounces of water per day (about 9 cups). Drink filtered water throughout the day rather than all at once. Start each morning with a full glass of water before eating or drinking anything else. Carry a water bottle to track your intake. Avoid replacing water with juice, soda, or other sweetened drinks. Water supports your kidneys in flushing waste products and keeps your colon moving so that toxins do not accumulate and get reabsorbed.',
    why: 'This helps your body flush waste products through the kidneys and keeps your digestive system moving so that processed toxins are removed rather than reabsorbed.',
    frequency: 'daily',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 8,
    module: '12'
  },
  {
    id: 'bowel-regularity-one-per-day',
    dresComponent: 'stress',
    title: 'Have at least one bowel movement every day',
    action: 'Aim to have at least one complete bowel movement every day. Anyone who is not doing so regularly is considered constipated, even if it does not feel severe. To support daily bowel movements: meet your daily water target (half an ounce of filtered water per pound of body weight), eat plenty of vegetables and high-fiber foods including insoluble fiber (fiber that does not dissolve in water — found in vegetables, whole grains, and legumes), which adds bulk to waste and moves it through, and soluble fiber (fiber that dissolves in water and forms a gel — found in oats, beans, and flaxseed), which binds to toxins and helps carry them out. Stay active with daily movement. If you are consistently not having a daily bowel movement, flag this as a priority area to work on.',
    why: 'This helps your body remove processed waste and toxins before they can be reabsorbed into your bloodstream, reducing the overall stress your organs have to manage.',
    frequency: 'daily',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 7,
    module: '12'
  },
  {
    id: 'reduce-environmental-toxins',
    dresComponent: 'stress',
    title: 'Reduce everyday toxin exposure at home',
    action: 'Make three foundational changes to reduce the toxins you absorb daily: (1) Choose organic produce to avoid pesticide and herbicide residues — at minimum, prioritize buying organic for produce you eat most often or with the heaviest pesticide loads. If you eat non-organic meat, choose lean cuts, because toxins concentrate in the fat. (2) Drink filtered water rather than unfiltered tap water. Use a water filter at home, and choose filtered or bottled water when eating out. (3) Replace nonstick cookware (pots and pans with a slick coating, such as Teflon) with cast iron or stainless steel. These coatings release chemicals into food when heated or scratched. These three steps reduce the ongoing chemical load your body has to process every day.',
    why: 'This helps your body lower the total amount of chemical stress it processes daily so it can direct more energy toward repair and recovery.',
    frequency: 'daily',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 7,
    module: '12'
  },
  {
    id: 'deliberate-daily-laughter',
    dresComponent: 'stress',
    title: 'Make time for genuine laughter every day',
    action: 'Build at least 10 to 15 minutes of genuine laughter into your day as a deliberate stress reduction practice. Watch a comedy show, film, or short videos that make you laugh out loud. Seek out the company of people who make you laugh. By the time a child reaches nursery school, he or she laughs about 300 times a day — adults average only 17 times a day. You can actively raise that number by choosing to seek out humor. Research showed that 10 minutes of genuine belly laughter can produce an effect similar to a pain reliever, and that watching comedy lowers stress hormones, reduces blood pressure, and increases immune cells.',
    why: 'This helps your body lower its stress hormones and support its immune system, because laughter triggers the release of natural pain-relieving and mood-lifting chemicals in the brain.',
    frequency: 'daily',
    clusters: ['A', 'B', 'C', 'D', 'E'],
    priority: 7,
    module: '12'
  },
  {
    id: 'mineral-supplement-before-sleep',
    dresComponent: 'supplement',
    title: 'Take a foundational mineral supplement before bed',
    action: 'Take a multi-mineral supplement before bed each night as part of your foundational health support. Minerals support the body\'s ability to relax and prepare for sleep. Follow the guidance in your personalized FDN (Functional Diagnostic Nutrition — a health coaching method that uses lab testing to identify hidden stressors) protocol for the specific mineral support that is right for you — no specific dosages or brands are prescribed at this level of the program.',
    why: 'This helps your body wind down and relax before sleep by supporting the mineral balance your nervous system needs to shift into rest and recovery mode.',
    frequency: 'daily',
    clusters: ['B', 'E'],
    priority: 4,
    module: '10'
  }
];
