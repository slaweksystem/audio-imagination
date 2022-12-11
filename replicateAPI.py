import replicate
import time


class Replicate:

    def __init__(self) -> None:
        secrets = self.loadSecrets()
        self.client = self.initializeReplicateClient(secrets)  
        pass
    
    def loadSecrets(self):
        secrets = {}
        with open ("secrets.txt", 'r') as f:
             for line in f:
                key, value = line.strip().split('=')
                secrets[key] = value
        return secrets

    def initializeReplicateClient(self, secrets):
        client = replicate.Client(api_token=secrets["REPLICATE_API_TOKEN"])
        return client

    def callDeforumOnReplicate(self, max_frames=100, prompt="a beautiful portrait of a woman by Artgerm, trending on Artstation",
    angle="0:(0)", zoom="0: (1.04)", translation_x="0: (0)", translation_y="0: (0)", color_coherence="Match Frame 0 LAB",
    sampler="plms", fps=15, seed=None):
        model = self.client.models.get("deforum/deforum_stable_diffusion")
        version = model.versions.get("e22e77495f2fb83c34d5fae2ad8ab63c0a87b6b573b6208e1535b23b89ea66d6")
        input = {
            "max_frames": max_frames,
            "prompt": prompt,
            "angle": angle,
            "zoom": zoom,
            "translation_x": translation_x,
            "translation_y": translation_y,
            "color_coherence": color_coherence,
            "sampler": sampler,
            "fps": fps,
            "seed": seed
        }
        prediction = self.client.predictions.create(version=version, input=input)
        return prediction

    def callSDOnReplicate(self, prompt="a beautiful portrait of a woman by Artgerm, trending on Artstation",
    negative_prompt="", width=128, height=128, prompt_strength=float(1), num_outputs=1, num_inference_steps=20,
    guidance_scale=float(7), scheduler="K_EULER", seed=None):
        model = self.client.models.get("stability-ai/stable-diffusion")
        version = model.versions.get("6359a0cab3ca6e4d3320c33d79096161208e9024d174b2311e5a21b6c7e1131c")
        input = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "prompt_strength": prompt_strength,
            "num_outputs": num_outputs,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "scheduler": scheduler,
            "seed": seed
        }
        prediction = self.client.predictions.create(version=version, input=input)
        return prediction

def checkPredictionStatus(prediction):
    prediction.reload()
    print(prediction.status)
    if prediction.status == 'succeeded':
        return prediction.output

def monitorPredictionStatus(prediction):
    prediction.reload()
    print(prediction.status)
    try:
        while prediction.status == 'processing' or prediction.status == 'starting':
            prediction.reload()
            print(prediction.status)
            print("Waiting")
            time.sleep(10)
            continue
    except KeyboardInterrupt:
        prediction.cancel()
        print("Canceled!")
    if prediction.status == 'succeeded':
        return prediction.output
    

if __name__ == "__main__":
    prediction = Replicate().callDeforumOnReplicate()
    monitorPredictionStatus(prediction)