Total time spent: 17.5 hours
## May 15, 2025
Today, I mostly focused on planning. I want this keyboard to:
- Be column staggered
- Have more convenient key placements
- Feel satisfying to type on
- Be overall more intuitive than normal keyboards.

Anaylizing my typing patterns, I notice that my hands often feel cramped, keys feel somewhat unintuitive in location, and I struggle to
hit keys like "tab" and "backspace" with my pinkie fingers. I decided that it would be best to not have a dedicated function row, and to instead have it accessible with an fn key.

With some thinking, I have made a plan for a keyboard with 52 keys. Currently, I think it'll have only 2 thumb keys per hand, but I might change that later on.
For inspiration, I looked on the internet ; especially on the Reddit sub r/ergomechkeyboards.

There, I found some designs that I want to take inspiration from
![image](https://github.com/user-attachments/assets/5139eb21-c63f-4cc1-9c48-a3afe0c2a901) by u/ianmcl
![image](https://github.com/user-attachments/assets/326f1f37-cceb-4489-a27c-f62837e401f0) from u/pedrorq
![image](https://github.com/user-attachments/assets/a213d5ea-a3eb-4c0d-a6a7-ed6bb87f62e3) the ZSA Voyager.

With a good idea of what I wanted to make in mind, I have started to plan out the layout for my keyboard.
![image](https://github.com/user-attachments/assets/a094d4a2-8f03-4267-ad48-c0c4e62964f7)


Time Spent: 2.5 hours

## May 16, 2025
Today, I started designing the left half of my keyboard. 
However, before that, I finished tweaking my keybaord design on [Keyboard-Layout-Editor](https://www.keyboard-layout-editor.com/#/)
This is what I came up with. I've decided to increase the amount of thumb keys to 6, so this will be a
54 key keyboard.
![Screenshot 2025-05-16 230038](https://github.com/user-attachments/assets/34c878c7-ebd3-460d-8241-bc349f7ec945)

 I also decided that I want to use low profile switches. I've tried to use normal profile keyboards in the past, but
 the height makes my wrists hurt. 
 
 The thing is, unlike regular profile switches, there isn't really
 a standard design for low profile switches. I had to go hunting for footprints, 3d models, hotswap sockets, etc for the Gateron
 KS-33 switches I chose to use.
 
 One I had my layout finalized, it was time to star schematic-y-ing. That was fortunately pretty straightforward.

 It was when I loaded up the pcb that I came across a problem. How was I going to properly postition all the keys? Now this
 isn't my first rodeo with keyboard-related designs, but this is the first one I've had one with a column stagger and angled switches.
 To make accomplish this task, I headed over to [ai03](https://kbplate.ai03.com/) where I generated plate for my design. At first, the edges of the
 cutout were rounded by default, but I removed this for convenience. I then downloaded it as a dxf and imported it into Kicad as a graphic.
 ![Screenshot 2025-05-16 231643](https://github.com/user-attachments/assets/d25792b7-2691-449a-b6a2-9e41b1f3f73e)

 I also edited the Gateron KS-33 footprints I had found to so that they would have a centered 14x14 box in them, the same dimensions as the
 switch plate. This allowed my to postion the switches relatively to the plate.
 

 Next, I need to place the diodes and add edge cuts!

![Screenshot 2025-05-16 231643](https://github.com/user-attachments/assets/1d74f49f-b79c-4b1c-b7d8-f82b11648bd5)


 Time Spent: 3 hours

 ## May 17, 2025
 Today I finished my PCBs, and started making the cases. It was sooooo tedious trying to place everything where it needed to be, finding footprints,
 3d models, editing footprints, etc. Closer to the end of the process, I decided it would be best to change the keyswitch footprint from [this
 one by siderkb on Github](https://camo.githubusercontent.com/41e7a4040d28bec680a1cc81e6fa1cbf86637d8cd1792a479a8ed29b25a4d441/68747470733a2f2f692e696d6775722e636f6d2f72525549466b302e706e67)

[To this one](https://camo.githubusercontent.com/dcc6496cad867bbc903a92fb7431d5b972b87b0c7c5b4b7377a76f2af5bd1d9c/68747470733a2f2f692e696d6775722e636f6d2f3746437a6a72612e706e67)
 
 I was not tryna do allat, so after completing the left half of my keyboard, I simply made copy of it, renamed it, and flipped the copied pcb in kicad.
 I then proceeded to flip certain elements, reroute, and update the schematic a bit for a proper design.
 Here's what it looks like looks like:
![Screenshot 2025-05-20 112907](https://github.com/user-attachments/assets/266d6bd4-5164-433a-8e87-5838756d948b)

 A bit of a tangent, but you may have noticed a blocky grey thing near the thumb keys on my pcb. This is what will allow the two 
 keyboard halves to communicate with each other! Normally, split keyboards use a TRRS jack to facilitate this communication. 
[ They look like this!](https://keeb.io/cdn/shop/products/IMG_9005.JPG?v=1568991566&width=2000)
The thing is, TRRS is not hotswappable. This means that if you accidentally unplug the connector cable while the keyboards are connected to power,
very bad things will happen. I'm kinda clumsy, so that option was out. 

Less commonly, USB-C is also used, but I decided to avoid that because it's hard to solder and I didn't want to use it non-standardly.

I decided to used a RJ11/6P4C connector because it is hotswappable and  pretty easy to solder. It is a bit chonky, but that just
means it has personality :)

With my pcbs done, it was time to start on the cases. To make my job a lot easier, I exported the edgecuts layers and a couple other as SVG's. I then
converted the SVG file to DXF, and imported it into a new Fusion360 project. This allows me to design my case very accurately to my pcb

At the moment, I am currently struggling to offset my case outline properly, because apparently the universe finds spiting me funny TT. As you can see,
a few segments of the outline are not included for some reason
![Screenshot 2025-05-17 235443](https://github.com/user-attachments/assets/f016f685-ecbc-49d6-8a56-b2bcc77c3de0)
Maybe it'll work tomorrow...

Time Spent: 5 hours TT

## May 19, 2025
I figured out how to offset my case outline! It turns out that if you zoomed in really really close, the lines weren't properly connected. 
I fixed this, and everthing went swimmingly. 

Until....I looked at the Gateron KS-33 data sheet. To my surprise, the max distance that can be between the pcb and switch is 2.5 millimeters. 

Now, with regular, non-low-profile switches, the maximum distance that can be between the pcb and switch is 5mm. I plan on getting my my switch plate 3d-printed.
It's reccomended that a 3d-printed switch plate be at least 3mm thick, to prevent bending. For a brief but not insignificant moment, I considered using
normal profile switches. But, I decided I really didn't want a tall keyboard. I will thug it out.

With that decision made, I finished designing the right half of my case pretty quickly. With a strong idea of what my casing will look like, the left half
shouldn't take too long(I jinxed it, didn't I?).
![Screenshot 2025-05-19 175035](https://github.com/user-attachments/assets/79894c4c-3d23-4c07-82cf-71763e8efdda)


I also got the boilerplate for my firmware done! I just need to figure what keys I want to put on each layer, and I'll be done

Bonus: When importing a 3d model of my PCB into Fusion360, I noticed that I had accidentally put a diode on the front-side instead of the back side. Oops. 
Stay observant y'all!

Time Spent: 4 hours

## May 20, 2025
I finished! Fortunately, I did not in fact jinx it. My cases are looking very handsome in the README, if I do say so myself.

While examining the CAD for my left case, I noticed that I had accidentally flipped the RJ11 jack the wrong way. Fortunately, it 
was an easy fix.
![image](https://github.com/user-attachments/assets/4a369052-3ca2-4017-bd95-731dd7509ddb)


Since there is going to be a spot where the pcb is visible, I added some silkscreen branding and a little bit of art. I'm quite
pleased with how it looks.

Finally, I made my firmware! It wasn't hard, but it did require switching between a lot of different tabs. I also
had to learn how layers work in KMK, which was interesting.

Time Spent: 3 hours
