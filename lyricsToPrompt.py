import random
import re

class lyricsToInput:
    
    def __init__(self, fps=15) -> None:
        self.fps = fps
        pass

    def defineStartInFrames(self, lyrics):
        return self.secondsToFrames(lyrics[0]['start'], self.fps)

    def defineEndInFrames(self, lyrics):
        return self.secondsToFrames(lyrics[-1]['end'], self.fps)
    
    def milisecondsToSeconds(self, miliseconds):
        seconds = miliseconds / 1000
        return seconds

    def secondsToFrames(self, seconds, fps):
        frames = seconds * fps
        return int(frames)

    def makePrompt(self, lyrics, title):
        prompt = "0: " + title + " | "
        
        for line in lyrics:
            prompt += str(line['startFrame']) + ': ' + line['sentence'] + ' | '
        prompt += str(lyrics[-1]['endFrame']) + ': ' + title
        return str(prompt)

    def applyStylization(self, lyrics, style):
        stylizations = {
            "cyberpunk": ["cyberpunk", "neon", "cybernetic", "synthwave", "sci-fi", "neotokyo", "futuristic", "bladerunner", "Akira", "megacity", "highly detailed"],
            "photorealistic": ["photo", "50mm", "realistic", "photography", "ultrarelistic", "award winning photography", "nikon", "photorealistic",
            "higly detailed", "ultra detailed","8k uhd"],
            "art": ["trending on artstation", "fine art", "oil painting", "golden ratio", "elegant", "symmetry", "by Bob Ross", "by Antoine Blanchard", "by Leonid Afremov"]
        }
        for line in lyrics:
            try:    
                additions = random.sample(stylizations[style], 4)
                for addition in additions:
                    line['sentence'] += addition + ", "
            except KeyError:
                print("Unknown style, using art")
                style = "art"
                pass
        return lyrics

    def createPromptKeyframesDict(self, lyrics):
        lyricsFrames = []
        for line in lyrics:
            lyricsFrames.append({"sentence": line['sentence'], "startFrame": self.secondsToFrames(self.milisecondsToSeconds(line['start']), self.fps),
                                "endFrame": self.secondsToFrames(self.milisecondsToSeconds(line['end']), self.fps)})
        return lyricsFrames

    def makeMovement(self, lyrics):
        movement = {
            "angle": "0: (0), ",
            "zoom": "0: (1.04), ",
            "translation_x": "0: (0), ",
            "translation_y": "0: (0), "
        }
        for line in lyrics:
            type = random.choice(list(movement))
            randomMovement = str(line["startFrame"]) + ": (" + str(round(random.uniform(-3.0, 3.0), 2)) + "), "
            movement[type] += randomMovement
        for type in movement:
            movement[type] = re.sub(", $", "", movement[type])
        return movement


    def makeOutput(self, lyrics, style, title):
        lyrics = self.createPromptKeyframesDict(lyrics)
        max_frame = lyrics[-1]['endFrame']
        lyrics = self.applyStylization(lyrics, style)
        prompt = self.makePrompt(lyrics, title)
        movement = self.makeMovement(lyrics)
        return prompt, movement, max_frame


if __name__ == "__main__":
    lyrics_list = [{'sentence': 'I stay out too late, got nothing in my break? ','start': 4860,'end': 9250},{'sentence': "That's what people say, that's what people say? ",'start': 10660,'end': 15170},{'sentence': 'I go on too many dates? ', 'start': 16260, 'end': 18560},{'sentence': "But I can't make them stay? ", 'start': 19380, 'end': 21250},{'sentence': "At least that's what people say, ", 'start': 22100,'end': 24210},{'sentence': "that's what people will say? But I keep cruel, ",'start': 25620,'end': 30360},{'sentence': "can't stop, won't stop moving? It's like I got this music in my mind thinking it's going to be all right? ",'start': 30940,'end': 40490},{'sentence': 'Because the players on a play, ', 'start': 41020, 'end': 42632},{'sentence': 'play, play? And the hat is going to hate. ','start': 42686,'end': 45704},{'sentence': "Hate, hate, hate, hate? Baby, I'm just going to shake, ",'start': 45752,'end': 48632},{'sentence': 'shake, shake, shake, shake? I shake it off, ','start': 48696,'end': 51340},{'sentence': 'I shake it off? Heartbreak is going to break, ','start': 51410,'end': 54620},{'sentence': 'break, break, break, break, break? And the fake is going to fake. ','start': 54690,'end': 57692},{'sentence': "Fake, fake, fake, fake? Baby, I'm just going to shake, ",'start': 57756,'end': 60604},{'sentence': 'shake, shake, shake, shake? I shake it off, ','start': 60652,'end': 63360},{'sentence': 'I shake it off? I never miss a beat? ','start': 63430,'end': 66320},{'sentence': "I'm lighting on my feet? And that's what they don't see, ",'start': 67380,'end': 72230},{'sentence': "that's what they don't say? I'm dipping on my oak? ",'start': 73640,'end': 78340},{'sentence': "I'll make the moves up as I go? ",'start': 79100,'end': 81210},{'sentence': "And that's what they don't know, ",'start': 82380,'end': 84250},{'sentence': "that's what they don't know? But I keep cruising, ",'start': 85660,'end': 90840},{'sentence': "kids, I won't stop grooming? It's like I got this music in my mind saying it's going to be all right? ",'start': 91000,'end': 100430},{'sentence': 'Because the players on a play, ','start': 100960,'end': 102620},{'sentence': 'play, play, play? And the hate is going to hate. ','start': 102690,'end': 105692},{'sentence': "Hate, hate, hate, hate? Baby, I'm just going to shake, ",'start': 105756,'end': 108604},{'sentence': 'shake, shake, shake, shake, shake it off, ','start': 108652,'end': 111328},{'sentence': 'I shake it off? Heart break is going to break, ','start': 111414,'end': 114640},{'sentence': 'break, break, break, break, break? And the figure is going to fake. ','start': 114710,'end': 117692},{'sentence': "Fake, fake, fake, fake? Baby, I'm just going to shake, ",'start': 117756,'end': 120616},{'sentence': 'shake, shake, shake, shake? I shake it off, ','start': 120668,'end': 123348},{'sentence': 'I shake it. Off, shake it off, ','start': 123434,'end': 126388},{'sentence': 'I shake it off, I shake it off, ','start': 126474,'end': 129348},{'sentence': 'I shake it off, I shake it off, ','start': 129434,'end': 132360},{'sentence': 'I shake it off, I shake it off, ','start': 132430,'end': 135368},{'sentence': 'I shake it off? Hey, just think, ','start': 135454,'end': 140184},{'sentence': "while you've been getting down and out about the liars and the dirty, ",'start': 140222,'end': 143336},{'sentence': 'dirty cheats of the world, you could have been getting down to this sick beats, ','start': 143368,'end': 148700},{'sentence': 'my ex man brought his new girlfriend. ','start': 149440,'end': 152040},{'sentence': "She's like, oh, my God. But I'm just going to shake it. ",'start': 152120,'end': 155136},{'sentence': 'To the fella over there with the. ','start': 155158,'end': 157056},{'sentence': 'Hell of good hair. Once you come on over, ','start': 157078,'end': 159200},{'sentence': 'baby, we. Can shake, shake, shake, ','start': 159270,'end': 161840},{'sentence': 'yeah, because the. Players on a play, ','start': 162820,'end': 165604},{'sentence': "play, play, play? I'm just gonna shake, ",'start': 165642,'end': 171632},{'sentence': 'shake, shake, shake, shake? I shake it off, ','start': 171696,'end': 174340},{'sentence': 'I shake it up? Heartbreak is gonna break? ','start': 174410,'end': 177620},{'sentence': 'Brick, Brick, brick breaking the fake, ','start': 177690,'end': 180672},{'sentence': "baby. I'm just gonna say shake, ",'start': 180736,'end': 184004},{'sentence': 'shake, shake, shake? I shake it off, ','start': 184052,'end': 186360},{'sentence': 'I shake it. Off, I shake it off, ','start': 186430,'end': 190730},{'sentence': 'I shake it off, I shake it off, ','start': 191180,'end': 193770},{'sentence': 'shake it off, I shake it off, ','start': 200380,'end': 202770},{'sentence': 'I shake it off, I shake it off, ','start': 203220,'end': 205730},{'sentence': 'I shake it off, I shake it off, ','start': 206180,'end': 208770},{'sentence': 'I shake it off, I shake it off? ','start': 209220,'end': 211230}]
    prompt, movement, max_frame = lyricsToInput().makeOutput(lyrics_list, style="art", title="DupaDupa")
    print(prompt)
    print(movement)
    print(max_frame)