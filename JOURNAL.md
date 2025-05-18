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
 one by siderkb on Github:
](https://camo.githubusercontent.com/41e7a4040d28bec680a1cc81e6fa1cbf86637d8cd1792a479a8ed29b25a4d441/68747470733a2f2f692e696d6775722e636f6d2f72525549466b302e706e67)
 
 I was not tryna do allat, so after completing the left half of my keyboard,
 I simply made copy of it, renamed it, and flipped the copied pcb in kicad. I then proceeded to edit so

Time Spent: 5 hours TT
