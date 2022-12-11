import replicate


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
        output = self.client.predictions.create(version=version, input=input)
        return output

if __name__ == "__main__":
    print(Replicate().callDeforumOnReplicate())